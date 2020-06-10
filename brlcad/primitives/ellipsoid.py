"""
Python wrapper for the ELL and SPH primitives of BRL-CAD.
"""

from .base import Primitive
import numpy as np
from brlcad.vmath.vector import Vector


class Ellipsoid(Primitive):

    def __init__(self, name, center, a, b, c, copy=False):
        Primitive.__init__(self, name=name)
        self.center = Vector(center, copy=copy)
        self.a = Vector(a, copy=copy)
        self.b = Vector(b, copy=copy)
        self.c = Vector(c, copy=copy)

    def __repr__(self):
        return "ELL(name={0}, center={1}, a={2}, b={3}, c={4})".format(
            self.name, repr(self.center), repr(self.a), repr(self.b), repr(self.c)
        )

    def __iter__(self):
        yield self.center
        yield self.a
        yield self.b
        yield self.c

    def update_params(self, params):
        params.update({
            "center": self.center,
            "a": self.a,
            "b": self.b,
            "c": self.c,
        })

    def copy(self):
        return Ellipsoid(self.name, self.center, self.a, self.b, self.c, copy=True)

    def has_same_data(self, other):
        return all(map(Vector.is_same, self, other))

    def _get_radius(self):
        """
        Returns the radius if this is a Sphere, None otherwise.
        Can also be used as a test if this is a sphere:
        >>> x = Ellipsoid("test", "0, 0, 0", (10, 0, 0), [0, 10, 0], Vector("0, 0, 10"))
        >>> x.radius
        10.0
        >>> x.a = Vector("1, 0, 0")
        >>> x.radius is None
        True
        """
        mag_a = self.a.norm()
        mag_b = self.b.norm()
        mag_c = self.c.norm()
        if np.allclose((mag_a, mag_b), (mag_b, mag_c)):
            return mag_a
        else:
            return None

    radius = property(_get_radius)

    @staticmethod
    def from_wdb(name, data):
        return Ellipsoid(
            name=name,
            center=data.v,
            a=data.a,
            b=data.b,
            c=data.c,
        )


class Sphere(Ellipsoid):

    def __init__(self, name, center, radius, copy=False):
        Ellipsoid.__init__(
            self, name=name, center=center,
            a=(radius, 0, 0), b=(0, radius, 0), c=(0, 0, radius),
            copy=copy
        )

    def __repr__(self):
        return "SPH(name={0}, center={1}, radius={2})".format(
            self.name, repr(self.center), self.radius
        )

    def update_params(self, params):
        """
        Updates sphere parameters: center and radius
        >>> x = Sphere("test", "0, 0, 0", 5)
        >>> p = {}
        >>> x.update_params(p)
        >>> set(p.keys()) == {"radius", "center"}
        True
        >>> p["center"].is_same((0, 0, 0))
        True
        >>> p["radius"] == 5
        True
        """
        params.update({
            "center": self.center,
            "radius": self.radius,
        })

    @staticmethod
    def from_wdb(name, data):
        return Sphere(
            name=name,
            center=data.v,
            radius=Vector(data.a).norm(),
        )
