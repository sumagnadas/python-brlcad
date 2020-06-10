from brlcad.vmath import Transform
from brlcad.database import Database
from brlcad import primitives

# An example of the Database class
database = Database("i dont have names to give.g", "No title as usual")

# Makes a sphere with default arguments
database.sphere("default_sph")

# Makes a sphere with given arguments
database.sphere("sph_with_args", (10, 10, 10), 2)

database.region(
            'sph_with_args_region',
            region_id = 16,
            tree = 'sph_with_args',
            shader="plastic {di .9 sp .4}",
            rgb_color=(66,102,0)
            )

#db.region(
#            'default_sph_region',
#            region_id = 16,
#            tree = 'default_sph',
#            shader="plastic {di .9 sp .4}",
#            rgb_color=(66,102,0)
#            )
