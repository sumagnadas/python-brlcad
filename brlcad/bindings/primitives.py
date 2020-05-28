r"""Wrapper for annot.h

Generated with:
/mnt/sda2/python/virtualenvs/python-brlcad/bin/ctypesgen -I/usr/brlcad/dev-7.31.0/include/brlcad/ /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/annot.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/cline.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/dsp.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/ell.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/epa.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/hf.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pg.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pipe.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/rhc.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/rpc.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/script.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/tgc.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/tor.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h -o annot.py -l/usr/brlcad/dev-7.31.0/lib/libwdb.so -l/usr/brlcad/dev-7.31.0/lib/libbu.so -l/usr/brlcad/dev-7.31.0/lib/librt.so -l/usr/brlcad/dev-7.31.0/lib/libbn.so

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/libwdb.so")
_libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/libbu.so")
_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/librt.so")
_libs["/usr/brlcad/dev-7.31.0/lib/libbn.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/libbn.so")

# 4 libraries
# End libraries

# No modules

u_char = c_ubyte# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 155

u_int = c_uint# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 156

u_long = c_ulong# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 157

u_short = c_ushort# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 158

__off_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 152

__off64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 153

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

# /usr/include/x86_64-linux-gnu/bits/mathcalls.h: 143
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("sqrt", "cdecl"):
    sqrt = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("sqrt", "cdecl")
    sqrt.argtypes = [c_double]
    sqrt.restype = c_double

# /usr/include/x86_64-linux-gnu/bits/mathcalls.h: 256
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rint", "cdecl"):
    rint = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rint", "cdecl")
    rint.argtypes = [c_double]
    rint.restype = c_double

fastf_t = c_double# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 330

vect2d_t = fastf_t * int(2)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 333

vect2dp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 336

point2d_t = fastf_t * int(2)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 339

point2dp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 342

vect_t = fastf_t * int(3)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 345

vectp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 348

point_t = fastf_t * int(3)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 351

pointp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 354

hvect_t = fastf_t * int(4)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 357

quat_t = hvect_t# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 360

hpoint_t = fastf_t * int(4)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 363

mat_t = fastf_t * int((4 * 4))# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 366

matp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 369

plane_t = fastf_t * int(4)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 393

enum_vmath_vector_component_ = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

X = 0# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

Y = 1# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

Z = 2# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

W = 3# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

H = W# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

vmath_vector_component = enum_vmath_vector_component_# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

enum_vmath_matrix_component_ = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

MSX = 0# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

MDX = 3# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

MSY = 5# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

MDY = 7# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

MSZ = 10# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

MDZ = 11# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

MSA = 15# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

vmath_matrix_component = enum_vmath_matrix_component_# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 416

off_t = __off64_t# /usr/include/x86_64-linux-gnu/sys/types.h: 87

time_t = __time_t# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 7

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 130
class struct_bu_list(Structure):
    pass

struct_bu_list.__slots__ = [
    'magic',
    'forw',
    'back',
]
struct_bu_list._fields_ = [
    ('magic', c_uint32),
    ('forw', POINTER(struct_bu_list)),
    ('back', POINTER(struct_bu_list)),
]

bu_list_t = struct_bu_list# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 135

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 489
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_list_new", "cdecl"):
    bu_list_new = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_list_new", "cdecl")
    bu_list_new.argtypes = []
    bu_list_new.restype = POINTER(struct_bu_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 494
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_list_pop", "cdecl"):
    bu_list_pop = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_list_pop", "cdecl")
    bu_list_pop.argtypes = [POINTER(struct_bu_list)]
    bu_list_pop.restype = POINTER(struct_bu_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 499
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_list_len", "cdecl"):
    bu_list_len = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_list_len", "cdecl")
    bu_list_len.argtypes = [POINTER(struct_bu_list)]
    bu_list_len.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 504
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_list_reverse", "cdecl"):
    bu_list_reverse = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_list_reverse", "cdecl")
    bu_list_reverse.argtypes = [POINTER(struct_bu_list)]
    bu_list_reverse.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 512
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_list_free", "cdecl"):
    bu_list_free = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_list_free", "cdecl")
    bu_list_free.argtypes = [POINTER(struct_bu_list)]
    bu_list_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 522
for _lib in _libs.values():
    if not _lib.has("bu_list_parallel_append", "cdecl"):
        continue
    bu_list_parallel_append = _lib.get("bu_list_parallel_append", "cdecl")
    bu_list_parallel_append.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list)]
    bu_list_parallel_append.restype = None
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 535
for _lib in _libs.values():
    if not _lib.has("bu_list_parallel_dequeue", "cdecl"):
        continue
    bu_list_parallel_dequeue = _lib.get("bu_list_parallel_dequeue", "cdecl")
    bu_list_parallel_dequeue.argtypes = [POINTER(struct_bu_list)]
    bu_list_parallel_dequeue.restype = POINTER(struct_bu_list)
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 540
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_ck_list", "cdecl"):
    bu_ck_list = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_ck_list", "cdecl")
    bu_ck_list.argtypes = [POINTER(struct_bu_list), String]
    bu_ck_list.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 547
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_ck_list_magic", "cdecl"):
    bu_ck_list_magic = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_ck_list_magic", "cdecl")
    bu_ck_list_magic.argtypes = [POINTER(struct_bu_list), String, c_uint32]
    bu_ck_list_magic.restype = None

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 49
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE# /usr/include/x86_64-linux-gnu/bits/types/FILE.h: 7

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 36
class struct__IO_marker(Structure):
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 37
class struct__IO_codecvt(Structure):
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 38
class struct__IO_wide_data(Structure):
    pass

_IO_lock_t = None# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 43

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '_codecvt',
    '_wide_data',
    '_freeres_list',
    '_freeres_buf',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * int(1)),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('_codecvt', POINTER(struct__IO_codecvt)),
    ('_wide_data', POINTER(struct__IO_wide_data)),
    ('_freeres_list', POINTER(struct__IO_FILE)),
    ('_freeres_buf', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * int((((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t)))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 53
class struct_bu_vls(Structure):
    pass

struct_bu_vls.__slots__ = [
    'vls_magic',
    'vls_str',
    'vls_offset',
    'vls_len',
    'vls_max',
]
struct_bu_vls._fields_ = [
    ('vls_magic', c_uint32),
    ('vls_str', String),
    ('vls_offset', c_size_t),
    ('vls_len', c_size_t),
    ('vls_max', c_size_t),
]

bu_vls_t = struct_bu_vls# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 60

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 95
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_init", "cdecl"):
    bu_vls_init = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_init", "cdecl")
    bu_vls_init.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_init.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 103
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_init_if_uninit", "cdecl"):
    bu_vls_init_if_uninit = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_init_if_uninit", "cdecl")
    bu_vls_init_if_uninit.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_init_if_uninit.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 110
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_vlsinit", "cdecl"):
    bu_vls_vlsinit = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_vlsinit", "cdecl")
    bu_vls_vlsinit.argtypes = []
    bu_vls_vlsinit.restype = POINTER(struct_bu_vls)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 116
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_addr", "cdecl"):
    bu_vls_addr = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_addr", "cdecl")
    bu_vls_addr.argtypes = [POINTER(struct_bu_vls)]
    if sizeof(c_int) == sizeof(c_void_p):
        bu_vls_addr.restype = ReturnString
    else:
        bu_vls_addr.restype = String
        bu_vls_addr.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 124
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_cstr", "cdecl"):
    bu_vls_cstr = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_cstr", "cdecl")
    bu_vls_cstr.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_cstr.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 131
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_extend", "cdecl"):
    bu_vls_extend = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_extend", "cdecl")
    bu_vls_extend.argtypes = [POINTER(struct_bu_vls), c_size_t]
    bu_vls_extend.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 144
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_setlen", "cdecl"):
    bu_vls_setlen = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_setlen", "cdecl")
    bu_vls_setlen.argtypes = [POINTER(struct_bu_vls), c_size_t]
    bu_vls_setlen.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 150
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strlen", "cdecl"):
    bu_vls_strlen = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strlen", "cdecl")
    bu_vls_strlen.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_strlen.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 158
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_trunc", "cdecl"):
    bu_vls_trunc = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_trunc", "cdecl")
    bu_vls_trunc.argtypes = [POINTER(struct_bu_vls), c_int]
    bu_vls_trunc.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 168
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_nibble", "cdecl"):
    bu_vls_nibble = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_nibble", "cdecl")
    bu_vls_nibble.argtypes = [POINTER(struct_bu_vls), off_t]
    bu_vls_nibble.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 174
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_free", "cdecl"):
    bu_vls_free = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_free", "cdecl")
    bu_vls_free.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 180
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_vlsfree", "cdecl"):
    bu_vls_vlsfree = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_vlsfree", "cdecl")
    bu_vls_vlsfree.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_vlsfree.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 186
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strdup", "cdecl"):
    bu_vls_strdup = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strdup", "cdecl")
    bu_vls_strdup.argtypes = [POINTER(struct_bu_vls)]
    if sizeof(c_int) == sizeof(c_void_p):
        bu_vls_strdup.restype = ReturnString
    else:
        bu_vls_strdup.restype = String
        bu_vls_strdup.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 197
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strgrab", "cdecl"):
    bu_vls_strgrab = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strgrab", "cdecl")
    bu_vls_strgrab.argtypes = [POINTER(struct_bu_vls)]
    if sizeof(c_int) == sizeof(c_void_p):
        bu_vls_strgrab.restype = ReturnString
    else:
        bu_vls_strgrab.restype = String
        bu_vls_strgrab.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 202
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strcpy", "cdecl"):
    bu_vls_strcpy = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strcpy", "cdecl")
    bu_vls_strcpy.argtypes = [POINTER(struct_bu_vls), String]
    bu_vls_strcpy.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 209
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strncpy", "cdecl"):
    bu_vls_strncpy = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strncpy", "cdecl")
    bu_vls_strncpy.argtypes = [POINTER(struct_bu_vls), String, c_size_t]
    bu_vls_strncpy.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 216
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strcat", "cdecl"):
    bu_vls_strcat = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strcat", "cdecl")
    bu_vls_strcat.argtypes = [POINTER(struct_bu_vls), String]
    bu_vls_strcat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 222
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strncat", "cdecl"):
    bu_vls_strncat = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strncat", "cdecl")
    bu_vls_strncat.argtypes = [POINTER(struct_bu_vls), String, c_size_t]
    bu_vls_strncat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 230
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_vlscat", "cdecl"):
    bu_vls_vlscat = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_vlscat", "cdecl")
    bu_vls_vlscat.argtypes = [POINTER(struct_bu_vls), POINTER(struct_bu_vls)]
    bu_vls_vlscat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 237
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_vlscatzap", "cdecl"):
    bu_vls_vlscatzap = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_vlscatzap", "cdecl")
    bu_vls_vlscatzap.argtypes = [POINTER(struct_bu_vls), POINTER(struct_bu_vls)]
    bu_vls_vlscatzap.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 245
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strcmp", "cdecl"):
    bu_vls_strcmp = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strcmp", "cdecl")
    bu_vls_strcmp.argtypes = [POINTER(struct_bu_vls), POINTER(struct_bu_vls)]
    bu_vls_strcmp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 254
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_strncmp", "cdecl"):
    bu_vls_strncmp = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_strncmp", "cdecl")
    bu_vls_strncmp.argtypes = [POINTER(struct_bu_vls), POINTER(struct_bu_vls), c_size_t]
    bu_vls_strncmp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 262
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_from_argv", "cdecl"):
    bu_vls_from_argv = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_from_argv", "cdecl")
    bu_vls_from_argv.argtypes = [POINTER(struct_bu_vls), c_int, POINTER(POINTER(c_char))]
    bu_vls_from_argv.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 269
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_fwrite", "cdecl"):
    bu_vls_fwrite = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_fwrite", "cdecl")
    bu_vls_fwrite.argtypes = [POINTER(FILE), POINTER(struct_bu_vls)]
    bu_vls_fwrite.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 275
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_write", "cdecl"):
    bu_vls_write = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_write", "cdecl")
    bu_vls_write.argtypes = [c_int, POINTER(struct_bu_vls)]
    bu_vls_write.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 286
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_read", "cdecl"):
    bu_vls_read = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_read", "cdecl")
    bu_vls_read.argtypes = [POINTER(struct_bu_vls), c_int]
    bu_vls_read.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 301
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_gets", "cdecl"):
    bu_vls_gets = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_gets", "cdecl")
    bu_vls_gets.argtypes = [POINTER(struct_bu_vls), POINTER(FILE)]
    bu_vls_gets.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 307
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_putc", "cdecl"):
    bu_vls_putc = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_putc", "cdecl")
    bu_vls_putc.argtypes = [POINTER(struct_bu_vls), c_int]
    bu_vls_putc.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 313
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_trimspace", "cdecl"):
    bu_vls_trimspace = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_trimspace", "cdecl")
    bu_vls_trimspace.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_trimspace.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 328
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_printf", "cdecl"):
    _func = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_printf", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(struct_bu_vls), String]
    bu_vls_printf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 340
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_sprintf", "cdecl"):
    _func = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_sprintf", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(struct_bu_vls), String]
    bu_vls_sprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 346
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_spaces", "cdecl"):
    bu_vls_spaces = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_spaces", "cdecl")
    bu_vls_spaces.argtypes = [POINTER(struct_bu_vls), c_size_t]
    bu_vls_spaces.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 361
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_print_positions_used", "cdecl"):
    bu_vls_print_positions_used = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_print_positions_used", "cdecl")
    bu_vls_print_positions_used.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_print_positions_used.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 368
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_detab", "cdecl"):
    bu_vls_detab = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_detab", "cdecl")
    bu_vls_detab.argtypes = [POINTER(struct_bu_vls)]
    bu_vls_detab.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 374
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_prepend", "cdecl"):
    bu_vls_prepend = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_prepend", "cdecl")
    bu_vls_prepend.argtypes = [POINTER(struct_bu_vls), String]
    bu_vls_prepend.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 388
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_substr", "cdecl"):
    bu_vls_substr = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_substr", "cdecl")
    bu_vls_substr.argtypes = [POINTER(struct_bu_vls), POINTER(struct_bu_vls), c_size_t, c_size_t]
    bu_vls_substr.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 404
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_vprintf", "cdecl"):
    bu_vls_vprintf = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_vprintf", "cdecl")
    bu_vls_vprintf.argtypes = [POINTER(struct_bu_vls), String, c_void_p]
    bu_vls_vprintf.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 449
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_encode", "cdecl"):
    bu_vls_encode = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_encode", "cdecl")
    bu_vls_encode.argtypes = [POINTER(struct_bu_vls), String]
    bu_vls_encode.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 462
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_decode", "cdecl"):
    bu_vls_decode = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_decode", "cdecl")
    bu_vls_decode.argtypes = [POINTER(struct_bu_vls), String]
    bu_vls_decode.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 501
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_simplify", "cdecl"):
    bu_vls_simplify = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_simplify", "cdecl")
    bu_vls_simplify.argtypes = [POINTER(struct_bu_vls), String, String, String]
    bu_vls_simplify.restype = c_int

bu_vls_uniq_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(None))# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 507

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 679
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("bu_vls_incr", "cdecl"):
    bu_vls_incr = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("bu_vls_incr", "cdecl")
    bu_vls_incr.argtypes = [POINTER(struct_bu_vls), String, String, bu_vls_uniq_t, POINTER(None)]
    bu_vls_incr.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h: 72
class struct_bn_tol(Structure):
    pass

struct_bn_tol.__slots__ = [
    'magic',
    'dist',
    'dist_sq',
    'perp',
    'para',
]
struct_bn_tol._fields_ = [
    ('magic', c_uint32),
    ('dist', c_double),
    ('dist_sq', c_double),
    ('perp', c_double),
    ('para', c_double),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bg/defines.h: 114
class struct_bg_tess_tol(Structure):
    pass

struct_bg_tess_tol.__slots__ = [
    'magic',
    'abs',
    'rel',
    'norm',
    'absmax',
    'absmin',
    'relmax',
    'relmin',
    'rel_lmax',
    'rel_lmin',
]
struct_bg_tess_tol._fields_ = [
    ('magic', c_uint32),
    ('abs', c_double),
    ('rel', c_double),
    ('norm', c_double),
    ('absmax', c_double),
    ('absmin', c_double),
    ('relmax', c_double),
    ('relmin', c_double),
    ('rel_lmax', c_double),
    ('rel_lmin', c_double),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1010
class struct_rt_annot_internal(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/annot.h: 36
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_copy_annot", "cdecl"):
    rt_copy_annot = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_copy_annot", "cdecl")
    rt_copy_annot.argtypes = [POINTER(struct_rt_annot_internal)]
    rt_copy_annot.restype = POINTER(struct_rt_annot_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/mapped_file.h: 81
class struct_bu_mapped_file(Structure):
    pass

struct_bu_mapped_file.__slots__ = [
    'name',
    'buf',
    'buflen',
    'is_mapped',
    'appl',
    'apbuf',
    'apbuflen',
    'modtime',
    'uses',
    'handle',
]
struct_bu_mapped_file._fields_ = [
    ('name', String),
    ('buf', POINTER(None)),
    ('buflen', c_size_t),
    ('is_mapped', c_int),
    ('appl', String),
    ('apbuf', POINTER(None)),
    ('apbuflen', c_size_t),
    ('modtime', time_t),
    ('uses', c_int),
    ('handle', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/ptbl.h: 53
class struct_bu_ptbl(Structure):
    pass

struct_bu_ptbl.__slots__ = [
    'l',
    'end',
    'blen',
    'buffer',
]
struct_bu_ptbl._fields_ = [
    ('l', struct_bu_list),
    ('end', c_size_t),
    ('blen', c_size_t),
    ('buffer', POINTER(POINTER(c_long))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 37
class struct_mem_map(Structure):
    pass

struct_mem_map.__slots__ = [
    'm_nxtp',
    'm_size',
    'm_addr',
]
struct_mem_map._fields_ = [
    ('m_nxtp', POINTER(struct_mem_map)),
    ('m_size', c_size_t),
    ('m_addr', off_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 44
class struct_region(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 38
class struct_mater_info(Structure):
    pass

struct_mater_info.__slots__ = [
    'ma_color',
    'ma_temperature',
    'ma_color_valid',
    'ma_cinherit',
    'ma_minherit',
    'ma_shader',
]
struct_mater_info._fields_ = [
    ('ma_color', c_float * int(3)),
    ('ma_temperature', c_float),
    ('ma_color_valid', c_char),
    ('ma_cinherit', c_char),
    ('ma_minherit', c_char),
    ('ma_shader', String),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 61
class struct_resource(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h: 63
class struct_db_i(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 59
class struct_directory(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_fullpath.h: 54
class struct_db_full_path(Structure):
    pass

struct_db_full_path.__slots__ = [
    'magic',
    'fp_len',
    'fp_maxlen',
    'fp_names',
    'fp_bool',
]
struct_db_full_path._fields_ = [
    ('magic', c_uint32),
    ('fp_len', c_size_t),
    ('fp_maxlen', c_size_t),
    ('fp_names', POINTER(POINTER(struct_directory))),
    ('fp_bool', POINTER(c_int)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 52
class struct_anim_mat(Structure):
    pass

struct_anim_mat.__slots__ = [
    'anm_op',
    'anm_mat',
]
struct_anim_mat._fields_ = [
    ('anm_op', c_int),
    ('anm_mat', mat_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 62
class struct_rt_anim_property(Structure):
    pass

struct_rt_anim_property.__slots__ = [
    'magic',
    'anp_op',
    'anp_shader',
]
struct_rt_anim_property._fields_ = [
    ('magic', c_uint32),
    ('anp_op', c_int),
    ('anp_shader', struct_bu_vls),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 71
class struct_rt_anim_color(Structure):
    pass

struct_rt_anim_color.__slots__ = [
    'anc_rgb',
]
struct_rt_anim_color._fields_ = [
    ('anc_rgb', c_int * int(3)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 76
class struct_animate(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 81
class union_animate_specific(Union):
    pass

union_animate_specific.__slots__ = [
    'anu_m',
    'anu_p',
    'anu_c',
    'anu_t',
]
union_animate_specific._fields_ = [
    ('anu_m', struct_anim_mat),
    ('anu_p', struct_rt_anim_property),
    ('anu_c', struct_rt_anim_color),
    ('anu_t', c_float),
]

struct_animate.__slots__ = [
    'magic',
    'an_forw',
    'an_path',
    'an_type',
    'an_u',
]
struct_animate._fields_ = [
    ('magic', c_uint32),
    ('an_forw', POINTER(struct_animate)),
    ('an_path', struct_db_full_path),
    ('an_type', c_int),
    ('an_u', union_animate_specific),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 62
class union_anon_24(Union):
    pass

union_anon_24.__slots__ = [
    'file_offset',
    'ptr',
]
union_anon_24._fields_ = [
    ('file_offset', off_t),
    ('ptr', POINTER(None)),
]

struct_directory.__slots__ = [
    'd_magic',
    'd_namep',
    'd_un',
    'd_forw',
    'd_animate',
    'd_uses',
    'd_len',
    'd_nref',
    'd_flags',
    'd_major_type',
    'd_minor_type',
    'd_use_hd',
    'd_shortname',
    'u_data',
]
struct_directory._fields_ = [
    ('d_magic', c_uint32),
    ('d_namep', String),
    ('d_un', union_anon_24),
    ('d_forw', POINTER(struct_directory)),
    ('d_animate', POINTER(struct_animate)),
    ('d_uses', c_long),
    ('d_len', c_size_t),
    ('d_nref', c_long),
    ('d_flags', c_int),
    ('d_major_type', c_ubyte),
    ('d_minor_type', c_ubyte),
    ('d_use_hd', struct_bu_list),
    ('d_shortname', c_char * int(16)),
    ('u_data', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 49
class struct_rt_wdb(Structure):
    pass

struct_db_i.__slots__ = [
    'dbi_magic',
    'dbi_filename',
    'dbi_read_only',
    'dbi_local2base',
    'dbi_base2local',
    'dbi_title',
    'dbi_filepath',
    'dbi_Head',
    'dbi_fp',
    'dbi_eof',
    'dbi_nrec',
    'dbi_uses',
    'dbi_freep',
    'dbi_inmem',
    'dbi_anroot',
    'dbi_mf',
    'dbi_clients',
    'dbi_version',
    'dbi_wdbp',
]
struct_db_i._fields_ = [
    ('dbi_magic', c_uint32),
    ('dbi_filename', String),
    ('dbi_read_only', c_int),
    ('dbi_local2base', c_double),
    ('dbi_base2local', c_double),
    ('dbi_title', String),
    ('dbi_filepath', POINTER(POINTER(c_char))),
    ('dbi_Head', POINTER(struct_directory) * int(8192)),
    ('dbi_fp', POINTER(FILE)),
    ('dbi_eof', off_t),
    ('dbi_nrec', c_size_t),
    ('dbi_uses', c_int),
    ('dbi_freep', POINTER(struct_mem_map)),
    ('dbi_inmem', POINTER(None)),
    ('dbi_anroot', POINTER(struct_animate)),
    ('dbi_mf', POINTER(struct_bu_mapped_file)),
    ('dbi_clients', struct_bu_ptbl),
    ('dbi_version', c_int),
    ('dbi_wdbp', POINTER(struct_rt_wdb)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/avs.h: 66
class struct_bu_attribute_value_pair(Structure):
    pass

struct_bu_attribute_value_pair.__slots__ = [
    'name',
    'value',
]
struct_bu_attribute_value_pair._fields_ = [
    ('name', String),
    ('value', String),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/avs.h: 89
class struct_bu_attribute_value_set(Structure):
    pass

struct_bu_attribute_value_set.__slots__ = [
    'magic',
    'count',
    'max',
    'readonly_min',
    'readonly_max',
    'avp',
]
struct_bu_attribute_value_set._fields_ = [
    ('magic', c_uint32),
    ('count', c_size_t),
    ('max', c_size_t),
    ('readonly_min', POINTER(None)),
    ('readonly_max', POINTER(None)),
    ('avp', POINTER(struct_bu_attribute_value_pair)),
]

bitv_t = c_ubyte# /usr/brlcad/dev-7.31.0/include/brlcad/bu/bitv.h: 62

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/bitv.h: 108
class struct_bu_bitv(Structure):
    pass

struct_bu_bitv.__slots__ = [
    'l',
    'nbits',
    'bits',
]
struct_bu_bitv._fields_ = [
    ('l', struct_bu_list),
    ('nbits', c_size_t),
    ('bits', bitv_t * int(2)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/color.h: 55
class struct_bu_color(Structure):
    pass

struct_bu_color.__slots__ = [
    'buc_rgb',
]
struct_bu_color._fields_ = [
    ('buc_rgb', hvect_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/parse.h: 210
class struct_bu_external(Structure):
    pass

struct_bu_external.__slots__ = [
    'ext_magic',
    'ext_nbytes',
    'ext_buf',
]
struct_bu_external._fields_ = [
    ('ext_magic', c_uint32),
    ('ext_nbytes', c_size_t),
    ('ext_buf', POINTER(c_uint8)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/../nmg.h: 188
class struct_knot_vector(Structure):
    pass

struct_knot_vector.__slots__ = [
    'magic',
    'k_size',
    'knots',
]
struct_knot_vector._fields_ = [
    ('magic', c_uint32),
    ('k_size', c_int),
    ('knots', POINTER(fastf_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/../nmg.h: 212
class struct_model(Structure):
    pass

struct_model.__slots__ = [
    'magic',
    'r_hd',
    'manifolds',
    'index',
    'maxindex',
]
struct_model._fields_ = [
    ('magic', c_uint32),
    ('r_hd', struct_bu_list),
    ('manifolds', String),
    ('index', c_long),
    ('maxindex', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/../nmg.h: 228
class struct_nmgregion_a(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/../nmg.h: 220
class struct_nmgregion(Structure):
    pass

struct_nmgregion.__slots__ = [
    'l',
    'm_p',
    'ra_p',
    's_hd',
    'index',
]
struct_nmgregion._fields_ = [
    ('l', struct_bu_list),
    ('m_p', POINTER(struct_model)),
    ('ra_p', POINTER(struct_nmgregion_a)),
    ('s_hd', struct_bu_list),
    ('index', c_long),
]

struct_nmgregion_a.__slots__ = [
    'magic',
    'min_pt',
    'max_pt',
    'index',
]
struct_nmgregion_a._fields_ = [
    ('magic', c_uint32),
    ('min_pt', point_t),
    ('max_pt', point_t),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/../nmg.h: 298
class struct_face_g_snurb(Structure):
    pass

struct_face_g_snurb.__slots__ = [
    'l',
    'f_hd',
    'order',
    'u',
    'v',
    's_size',
    'pt_type',
    'ctl_points',
    'dir',
    'min_pt',
    'max_pt',
    'index',
]
struct_face_g_snurb._fields_ = [
    ('l', struct_bu_list),
    ('f_hd', struct_bu_list),
    ('order', c_int * int(2)),
    ('u', struct_knot_vector),
    ('v', struct_knot_vector),
    ('s_size', c_int * int(2)),
    ('pt_type', c_int),
    ('ctl_points', POINTER(fastf_t)),
    ('dir', c_int),
    ('min_pt', point_t),
    ('max_pt', point_t),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 85
class struct__on_brep_placeholder(Structure):
    pass

struct__on_brep_placeholder.__slots__ = [
    'dummy',
]
struct__on_brep_placeholder._fields_ = [
    ('dummy', c_int),
]

ON_Brep = struct__on_brep_placeholder# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 85

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 60
class struct_rt_tor_internal(Structure):
    pass

struct_rt_tor_internal.__slots__ = [
    'magic',
    'v',
    'h',
    'r_h',
    'r_a',
    'a',
    'b',
    'r_b',
]
struct_rt_tor_internal._fields_ = [
    ('magic', c_uint32),
    ('v', point_t),
    ('h', vect_t),
    ('r_h', fastf_t),
    ('r_a', fastf_t),
    ('a', vect_t),
    ('b', vect_t),
    ('r_b', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 79
class struct_rt_tgc_internal(Structure):
    pass

struct_rt_tgc_internal.__slots__ = [
    'magic',
    'v',
    'h',
    'a',
    'b',
    'c',
    'd',
]
struct_rt_tgc_internal._fields_ = [
    ('magic', c_uint32),
    ('v', point_t),
    ('h', vect_t),
    ('a', vect_t),
    ('b', vect_t),
    ('c', vect_t),
    ('d', vect_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 96
class struct_rt_ell_internal(Structure):
    pass

struct_rt_ell_internal.__slots__ = [
    'magic',
    'v',
    'a',
    'b',
    'c',
]
struct_rt_ell_internal._fields_ = [
    ('magic', c_uint32),
    ('v', point_t),
    ('a', vect_t),
    ('b', vect_t),
    ('c', vect_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 111
class struct_rt_superell_internal(Structure):
    pass

struct_rt_superell_internal.__slots__ = [
    'magic',
    'v',
    'a',
    'b',
    'c',
    'n',
    'e',
]
struct_rt_superell_internal._fields_ = [
    ('magic', c_uint32),
    ('v', point_t),
    ('a', vect_t),
    ('b', vect_t),
    ('c', vect_t),
    ('n', c_double),
    ('e', c_double),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 156
class struct_rt_metaball_internal(Structure):
    pass

struct_rt_metaball_internal.__slots__ = [
    'magic',
    'method',
    'threshold',
    'initstep',
    'finalstep',
    'metaball_ctrl_head',
]
struct_rt_metaball_internal._fields_ = [
    ('magic', c_uint32),
    ('method', c_int),
    ('threshold', fastf_t),
    ('initstep', fastf_t),
    ('finalstep', fastf_t),
    ('metaball_ctrl_head', struct_bu_list),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 169
class struct_wdb_metaball_pnt(Structure):
    pass

struct_wdb_metaball_pnt.__slots__ = [
    'l',
    'type',
    'fldstr',
    'sweat',
    'coord',
    'coord2',
]
struct_wdb_metaball_pnt._fields_ = [
    ('l', struct_bu_list),
    ('type', c_int),
    ('fldstr', fastf_t),
    ('sweat', fastf_t),
    ('coord', point_t),
    ('coord2', point_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 191
class struct_rt_arb_internal(Structure):
    pass

struct_rt_arb_internal.__slots__ = [
    'magic',
    'pt',
]
struct_rt_arb_internal._fields_ = [
    ('magic', c_uint32),
    ('pt', point_t * int(8)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 203
class struct_rt_ars_internal(Structure):
    pass

struct_rt_ars_internal.__slots__ = [
    'magic',
    'ncurves',
    'pts_per_curve',
    'curves',
]
struct_rt_ars_internal._fields_ = [
    ('magic', c_uint32),
    ('ncurves', c_size_t),
    ('pts_per_curve', c_size_t),
    ('curves', POINTER(POINTER(fastf_t))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 217
class struct_rt_half_internal(Structure):
    pass

struct_rt_half_internal.__slots__ = [
    'magic',
    'eqn',
]
struct_rt_half_internal._fields_ = [
    ('magic', c_uint32),
    ('eqn', plane_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 229
class struct_rt_grip_internal(Structure):
    pass

struct_rt_grip_internal.__slots__ = [
    'magic',
    'center',
    'normal',
    'mag',
]
struct_rt_grip_internal._fields_ = [
    ('magic', c_uint32),
    ('center', point_t),
    ('normal', vect_t),
    ('mag', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 244
class struct_rt_joint_internal(Structure):
    pass

struct_rt_joint_internal.__slots__ = [
    'magic',
    'location',
    'reference_path_1',
    'reference_path_2',
    'vector1',
    'vector2',
    'value',
]
struct_rt_joint_internal._fields_ = [
    ('magic', c_uint32),
    ('location', point_t),
    ('reference_path_1', struct_bu_vls),
    ('reference_path_2', struct_bu_vls),
    ('vector1', vect_t),
    ('vector2', vect_t),
    ('value', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 263
class struct_rt_pg_face_internal(Structure):
    pass

struct_rt_pg_face_internal.__slots__ = [
    'npts',
    'verts',
    'norms',
]
struct_rt_pg_face_internal._fields_ = [
    ('npts', c_size_t),
    ('verts', POINTER(fastf_t)),
    ('norms', POINTER(fastf_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 268
class struct_rt_pg_internal(Structure):
    pass

struct_rt_pg_internal.__slots__ = [
    'magic',
    'npoly',
    'poly',
    'max_npts',
]
struct_rt_pg_internal._fields_ = [
    ('magic', c_uint32),
    ('npoly', c_size_t),
    ('poly', POINTER(struct_rt_pg_face_internal)),
    ('max_npts', c_size_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 281
class struct_rt_nurb_internal(Structure):
    pass

struct_rt_nurb_internal.__slots__ = [
    'magic',
    'nsrf',
    'srfs',
    'brep',
]
struct_rt_nurb_internal._fields_ = [
    ('magic', c_uint32),
    ('nsrf', c_int),
    ('srfs', POINTER(POINTER(struct_face_g_snurb))),
    ('brep', POINTER(ON_Brep)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 297
class struct_rt_brep_internal(Structure):
    pass

struct_rt_brep_internal.__slots__ = [
    'magic',
    'brep',
]
struct_rt_brep_internal._fields_ = [
    ('magic', c_uint32),
    ('brep', POINTER(ON_Brep)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h: 46
class struct_rt_db_internal(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 323
class struct_rt_ebm_internal(Structure):
    pass

struct_rt_ebm_internal.__slots__ = [
    'magic',
    'name',
    'xdim',
    'ydim',
    'tallness',
    'mat',
    'buf',
    'mp',
    'bip',
    'datasrc',
]
struct_rt_ebm_internal._fields_ = [
    ('magic', c_uint32),
    ('name', c_char * int(256)),
    ('xdim', c_uint32),
    ('ydim', c_uint32),
    ('tallness', fastf_t),
    ('mat', mat_t),
    ('buf', POINTER(c_ubyte)),
    ('mp', POINTER(struct_bu_mapped_file)),
    ('bip', POINTER(struct_rt_db_internal)),
    ('datasrc', c_char),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 349
class struct_rt_vol_internal(Structure):
    pass

struct_rt_vol_internal.__slots__ = [
    'magic',
    'file',
    'xdim',
    'ydim',
    'zdim',
    'lo',
    'hi',
    'cellsize',
    'mat',
    'map',
]
struct_rt_vol_internal._fields_ = [
    ('magic', c_uint32),
    ('file', c_char * int(128)),
    ('xdim', c_uint32),
    ('ydim', c_uint32),
    ('zdim', c_uint32),
    ('lo', c_uint32),
    ('hi', c_uint32),
    ('cellsize', vect_t),
    ('mat', mat_t),
    ('map', POINTER(c_ubyte)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 373
class struct_rt_hf_internal(Structure):
    pass

struct_rt_hf_internal.__slots__ = [
    'magic',
    'cfile',
    'dfile',
    'fmt',
    'w',
    'n',
    'shorts',
    'file2mm',
    'v',
    'x',
    'y',
    'xlen',
    'ylen',
    'zscale',
    'mp',
]
struct_rt_hf_internal._fields_ = [
    ('magic', c_uint32),
    ('cfile', c_char * int(128)),
    ('dfile', c_char * int(128)),
    ('fmt', c_char * int(8)),
    ('w', c_uint32),
    ('n', c_uint32),
    ('shorts', c_uint32),
    ('file2mm', fastf_t),
    ('v', vect_t),
    ('x', vect_t),
    ('y', vect_t),
    ('xlen', fastf_t),
    ('ylen', fastf_t),
    ('zscale', fastf_t),
    ('mp', POINTER(struct_bu_mapped_file)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 403
class struct_rt_arbn_internal(Structure):
    pass

struct_rt_arbn_internal.__slots__ = [
    'magic',
    'neqn',
    'eqn',
]
struct_rt_arbn_internal._fields_ = [
    ('magic', c_uint32),
    ('neqn', c_size_t),
    ('eqn', POINTER(plane_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 416
class struct_rt_pipe_internal(Structure):
    pass

struct_rt_pipe_internal.__slots__ = [
    'pipe_magic',
    'pipe_segs_head',
    'pipe_count',
]
struct_rt_pipe_internal._fields_ = [
    ('pipe_magic', c_uint32),
    ('pipe_segs_head', struct_bu_list),
    ('pipe_count', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 423
class struct_wdb_pipe_pnt(Structure):
    pass

struct_wdb_pipe_pnt.__slots__ = [
    'l',
    'pp_coord',
    'pp_id',
    'pp_od',
    'pp_bendradius',
]
struct_wdb_pipe_pnt._fields_ = [
    ('l', struct_bu_list),
    ('pp_coord', point_t),
    ('pp_id', fastf_t),
    ('pp_od', fastf_t),
    ('pp_bendradius', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 438
class struct_rt_part_internal(Structure):
    pass

struct_rt_part_internal.__slots__ = [
    'part_magic',
    'part_V',
    'part_H',
    'part_vrad',
    'part_hrad',
    'part_type',
]
struct_rt_part_internal._fields_ = [
    ('part_magic', c_uint32),
    ('part_V', point_t),
    ('part_H', vect_t),
    ('part_vrad', fastf_t),
    ('part_hrad', fastf_t),
    ('part_type', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 459
class struct_rt_rpc_internal(Structure):
    pass

struct_rt_rpc_internal.__slots__ = [
    'rpc_magic',
    'rpc_V',
    'rpc_H',
    'rpc_B',
    'rpc_r',
]
struct_rt_rpc_internal._fields_ = [
    ('rpc_magic', c_uint32),
    ('rpc_V', point_t),
    ('rpc_H', vect_t),
    ('rpc_B', vect_t),
    ('rpc_r', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 474
class struct_rt_rhc_internal(Structure):
    pass

struct_rt_rhc_internal.__slots__ = [
    'rhc_magic',
    'rhc_V',
    'rhc_H',
    'rhc_B',
    'rhc_r',
    'rhc_c',
]
struct_rt_rhc_internal._fields_ = [
    ('rhc_magic', c_uint32),
    ('rhc_V', point_t),
    ('rhc_H', vect_t),
    ('rhc_B', vect_t),
    ('rhc_r', fastf_t),
    ('rhc_c', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 490
class struct_rt_epa_internal(Structure):
    pass

struct_rt_epa_internal.__slots__ = [
    'epa_magic',
    'epa_V',
    'epa_H',
    'epa_Au',
    'epa_r1',
    'epa_r2',
]
struct_rt_epa_internal._fields_ = [
    ('epa_magic', c_uint32),
    ('epa_V', point_t),
    ('epa_H', vect_t),
    ('epa_Au', vect_t),
    ('epa_r1', fastf_t),
    ('epa_r2', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 506
class struct_rt_ehy_internal(Structure):
    pass

struct_rt_ehy_internal.__slots__ = [
    'ehy_magic',
    'ehy_V',
    'ehy_H',
    'ehy_Au',
    'ehy_r1',
    'ehy_r2',
    'ehy_c',
]
struct_rt_ehy_internal._fields_ = [
    ('ehy_magic', c_uint32),
    ('ehy_V', point_t),
    ('ehy_H', vect_t),
    ('ehy_Au', vect_t),
    ('ehy_r1', fastf_t),
    ('ehy_r2', fastf_t),
    ('ehy_c', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 523
class struct_rt_hyp_internal(Structure):
    pass

struct_rt_hyp_internal.__slots__ = [
    'hyp_magic',
    'hyp_Vi',
    'hyp_Hi',
    'hyp_A',
    'hyp_b',
    'hyp_bnr',
]
struct_rt_hyp_internal._fields_ = [
    ('hyp_magic', c_uint32),
    ('hyp_Vi', point_t),
    ('hyp_Hi', vect_t),
    ('hyp_A', vect_t),
    ('hyp_b', fastf_t),
    ('hyp_bnr', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 539
class struct_rt_eto_internal(Structure):
    pass

struct_rt_eto_internal.__slots__ = [
    'eto_magic',
    'eto_V',
    'eto_N',
    'eto_C',
    'eto_r',
    'eto_rd',
]
struct_rt_eto_internal._fields_ = [
    ('eto_magic', c_uint32),
    ('eto_V', point_t),
    ('eto_N', vect_t),
    ('eto_C', vect_t),
    ('eto_r', fastf_t),
    ('eto_rd', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 556
class struct_rt_dsp_internal(Structure):
    pass

struct_rt_dsp_internal.__slots__ = [
    'magic',
    'dsp_name',
    'dsp_xcnt',
    'dsp_ycnt',
    'dsp_smooth',
    'dsp_cuttype',
    'dsp_mtos',
    'dsp_stom',
    'dsp_buf',
    'dsp_mp',
    'dsp_bip',
    'dsp_datasrc',
]
struct_rt_dsp_internal._fields_ = [
    ('magic', c_uint32),
    ('dsp_name', struct_bu_vls),
    ('dsp_xcnt', c_uint32),
    ('dsp_ycnt', c_uint32),
    ('dsp_smooth', c_ushort),
    ('dsp_cuttype', c_ubyte),
    ('dsp_mtos', mat_t),
    ('dsp_stom', mat_t),
    ('dsp_buf', POINTER(c_ushort)),
    ('dsp_mp', POINTER(struct_bu_mapped_file)),
    ('dsp_bip', POINTER(struct_rt_db_internal)),
    ('dsp_datasrc', c_char),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 597
class struct_rt_curve(Structure):
    pass

struct_rt_curve.__slots__ = [
    'count',
    'reverse',
    'segment',
]
struct_rt_curve._fields_ = [
    ('count', c_size_t),
    ('reverse', POINTER(c_int)),
    ('segment', POINTER(POINTER(None))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 609
class struct_line_seg(Structure):
    pass

struct_line_seg.__slots__ = [
    'magic',
    'start',
    'end',
]
struct_line_seg._fields_ = [
    ('magic', c_uint32),
    ('start', c_int),
    ('end', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 616
class struct_carc_seg(Structure):
    pass

struct_carc_seg.__slots__ = [
    'magic',
    'start',
    'end',
    'radius',
    'center_is_left',
    'orientation',
    'center',
]
struct_carc_seg._fields_ = [
    ('magic', c_uint32),
    ('start', c_int),
    ('end', c_int),
    ('radius', fastf_t),
    ('center_is_left', c_int),
    ('orientation', c_int),
    ('center', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 630
class struct_nurb_seg(Structure):
    pass

struct_nurb_seg.__slots__ = [
    'magic',
    'order',
    'pt_type',
    'k',
    'c_size',
    'ctl_points',
    'weights',
]
struct_nurb_seg._fields_ = [
    ('magic', c_uint32),
    ('order', c_int),
    ('pt_type', c_int),
    ('k', struct_knot_vector),
    ('c_size', c_int),
    ('ctl_points', POINTER(c_int)),
    ('weights', POINTER(fastf_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 642
class struct_bezier_seg(Structure):
    pass

struct_bezier_seg.__slots__ = [
    'magic',
    'degree',
    'ctl_points',
]
struct_bezier_seg._fields_ = [
    ('magic', c_uint32),
    ('degree', c_int),
    ('ctl_points', POINTER(c_int)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 651
class struct_rt_sketch_internal(Structure):
    pass

struct_rt_sketch_internal.__slots__ = [
    'magic',
    'V',
    'u_vec',
    'v_vec',
    'vert_count',
    'verts',
    'curve',
]
struct_rt_sketch_internal._fields_ = [
    ('magic', c_uint32),
    ('V', point_t),
    ('u_vec', vect_t),
    ('v_vec', vect_t),
    ('vert_count', c_size_t),
    ('verts', POINTER(point2d_t)),
    ('curve', struct_rt_curve),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 676
class struct_rt_submodel_internal(Structure):
    pass

struct_rt_submodel_internal.__slots__ = [
    'magic',
    'file',
    'treetop',
    'meth',
    'root2leaf',
    'dbip',
]
struct_rt_submodel_internal._fields_ = [
    ('magic', c_uint32),
    ('file', struct_bu_vls),
    ('treetop', struct_bu_vls),
    ('meth', c_int),
    ('root2leaf', mat_t),
    ('dbip', POINTER(struct_db_i)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 695
class struct_rt_extrude_internal(Structure):
    pass

struct_rt_extrude_internal.__slots__ = [
    'magic',
    'V',
    'h',
    'u_vec',
    'v_vec',
    'keypoint',
    'sketch_name',
    'skt',
]
struct_rt_extrude_internal._fields_ = [
    ('magic', c_uint32),
    ('V', point_t),
    ('h', vect_t),
    ('u_vec', vect_t),
    ('v_vec', vect_t),
    ('keypoint', c_int),
    ('sketch_name', String),
    ('skt', POINTER(struct_rt_sketch_internal)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 720
class struct_rt_revolve_internal(Structure):
    pass

struct_rt_revolve_internal.__slots__ = [
    'magic',
    'v3d',
    'axis3d',
    'v2d',
    'axis2d',
    'r',
    'ang',
    'sketch_name',
    'skt',
]
struct_rt_revolve_internal._fields_ = [
    ('magic', c_uint32),
    ('v3d', point_t),
    ('axis3d', vect_t),
    ('v2d', point2d_t),
    ('axis2d', vect2d_t),
    ('r', vect_t),
    ('ang', fastf_t),
    ('sketch_name', struct_bu_vls),
    ('skt', POINTER(struct_rt_sketch_internal)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 744
class struct_rt_cline_internal(Structure):
    pass

struct_rt_cline_internal.__slots__ = [
    'magic',
    'v',
    'h',
    'radius',
    'thickness',
]
struct_rt_cline_internal._fields_ = [
    ('magic', c_uint32),
    ('v', point_t),
    ('h', vect_t),
    ('radius', fastf_t),
    ('thickness', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 761
class struct_rt_bot_internal(Structure):
    pass

struct_rt_bot_internal.__slots__ = [
    'magic',
    'mode',
    'orientation',
    'bot_flags',
    'num_faces',
    'faces',
    'num_vertices',
    'vertices',
    'thickness',
    'face_mode',
    'num_normals',
    'normals',
    'num_face_normals',
    'face_normals',
    'num_uvs',
    'uvs',
    'num_face_uvs',
    'face_uvs',
    'tie',
]
struct_rt_bot_internal._fields_ = [
    ('magic', c_uint32),
    ('mode', c_ubyte),
    ('orientation', c_ubyte),
    ('bot_flags', c_ubyte),
    ('num_faces', c_size_t),
    ('faces', POINTER(c_int)),
    ('num_vertices', c_size_t),
    ('vertices', POINTER(fastf_t)),
    ('thickness', POINTER(fastf_t)),
    ('face_mode', POINTER(struct_bu_bitv)),
    ('num_normals', c_size_t),
    ('normals', POINTER(fastf_t)),
    ('num_face_normals', c_size_t),
    ('face_normals', POINTER(c_int)),
    ('num_uvs', c_size_t),
    ('uvs', POINTER(fastf_t)),
    ('num_face_uvs', c_size_t),
    ('face_uvs', POINTER(c_int)),
    ('tie', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 828
class struct_rt_bot_list(Structure):
    pass

struct_rt_bot_list.__slots__ = [
    'l',
    'bot',
]
struct_rt_bot_list._fields_ = [
    ('l', struct_bu_list),
    ('bot', POINTER(struct_rt_bot_internal)),
]

enum_anon_51 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_PNT = 0# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_COL = (0 + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_SCA = (0 + 2)# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_NRM = (0 + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_COL_SCA = ((0 + 1) + 2)# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_COL_NRM = ((0 + 1) + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_SCA_NRM = ((0 + 2) + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_TYPE_COL_SCA_NRM = (((0 + 1) + 2) + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

RT_PNT_UNKNOWN = 8# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

rt_pnt_type = enum_anon_51# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 899

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 901
class struct_pnt(Structure):
    pass

struct_pnt.__slots__ = [
    'l',
    'v',
]
struct_pnt._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 905
class struct_pnt_color(Structure):
    pass

struct_pnt_color.__slots__ = [
    'l',
    'v',
    'c',
]
struct_pnt_color._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
    ('c', struct_bu_color),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 910
class struct_pnt_scale(Structure):
    pass

struct_pnt_scale.__slots__ = [
    'l',
    'v',
    's',
]
struct_pnt_scale._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
    ('s', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 915
class struct_pnt_normal(Structure):
    pass

struct_pnt_normal.__slots__ = [
    'l',
    'v',
    'n',
]
struct_pnt_normal._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
    ('n', vect_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 920
class struct_pnt_color_scale(Structure):
    pass

struct_pnt_color_scale.__slots__ = [
    'l',
    'v',
    'c',
    's',
]
struct_pnt_color_scale._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
    ('c', struct_bu_color),
    ('s', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 926
class struct_pnt_color_normal(Structure):
    pass

struct_pnt_color_normal.__slots__ = [
    'l',
    'v',
    'c',
    'n',
]
struct_pnt_color_normal._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
    ('c', struct_bu_color),
    ('n', vect_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 932
class struct_pnt_scale_normal(Structure):
    pass

struct_pnt_scale_normal.__slots__ = [
    'l',
    'v',
    's',
    'n',
]
struct_pnt_scale_normal._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
    ('s', fastf_t),
    ('n', vect_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 938
class struct_pnt_color_scale_normal(Structure):
    pass

struct_pnt_color_scale_normal.__slots__ = [
    'l',
    'v',
    'c',
    's',
    'n',
]
struct_pnt_color_scale_normal._fields_ = [
    ('l', struct_bu_list),
    ('v', point_t),
    ('c', struct_bu_color),
    ('s', fastf_t),
    ('n', vect_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 947
class struct_rt_pnts_internal(Structure):
    pass

struct_rt_pnts_internal.__slots__ = [
    'magic',
    'scale',
    'type',
    'count',
    'point',
]
struct_rt_pnts_internal._fields_ = [
    ('magic', c_uint32),
    ('scale', c_double),
    ('type', rt_pnt_type),
    ('count', c_ulong),
    ('point', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 971
class struct_rt_ant(Structure):
    pass

struct_rt_ant.__slots__ = [
    'count',
    'reverse',
    'segments',
]
struct_rt_ant._fields_ = [
    ('count', c_size_t),
    ('reverse', POINTER(c_int)),
    ('segments', POINTER(POINTER(None))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 981
class struct_txt_seg(Structure):
    pass

struct_txt_seg.__slots__ = [
    'magic',
    'ref_pt',
    'rel_pos',
    'label',
]
struct_txt_seg._fields_ = [
    ('magic', c_uint32),
    ('ref_pt', c_int),
    ('rel_pos', c_int),
    ('label', struct_bu_vls),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1005
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_txt_pos_flag", "cdecl"):
    rt_txt_pos_flag = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_txt_pos_flag", "cdecl")
    rt_txt_pos_flag.argtypes = [POINTER(c_int), c_int, c_int]
    rt_txt_pos_flag.restype = c_int

struct_rt_annot_internal.__slots__ = [
    'magic',
    'V',
    'vert_count',
    'verts',
    'ant',
]
struct_rt_annot_internal._fields_ = [
    ('magic', c_uint32),
    ('V', point_t),
    ('vert_count', c_size_t),
    ('verts', POINTER(point2d_t)),
    ('ant', struct_rt_ant),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1054
class struct_rt_datum_internal(Structure):
    pass

struct_rt_datum_internal.__slots__ = [
    'magic',
    'pnt',
    'dir',
    'w',
    'next',
]
struct_rt_datum_internal._fields_ = [
    ('magic', c_uint32),
    ('pnt', point_t),
    ('dir', vect_t),
    ('w', fastf_t),
    ('next', POINTER(struct_rt_datum_internal)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1073
class struct_rt_hrt_internal(Structure):
    pass

struct_rt_hrt_internal.__slots__ = [
    'hrt_magic',
    'v',
    'xdir',
    'ydir',
    'zdir',
    'd',
]
struct_rt_hrt_internal._fields_ = [
    ('hrt_magic', c_uint32),
    ('v', point_t),
    ('xdir', vect_t),
    ('ydir', vect_t),
    ('zdir', vect_t),
    ('d', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1087
class struct_rt_script_internal(Structure):
    pass

struct_rt_script_internal.__slots__ = [
    'script_magic',
    's_type',
]
struct_rt_script_internal._fields_ = [
    ('script_magic', c_uint32),
    ('s_type', struct_bu_vls),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 147
class union_tree(Union):
    pass

struct_region.__slots__ = [
    'l',
    'reg_name',
    'reg_treetop',
    'reg_bit',
    'reg_regionid',
    'reg_aircode',
    'reg_gmater',
    'reg_los',
    'reg_mater',
    'reg_mfuncs',
    'reg_udata',
    'reg_transmit',
    'reg_instnum',
    'reg_all_unions',
    'reg_is_fastgen',
    'attr_values',
]
struct_region._fields_ = [
    ('l', struct_bu_list),
    ('reg_name', String),
    ('reg_treetop', POINTER(union_tree)),
    ('reg_bit', c_int),
    ('reg_regionid', c_int),
    ('reg_aircode', c_int),
    ('reg_gmater', c_int),
    ('reg_los', c_int),
    ('reg_mater', struct_mater_info),
    ('reg_mfuncs', POINTER(None)),
    ('reg_udata', POINTER(None)),
    ('reg_transmit', c_int),
    ('reg_instnum', c_long),
    ('reg_all_unions', c_short),
    ('reg_is_fastgen', c_short),
    ('attr_values', struct_bu_attribute_value_set),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 43
class struct_bound_rpp(Structure):
    pass

struct_bound_rpp.__slots__ = [
    'min',
    'max',
]
struct_bound_rpp._fields_ = [
    ('min', point_t),
    ('max', point_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 48
class struct_rt_functab(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 60
class struct_rt_i(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 56
class struct_soltab(Structure):
    pass

struct_soltab.__slots__ = [
    'l',
    'l2',
    'st_meth',
    'st_rtip',
    'st_uses',
    'st_id',
    'st_center',
    'st_aradius',
    'st_bradius',
    'st_specific',
    'st_dp',
    'st_min',
    'st_max',
    'st_bit',
    'st_regions',
    'st_matp',
    'st_path',
    'st_npieces',
    'st_piecestate_num',
    'st_piece_rpps',
]
struct_soltab._fields_ = [
    ('l', struct_bu_list),
    ('l2', struct_bu_list),
    ('st_meth', POINTER(struct_rt_functab)),
    ('st_rtip', POINTER(struct_rt_i)),
    ('st_uses', c_long),
    ('st_id', c_int),
    ('st_center', point_t),
    ('st_aradius', fastf_t),
    ('st_bradius', fastf_t),
    ('st_specific', POINTER(None)),
    ('st_dp', POINTER(struct_directory)),
    ('st_min', point_t),
    ('st_max', point_t),
    ('st_bit', c_long),
    ('st_regions', struct_bu_ptbl),
    ('st_matp', matp_t),
    ('st_path', struct_db_full_path),
    ('st_npieces', c_long),
    ('st_piecestate_num', c_long),
    ('st_piece_rpps', POINTER(struct_bound_rpp)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 101
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_free_soltab", "cdecl"):
    rt_free_soltab = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_free_soltab", "cdecl")
    rt_free_soltab.argtypes = [POINTER(struct_soltab)]
    rt_free_soltab.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 104
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_pr_soltab", "cdecl"):
    rt_pr_soltab = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_pr_soltab", "cdecl")
    rt_pr_soltab.argtypes = [POINTER(struct_soltab)]
    rt_pr_soltab.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tol.h: 89
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_tol_default", "cdecl"):
    rt_tol_default = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_tol_default", "cdecl")
    rt_tol_default.argtypes = [POINTER(struct_bn_tol)]
    rt_tol_default.restype = POINTER(struct_bn_tol)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 56
class struct_db_tree_state(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 49
class struct_rt_comb_internal(Structure):
    pass

struct_db_tree_state.__slots__ = [
    'magic',
    'ts_dbip',
    'ts_sofar',
    'ts_regionid',
    'ts_aircode',
    'ts_gmater',
    'ts_los',
    'ts_mater',
    'ts_mat',
    'ts_is_fastgen',
    'ts_attrs',
    'ts_stop_at_regions',
    'ts_region_start_func',
    'ts_region_end_func',
    'ts_leaf_func',
    'ts_ttol',
    'ts_tol',
    'ts_m',
    'ts_rtip',
    'ts_resp',
]
struct_db_tree_state._fields_ = [
    ('magic', c_uint32),
    ('ts_dbip', POINTER(struct_db_i)),
    ('ts_sofar', c_int),
    ('ts_regionid', c_int),
    ('ts_aircode', c_int),
    ('ts_gmater', c_int),
    ('ts_los', c_int),
    ('ts_mater', struct_mater_info),
    ('ts_mat', mat_t),
    ('ts_is_fastgen', c_int),
    ('ts_attrs', struct_bu_attribute_value_set),
    ('ts_stop_at_regions', c_int),
    ('ts_region_start_func', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_rt_comb_internal), POINTER(None))),
    ('ts_region_end_func', CFUNCTYPE(UNCHECKED(POINTER(union_tree)), POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(union_tree), POINTER(None))),
    ('ts_leaf_func', CFUNCTYPE(UNCHECKED(POINTER(union_tree)), POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_rt_db_internal), POINTER(None))),
    ('ts_ttol', POINTER(struct_bg_tess_tol)),
    ('ts_tol', POINTER(struct_bn_tol)),
    ('ts_m', POINTER(POINTER(struct_model))),
    ('ts_rtip', POINTER(struct_rt_i)),
    ('ts_resp', POINTER(struct_resource)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 140
class struct_combined_tree_state(Structure):
    pass

struct_combined_tree_state.__slots__ = [
    'magic',
    'cts_s',
    'cts_p',
]
struct_combined_tree_state._fields_ = [
    ('magic', c_uint32),
    ('cts_s', struct_db_tree_state),
    ('cts_p', struct_db_full_path),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 150
class struct_tree_node(Structure):
    pass

struct_tree_node.__slots__ = [
    'magic',
    'tb_op',
    'tb_regionp',
    'tb_left',
    'tb_right',
]
struct_tree_node._fields_ = [
    ('magic', c_uint32),
    ('tb_op', c_int),
    ('tb_regionp', POINTER(struct_region)),
    ('tb_left', POINTER(union_tree)),
    ('tb_right', POINTER(union_tree)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 157
class struct_tree_leaf(Structure):
    pass

struct_tree_leaf.__slots__ = [
    'magic',
    'tu_op',
    'tu_regionp',
    'tu_stp',
]
struct_tree_leaf._fields_ = [
    ('magic', c_uint32),
    ('tu_op', c_int),
    ('tu_regionp', POINTER(struct_region)),
    ('tu_stp', POINTER(struct_soltab)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 163
class struct_tree_cts(Structure):
    pass

struct_tree_cts.__slots__ = [
    'magic',
    'tc_op',
    'tc_pad',
    'tc_ctsp',
]
struct_tree_cts._fields_ = [
    ('magic', c_uint32),
    ('tc_op', c_int),
    ('tc_pad', POINTER(struct_region)),
    ('tc_ctsp', POINTER(struct_combined_tree_state)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 169
class struct_tree_nmgregion(Structure):
    pass

struct_tree_nmgregion.__slots__ = [
    'magic',
    'td_op',
    'td_name',
    'td_r',
]
struct_tree_nmgregion._fields_ = [
    ('magic', c_uint32),
    ('td_op', c_int),
    ('td_name', String),
    ('td_r', POINTER(struct_nmgregion)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 175
class struct_tree_db_leaf(Structure):
    pass

struct_tree_db_leaf.__slots__ = [
    'magic',
    'tl_op',
    'tl_mat',
    'tl_name',
]
struct_tree_db_leaf._fields_ = [
    ('magic', c_uint32),
    ('tl_op', c_int),
    ('tl_mat', matp_t),
    ('tl_name', String),
]

union_tree.__slots__ = [
    'magic',
    'tr_b',
    'tr_a',
    'tr_c',
    'tr_d',
    'tr_l',
]
union_tree._fields_ = [
    ('magic', c_uint32),
    ('tr_b', struct_tree_node),
    ('tr_a', struct_tree_leaf),
    ('tr_c', struct_tree_cts),
    ('tr_d', struct_tree_nmgregion),
    ('tr_l', struct_tree_db_leaf),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 91
class struct_rt_piecestate(Structure):
    pass

struct_resource.__slots__ = [
    're_magic',
    're_cpu',
    're_seg',
    're_seg_blocks',
    're_seglen',
    're_segget',
    're_segfree',
    're_parthead',
    're_partlen',
    're_partget',
    're_partfree',
    're_solid_bitv',
    're_region_ptbl',
    're_nmgfree',
    're_boolstack',
    're_boolslen',
    're_randptr',
    're_nshootray',
    're_nmiss_model',
    're_shots',
    're_shot_hit',
    're_shot_miss',
    're_prune_solrpp',
    're_ndup',
    're_nempty_cells',
    're_pieces',
    're_piece_ndup',
    're_piece_shots',
    're_piece_shot_hit',
    're_piece_shot_miss',
    're_pieces_pending',
    're_tree_hd',
    're_tree_get',
    're_tree_malloc',
    're_tree_free',
    're_directory_hd',
    're_directory_blocks',
]
struct_resource._fields_ = [
    ('re_magic', c_uint32),
    ('re_cpu', c_int),
    ('re_seg', struct_bu_list),
    ('re_seg_blocks', struct_bu_ptbl),
    ('re_seglen', c_long),
    ('re_segget', c_long),
    ('re_segfree', c_long),
    ('re_parthead', struct_bu_list),
    ('re_partlen', c_long),
    ('re_partget', c_long),
    ('re_partfree', c_long),
    ('re_solid_bitv', struct_bu_list),
    ('re_region_ptbl', struct_bu_list),
    ('re_nmgfree', struct_bu_list),
    ('re_boolstack', POINTER(POINTER(union_tree))),
    ('re_boolslen', c_long),
    ('re_randptr', POINTER(c_float)),
    ('re_nshootray', c_long),
    ('re_nmiss_model', c_long),
    ('re_shots', c_long),
    ('re_shot_hit', c_long),
    ('re_shot_miss', c_long),
    ('re_prune_solrpp', c_long),
    ('re_ndup', c_long),
    ('re_nempty_cells', c_long),
    ('re_pieces', POINTER(struct_rt_piecestate)),
    ('re_piece_ndup', c_long),
    ('re_piece_shots', c_long),
    ('re_piece_shot_hit', c_long),
    ('re_piece_shot_miss', c_long),
    ('re_pieces_pending', struct_bu_ptbl),
    ('re_tree_hd', POINTER(union_tree)),
    ('re_tree_get', c_long),
    ('re_tree_malloc', c_long),
    ('re_tree_free', c_long),
    ('re_directory_hd', POINTER(struct_directory)),
    ('re_directory_blocks', struct_bu_ptbl),
]

struct_rt_db_internal.__slots__ = [
    'idb_magic',
    'idb_major_type',
    'idb_minor_type',
    'idb_meth',
    'idb_ptr',
    'idb_avs',
]
struct_rt_db_internal._fields_ = [
    ('idb_magic', c_uint32),
    ('idb_major_type', c_int),
    ('idb_minor_type', c_int),
    ('idb_meth', POINTER(struct_rt_functab)),
    ('idb_ptr', POINTER(None)),
    ('idb_avs', struct_bu_attribute_value_set),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h: 73
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_db_get_internal", "cdecl"):
    rt_db_get_internal = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_db_get_internal", "cdecl")
    rt_db_get_internal.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_directory), POINTER(struct_db_i), mat_t, POINTER(struct_resource)]
    rt_db_get_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h: 88
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_db_put_internal", "cdecl"):
    rt_db_put_internal = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_db_put_internal", "cdecl")
    rt_db_put_internal.argtypes = [POINTER(struct_directory), POINTER(struct_db_i), POINTER(struct_rt_db_internal), POINTER(struct_resource)]
    rt_db_put_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h: 106
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_fwrite_internal", "cdecl"):
    rt_fwrite_internal = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_fwrite_internal", "cdecl")
    rt_fwrite_internal.argtypes = [POINTER(FILE), String, POINTER(struct_rt_db_internal), c_double]
    rt_fwrite_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h: 110
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_db_free_internal", "cdecl"):
    rt_db_free_internal = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_db_free_internal", "cdecl")
    rt_db_free_internal.argtypes = [POINTER(struct_rt_db_internal)]
    rt_db_free_internal.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h: 120
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_db_lookup_internal", "cdecl"):
    rt_db_lookup_internal = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_db_lookup_internal", "cdecl")
    rt_db_lookup_internal.argtypes = [POINTER(struct_db_i), String, POINTER(POINTER(struct_directory)), POINTER(struct_rt_db_internal), c_int, POINTER(struct_resource)]
    rt_db_lookup_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/observer.h: 45
class struct_bu_observer(Structure):
    pass

struct_bu_observer.__slots__ = [
    'magic',
    'observer',
    'cmd',
]
struct_bu_observer._fields_ = [
    ('magic', c_uint32),
    ('observer', struct_bu_vls),
    ('cmd', struct_bu_vls),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/observer.h: 53
class struct_bu_observer_list(Structure):
    pass

struct_bu_observer_list.__slots__ = [
    'size',
    'capacity',
    'observers',
]
struct_bu_observer_list._fields_ = [
    ('size', c_size_t),
    ('capacity', c_size_t),
    ('observers', POINTER(struct_bu_observer)),
]

struct_rt_wdb.__slots__ = [
    'l',
    'type',
    'dbip',
    'wdb_initial_tree_state',
    'wdb_ttol',
    'wdb_tol',
    'wdb_resp',
    'wdb_prestr',
    'wdb_ncharadd',
    'wdb_num_dups',
    'wdb_item_default',
    'wdb_air_default',
    'wdb_mat_default',
    'wdb_los_default',
    'wdb_name',
    'wdb_observers',
    'wdb_interp',
]
struct_rt_wdb._fields_ = [
    ('l', struct_bu_list),
    ('type', c_int),
    ('dbip', POINTER(struct_db_i)),
    ('wdb_initial_tree_state', struct_db_tree_state),
    ('wdb_ttol', struct_bg_tess_tol),
    ('wdb_tol', struct_bn_tol),
    ('wdb_resp', POINTER(struct_resource)),
    ('wdb_prestr', struct_bu_vls),
    ('wdb_ncharadd', c_int),
    ('wdb_num_dups', c_int),
    ('wdb_item_default', c_int),
    ('wdb_air_default', c_int),
    ('wdb_mat_default', c_int),
    ('wdb_los_default', c_int),
    ('wdb_name', struct_bu_vls),
    ('wdb_observers', struct_bu_observer_list),
    ('wdb_interp', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 92
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_fopen", "cdecl"):
    wdb_fopen = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_fopen", "cdecl")
    wdb_fopen.argtypes = [String]
    wdb_fopen.restype = POINTER(struct_rt_wdb)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 104
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_fopen_v", "cdecl"):
    wdb_fopen_v = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_fopen_v", "cdecl")
    wdb_fopen_v.argtypes = [String, c_int]
    wdb_fopen_v.restype = POINTER(struct_rt_wdb)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 117
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_dbopen", "cdecl"):
    wdb_dbopen = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_dbopen", "cdecl")
    wdb_dbopen.argtypes = [POINTER(struct_db_i), c_int]
    wdb_dbopen.restype = POINTER(struct_rt_wdb)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 131
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_import", "cdecl"):
    wdb_import = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_import", "cdecl")
    wdb_import.argtypes = [POINTER(struct_rt_wdb), POINTER(struct_rt_db_internal), String, mat_t]
    wdb_import.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 144
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_export_external", "cdecl"):
    wdb_export_external = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_export_external", "cdecl")
    wdb_export_external.argtypes = [POINTER(struct_rt_wdb), POINTER(struct_bu_external), String, c_int, c_ubyte]
    wdb_export_external.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 166
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_put_internal", "cdecl"):
    wdb_put_internal = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_put_internal", "cdecl")
    wdb_put_internal.argtypes = [POINTER(struct_rt_wdb), String, POINTER(struct_rt_db_internal), c_double]
    wdb_put_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 190
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_export", "cdecl"):
    wdb_export = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_export", "cdecl")
    wdb_export.argtypes = [POINTER(struct_rt_wdb), String, POINTER(None), c_int, c_double]
    wdb_export.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 195
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_init", "cdecl"):
    wdb_init = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_init", "cdecl")
    wdb_init.argtypes = [POINTER(struct_rt_wdb), POINTER(struct_db_i), c_int]
    wdb_init.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 204
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_close", "cdecl"):
    wdb_close = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_close", "cdecl")
    wdb_close.argtypes = [POINTER(struct_rt_wdb)]
    wdb_close.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 215
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_import_from_path", "cdecl"):
    wdb_import_from_path = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_import_from_path", "cdecl")
    wdb_import_from_path.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), String, POINTER(struct_rt_wdb)]
    wdb_import_from_path.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 231
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("wdb_import_from_path2", "cdecl"):
    wdb_import_from_path2 = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("wdb_import_from_path2", "cdecl")
    wdb_import_from_path2.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), String, POINTER(struct_rt_wdb), matp_t]
    wdb_import_from_path2.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 38
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_get_cgtype", "cdecl"):
    rt_arb_get_cgtype = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_get_cgtype", "cdecl")
    rt_arb_get_cgtype.argtypes = [POINTER(c_int), POINTER(struct_rt_arb_internal), POINTER(struct_bn_tol), POINTER(c_int), POINTER(c_int)]
    rt_arb_get_cgtype.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 44
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_std_type", "cdecl"):
    rt_arb_std_type = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_std_type", "cdecl")
    rt_arb_std_type.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_bn_tol)]
    rt_arb_std_type.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 46
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_centroid", "cdecl"):
    rt_arb_centroid = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_centroid", "cdecl")
    rt_arb_centroid.argtypes = [POINTER(point_t), POINTER(struct_rt_db_internal)]
    rt_arb_centroid.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 48
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_calc_points", "cdecl"):
    rt_arb_calc_points = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_calc_points", "cdecl")
    rt_arb_calc_points.argtypes = [POINTER(struct_rt_arb_internal), c_int, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_calc_points.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 49
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_check_points", "cdecl"):
    rt_arb_check_points = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_check_points", "cdecl")
    rt_arb_check_points.argtypes = [POINTER(struct_rt_arb_internal), c_int, POINTER(struct_bn_tol)]
    rt_arb_check_points.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 52
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_3face_intersect", "cdecl"):
    rt_arb_3face_intersect = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_3face_intersect", "cdecl")
    rt_arb_3face_intersect.argtypes = [point_t, plane_t * int(6), c_int, c_int]
    rt_arb_3face_intersect.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 56
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_calc_planes", "cdecl"):
    rt_arb_calc_planes = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_calc_planes", "cdecl")
    rt_arb_calc_planes.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_arb_internal), c_int, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_calc_planes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 61
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_move_edge", "cdecl"):
    rt_arb_move_edge = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_move_edge", "cdecl")
    rt_arb_move_edge.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_arb_internal), vect_t, c_int, c_int, c_int, c_int, vect_t, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_move_edge.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 71
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_edit", "cdecl"):
    rt_arb_edit = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_edit", "cdecl")
    rt_arb_edit.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_arb_internal), c_int, c_int, vect_t, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_edit.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/arb8.h: 78
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_arb_find_e_nearest_pt2", "cdecl"):
    rt_arb_find_e_nearest_pt2 = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_arb_find_e_nearest_pt2", "cdecl")
    rt_arb_find_e_nearest_pt2.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_rt_db_internal), point_t, mat_t, fastf_t]
    rt_arb_find_e_nearest_pt2.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/hash.h: 47
class struct_bu_hash_tbl(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 49
class struct_rt_view_info(Structure):
    pass

struct_rt_view_info.__slots__ = [
    'vhead',
    'tol',
    'point_spacing',
    'curve_spacing',
    'bot_threshold',
]
struct_rt_view_info._fields_ = [
    ('vhead', POINTER(struct_bu_list)),
    ('tol', POINTER(struct_bn_tol)),
    ('point_spacing', fastf_t),
    ('curve_spacing', fastf_t),
    ('bot_threshold', c_size_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 78
class struct_rt_selection(Structure):
    pass

struct_rt_selection.__slots__ = [
    'obj',
]
struct_rt_selection._fields_ = [
    ('obj', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 86
class struct_rt_selection_set(Structure):
    pass

struct_rt_selection_set.__slots__ = [
    'selections',
    'free_selection',
]
struct_rt_selection_set._fields_ = [
    ('selections', struct_bu_ptbl),
    ('free_selection', CFUNCTYPE(UNCHECKED(None), POINTER(struct_rt_selection))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 104
class struct_rt_object_selections(Structure):
    pass

struct_rt_object_selections.__slots__ = [
    'sets',
]
struct_rt_object_selections._fields_ = [
    ('sets', POINTER(struct_bu_hash_tbl)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 117
class struct_rt_selection_query(Structure):
    pass

struct_rt_selection_query.__slots__ = [
    'start',
    'dir',
    'sorting',
]
struct_rt_selection_query._fields_ = [
    ('start', point_t),
    ('dir', vect_t),
    ('sorting', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 132
class struct_rt_selection_translation(Structure):
    pass

struct_rt_selection_translation.__slots__ = [
    'dx',
    'dy',
    'dz',
]
struct_rt_selection_translation._fields_ = [
    ('dx', fastf_t),
    ('dy', fastf_t),
    ('dz', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 148
class union_anon_53(Union):
    pass

union_anon_53.__slots__ = [
    'tran',
]
union_anon_53._fields_ = [
    ('tran', struct_rt_selection_translation),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 144
class struct_rt_selection_operation(Structure):
    pass

struct_rt_selection_operation.__slots__ = [
    'type',
    'parameters',
]
struct_rt_selection_operation._fields_ = [
    ('type', c_int),
    ('parameters', union_anon_53),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 57
class struct_bot_specific(Structure):
    pass

struct_bot_specific.__slots__ = [
    'bot_mode',
    'bot_orientation',
    'bot_flags',
    'bot_ntri',
    'bot_thickness',
    'bot_facemode',
    'bot_facelist',
    'bot_facearray',
    'bot_tri_per_piece',
    'tie',
]
struct_bot_specific._fields_ = [
    ('bot_mode', c_ubyte),
    ('bot_orientation', c_ubyte),
    ('bot_flags', c_ubyte),
    ('bot_ntri', c_size_t),
    ('bot_thickness', POINTER(fastf_t)),
    ('bot_facemode', POINTER(struct_bu_bitv)),
    ('bot_facelist', POINTER(None)),
    ('bot_facearray', POINTER(POINTER(None))),
    ('bot_tri_per_piece', c_size_t),
    ('tie', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 76
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_prep_pieces", "cdecl"):
    rt_bot_prep_pieces = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_prep_pieces", "cdecl")
    rt_bot_prep_pieces.argtypes = [POINTER(struct_bot_specific), POINTER(struct_soltab), c_size_t, POINTER(struct_bn_tol)]
    rt_bot_prep_pieces.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 81
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_botface", "cdecl"):
    rt_botface = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_botface", "cdecl")
    rt_botface.argtypes = [POINTER(struct_soltab), POINTER(struct_bot_specific), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_size_t, POINTER(struct_bn_tol)]
    rt_botface.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 91
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_get_edge_list", "cdecl"):
    rt_bot_get_edge_list = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_get_edge_list", "cdecl")
    rt_bot_get_edge_list.argtypes = [POINTER(struct_rt_bot_internal), POINTER(POINTER(c_size_t))]
    rt_bot_get_edge_list.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 93
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_edge_in_list", "cdecl"):
    rt_bot_edge_in_list = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_edge_in_list", "cdecl")
    rt_bot_edge_in_list.argtypes = [c_size_t, c_size_t, POINTER(c_size_t), c_size_t]
    rt_bot_edge_in_list.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 97
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_plot", "cdecl"):
    rt_bot_plot = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_plot", "cdecl")
    rt_bot_plot.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_bot_plot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 102
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_plot_poly", "cdecl"):
    rt_bot_plot_poly = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_plot_poly", "cdecl")
    rt_bot_plot_poly.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_bot_plot_poly.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 106
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_find_v_nearest_pt2", "cdecl"):
    rt_bot_find_v_nearest_pt2 = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_find_v_nearest_pt2", "cdecl")
    rt_bot_find_v_nearest_pt2.argtypes = [POINTER(struct_rt_bot_internal), point_t, mat_t]
    rt_bot_find_v_nearest_pt2.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 109
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_find_e_nearest_pt2", "cdecl"):
    rt_bot_find_e_nearest_pt2 = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_find_e_nearest_pt2", "cdecl")
    rt_bot_find_e_nearest_pt2.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(struct_rt_bot_internal), point_t, mat_t]
    rt_bot_find_e_nearest_pt2.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 110
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_propget", "cdecl"):
    rt_bot_propget = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_propget", "cdecl")
    rt_bot_propget.argtypes = [POINTER(struct_rt_bot_internal), String]
    rt_bot_propget.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 112
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_vertex_fuse", "cdecl"):
    rt_bot_vertex_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_vertex_fuse", "cdecl")
    rt_bot_vertex_fuse.argtypes = [POINTER(struct_rt_bot_internal), POINTER(struct_bn_tol)]
    rt_bot_vertex_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 114
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_face_fuse", "cdecl"):
    rt_bot_face_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_face_fuse", "cdecl")
    rt_bot_face_fuse.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_face_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 115
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_condense", "cdecl"):
    rt_bot_condense = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_condense", "cdecl")
    rt_bot_condense.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_condense.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 116
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_smooth", "cdecl"):
    rt_bot_smooth = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_smooth", "cdecl")
    rt_bot_smooth.argtypes = [POINTER(struct_rt_bot_internal), String, POINTER(struct_db_i), fastf_t]
    rt_bot_smooth.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 120
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_flip", "cdecl"):
    rt_bot_flip = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_flip", "cdecl")
    rt_bot_flip.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_flip.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 121
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_sync", "cdecl"):
    rt_bot_sync = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_sync", "cdecl")
    rt_bot_sync.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_sync.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 122
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_split", "cdecl"):
    rt_bot_split = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_split", "cdecl")
    rt_bot_split.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_split.restype = POINTER(struct_rt_bot_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 123
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_patches", "cdecl"):
    rt_bot_patches = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_patches", "cdecl")
    rt_bot_patches.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_patches.restype = POINTER(struct_rt_bot_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 124
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_list_free", "cdecl"):
    rt_bot_list_free = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_list_free", "cdecl")
    rt_bot_list_free.argtypes = [POINTER(struct_rt_bot_list), c_int]
    rt_bot_list_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 127
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_same_orientation", "cdecl"):
    rt_bot_same_orientation = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_same_orientation", "cdecl")
    rt_bot_same_orientation.argtypes = [POINTER(c_int), POINTER(c_int)]
    rt_bot_same_orientation.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 130
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_tess", "cdecl"):
    rt_bot_tess = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_tess", "cdecl")
    rt_bot_tess.argtypes = [POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_bot_tess.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 136
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_merge", "cdecl"):
    rt_bot_merge = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_merge", "cdecl")
    rt_bot_merge.argtypes = [c_size_t, POINTER(POINTER(struct_rt_bot_internal))]
    rt_bot_merge.restype = POINTER(struct_rt_bot_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 141
try:
    rt_bot_minpieces = (c_size_t).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"], "rt_bot_minpieces")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 142
try:
    rt_bot_tri_per_piece = (c_size_t).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"], "rt_bot_tri_per_piece")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 143
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_sort_faces", "cdecl"):
    rt_bot_sort_faces = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_sort_faces", "cdecl")
    rt_bot_sort_faces.argtypes = [POINTER(struct_rt_bot_internal), c_size_t]
    rt_bot_sort_faces.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 145
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_decimate", "cdecl"):
    rt_bot_decimate = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_decimate", "cdecl")
    rt_bot_decimate.argtypes = [POINTER(struct_rt_bot_internal), fastf_t, fastf_t, fastf_t]
    rt_bot_decimate.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 149
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_bot_decimate_gct", "cdecl"):
    rt_bot_decimate_gct = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_bot_decimate_gct", "cdecl")
    rt_bot_decimate_gct.argtypes = [POINTER(struct_rt_bot_internal), fastf_t]
    rt_bot_decimate_gct.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 37
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_brep_plot", "cdecl"):
    rt_brep_plot = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_brep_plot", "cdecl")
    rt_brep_plot.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_brep_plot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 42
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_brep_plot_poly", "cdecl"):
    rt_brep_plot_poly = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_brep_plot_poly", "cdecl")
    rt_brep_plot_poly.argtypes = [POINTER(struct_bu_list), POINTER(struct_db_full_path), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_brep_plot_poly.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 52
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_brep_valid", "cdecl"):
    rt_brep_valid = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_brep_valid", "cdecl")
    rt_brep_valid.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int]
    rt_brep_valid.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 57
for _lib in _libs.values():
    if not _lib.has("rt_brep_normalize", "cdecl"):
        continue
    rt_brep_normalize = _lib.get("rt_brep_normalize", "cdecl")
    rt_brep_normalize.argtypes = [POINTER(struct_rt_db_internal), c_double]
    rt_brep_normalize.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 62
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_brep_plate_mode", "cdecl"):
    rt_brep_plate_mode = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_brep_plate_mode", "cdecl")
    rt_brep_plate_mode.argtypes = [POINTER(struct_rt_db_internal)]
    rt_brep_plate_mode.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 67
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_brep_plate_mode_getvals", "cdecl"):
    rt_brep_plate_mode_getvals = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_brep_plate_mode_getvals", "cdecl")
    rt_brep_plate_mode_getvals.argtypes = [POINTER(c_double), POINTER(c_int), POINTER(struct_rt_db_internal)]
    rt_brep_plate_mode_getvals.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/cline.h: 38
try:
    rt_cline_radius = (fastf_t).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"], "rt_cline_radius")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/dsp.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("dsp_pos", "cdecl"):
    dsp_pos = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("dsp_pos", "cdecl")
    dsp_pos.argtypes = [point_t, POINTER(struct_soltab), point_t]
    dsp_pos.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/ell.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_ell_16pnts", "cdecl"):
    rt_ell_16pnts = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_ell_16pnts", "cdecl")
    rt_ell_16pnts.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t)]
    rt_ell_16pnts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/epa.h: 33
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_ell", "cdecl"):
    rt_ell = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_ell", "cdecl")
    rt_ell.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_int]
    rt_ell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/hf.h: 33
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_hf_to_dsp", "cdecl"):
    rt_hf_to_dsp = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_hf_to_dsp", "cdecl")
    rt_hf_to_dsp.argtypes = [POINTER(struct_rt_db_internal)]
    rt_hf_to_dsp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 35
for _lib in _libs.values():
    if not _lib.has("rt_vls_metaball_pnt", "cdecl"):
        continue
    rt_vls_metaball_pnt = _lib.get("rt_vls_metaball_pnt", "cdecl")
    rt_vls_metaball_pnt.argtypes = [POINTER(struct_bu_vls), c_int, POINTER(struct_rt_db_internal), c_double]
    rt_vls_metaball_pnt.restype = None
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 39
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_metaball_pnt_print", "cdecl"):
    rt_metaball_pnt_print = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_metaball_pnt_print", "cdecl")
    rt_metaball_pnt_print.argtypes = [POINTER(struct_wdb_metaball_pnt), c_double]
    rt_metaball_pnt_print.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 40
for _lib in _libs.values():
    if not _lib.has("rt_metaball_ck", "cdecl"):
        continue
    rt_metaball_ck = _lib.get("rt_metaball_ck", "cdecl")
    rt_metaball_ck.argtypes = [POINTER(struct_bu_list)]
    rt_metaball_ck.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 41
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_metaball_point_value", "cdecl"):
    rt_metaball_point_value = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_metaball_point_value", "cdecl")
    rt_metaball_point_value.argtypes = [POINTER(point_t), POINTER(struct_rt_metaball_internal)]
    rt_metaball_point_value.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 43
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_metaball_point_inside", "cdecl"):
    rt_metaball_point_inside = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_metaball_point_inside", "cdecl")
    rt_metaball_point_inside.argtypes = [POINTER(point_t), POINTER(struct_rt_metaball_internal)]
    rt_metaball_point_inside.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 45
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_metaball_lookup_type_id", "cdecl"):
    rt_metaball_lookup_type_id = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_metaball_lookup_type_id", "cdecl")
    rt_metaball_lookup_type_id.argtypes = [String]
    rt_metaball_lookup_type_id.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 46
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_metaball_lookup_type_name", "cdecl"):
    rt_metaball_lookup_type_name = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_metaball_lookup_type_name", "cdecl")
    rt_metaball_lookup_type_name.argtypes = [c_int]
    rt_metaball_lookup_type_name.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/metaball.h: 47
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_metaball_add_point", "cdecl"):
    rt_metaball_add_point = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_metaball_add_point", "cdecl")
    rt_metaball_add_point.argtypes = [POINTER(struct_rt_metaball_internal), POINTER(point_t), fastf_t, fastf_t]
    rt_metaball_add_point.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pg.h: 35
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_pg_to_bot", "cdecl"):
    rt_pg_to_bot = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_pg_to_bot", "cdecl")
    rt_pg_to_bot.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_bn_tol), POINTER(struct_resource)]
    rt_pg_to_bot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pg.h: 38
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_pg_plot", "cdecl"):
    rt_pg_plot = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_pg_plot", "cdecl")
    rt_pg_plot.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_pg_plot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pg.h: 43
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_pg_plot_poly", "cdecl"):
    rt_pg_plot_poly = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_pg_plot_poly", "cdecl")
    rt_pg_plot_poly.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_pg_plot_poly.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pipe.h: 35
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_vls_pipe_pnt", "cdecl"):
    rt_vls_pipe_pnt = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_vls_pipe_pnt", "cdecl")
    rt_vls_pipe_pnt.argtypes = [POINTER(struct_bu_vls), c_int, POINTER(struct_rt_db_internal), c_double]
    rt_vls_pipe_pnt.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pipe.h: 39
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_pipe_pnt_print", "cdecl"):
    rt_pipe_pnt_print = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_pipe_pnt_print", "cdecl")
    rt_pipe_pnt_print.argtypes = [POINTER(struct_wdb_pipe_pnt), c_double]
    rt_pipe_pnt_print.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/pipe.h: 40
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_pipe_ck", "cdecl"):
    rt_pipe_ck = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_pipe_ck", "cdecl")
    rt_pipe_ck.argtypes = [POINTER(struct_bu_list)]
    rt_pipe_ck.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/rhc.h: 34
class struct_rt_pnt_node(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/rhc.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_mk_hyperbola", "cdecl"):
    rt_mk_hyperbola = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_mk_hyperbola", "cdecl")
    rt_mk_hyperbola.argtypes = [POINTER(struct_rt_pnt_node), fastf_t, fastf_t, fastf_t, fastf_t, fastf_t]
    rt_mk_hyperbola.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/rpc.h: 33
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_mk_parabola", "cdecl"):
    rt_mk_parabola = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_mk_parabola", "cdecl")
    rt_mk_parabola.argtypes = [POINTER(struct_rt_pnt_node), fastf_t, fastf_t, fastf_t, fastf_t]
    rt_mk_parabola.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 36
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("curve_to_vlist", "cdecl"):
    curve_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("curve_to_vlist", "cdecl")
    curve_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_bg_tess_tol), point_t, vect_t, vect_t, POINTER(struct_rt_sketch_internal), POINTER(struct_rt_curve)]
    curve_to_vlist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 44
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_check_curve", "cdecl"):
    rt_check_curve = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_check_curve", "cdecl")
    rt_check_curve.argtypes = [POINTER(struct_rt_curve), POINTER(struct_rt_sketch_internal), c_int]
    rt_check_curve.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 48
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_curve_reverse_segment", "cdecl"):
    rt_curve_reverse_segment = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_curve_reverse_segment", "cdecl")
    rt_curve_reverse_segment.argtypes = [POINTER(c_uint32)]
    rt_curve_reverse_segment.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 49
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_curve_order_segments", "cdecl"):
    rt_curve_order_segments = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_curve_order_segments", "cdecl")
    rt_curve_order_segments.argtypes = [POINTER(struct_rt_curve)]
    rt_curve_order_segments.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 51
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_copy_curve", "cdecl"):
    rt_copy_curve = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_copy_curve", "cdecl")
    rt_copy_curve.argtypes = [POINTER(struct_rt_curve), POINTER(struct_rt_curve)]
    rt_copy_curve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 54
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_curve_free", "cdecl"):
    rt_curve_free = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_curve_free", "cdecl")
    rt_curve_free.argtypes = [POINTER(struct_rt_curve)]
    rt_curve_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 55
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_copy_curve", "cdecl"):
    rt_copy_curve = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_copy_curve", "cdecl")
    rt_copy_curve.argtypes = [POINTER(struct_rt_curve), POINTER(struct_rt_curve)]
    rt_copy_curve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 57
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_copy_sketch", "cdecl"):
    rt_copy_sketch = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_copy_sketch", "cdecl")
    rt_copy_sketch.argtypes = [POINTER(struct_rt_sketch_internal)]
    rt_copy_sketch.restype = POINTER(struct_rt_sketch_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/sketch.h: 58
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("curve_to_tcl_list", "cdecl"):
    curve_to_tcl_list = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("curve_to_tcl_list", "cdecl")
    curve_to_tcl_list.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_curve)]
    curve_to_tcl_list.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/tgc.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_pnt_sort", "cdecl"):
    rt_pnt_sort = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_pnt_sort", "cdecl")
    rt_pnt_sort.argtypes = [POINTER(fastf_t), c_int]
    rt_pnt_sort.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/tor.h: 32
if _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].has("rt_num_circular_segments", "cdecl"):
    rt_num_circular_segments = _libs["/usr/brlcad/dev-7.31.0/lib/libwdb.so"].get("rt_num_circular_segments", "cdecl")
    rt_num_circular_segments.argtypes = [c_double, c_double]
    rt_num_circular_segments.restype = c_int

# <built-in>
try:
    __FLT_EPSILON__ = 1.1920928955078125e-07
except:
    pass

# <built-in>
try:
    __DBL_EPSILON__ = (c_double (ord_if_char(2.220446049250313e-16))).value
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 146
def FMAX(a, b):
    return (a > b) and a or b

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 150
def FMIN(a, b):
    return (a < b) and a or b

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 159
try:
    HAVE_U_TYPES = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 165
try:
    _FILE_OFFSET_BITS = 64
except:
    pass

# /usr/include/linux/limits.h: 13
try:
    PATH_MAX = 4096
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 196
try:
    __STDC_LIMIT_MACROS = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 199
try:
    __STDC_CONSTANT_MACROS = 1
except:
    pass

b_off_t = off_t# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 222

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 245
def GCC_PREREQ(major, minor):
    return 0

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 269
def ICC_PREREQ(version):
    return 0

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 320
def UNUSED(parameter):
    return parameter

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 341
def LIKELY(expression):
    return expression

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 362
def UNLIKELY(expression):
    return expression

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 469
def CPP_STR(x):
    return x

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 479
def CPP_XSTR(x):
    return (CPP_STR (x))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 109
try:
    _USE_MATH_DEFINES = 1
except:
    pass

# /usr/include/math.h: 62
try:
    HUGE_VALF = float('inf')
except:
    pass

# /usr/include/math.h: 93
try:
    INFINITY = HUGE_VALF
except:
    pass

# /usr/lib/gcc/x86_64-linux-gnu/9/include/float.h: 113
try:
    FLT_EPSILON = __FLT_EPSILON__
except:
    pass

# /usr/lib/gcc/x86_64-linux-gnu/9/include/float.h: 114
try:
    DBL_EPSILON = __DBL_EPSILON__
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 128
try:
    M_1_2PI = 0.15915494309189535
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 143
try:
    M_EULER = 0.5772156649015329
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 158
try:
    M_LNPI = 1.1447298858494002
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 164
try:
    M_2PI = 6.283185307179586
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 170
try:
    M_PI_3 = 1.0471975511965979
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 182
try:
    M_SQRT3 = 1.7320508075688772
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 185
try:
    M_SQRTPI = 1.772453850905516
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 189
try:
    DEG2RAD = 0.017453292519943295
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 192
try:
    RAD2DEG = 57.29577951308232
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 234
try:
    MAX_FASTF = 1e+73
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 235
try:
    SQRT_MAX_FASTF = 1e+36
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 236
try:
    SMALL_FASTF = 1e-77
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 240
try:
    SQRT_SMALL_FASTF = 1e-39
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 245
try:
    SMALL = SQRT_SMALL_FASTF
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 288
try:
    VDIVIDE_TOL = DBL_EPSILON
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 293
try:
    VUNITIZE_TOL = FLT_EPSILON
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 301
try:
    ELEMENTS_PER_VECT2D = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 304
try:
    ELEMENTS_PER_POINT2D = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 307
try:
    ELEMENTS_PER_VECT = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 310
try:
    ELEMENTS_PER_POINT = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 313
try:
    ELEMENTS_PER_HVECT = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 316
try:
    ELEMENTS_PER_HPOINT = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 319
try:
    ELEMENTS_PER_PLANE = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 322
try:
    ELEMENTS_PER_MAT = (ELEMENTS_PER_PLANE * ELEMENTS_PER_PLANE)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 422
def INVALID(n):
    return (not ((n > (-INFINITY)) and (n < INFINITY)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 428
def VINVALID(v):
    return (((INVALID ((v [X]))) or (INVALID ((v [Y])))) or (INVALID ((v [Z]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 434
def V2INVALID(v):
    return ((INVALID ((v [X]))) or (INVALID ((v [Y]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 440
def HINVALID(v):
    return ((((INVALID ((v [X]))) or (INVALID ((v [Y])))) or (INVALID ((v [Z])))) or (INVALID ((v [W]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 461
def NEAR_ZERO(val, epsilon):
    return ((val > (-epsilon)) and (val < epsilon))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 468
def VNEAR_ZERO(v, tol):
    return (((NEAR_ZERO ((v [X]), tol)) and (NEAR_ZERO ((v [Y]), tol))) and (NEAR_ZERO ((v [Z]), tol)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 477
def V2NEAR_ZERO(v, tol):
    return ((NEAR_ZERO ((v [X]), tol)) and (NEAR_ZERO ((v [Y]), tol)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 496
def ZERO(_a):
    return (NEAR_ZERO (_a, SMALL_FASTF))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 504
def VZERO(_a):
    return (VNEAR_ZERO (_a, SMALL_FASTF))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 512
def V2ZERO(_a):
    return (V2NEAR_ZERO (_a, SMALL_FASTF))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 527
def NEAR_EQUAL(_a, _b, _tol):
    return (NEAR_ZERO ((_a - _b), _tol))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 533
def VNEAR_EQUAL(_a, _b, _tol):
    return (((NEAR_EQUAL ((_a [X]), (_b [X]), _tol)) and (NEAR_EQUAL ((_a [Y]), (_b [Y]), _tol))) and (NEAR_EQUAL ((_a [Z]), (_b [Z]), _tol)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 542
def V2NEAR_EQUAL(a, b, tol):
    return ((NEAR_EQUAL ((a [X]), (b [X]), tol)) and (NEAR_EQUAL ((a [Y]), (b [Y]), tol)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 550
def HNEAR_EQUAL(_a, _b, _tol):
    return ((((NEAR_EQUAL ((_a [X]), (_b [X]), _tol)) and (NEAR_EQUAL ((_a [Y]), (_b [Y]), _tol))) and (NEAR_EQUAL ((_a [Z]), (_b [Z]), _tol))) and (NEAR_EQUAL ((_a [W]), (_b [W]), _tol)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 562
def EQUAL(_a, _b):
    return (NEAR_EQUAL (_a, _b, SMALL_FASTF))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 571
def VEQUAL(_a, _b):
    return (VNEAR_EQUAL (_a, _b, SMALL_FASTF))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 577
def V2EQUAL(_a, _b):
    return (V2NEAR_EQUAL (_a, _b, SMALL_FASTF))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 583
def HEQUAL(_a, _b):
    return (HNEAR_EQUAL (_a, _b, SMALL_FASTF))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 587
def DIST_PNT_PLANE(_pt, _pl):
    return ((VDOT (_pt, _pl)) - (_pl [W]))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 590
def DIST_PNT_PNT_SQ(_a, _b):
    return (((((_a [X]) - (_b [X])) * ((_a [X]) - (_b [X]))) + (((_a [Y]) - (_b [Y])) * ((_a [Y]) - (_b [Y])))) + (((_a [Z]) - (_b [Z])) * ((_a [Z]) - (_b [Z]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 594
def DIST_PNT_PNT(_a, _b):
    return (sqrt ((DIST_PNT_PNT_SQ (_a, _b))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 597
def DIST_PNT2_PNT2_SQ(_a, _b):
    return ((((_a [X]) - (_b [X])) * ((_a [X]) - (_b [X]))) + (((_a [Y]) - (_b [Y])) * ((_a [Y]) - (_b [Y]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 600
def DIST_PNT2_PNT2(_a, _b):
    return (sqrt ((DIST_PNT2_PNT2_SQ (_a, _b))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1431
def MAGSQ(v):
    return ((((v [X]) * (v [X])) + ((v [Y]) * (v [Y]))) + ((v [Z]) * (v [Z])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1432
def MAG2SQ(v):
    return (((v [X]) * (v [X])) + ((v [Y]) * (v [Y])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1439
def MAGNITUDE(v):
    return (sqrt ((MAGSQ (v))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1445
def MAGNITUDE2(v):
    return (sqrt ((MAG2SQ (v))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1473
def V2CROSS(a, b):
    return (((a [X]) * (b [Y])) - ((a [Y]) * (b [X])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1482
def VDOT(a, b):
    return ((((a [X]) * (b [X])) + ((a [Y]) * (b [Y]))) + ((a [Z]) * (b [Z])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1484
def V2DOT(a, b):
    return (((a [X]) * (b [X])) + ((a [Y]) * (b [Y])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1486
def HDOT(a, b):
    return (((((a [X]) * (b [X])) + ((a [Y]) * (b [Y]))) + ((a [Z]) * (b [Z]))) + ((a [W]) * (b [W])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1539
def VSUB2DOT(_pt2, _pt, _vec):
    return (((((_pt2 [X]) - (_pt [X])) * (_vec [X])) + (((_pt2 [Y]) - (_pt [Y])) * (_vec [Y]))) + (((_pt2 [Z]) - (_pt [Z])) * (_vec [Z])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1561
def INTCLAMP(_a):
    return (NEAR_EQUAL (_a, (rint (_a)), VUNITIZE_TOL)) and (rint (_a)) or _a

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1928
def QMAGSQ(a):
    return (((((a [X]) * (a [X])) + ((a [Y]) * (a [Y]))) + ((a [Z]) * (a [Z]))) + ((a [W]) * (a [W])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1933
def QMAGNITUDE(a):
    return (sqrt ((QMAGSQ (a))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1936
def QDOT(a, b):
    return (((((a [X]) * (b [X])) + ((a [Y]) * (b [Y]))) + ((a [Z]) * (b [Z]))) + ((a [W]) * (b [W])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 1995
def V3RPP_DISJOINT(_l1, _h1, _l2, _h2):
    return (((((((_l1 [X]) > (_h2 [X])) or ((_l1 [Y]) > (_h2 [Y]))) or ((_l1 [Z]) > (_h2 [Z]))) or ((_l2 [X]) > (_h1 [X]))) or ((_l2 [Y]) > (_h1 [Y]))) or ((_l2 [Z]) > (_h1 [Z])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 2003
def V3RPP_DISJOINT_TOL(_l1, _h1, _l2, _h2, _t):
    return (((((((_l1 [X]) > ((_h2 [X]) + _t)) or ((_l1 [Y]) > ((_h2 [Y]) + _t))) or ((_l1 [Z]) > ((_h2 [Z]) + _t))) or ((_l2 [X]) > ((_h1 [X]) + _t))) or ((_l2 [Y]) > ((_h1 [Y]) + _t))) or ((_l2 [Z]) > ((_h1 [Z]) + _t)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 2012
def V3RPP_OVERLAP(_l1, _h1, _l2, _h2):
    return (not (((((((_l1 [X]) > (_h2 [X])) or ((_l1 [Y]) > (_h2 [Y]))) or ((_l1 [Z]) > (_h2 [Z]))) or ((_l2 [X]) > (_h1 [X]))) or ((_l2 [Y]) > (_h1 [Y]))) or ((_l2 [Z]) > (_h1 [Z]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 2020
def V3RPP_OVERLAP_TOL(_l1, _h1, _l2, _h2, _t):
    return (not (((((((_l1 [X]) > ((_h2 [X]) + _t)) or ((_l1 [Y]) > ((_h2 [Y]) + _t))) or ((_l1 [Z]) > ((_h2 [Z]) + _t))) or ((_l2 [X]) > ((_h1 [X]) + _t))) or ((_l2 [Y]) > ((_h1 [Y]) + _t))) or ((_l2 [Z]) > ((_h1 [Z]) + _t))))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 2033
def V3PNT_IN_RPP(_pt, _lo, _hi):
    return (((((((_pt [X]) >= (_lo [X])) and ((_pt [X]) <= (_hi [X]))) and ((_pt [Y]) >= (_lo [Y]))) and ((_pt [Y]) <= (_hi [Y]))) and ((_pt [Z]) >= (_lo [Z]))) and ((_pt [Z]) <= (_hi [Z])))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 2043
def V3PNT_IN_RPP_TOL(_pt, _lo, _hi, _t):
    return (((((((_pt [X]) >= ((_lo [X]) - _t)) and ((_pt [X]) <= ((_hi [X]) + _t))) and ((_pt [Y]) >= ((_lo [Y]) - _t))) and ((_pt [Y]) <= ((_hi [Y]) + _t))) and ((_pt [Z]) >= ((_lo [Z]) - _t))) and ((_pt [Z]) <= ((_hi [Z]) + _t)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 2052
def V3PNT_OUT_RPP_TOL(_pt, _lo, _hi, _t):
    return (((((((_pt [X]) < ((_lo [X]) - _t)) or ((_pt [X]) > ((_hi [X]) + _t))) or ((_pt [Y]) < ((_lo [Y]) - _t))) or ((_pt [Y]) > ((_hi [Y]) + _t))) or ((_pt [Z]) < ((_lo [Z]) - _t))) or ((_pt [Z]) > ((_hi [Z]) + _t)))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 2063
def V3RPP1_IN_RPP2(_lo1, _hi1, _lo2, _hi2):
    return (((((((_lo1 [X]) >= (_lo2 [X])) and ((_hi1 [X]) <= (_hi2 [X]))) and ((_lo1 [Y]) >= (_lo2 [Y]))) and ((_hi1 [Y]) <= (_hi2 [Y]))) and ((_lo1 [Z]) >= (_lo2 [Z]))) and ((_hi1 [Z]) <= (_hi2 [Z])))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/defines.h: 50
try:
    BRLCAD_OK = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/defines.h: 51
try:
    BRLCAD_ERROR = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/defines.h: 66
try:
    BU_DIR_SEPARATOR = b'/'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/defines.h: 77
try:
    MAXPATHLEN = PATH_MAX
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/defines.h: 96
try:
    BU_PATH_SEPARATOR = b':'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 74
try:
    BU_VLS_MAGIC = 2301836219
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 83
try:
    BN_TOL_MAGIC = 2563191995
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 99
try:
    RT_BREP_INTERNAL_MAGIC = 1112687952
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 136
try:
    BU_LIST_NULL = cast(0, POINTER(struct_bu_list))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 147
def BU_LIST_MAGIC_EQUAL(_l, _magic):
    return (((_l.contents.magic).value) == _magic)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 188
def BU_LIST_IS_INITIALIZED(_headp):
    return ((cast(_headp, POINTER(struct_bu_list)) != BU_LIST_NULL) and (LIKELY ((((_headp.contents.forw).value) != BU_LIST_NULL))))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 308
def BU_LIST_IS_EMPTY(headp):
    return (((headp.contents.forw).value) == headp)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 309
def BU_LIST_NON_EMPTY(headp):
    return (((headp.contents.forw).value) != headp)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 312
def BU_LIST_IS_CLEAR(headp):
    return (((((headp.contents.magic).value) == 0) and (((headp.contents.forw).value) == BU_LIST_NULL)) and (((headp.contents.back).value) == BU_LIST_NULL))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 335
def BU_LIST_IS_HEAD(p, headp):
    return (cast(p, POINTER(struct_bu_list)) == cast(headp, POINTER(struct_bu_list)))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 337
def BU_LIST_NOT_HEAD(p, headp):
    return (not (BU_LIST_IS_HEAD (p, headp)))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 343
def BU_LIST_PREV_IS_HEAD(p, headp):
    return (((cast(p, POINTER(struct_bu_list)).contents.back).value) == cast(headp, POINTER(struct_bu_list)))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 345
def BU_LIST_PREV_NOT_HEAD(p, headp):
    return (not (BU_LIST_PREV_IS_HEAD (p, headp)))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 351
def BU_LIST_NEXT_IS_HEAD(p, headp):
    return (((cast(p, POINTER(struct_bu_list)).contents.forw).value) == cast(headp, POINTER(struct_bu_list)))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 353
def BU_LIST_NEXT_NOT_HEAD(p, headp):
    return (not (BU_LIST_NEXT_IS_HEAD (p, headp)))

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 429
def BU_LIST_FIRST_MAGIC(headp):
    return ((headp.contents.forw).contents.magic)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 430
def BU_LIST_LAST_MAGIC(headp):
    return ((headp.contents.back).contents.magic)

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 61
try:
    BU_VLS_NULL = cast(0, POINTER(struct_bu_vls))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 89
def BU_VLS_IS_INITIALIZED(_vp):
    return ((cast(_vp, POINTER(struct_bu_vls)) != BU_VLS_NULL) and (((_vp.contents.vls_magic).value) == BU_VLS_MAGIC))

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/defines.h: 45
try:
    BN_AZIMUTH = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/defines.h: 46
try:
    BN_ELEVATION = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/defines.h: 47
try:
    BN_TWIST = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h: 105
def BN_TOL_IS_INITIALIZED(_p):
    return ((cast(_p, POINTER(struct_bn_tol)) != cast(0, POINTER(struct_bn_tol))) and (LIKELY ((((_p.contents.magic).value) == BN_TOL_MAGIC))))

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h: 110
try:
    BN_TOL_DIST = 0.0005
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h: 116
def BN_VECT_ARE_PARALLEL(_dot, _tol):
    return (_dot <= (-SMALL_FASTF)) and (NEAR_EQUAL (_dot, (-1.0), (_tol.contents.perp))) or (NEAR_EQUAL (_dot, 1.0, (_tol.contents.perp)))

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h: 123
def BN_VECT_ARE_PERP(_dot, _tol):
    return (_dot < 0) and ((-_dot) <= ((_tol.contents.perp).value)) or (_dot <= ((_tol.contents.perp).value))

# /usr/brlcad/dev-7.31.0/include/brlcad/bg/defines.h: 47
try:
    BG_CW = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bg/defines.h: 48
try:
    BG_CCW = (-1)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 76
try:
    ID_NULL = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 77
try:
    ID_TOR = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 78
try:
    ID_TGC = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 79
try:
    ID_ELL = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 80
try:
    ID_ARB8 = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 81
try:
    ID_ARS = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 82
try:
    ID_HALF = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 83
try:
    ID_REC = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 84
try:
    ID_POLY = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 85
try:
    ID_BSPLINE = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 86
try:
    ID_SPH = 10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 87
try:
    ID_NMG = 11
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 88
try:
    ID_EBM = 12
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 89
try:
    ID_VOL = 13
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 90
try:
    ID_ARBN = 14
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 91
try:
    ID_PIPE = 15
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 92
try:
    ID_PARTICLE = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 93
try:
    ID_RPC = 17
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 94
try:
    ID_RHC = 18
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 95
try:
    ID_EPA = 19
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 96
try:
    ID_EHY = 20
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 97
try:
    ID_ETO = 21
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 98
try:
    ID_GRIP = 22
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 99
try:
    ID_JOINT = 23
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 100
try:
    ID_HF = 24
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 101
try:
    ID_DSP = 25
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 102
try:
    ID_SKETCH = 26
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 103
try:
    ID_EXTRUDE = 27
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 104
try:
    ID_SUBMODEL = 28
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 105
try:
    ID_CLINE = 29
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 106
try:
    ID_BOT = 30
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 112
try:
    ID_MAX_SOLID = 46
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 117
try:
    ID_COMBINATION = 31
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 118
try:
    ID_UNUSED1 = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 119
try:
    ID_BINUNIF = 33
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 120
try:
    ID_UNUSED2 = 34
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 121
try:
    ID_CONSTRAINT = 39
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 125
try:
    ID_SUPERELL = 35
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 126
try:
    ID_METABALL = 36
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 127
try:
    ID_BREP = 37
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 128
try:
    ID_HYP = 38
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 129
try:
    ID_REVOLVE = 40
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 130
try:
    ID_PNTS = 41
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 131
try:
    ID_ANNOT = 42
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 132
try:
    ID_HRT = 43
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 133
try:
    ID_DATUM = 44
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 134
try:
    ID_SCRIPT = 45
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 135
try:
    ID_MAXIMUM = 46
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 147
try:
    RT_DBNHASH = 8192
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 165
def RT_DBHASH(sum):
    return ((c_size_t (ord_if_char(sum))).value & (RT_DBNHASH - 1))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 169
try:
    RT_DEFAULT_MINPIECES = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 170
try:
    RT_DEFAULT_TRIS_PER_PIECE = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 171
try:
    RT_DEFAULT_MINTIE = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 174
try:
    BACKING_DIST = (-2.0)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 175
try:
    OFFSET_DIST = 0.01
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 180
def RT_BADNUM(n):
    return (not ((n >= (-INFINITY)) and (n <= INFINITY)))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 181
def RT_BADVEC(v):
    return (((RT_BADNUM ((v [X]))) or (RT_BADNUM ((v [Y])))) or (RT_BADNUM ((v [Z]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 184
try:
    RT_MAXLINE = 10240
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/defines.h: 186
try:
    RT_PART_NUBSPT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h: 90
try:
    DBI_NULL = cast(0, POINTER(struct_db_i))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/../nmg.h: 880
def RT_NURB_EXTRACT_COORDS(pt):
    return (pt >> 5)

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 89
try:
    BREP_MAX_ITERATIONS = 100
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 92
try:
    BREP_INTERSECTION_ROOT_EPSILON = 1e-06
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 95
try:
    BREP_INTERSECTION_ROOT_SETTLE = 0.01
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 100
try:
    BREP_GRAZING_DOT_TOL = 1.7453e-05
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 103
try:
    DO_VECTOR = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 106
try:
    BREP_MAX_FT_DEPTH = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 107
try:
    BREP_MAX_LN_DEPTH = 20
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 109
def SIGN(x):
    return (x >= 0) and 1 or (-1)

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 112
try:
    BREP_SURFACE_FLATNESS = 0.85
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 113
try:
    BREP_SURFACE_STRAIGHTNESS = 0.75
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 116
try:
    BREP_MAX_FCP_ITERATIONS = 50
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 119
try:
    BREP_FCP_ROOT_EPSILON = 1e-05
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 124
try:
    BREP_BB_CRV_PNT_CNT = 10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 126
try:
    BREP_CURVE_FLATNESS = 0.95
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 129
try:
    BREP_SURF_SUB_FACTOR = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 130
try:
    BREP_TRIM_SUB_FACTOR = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 141
try:
    BREP_EDGE_MISS_TOLERANCE = 0.005
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 143
try:
    BREP_SAME_POINT_TOLERANCE = 1e-06
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 146
try:
    BREP_UV_DIST_FUZZ = 1e-06
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 149
def ON_PRINT4(p):
    return (((((((('[' << (p [0])) << ', ') << (p [1])) << ', ') << (p [2])) << ', ') << (p [3])) << ']')

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 150
def ON_PRINT3(p):
    return (((((('(' << (p [0])) << ', ') << (p [1])) << ', ') << (p [2])) << ')')

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 151
def ON_PRINT2(p):
    return (((('(' << (p [0])) << ', ') << (p [1])) << ')')

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 152
def PT(p):
    return (ON_PRINT3 (p))

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 153
def PT2(p):
    return (ON_PRINT2 (p))

# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 154
def IVAL(_ival):
    return (((('[' << (((_ival.m_t).value) [0])) << ', ') << (((_ival.m_t).value) [1])) << ']')

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 53
try:
    NAMELEN = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 159
try:
    METABALL_METABALL = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 160
try:
    METABALL_ISOPOTENTIAL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 161
try:
    METABALL_BLOB = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 177
try:
    WDB_METABALLPT_TYPE_POINT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 178
try:
    WDB_METABALLPT_TYPE_LINE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 179
try:
    WDB_METABALL_PNT_NULL = cast(0, POINTER(struct_wdb_metaball_pnt))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 290
def RT_NURB_GET_CONTROL_POINT(_s, _u, _v):
    return ((_s.contents.ctl_points) [(((_v * (((_s.contents.s_size).value) [0])) + _u) * (RT_NURB_EXTRACT_COORDS (((_s.contents.pt_type).value))))])

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 305
def RT_BREP_TEST_MAGIC(_p):
    return (_p and ((cast(_p, POINTER(c_uint32))[0]) == (c_uint32 (ord_if_char(RT_BREP_INTERNAL_MAGIC))).value))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 322
try:
    RT_EBM_NAME_LEN = 256
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 336
try:
    RT_EBM_SRC_FILE = b'f'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 337
try:
    RT_EBM_SRC_OBJ = b'o'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 348
try:
    RT_VOL_NAME_LEN = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 449
try:
    RT_PARTICLE_TYPE_SPHERE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 450
try:
    RT_PARTICLE_TYPE_CYLINDER = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 451
try:
    RT_PARTICLE_TYPE_CONE = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 555
try:
    DSP_NAME_LEN = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 567
try:
    DSP_CUT_DIR_ADAPT = b'a'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 568
try:
    DSP_CUT_DIR_llUR = b'l'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 569
try:
    DSP_CUT_DIR_ULlr = b'L'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 579
try:
    RT_DSP_SRC_V4_FILE = b'4'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 580
try:
    RT_DSP_SRC_FILE = b'f'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 581
try:
    RT_DSP_SRC_OBJ = b'o'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 650
try:
    SKETCH_NAME_LEN = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 835
try:
    RT_BOT_UNORIENTED = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 836
try:
    RT_BOT_CCW = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 837
try:
    RT_BOT_CW = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 840
try:
    RT_BOT_SURFACE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 841
try:
    RT_BOT_SOLID = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 848
try:
    RT_BOT_PLATE = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 854
try:
    RT_BOT_PLATE_NOCOS = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 857
try:
    RT_BOT_HAS_SURFACE_NORMALS = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 858
try:
    RT_BOT_USE_NORMALS = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 859
try:
    RT_BOT_USE_FLOATS = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 860
try:
    RT_BOT_HAS_TEXTURE_UVS = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 861
try:
    RT_BOT_HAS_UNUSED1 = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 862
try:
    RT_BOT_HAS_UNUSED2 = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 863
try:
    RT_BOT_HAS_UNUSED3 = 64
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 864
try:
    RT_BOT_HAS_UNUSED4 = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 991
try:
    RT_TXT_POS_BL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 992
try:
    RT_TXT_POS_BC = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 993
try:
    RT_TXT_POS_BR = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 994
try:
    RT_TXT_POS_ML = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 995
try:
    RT_TXT_POS_MC = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 996
try:
    RT_TXT_POS_MR = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 997
try:
    RT_TXT_POS_TL = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 998
try:
    RT_TXT_POS_TC = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 999
try:
    RT_TXT_POS_TR = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 80
try:
    RT_SOLTAB_NULL = cast(0, POINTER(struct_soltab))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 81
try:
    SOLTAB_NULL = RT_SOLTAB_NULL
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tol.h: 77
try:
    RT_LEN_TOL = 1e-08
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tol.h: 78
try:
    RT_DOT_TOL = 0.001
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tol.h: 79
try:
    RT_PCOEF_TOL = 1e-10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tol.h: 80
try:
    RT_ROOT_TOL = 1e-05
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 80
try:
    RT_WDB_TYPE_DB_DISK = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 81
try:
    RT_WDB_TYPE_DB_DISK_APPEND_ONLY = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 82
try:
    RT_WDB_TYPE_DB_INMEM = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 83
try:
    RT_WDB_TYPE_DB_INMEM_APPEND_ONLY = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 36
try:
    RT_MINVIEWSIZE = 0.0001
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 37
try:
    RT_MINVIEWSCALE = 5e-05
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 121
try:
    RT_SORT_UNSORTED = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 122
try:
    RT_SORT_CLOSEST_TO_START = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 145
try:
    RT_SELECTION_NOP = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 146
try:
    RT_SELECTION_TRANSLATION = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 49
try:
    RT_BREP_OPENNURBS = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 50
try:
    RT_BREP_UV_PARAM = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/brep.h: 51
try:
    RT_BREP_EDGE_CRACK = 4
except:
    pass

bu_list = struct_bu_list# /usr/brlcad/dev-7.31.0/include/brlcad/bu/list.h: 130

bu_vls = struct_bu_vls# /usr/brlcad/dev-7.31.0/include/brlcad/bu/vls.h: 53

bn_tol = struct_bn_tol# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h: 72

bg_tess_tol = struct_bg_tess_tol# /usr/brlcad/dev-7.31.0/include/brlcad/bg/defines.h: 114

rt_annot_internal = struct_rt_annot_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1010

db_i = struct_db_i# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h: 63

rt_wdb = struct_rt_wdb# /usr/brlcad/dev-7.31.0/include/brlcad/rt/wdb.h: 49

_on_brep_placeholder = struct__on_brep_placeholder# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 85

rt_tor_internal = struct_rt_tor_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 60

rt_tgc_internal = struct_rt_tgc_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 79

rt_ell_internal = struct_rt_ell_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 96

rt_superell_internal = struct_rt_superell_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 111

rt_metaball_internal = struct_rt_metaball_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 156

wdb_metaball_pnt = struct_wdb_metaball_pnt# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 169

rt_arb_internal = struct_rt_arb_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 191

rt_ars_internal = struct_rt_ars_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 203

rt_half_internal = struct_rt_half_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 217

rt_grip_internal = struct_rt_grip_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 229

rt_joint_internal = struct_rt_joint_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 244

rt_pg_face_internal = struct_rt_pg_face_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 263

rt_pg_internal = struct_rt_pg_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 268

rt_nurb_internal = struct_rt_nurb_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 281

rt_brep_internal = struct_rt_brep_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 297

rt_db_internal = struct_rt_db_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_internal.h: 46

rt_ebm_internal = struct_rt_ebm_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 323

rt_vol_internal = struct_rt_vol_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 349

rt_hf_internal = struct_rt_hf_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 373

rt_arbn_internal = struct_rt_arbn_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 403

rt_pipe_internal = struct_rt_pipe_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 416

wdb_pipe_pnt = struct_wdb_pipe_pnt# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 423

rt_part_internal = struct_rt_part_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 438

rt_rpc_internal = struct_rt_rpc_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 459

rt_rhc_internal = struct_rt_rhc_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 474

rt_epa_internal = struct_rt_epa_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 490

rt_ehy_internal = struct_rt_ehy_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 506

rt_hyp_internal = struct_rt_hyp_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 523

rt_eto_internal = struct_rt_eto_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 539

rt_dsp_internal = struct_rt_dsp_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 556

rt_curve = struct_rt_curve# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 597

line_seg = struct_line_seg# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 609

carc_seg = struct_carc_seg# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 616

nurb_seg = struct_nurb_seg# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 630

bezier_seg = struct_bezier_seg# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 642

rt_sketch_internal = struct_rt_sketch_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 651

rt_submodel_internal = struct_rt_submodel_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 676

rt_extrude_internal = struct_rt_extrude_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 695

rt_revolve_internal = struct_rt_revolve_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 720

rt_cline_internal = struct_rt_cline_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 744

rt_bot_internal = struct_rt_bot_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 761

rt_bot_list = struct_rt_bot_list# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 828

pnt = struct_pnt# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 901

pnt_color = struct_pnt_color# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 905

pnt_scale = struct_pnt_scale# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 910

pnt_normal = struct_pnt_normal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 915

pnt_color_scale = struct_pnt_color_scale# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 920

pnt_color_normal = struct_pnt_color_normal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 926

pnt_scale_normal = struct_pnt_scale_normal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 932

pnt_color_scale_normal = struct_pnt_color_scale_normal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 938

rt_pnts_internal = struct_rt_pnts_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 947

rt_ant = struct_rt_ant# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 971

txt_seg = struct_txt_seg# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 981

rt_datum_internal = struct_rt_datum_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1054

rt_hrt_internal = struct_rt_hrt_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1073

rt_script_internal = struct_rt_script_internal# /usr/brlcad/dev-7.31.0/include/brlcad/rt/geom.h: 1087

bound_rpp = struct_bound_rpp# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 43

rt_functab = struct_rt_functab# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 48

rt_i = struct_rt_i# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 60

soltab = struct_soltab# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 56

rt_view_info = struct_rt_view_info# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 49

rt_selection = struct_rt_selection# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 78

rt_selection_set = struct_rt_selection_set# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 86

rt_object_selections = struct_rt_object_selections# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 104

rt_selection_query = struct_rt_selection_query# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 117

rt_selection_translation = struct_rt_selection_translation# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 132

rt_selection_operation = struct_rt_selection_operation# /usr/brlcad/dev-7.31.0/include/brlcad/rt/view.h: 144

bot_specific = struct_bot_specific# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/bot.h: 57

rt_pnt_node = struct_rt_pnt_node# /usr/brlcad/dev-7.31.0/include/brlcad/rt/primitives/rhc.h: 34

# No inserted files

# No prefix-stripping

