r"""Wrapper for magic.h

Generated with:
/mnt/sda2/python/virtualenvs/python-brlcad/bin/ctypesgen -I/usr/brlcad/dev-7.31.0/include/brlcad/ /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h -o magic.py -l/usr/brlcad/dev-7.31.0/lib/libbu.so

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

# 1 libraries
# End libraries

# No modules

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 255
if _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].has("bu_badmagic", "cdecl"):
    bu_badmagic = _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].get("bu_badmagic", "cdecl")
    bu_badmagic.argtypes = [POINTER(c_uint32), c_uint32, String, String, c_int]
    bu_badmagic.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 267
if _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].has("bu_identify_magic", "cdecl"):
    bu_identify_magic = _libs["/usr/brlcad/dev-7.31.0/lib/libbu.so"].get("bu_identify_magic", "cdecl")
    bu_identify_magic.argtypes = [c_uint32]
    bu_identify_magic.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 55
try:
    BU_AVS_MAGIC = 1098273569
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 56
try:
    BU_BITV_MAGIC = 1651078262
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 57
try:
    BU_COLOR_MAGIC = 1651860332
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 58
try:
    BU_EXTERNAL_MAGIC = 1989000144
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 59
try:
    BU_HASH_ENTRY_MAGIC = 1212501588
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 60
try:
    BU_HASH_RECORD_MAGIC = 1751217000
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 61
try:
    BU_HASH_TBL_MAGIC = 1212240712
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 62
try:
    BU_HIST_MAGIC = 1214870388
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 63
try:
    BU_HOOK_LIST_MAGIC = 2429935277
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 64
try:
    BU_IMAGE_FILE_MAGIC = 1651074669
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 65
try:
    BU_LIST_HEAD_MAGIC = 16868736
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 66
try:
    BU_MAPPED_FILE_MAGIC = 1298231398
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 67
try:
    BU_OBSERVER_MAGIC = 1702454643
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 68
try:
    BU_PTBL_MAGIC = 1886675564
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 69
try:
    BU_RB_LIST_MAGIC = 1919052915
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 70
try:
    BU_RB_NODE_MAGIC = 1919053423
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 71
try:
    BU_RB_PKG_MAGIC = 1919053931
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 72
try:
    BU_RB_TREE_MAGIC = 1919054962
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 73
try:
    BU_VLB_MAGIC = 1599491138
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 74
try:
    BU_VLS_MAGIC = 2301836219
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 78
try:
    BN_GAUSS_MAGIC = 512256128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 79
try:
    BN_POLY_MAGIC = 1349471353
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 80
try:
    BN_SPM_MAGIC = 1093109368
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 81
try:
    BN_TABDATA_MAGIC = 1400073584
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 82
try:
    BN_TABLE_MAGIC = 1399874420
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 83
try:
    BN_TOL_MAGIC = 2563191995
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 84
try:
    BN_UNIF_MAGIC = 12481632
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 85
try:
    BN_VERT_TREE_MAGIC = 1447383636
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 86
try:
    BN_VLBLOCK_MAGIC = 2551959826
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 87
try:
    BN_VLIST_MAGIC = 2552460404
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 90
try:
    BG_TESS_TOL_MAGIC = 3104378283
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 94
try:
    RT_ARBN_INTERNAL_MAGIC = 404972641
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 95
try:
    RT_ARB_INTERNAL_MAGIC = 2616184848
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 96
try:
    RT_ARS_INTERNAL_MAGIC = 2011020259
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 97
try:
    RT_BINUNIF_INTERNAL_MAGIC = 1114205781
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 98
try:
    RT_BOT_INTERNAL_MAGIC = 1651471474
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 99
try:
    RT_BREP_INTERNAL_MAGIC = 1112687952
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 100
try:
    RT_CLINE_INTERNAL_MAGIC = 1131836280
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 101
try:
    RT_DATUM_INTERNAL_MAGIC = 1684108397
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 102
try:
    RT_DSP_INTERNAL_MAGIC = 3558
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 103
try:
    RT_EBM_INTERNAL_MAGIC = 4177637937
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 104
try:
    RT_EHY_INTERNAL_MAGIC = 2865557137
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 105
try:
    RT_ELL_INTERNAL_MAGIC = 2478515199
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 106
try:
    RT_EPA_INTERNAL_MAGIC = 2865557136
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 107
try:
    RT_ETO_INTERNAL_MAGIC = 2865557138
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 108
try:
    RT_EXTRUDE_INTERNAL_MAGIC = 1702392946
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 109
try:
    RT_GRIP_INTERNAL_MAGIC = 823747077
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 110
try:
    RT_HALF_INTERNAL_MAGIC = 2861022173
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 111
try:
    RT_HF_INTERNAL_MAGIC = 1212565837
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 112
try:
    RT_HYP_INTERNAL_MAGIC = 1752789093
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 113
try:
    RT_JOINT_INTERNAL_MAGIC = 1248815470
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 114
try:
    RT_METABALL_INTERNAL_MAGIC = 1650551916
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 115
try:
    RT_NURB_INTERNAL_MAGIC = 2829277
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 116
try:
    RT_PART_INTERNAL_MAGIC = 2865557127
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 117
try:
    RT_PG_INTERNAL_MAGIC = 2617170055
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 118
try:
    RT_PIPE_INTERNAL_MAGIC = 2111290174
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 119
try:
    RT_REVOLVE_INTERNAL_MAGIC = 1919252076
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 120
try:
    RT_RHC_INTERNAL_MAGIC = 2865557129
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 121
try:
    RT_RPC_INTERNAL_MAGIC = 2865557128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 122
try:
    RT_SKETCH_INTERNAL_MAGIC = 1936418164
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 123
try:
    RT_SUBMODEL_INTERNAL_MAGIC = 1937072749
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 124
try:
    RT_SUPERELL_INTERNAL_MAGIC = 4287871779
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 125
try:
    RT_TGC_INTERNAL_MAGIC = 2864438663
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 126
try:
    RT_TOR_INTERNAL_MAGIC = 2617240967
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 127
try:
    RT_VOL_INTERNAL_MAGIC = 2558239184
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 128
try:
    RT_PNTS_INTERNAL_MAGIC = 1886286963
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 129
try:
    RT_ANNOT_INTERNAL_MAGIC = 1634627183
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 130
try:
    RT_HRT_INTERNAL_MAGIC = 1752331327
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 131
try:
    RT_SCRIPT_INTERNAL_MAGIC = 1935897193
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 135
try:
    NMG_EDGEUSE2_MAGIC = 2442236305
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 136
try:
    NMG_EDGEUSE_MAGIC = 2425393296
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 137
try:
    NMG_EDGE_G_CNURB_MAGIC = 1668182626
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 138
try:
    NMG_EDGE_G_LSEG_MAGIC = 1818847080
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 139
try:
    NMG_EDGE_MAGIC = 858993459
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 140
try:
    NMG_FACEUSE_MAGIC = 1448498774
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 141
try:
    NMG_FACE_G_PLANE_MAGIC = 1919643237
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 142
try:
    NMG_FACE_G_SNURB_MAGIC = 1936618082
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 143
try:
    NMG_FACE_MAGIC = 1162167621
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 144
try:
    NMG_INTER_STRUCT_MAGIC = 2576425248
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 145
try:
    NMG_KNOT_VECTOR_MAGIC = 1802399604
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 146
try:
    NMG_LOOPUSE_MAGIC = 2021161080
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 147
try:
    NMG_LOOP_G_MAGIC = 1679827532
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 148
try:
    NMG_LOOP_MAGIC = 1734829927
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 149
try:
    NMG_MODEL_MAGIC = 303174162
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 150
try:
    NMG_RADIAL_MAGIC = 1382106145
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 151
try:
    NMG_RAY_DATA_MAGIC = 23402353
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 152
try:
    NMG_REGION_A_MAGIC = 1768843040
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 153
try:
    NMG_REGION_MAGIC = 589505315
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 154
try:
    NMG_RT_HIT_MAGIC = 1214870528
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 155
try:
    NMG_RT_HIT_SUB_MAGIC = 1214868736
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 156
try:
    NMG_RT_MISS_MAGIC = 1298756352
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 157
try:
    NMG_SHELL_A_MAGIC = 1696626529
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 158
try:
    NMG_SHELL_MAGIC = 1896313669
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 159
try:
    NMG_VERTEXUSE_A_CNURB_MAGIC = 541159012
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 160
try:
    NMG_VERTEXUSE_A_PLANE_MAGIC = 1768384628
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 161
try:
    NMG_VERTEXUSE_MAGIC = 305402420
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 162
try:
    NMG_VERTEX_G_MAGIC = 1920169735
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 163
try:
    NMG_VERTEX_MAGIC = 1192227
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 167
try:
    RT_ANP_MAGIC = 1095791216
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 168
try:
    RT_AP_MAGIC = 1097887852
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 169
try:
    RT_COMB_MAGIC = 1131375945
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 170
try:
    RT_CONSTRAINT_MAGIC = 1885563245
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 171
try:
    RT_CTS_MAGIC = 2560135459
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 172
try:
    RT_DB_TRAVERSE_MAGIC = 1684173938
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 173
try:
    RT_DBTS_MAGIC = 1684173939
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 174
try:
    RT_DB_INTERNAL_MAGIC = 230414439
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 175
try:
    RT_DIR_MAGIC = 89461266
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 176
try:
    RT_FUNCTAB_MAGIC = 1182092899
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 177
try:
    RT_HIT_MAGIC = 543713652
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 178
try:
    RT_HTBL_MAGIC = 1752457836
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 179
try:
    RT_PIECELIST_MAGIC = 1885564019
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 180
try:
    RT_PIECESTATE_MAGIC = 1885565812
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 181
try:
    RT_RAY_MAGIC = 2020761977
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 182
try:
    RT_REGION_MAGIC = 3757801473
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 183
try:
    RT_SEG_MAGIC = 2562514673
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 184
try:
    RT_SOLTAB2_MAGIC = 2462043618
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 185
try:
    RT_SOLTAB_MAGIC = 2462043616
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 186
try:
    RT_TREE_MAGIC = 2434339217
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 187
try:
    RT_WDB_MAGIC = 1599562850
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 191
try:
    GED_CMD_MAGIC = 1702389091
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 195
try:
    FB_MAGIC = 4227531003
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 196
try:
    FB_WGL_MAGIC = 1464813122
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 197
try:
    FB_OGL_MAGIC = 1481590338
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 198
try:
    FB_X24_MAGIC = 1479689794
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 199
try:
    FB_TK_MAGIC = 1414219330
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 200
try:
    FB_QT_MAGIC = 1364477506
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 201
try:
    FB_DEBUG_MAGIC = 1145194050
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 202
try:
    FB_DISK_MAGIC = 1145652802
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 203
try:
    FB_STK_MAGIC = 1398031938
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 204
try:
    FB_MEMORY_MAGIC = 1296385602
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 205
try:
    FB_REMOTE_MAGIC = 1380795970
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 206
try:
    FB_NULL_MAGIC = 1314211394
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 207
try:
    FB_OSGL_MAGIC = 1330071106
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 211
try:
    ANIMATE_MAGIC = 1095649635
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 212
try:
    CURVE_BEZIER_MAGIC = 1650817641
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 213
try:
    CURVE_CARC_MAGIC = 1667330659
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 214
try:
    CURVE_LSEG_MAGIC = 1819501927
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 215
try:
    CURVE_NURB_MAGIC = 1853190754
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 216
try:
    ANN_TSEG_MAGIC = 1953719655
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 217
try:
    DB5_RAW_INTERNAL_MAGIC = 1681224297
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 218
try:
    DBI_MAGIC = 1461732225
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 219
try:
    DB_FULL_PATH_MAGIC = 1684170352
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 220
try:
    LIGHT_MAGIC = 3688742327
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 221
try:
    MF_MAGIC = 1435926616
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 222
try:
    PIXEL_EXT_MAGIC = 1350071296
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 223
try:
    PL_MAGIC = 200208397
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 224
try:
    PT_HD_MAGIC = 2271770240
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 225
try:
    PT_MAGIC = 2271770241
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 226
try:
    RESOURCE_MAGIC = 2204440629
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 227
try:
    RTI_MAGIC = 2567968344
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 228
try:
    WDB_METABALLPT_MAGIC = 1835167860
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 229
try:
    WDB_PIPESEG_MAGIC = 2535718895
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 230
try:
    WMEMBER_MAGIC = 1125288210
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/magic.h: 231
try:
    ICV_IMAGE_MAGIC = 1651074669
except:
    pass

# No inserted files

# No prefix-stripping

