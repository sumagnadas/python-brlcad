from .bindings.wdb import rt_wdb
from .bindings.raytrace import point_t
from .exceptions import BRLCADException
import brlcad.bindings.wdb as wdb
import brlcad.bindings.raytrace as rt
import os


class Database(rt_wdb):
    def __init__(self, db_file, title=None):
        try:
            if os.path.exists(db_file) and os.path.isfile(db_file):
                self.db_ip = rt.db_open(db_file, "r+w")
                if self.db_ip == rt.DBI_NULL:
                    raise BRLCADException("Can't open existing DB file: <{0}>".format(db_file))
                if rt.db_dirbuild(self.db_ip) < 0:
                    raise BRLCADException("Failed loading directory of DB file: <{}>".format(db_file))
                rt.ctypes.cast(self.db_ip, rt.ctypes.POINTER(wdb.struct_db_i))
                self.db_fp = wdb.wdb_dbopen(rt.ctypes.cast(self.db_ip, rt.ctypes.POINTER(wdb.struct_db_i)), rt.RT_WDB_TYPE_DB_INMEM)
                if self.db_fp == rt.ctypes.cast(0, rt.ctypes.POINTER(rt_wdb)):
                    raise BRLCADException("Failed read existing DB file: <{}>".format(db_file))
            else:
                self.db_fp = wdb.wdb_fopen(db_file)
                self.db_ip = self.db_fp.contents.dbip
                if title:
                    wdb.mk_id(self.db_fp, title)
        except Exception as e:
            raise BRLCADException("Can't open DB file <{0}>: {1}".format(db_file, e))

    def sphere(self, name, center=(0, 0, 0), radius=1):
        wdb.mk_sph(self.db_fp, name, point_t(*center), radius)

    def extrude(self, name, sketch=None, base=None, height=None, u_vec=None, v_vec=None):
        wdb.mk_extrusion(
            self.db_fp, name, sketch.name,
            point_t((0, 0, 0) if base is None else  base),
            point_t((0, 0, 1) if height is None else height),
            point_t((1, 0, 0) if u_vec is None else u_vec),
            point_t((0, 1, 0) if v_vec is None else v_vec),
            0
        )

    def lookup_internal(self, name):
        db_internal = rt.rt_db_internal()
        dpp = wdb.pointer(wdb.POINTER(rt.directory)())
        idb_type = rt.rt_db_lookup_internal(
            self.db_ip, name,
            dpp,
            wdb.byref(db_internal),
            rt.LOOKUP_QUIET,
            wdb.byref(rt.rt_uniresource)
        )
        return idb_type, db_internal, dpp
