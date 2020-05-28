from brlcad.database import Database

# An example of the Database class
database = Database("i dont have names to give.g", "No title as usual")

# Makes a sphere with default arguments
database.sphere("default_sph")

# Makes a sphere with given arguments
database.sphere("sph_with_args", (10, 10, 10), 2)
