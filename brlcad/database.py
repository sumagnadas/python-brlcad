from .bindings.wdb import rt_wdb
from .bindings.raytrace import point_t
import brlcad.bindings.wdb as wdb
import brlcad.bindings.raytrace as rt
import os


class Database(rt_wdb):
    def __init__(self, db_file, title=None):
        try:
            self.db_fp = wdb.wdb_fopen(db_file)
            self.db_ip = self.db_fp.contents.dbip
            if title:
                wdb.mk_id(self.db_fp, title)
        except Exception as e:
            raise Exception("Can't open DB file <{0}>: {1}".format(db_file, e))

    def sphere(self, name, center=(0, 0, 0), radius=1):
        wdb.mk_sph(self.db_fp, name, point_t(*center), radius)
