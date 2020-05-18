#from raytrace import *
#from vmath import *
#from test1 import *
#from common import *
#from ctypes import *
from sys import argv, exit
import array


script, filename, shape = argv

callback_types_hit = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_application), POINTER(struct_partition), POINTER(struct_seg))
callback_types_miss = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_application))

def BU_CKMAG(_ptr, _magic, _str):
    return (_ptr)

def VMOVE(o, v):
    o[X] = v[X]
    o[Y] = v[Y]
    o[Z] = v[Z]

def RT_CK_HIT(_p):
    BU_CKMAG(_p, 0x20686974, "struct hit")

def RT_HIT_NORMAL(_normal, _hitp, _stp, _unused, _flipflag):
    _n = _normal
    if hasattr(_stp.contents.st_meth.contents, 'ft_norm'):
        _stp.contents.st_meth.contents.ft_norm(_hitp, _stp, _hitp.contents.hit_rayp)
    if _n != None:
        _f = array.array('B', _flipflag)[0]
    if _f:
        VREVERSE(fastf_t(_normal), _hitp.contents.hit_normal)
    else:
        VMOVE(_normal, _hitp.contents.hit_normal)

def VJOIN1(o, a, sb, b):
    o[X] = a[X] + sb * b[X]
    o[Y] = a[Y] + sb * b[Y]
    o[Z] = a[Z] + sb * b[Z]
def RT_APPLICATION_INIT(_p):
    _p.a_magic = 0x4170706c

def VPRINT(a, b):
    print(f"{a} ({b[X]}, {b[Y]}, {b[Z]})")

def hit_ray(ap, partheadp, segs):
    hitp = hit()
    stp = soltab()
    cur = curvature(vect_t(0.0, 0.0, 0.0), 0.0, 0.0)
    pt = point_t()
    inormal = vect_t()
    onormal = vect_t()
    i = 1
    pp = partheadp.contents.pt_forw.contents
    while addressof(pp) != addressof(partheadp.contents):
        bu_log("\n--- Hit region {} (in {} , out {})\n".format(
               pp.pt_regionp.contents.reg_name,
    	       pp.pt_inseg.contents.seg_stp.contents.st_dp.contents.d_namep,
    	       pp.pt_outseg.contents.seg_stp.contents.st_dp.contents.d_namep))
        hitp = pp.pt_inhit
        VJOIN1(pt, ap.contents.a_ray.r_pt, hitp.contents.hit_dist, ap.contents.a_ray.r_dir)
        stp = pp.pt_inseg.contents.seg_stp
        RT_HIT_NORMAL(inormal, hitp, stp, (ap.contents.a_ray), pp.pt_inflip)
        rt_pr_hit("  In", hitp)
        VPRINT(   "  Ipoint", pt)
        VPRINT(   "  Inormal", inormal)
        VPRINT("PDir", cur.crv_pdir)
        bu_log(" c1={}\n".format(cur.crv_c1))
        bu_log(" c2={}\n".format(cur.crv_c2))
        RT_HIT_NORMAL(onormal, hitp, stp, (ap.contents.a_ray), pp.pt_outflip)
        rt_pr_hit("  Out", hitp)
        VPRINT(   "  Opoint", pt)
        VPRINT(   "  Onormal", onormal)
        pp = pp.pt_forw.contents
    return 1

def miss(ap):
    bu_log("missed\n")
    return 0
def VSET(o,a,b,c):
    o[X] = a
    o[Y] = b
    o[Z] = c

def main():
    title = create_string_buffer(100)
    rtip = rt_dirbuild(filename, title, sizeof(title))
    if rtip == RTI_NULL:
        bu_log("Building the database directory for {} FAILED\n".format(filename))
        exit(0)
    title = title.value.decode("utf-8")
    if title:
        bu_log(f"Title:\n{title}\n")
    if rt_gettree(rtip, shape) < 0:
        bu_log("Loading the geometry for {} FAILED\n".format(shape))
    ap = application()
    rt_prep_parallel(rtip, 1)
    ap.a_rt_i = rtip
    ap.a_onehit = 0

    VSET(ap.a_ray.r_pt, 0.0, 0.0, 10000.0)
    VSET(ap.a_ray.r_dir, 0.0, 0.0, -1.0)

    VPRINT("Pnt", ap.a_ray.r_pt)
    VPRINT("Dir", ap.a_ray.r_dir)
    ap.a_hit = callback_types_hit(hit_ray)
    ap.a_miss = callback_types_miss(miss)
    c_void_p(rt_shootray(pointer(ap)))
    """
    return i
    """
if __name__ == "__main__":
    i = main()
    print(0)
