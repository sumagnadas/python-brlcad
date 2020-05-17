r"""Wrapper for vmath.h

Generated with:
/mnt/sda2/python/virtualenvs/python-brlcad/bin/ctypesgen -I/usr/brlcad/dev-7.31.0/include/brlcad/ /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h /usr/brlcad/dev-7.31.0/include/brlcad/common.h -o vmath.py -l/usr/brlcad/dev-7.31.0/lib/libbu.so -l/usr/brlcad/dev-7.31.0/lib/librt.so

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
_libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/libbu.so")
_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/librt.so")

# 2 libraries
# End libraries

# No modules

u_char = c_ubyte# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 155

u_int = c_uint# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 156

u_long = c_ulong# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 157

u_short = c_ushort# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 158

# /usr/include/x86_64-linux-gnu/bits/mathcalls.h: 143
if _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].has("sqrt", "cdecl"):
    sqrt = _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].get("sqrt", "cdecl")
    sqrt.argtypes = [c_double]
    sqrt.restype = c_double

# /usr/include/x86_64-linux-gnu/bits/mathcalls.h: 256
if _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].has("rint", "cdecl"):
    rint = _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].get("rint", "cdecl")
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

# No inserted files

# No prefix-stripping

