from raytrace import *
from wdb import *
file = db_open("geometry.g", "r+w")
mk_sph(wdb_fopen("geometry.g"), "sph.s", point_t(0.5, 5, 8), 0.75)
