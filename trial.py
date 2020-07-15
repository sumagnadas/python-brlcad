from brlcad.database import Database, wdb
import pdb
import os

h = Database('geometry1.g')
print(h.ls())
rgb = (wdb.c_ubyte * 3)()
rgb[0] = 153

wdb.mk_region1(h.db_fp, 'random', 'comb0', "", "", rgb)
print(h.ls())
h.close()
