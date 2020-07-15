from .bindings.wdb import rt_wdb
from .bindings.raytrace import point_t
from .exceptions import BRLCADException
import brlcad.primitives.table as p_table
import brlcad.primitives as primitives
import brlcad.ctypes_adaptors as cta
import brlcad.bindings.wdb as wdb
import brlcad.bindings.raytrace as rt
import os


SAVE_MAP = {}

def mk_wrap_primitive(primitive_class):
    def wrapper_func(mk_func):
        if primitive_class == primitives.Primitive:
            pass
        elif primitive_class in SAVE_MAP and SAVE_MAP[primitive_class] != mk_func:
            raise BRLCADException(
                "Bad setup, multiple save functions ({}, {}) assigned to primitive: {}".format(
                    mk_func, SAVE_MAP[primitive_class], primitive_class
                )
            )
        else:
            def wrapped_func(db_self, *args, **kwargs):
                if len(args) == 1 and isinstance(args[0], primitives.Primitive):
                    shape = args[0]
                    if not isinstance(shape, primitive_class):
                        raise(
                            "{0} expects primitive of type {1} but got {2}".format(
                                mk_func.func_name, primitive_class, type(shape)
                            )
                        )
                    shape.update_params(kwargs)
                    mk_func(db_self, shape.name, **kwargs)
                else:
                    mk_func(db_self, *args, **kwargs)
            SAVE_MAP[primitive_class] = wrapped_func
        return mk_func
    return wrapper_func

class Database(rt_wdb):
    def __init__(self, db_file, title=None):
        try:
            if os.path.isfile(db_file):
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

    def __iter__(self):
        for i in range(0, rt.RT_DBNHASH):
            dp = self.db_ip.contents.dbi_Head[i]
            while dp:
                crt_dir = dp.contents
                yield crt_dir
                dp = crt_dir.d_forw

    def __lookup_internal__(self, name):
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

    def lookup(self, name):
        idb_type, db_internal, dpp = self.__lookup_internal__(name)
        if not idb_type:
            return None
        return p_table.create_primitive(idb_type, db_internal, dpp.contents.contents)

    def delete(self, name):
        idb_type, db_internal, dpp = self._lookup_internal(name)
        if not idb_type:
            return False
        result1 = not libwdb.db_delete(self.db_ip, dpp.contents)
        result2 = not libwdb.db_dirdelete(self.db_ip, dpp.contents)
        return result1 and result2

    def ls(self, pattern=None):
        name_generator = (str(x.d_namep) for x in self if not(x.d_flags & rt.RT_DIR_HIDDEN))
        return [x for x in name_generator if pattern is None or fnmatch.fnmatch(name=x, pat=pattern)]

    @mk_wrap_primitive(primitives.Sphere)
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
    @mk_wrap_primitive(primitives.Combination)
    def combination(self, name, is_region=False, tree=None, inherit=False,
                    shader=None, material=None, rgb_color=None, temperature=0,
                    region_id=0, air_code=0, gift_material=0, line_of_sight=0,
                    is_fastgen=wdb.REGION_NON_FASTGEN):
        if not tree:
            raise ValueError("Empty tree for combination: {0}".format(name))
        tree = primitives.wrap_tree(tree)
        new_comb = cta.brlcad_new(rt.struct_rt_comb_internal)
        new_comb.magic = rt.RT_COMB_MAGIC
        new_comb.tree = tree.build_tree()
        new_comb.tree.contents.magic = 2434339217
        new_comb.tree.contents.tr_l.tl_op = rt.OP_DB_LEAF
        new_comb.tree.contents.tr_l.tl_mat = None
        new_comb.region_flag = 0 if not is_region else 1
        new_comb.is_fastgen = is_fastgen
        new_comb.region_id = region_id
        new_comb.aircode = air_code
        new_comb.GIFTmater = gift_material
        new_comb.los = line_of_sight
        new_comb.rgb_valid = 0 if not rgb_color else 1
        new_comb.rgb = cta.rgb(rgb_color)
        new_comb.temperature = temperature
        new_comb.shader = cta.str_to_vls(shader).contents
        new_comb.material = cta.str_to_vls(material).contents
        new_comb.inherit = cta.bool_to_char(inherit)
        wdb.wdb_export(self.db_fp, name, wdb.byref(new_comb), rt.ID_COMBINATION, 1)

    def region(self, *args, **kwargs):
        kwargs["is_region"] = True
        return self.combination(*args, **kwargs)

    def close(self):
        wdb.wdb_close(self.db_fp)
