r"""Wrapper for ged.h

Generated with:
./genwrapper.py

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
_libs["/usr/brlcad/dev-7.31.0/lib/libbn.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/libbn.so")
_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/librt.so")
_libs["/usr/brlcad/dev-7.31.0/lib/libged.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/libged.so")

# 4 libraries
# End libraries

# No modules

__off_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 152

__off64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 153

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

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

fastf_t = c_double# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 330

vect_t = fastf_t * int(3)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 345

point_t = fastf_t * int(3)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 351

mat_t = fastf_t * int((4 * 4))# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 366

matp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 369

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 51
class struct_display_list(Structure):
    pass

struct_display_list.__slots__ = [
    'l',
    'dl_dp',
    'dl_path',
    'dl_headSolid',
    'dl_wflag',
]
struct_display_list._fields_ = [
    ('l', struct_bu_list),
    ('dl_dp', POINTER(None)),
    ('dl_path', struct_bu_vls),
    ('dl_headSolid', struct_bu_list),
    ('dl_wflag', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 59
class struct_bview_adc_state(Structure):
    pass

struct_bview_adc_state.__slots__ = [
    'draw',
    'dv_x',
    'dv_y',
    'dv_a1',
    'dv_a2',
    'dv_dist',
    'pos_model',
    'pos_view',
    'pos_grid',
    'a1',
    'a2',
    'dst',
    'anchor_pos',
    'anchor_a1',
    'anchor_a2',
    'anchor_dst',
    'anchor_pt_a1',
    'anchor_pt_a2',
    'anchor_pt_dst',
    'line_color',
    'tick_color',
    'line_width',
]
struct_bview_adc_state._fields_ = [
    ('draw', c_int),
    ('dv_x', c_int),
    ('dv_y', c_int),
    ('dv_a1', c_int),
    ('dv_a2', c_int),
    ('dv_dist', c_int),
    ('pos_model', fastf_t * int(3)),
    ('pos_view', fastf_t * int(3)),
    ('pos_grid', fastf_t * int(3)),
    ('a1', fastf_t),
    ('a2', fastf_t),
    ('dst', fastf_t),
    ('anchor_pos', c_int),
    ('anchor_a1', c_int),
    ('anchor_a2', c_int),
    ('anchor_dst', c_int),
    ('anchor_pt_a1', fastf_t * int(3)),
    ('anchor_pt_a2', fastf_t * int(3)),
    ('anchor_pt_dst', fastf_t * int(3)),
    ('line_color', c_int * int(3)),
    ('tick_color', c_int * int(3)),
    ('line_width', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 84
class struct_bview_axes_state(Structure):
    pass

struct_bview_axes_state.__slots__ = [
    'draw',
    'axes_pos',
    'axes_size',
    'line_width',
    'pos_only',
    'axes_color',
    'label_color',
    'triple_color',
    'tick_enabled',
    'tick_length',
    'tick_major_length',
    'tick_interval',
    'ticks_per_major',
    'tick_threshold',
    'tick_color',
    'tick_major_color',
]
struct_bview_axes_state._fields_ = [
    ('draw', c_int),
    ('axes_pos', point_t),
    ('axes_size', fastf_t),
    ('line_width', c_int),
    ('pos_only', c_int),
    ('axes_color', c_int * int(3)),
    ('label_color', c_int * int(3)),
    ('triple_color', c_int),
    ('tick_enabled', c_int),
    ('tick_length', c_int),
    ('tick_major_length', c_int),
    ('tick_interval', fastf_t),
    ('ticks_per_major', c_int),
    ('tick_threshold', c_int),
    ('tick_color', c_int * int(3)),
    ('tick_major_color', c_int * int(3)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 103
class struct_bview_data_axes_state(Structure):
    pass

struct_bview_data_axes_state.__slots__ = [
    'draw',
    'color',
    'line_width',
    'size',
    'num_points',
    'points',
]
struct_bview_data_axes_state._fields_ = [
    ('draw', c_int),
    ('color', c_int * int(3)),
    ('line_width', c_int),
    ('size', fastf_t),
    ('num_points', c_int),
    ('points', POINTER(point_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 112
class struct_bview_grid_state(Structure):
    pass

struct_bview_grid_state.__slots__ = [
    'draw',
    'snap',
    'anchor',
    'res_h',
    'res_v',
    'res_major_h',
    'res_major_v',
    'color',
]
struct_bview_grid_state._fields_ = [
    ('draw', c_int),
    ('snap', c_int),
    ('anchor', fastf_t * int(3)),
    ('res_h', fastf_t),
    ('res_v', fastf_t),
    ('res_major_h', c_int),
    ('res_major_v', c_int),
    ('color', c_int * int(3)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 123
class struct_bview_interactive_rect_state(Structure):
    pass

struct_bview_interactive_rect_state.__slots__ = [
    'active',
    'draw',
    'line_width',
    'line_style',
    'pos',
    'dim',
    'x',
    'y',
    'width',
    'height',
    'bg',
    'color',
    'cdim',
    'aspect',
]
struct_bview_interactive_rect_state._fields_ = [
    ('active', c_int),
    ('draw', c_int),
    ('line_width', c_int),
    ('line_style', c_int),
    ('pos', c_int * int(2)),
    ('dim', c_int * int(2)),
    ('x', fastf_t),
    ('y', fastf_t),
    ('width', fastf_t),
    ('height', fastf_t),
    ('bg', c_int * int(3)),
    ('color', c_int * int(3)),
    ('cdim', c_int * int(2)),
    ('aspect', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 141
class struct_bview_data_arrow_state(Structure):
    pass

struct_bview_data_arrow_state.__slots__ = [
    'gdas_draw',
    'gdas_color',
    'gdas_line_width',
    'gdas_tip_length',
    'gdas_tip_width',
    'gdas_num_points',
    'gdas_points',
]
struct_bview_data_arrow_state._fields_ = [
    ('gdas_draw', c_int),
    ('gdas_color', c_int * int(3)),
    ('gdas_line_width', c_int),
    ('gdas_tip_length', c_int),
    ('gdas_tip_width', c_int),
    ('gdas_num_points', c_int),
    ('gdas_points', POINTER(point_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 151
class struct_bview_data_label_state(Structure):
    pass

struct_bview_data_label_state.__slots__ = [
    'gdls_draw',
    'gdls_color',
    'gdls_num_labels',
    'gdls_size',
    'gdls_labels',
    'gdls_points',
]
struct_bview_data_label_state._fields_ = [
    ('gdls_draw', c_int),
    ('gdls_color', c_int * int(3)),
    ('gdls_num_labels', c_int),
    ('gdls_size', c_int),
    ('gdls_labels', POINTER(POINTER(c_char))),
    ('gdls_points', POINTER(point_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 160
class struct_bview_data_line_state(Structure):
    pass

struct_bview_data_line_state.__slots__ = [
    'gdls_draw',
    'gdls_color',
    'gdls_line_width',
    'gdls_num_points',
    'gdls_points',
]
struct_bview_data_line_state._fields_ = [
    ('gdls_draw', c_int),
    ('gdls_color', c_int * int(3)),
    ('gdls_line_width', c_int),
    ('gdls_num_points', c_int),
    ('gdls_points', POINTER(point_t)),
]

enum_anon_261 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 168

ClipType = enum_anon_261# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 168

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 173
class struct_anon_262(Structure):
    pass

struct_anon_262.__slots__ = [
    'gpc_num_points',
    'gpc_point',
]
struct_anon_262._fields_ = [
    ('gpc_num_points', c_size_t),
    ('gpc_point', POINTER(point_t)),
]

bview_poly_contour = struct_anon_262# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 173

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 182
class struct_anon_263(Structure):
    pass

struct_anon_263.__slots__ = [
    'gp_num_contours',
    'gp_color',
    'gp_line_width',
    'gp_line_style',
    'gp_hole',
    'gp_contour',
]
struct_anon_263._fields_ = [
    ('gp_num_contours', c_size_t),
    ('gp_color', c_int * int(3)),
    ('gp_line_width', c_int),
    ('gp_line_style', c_int),
    ('gp_hole', POINTER(c_int)),
    ('gp_contour', POINTER(bview_poly_contour)),
]

bview_polygon = struct_anon_263# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 182

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 187
class struct_anon_264(Structure):
    pass

struct_anon_264.__slots__ = [
    'gp_num_polygons',
    'gp_polygon',
]
struct_anon_264._fields_ = [
    ('gp_num_polygons', c_size_t),
    ('gp_polygon', POINTER(bview_polygon)),
]

bview_polygons = struct_anon_264# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 187

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 208
class struct_anon_265(Structure):
    pass

struct_anon_265.__slots__ = [
    'gdps_draw',
    'gdps_moveAll',
    'gdps_color',
    'gdps_line_width',
    'gdps_line_style',
    'gdps_cflag',
    'gdps_target_polygon_i',
    'gdps_curr_polygon_i',
    'gdps_curr_point_i',
    'gdps_prev_point',
    'gdps_clip_type',
    'gdps_scale',
    'gdps_origin',
    'gdps_rotation',
    'gdps_view2model',
    'gdps_model2view',
    'gdps_polygons',
    'gdps_data_vZ',
]
struct_anon_265._fields_ = [
    ('gdps_draw', c_int),
    ('gdps_moveAll', c_int),
    ('gdps_color', c_int * int(3)),
    ('gdps_line_width', c_int),
    ('gdps_line_style', c_int),
    ('gdps_cflag', c_int),
    ('gdps_target_polygon_i', c_size_t),
    ('gdps_curr_polygon_i', c_size_t),
    ('gdps_curr_point_i', c_size_t),
    ('gdps_prev_point', point_t),
    ('gdps_clip_type', ClipType),
    ('gdps_scale', fastf_t),
    ('gdps_origin', point_t),
    ('gdps_rotation', mat_t),
    ('gdps_view2model', mat_t),
    ('gdps_model2view', mat_t),
    ('gdps_polygons', bview_polygons),
    ('gdps_data_vZ', fastf_t),
]

bview_data_polygon_state = struct_anon_265# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 208

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 210
class struct_bview_other_state(Structure):
    pass

struct_bview_other_state.__slots__ = [
    'gos_draw',
    'gos_line_color',
    'gos_text_color',
]
struct_bview_other_state._fields_ = [
    ('gos_draw', c_int),
    ('gos_line_color', c_int * int(3)),
    ('gos_text_color', c_int * int(3)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/dm/bview.h: 216
class struct_bview(Structure):
    pass

struct_bview.__slots__ = [
    'l',
    'gv_scale',
    'gv_size',
    'gv_isize',
    'gv_perspective',
    'gv_aet',
    'gv_eye_pos',
    'gv_keypoint',
    'gv_coord',
    'gv_rotate_about',
    'gv_rotation',
    'gv_center',
    'gv_model2view',
    'gv_pmodel2view',
    'gv_view2model',
    'gv_pmat',
    'gv_callback',
    'gv_clientData',
    'gv_prevMouseX',
    'gv_prevMouseY',
    'gv_minMouseDelta',
    'gv_maxMouseDelta',
    'gv_rscale',
    'gv_sscale',
    'gv_mode',
    'gv_zclip',
    'gv_adc',
    'gv_model_axes',
    'gv_view_axes',
    'gv_data_arrows',
    'gv_data_axes',
    'gv_data_labels',
    'gv_data_lines',
    'gv_data_polygons',
    'gv_sdata_arrows',
    'gv_sdata_axes',
    'gv_sdata_labels',
    'gv_sdata_lines',
    'gv_sdata_polygons',
    'gv_grid',
    'gv_center_dot',
    'gv_prim_labels',
    'gv_view_params',
    'gv_view_scale',
    'gv_rect',
    'gv_adaptive_plot',
    'gv_redraw_on_zoom',
    'gv_x_samples',
    'gv_y_samples',
    'gv_point_scale',
    'gv_curve_scale',
    'gv_data_vZ',
    'gv_bot_threshold',
]
struct_bview._fields_ = [
    ('l', struct_bu_list),
    ('gv_scale', fastf_t),
    ('gv_size', fastf_t),
    ('gv_isize', fastf_t),
    ('gv_perspective', fastf_t),
    ('gv_aet', vect_t),
    ('gv_eye_pos', vect_t),
    ('gv_keypoint', vect_t),
    ('gv_coord', c_char),
    ('gv_rotate_about', c_char),
    ('gv_rotation', mat_t),
    ('gv_center', mat_t),
    ('gv_model2view', mat_t),
    ('gv_pmodel2view', mat_t),
    ('gv_view2model', mat_t),
    ('gv_pmat', mat_t),
    ('gv_callback', CFUNCTYPE(UNCHECKED(None), )),
    ('gv_clientData', POINTER(None)),
    ('gv_prevMouseX', fastf_t),
    ('gv_prevMouseY', fastf_t),
    ('gv_minMouseDelta', fastf_t),
    ('gv_maxMouseDelta', fastf_t),
    ('gv_rscale', fastf_t),
    ('gv_sscale', fastf_t),
    ('gv_mode', c_int),
    ('gv_zclip', c_int),
    ('gv_adc', struct_bview_adc_state),
    ('gv_model_axes', struct_bview_axes_state),
    ('gv_view_axes', struct_bview_axes_state),
    ('gv_data_arrows', struct_bview_data_arrow_state),
    ('gv_data_axes', struct_bview_data_axes_state),
    ('gv_data_labels', struct_bview_data_label_state),
    ('gv_data_lines', struct_bview_data_line_state),
    ('gv_data_polygons', bview_data_polygon_state),
    ('gv_sdata_arrows', struct_bview_data_arrow_state),
    ('gv_sdata_axes', struct_bview_data_axes_state),
    ('gv_sdata_labels', struct_bview_data_label_state),
    ('gv_sdata_lines', struct_bview_data_line_state),
    ('gv_sdata_polygons', bview_data_polygon_state),
    ('gv_grid', struct_bview_grid_state),
    ('gv_center_dot', struct_bview_other_state),
    ('gv_prim_labels', struct_bview_other_state),
    ('gv_view_params', struct_bview_other_state),
    ('gv_view_scale', struct_bview_other_state),
    ('gv_rect', struct_bview_interactive_rect_state),
    ('gv_adaptive_plot', c_int),
    ('gv_redraw_on_zoom', c_int),
    ('gv_x_samples', c_int),
    ('gv_y_samples', c_int),
    ('gv_point_scale', fastf_t),
    ('gv_curve_scale', fastf_t),
    ('gv_data_vZ', fastf_t),
    ('gv_bot_threshold', c_size_t),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/hash.h: 47
class struct_bu_hash_tbl(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/hist.h: 49
class struct_bu_hist(Structure):
    pass

struct_bu_hist.__slots__ = [
    'magic',
    'hg_min',
    'hg_max',
    'hg_clumpsize',
    'hg_nsamples',
    'hg_nbins',
    'hg_bins',
]
struct_bu_hist._fields_ = [
    ('magic', c_uint32),
    ('hg_min', fastf_t),
    ('hg_max', fastf_t),
    ('hg_clumpsize', fastf_t),
    ('hg_nsamples', c_size_t),
    ('hg_nbins', c_size_t),
    ('hg_bins', POINTER(c_long)),
]

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

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/parse.h: 139
class struct_bu_structparse(Structure):
    pass

struct_bu_structparse.__slots__ = [
    'sp_fmt',
    'sp_count',
    'sp_name',
    'sp_offset',
    'sp_hook',
    'sp_desc',
    'sp_default',
]
struct_bu_structparse._fields_ = [
    ('sp_fmt', c_char * int(4)),
    ('sp_count', c_size_t),
    ('sp_name', String),
    ('sp_offset', c_size_t),
    ('sp_hook', CFUNCTYPE(UNCHECKED(None), POINTER(struct_bu_structparse), String, POINTER(None), String, POINTER(None))),
    ('sp_desc', String),
    ('sp_default', POINTER(None)),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tabdata.h: 90
class struct_bn_table(Structure):
    pass

struct_bn_table.__slots__ = [
    'magic',
    'nx',
    'x',
]
struct_bn_table._fields_ = [
    ('magic', c_uint32),
    ('nx', c_size_t),
    ('x', fastf_t * int(1)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tabdata.h: 117
class struct_bn_tabdata(Structure):
    pass

struct_bn_tabdata.__slots__ = [
    'magic',
    'ny',
    'table',
    'y',
]
struct_bn_tabdata._fields_ = [
    ('magic', c_uint32),
    ('ny', c_size_t),
    ('table', POINTER(struct_bn_table)),
    ('y', fastf_t * int(1)),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 212
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

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 228
class struct_nmgregion_a(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 220
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

# /usr/brlcad/dev-7.31.0/include/brlcad/pc.h: 82
class union_anon_279(Union):
    pass

union_anon_279.__slots__ = [
    'expression',
    'ptr',
]
union_anon_279._fields_ = [
    ('expression', struct_bu_vls),
    ('ptr', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/pc.h: 74
class struct_pc_param(Structure):
    pass

struct_pc_param.__slots__ = [
    'l',
    'name',
    'ctype',
    'dtype',
    'data',
]
struct_pc_param._fields_ = [
    ('l', struct_bu_list),
    ('name', struct_bu_vls),
    ('ctype', c_int),
    ('dtype', c_int),
    ('data', union_anon_279),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/pc.h: 88
class struct_pc_constraint_fp(Structure):
    pass

struct_pc_constraint_fp.__slots__ = [
    'nargs',
    'dimension',
    'fp',
]
struct_pc_constraint_fp._fields_ = [
    ('nargs', c_int),
    ('dimension', c_int),
    ('fp', CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(c_double)))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/pc.h: 98
class union_anon_280(Union):
    pass

union_anon_280.__slots__ = [
    'expression',
    'cf',
]
union_anon_280._fields_ = [
    ('expression', struct_bu_vls),
    ('cf', struct_pc_constraint_fp),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/pc.h: 94
class struct_pc_constrnt(Structure):
    pass

struct_pc_constrnt.__slots__ = [
    'l',
    'name',
    'ctype',
    'data',
    'args',
]
struct_pc_constrnt._fields_ = [
    ('l', struct_bu_list),
    ('name', struct_bu_vls),
    ('ctype', c_int),
    ('data', union_anon_280),
    ('args', POINTER(POINTER(c_char))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/pc.h: 105
class struct_pc_pc_set(Structure):
    pass

struct_pc_pc_set.__slots__ = [
    'ps',
    'cs',
]
struct_pc_pc_set._fields_ = [
    ('ps', POINTER(struct_pc_param)),
    ('cs', POINTER(struct_pc_constrnt)),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 191
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 46
class struct_rt_db_internal(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h: 63
class struct_db_i(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 61
class struct_resource(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 59
class struct_directory(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 54
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
class union_anon_300(Union):
    pass

union_anon_300.__slots__ = [
    'file_offset',
    'ptr',
]
union_anon_300._fields_ = [
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
    ('d_un', union_anon_300),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 49
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 69
class struct_rt_functab(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 61
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 41
class struct_xray(Structure):
    pass

struct_xray.__slots__ = [
    'magic',
    'index',
    'r_pt',
    'r_dir',
    'r_min',
    'r_max',
]
struct_xray._fields_ = [
    ('magic', c_uint32),
    ('index', c_int),
    ('r_pt', point_t),
    ('r_dir', vect_t),
    ('r_min', fastf_t),
    ('r_max', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 74
class struct_pixel_ext(Structure):
    pass

struct_pixel_ext.__slots__ = [
    'magic',
    'corner',
]
struct_pixel_ext._fields_ = [
    ('magic', c_uint32),
    ('corner', struct_xray * int(4)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 61
class struct_hit(Structure):
    pass

struct_hit.__slots__ = [
    'hit_magic',
    'hit_dist',
    'hit_point',
    'hit_normal',
    'hit_vpriv',
    'hit_private',
    'hit_surfno',
    'hit_rayp',
]
struct_hit._fields_ = [
    ('hit_magic', c_uint32),
    ('hit_dist', fastf_t),
    ('hit_point', point_t),
    ('hit_normal', vect_t),
    ('hit_vpriv', vect_t),
    ('hit_private', POINTER(None)),
    ('hit_surfno', c_int),
    ('hit_rayp', POINTER(struct_xray)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 118
class struct_curvature(Structure):
    pass

struct_curvature.__slots__ = [
    'crv_pdir',
    'crv_c1',
    'crv_c2',
]
struct_curvature._fields_ = [
    ('crv_pdir', vect_t),
    ('crv_c1', fastf_t),
    ('crv_c2', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 152
class struct_uvcoord(Structure):
    pass

struct_uvcoord.__slots__ = [
    'uv_u',
    'uv_v',
    'uv_du',
    'uv_dv',
]
struct_uvcoord._fields_ = [
    ('uv_u', fastf_t),
    ('uv_v', fastf_t),
    ('uv_du', fastf_t),
    ('uv_dv', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/seg.h: 59
class struct_seg(Structure):
    pass

struct_seg.__slots__ = [
    'l',
    'seg_in',
    'seg_out',
    'seg_stp',
]
struct_seg._fields_ = [
    ('l', struct_bu_list),
    ('seg_in', struct_hit),
    ('seg_out', struct_hit),
    ('seg_stp', POINTER(struct_soltab)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 53
class struct_partition(Structure):
    pass

struct_partition.__slots__ = [
    'pt_magic',
    'pt_forw',
    'pt_back',
    'pt_inseg',
    'pt_inhit',
    'pt_outseg',
    'pt_outhit',
    'pt_regionp',
    'pt_inflip',
    'pt_outflip',
    'pt_overlap_reg',
    'pt_seglist',
]
struct_partition._fields_ = [
    ('pt_magic', c_uint32),
    ('pt_forw', POINTER(struct_partition)),
    ('pt_back', POINTER(struct_partition)),
    ('pt_inseg', POINTER(struct_seg)),
    ('pt_inhit', POINTER(struct_hit)),
    ('pt_outseg', POINTER(struct_seg)),
    ('pt_outhit', POINTER(struct_hit)),
    ('pt_regionp', POINTER(struct_region)),
    ('pt_inflip', c_char),
    ('pt_outflip', c_char),
    ('pt_overlap_reg', POINTER(POINTER(struct_region))),
    ('pt_seglist', struct_bu_ptbl),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/application.h: 99
class struct_application(Structure):
    pass

struct_application.__slots__ = [
    'a_magic',
    'a_ray',
    'a_hit',
    'a_miss',
    'a_onehit',
    'a_ray_length',
    'a_rt_i',
    'a_zero1',
    'a_resource',
    'a_overlap',
    'a_multioverlap',
    'a_logoverlap',
    'a_level',
    'a_x',
    'a_y',
    'a_purpose',
    'a_rbeam',
    'a_diverge',
    'a_return',
    'a_no_booleans',
    'attrs',
    'a_bot_reverse_normal_disabled',
    'a_pixelext',
    'a_finished_segs_hdp',
    'a_Final_Part_hdp',
    'a_inv_dir',
    'a_user',
    'a_uptr',
    'a_spectrum',
    'a_color',
    'a_dist',
    'a_uvec',
    'a_vvec',
    'a_refrac_index',
    'a_cumlen',
    'a_flag',
    'a_zero2',
]
struct_application._fields_ = [
    ('a_magic', c_uint32),
    ('a_ray', struct_xray),
    ('a_hit', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_application), POINTER(struct_partition), POINTER(struct_seg))),
    ('a_miss', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_application))),
    ('a_onehit', c_int),
    ('a_ray_length', fastf_t),
    ('a_rt_i', POINTER(struct_rt_i)),
    ('a_zero1', c_int),
    ('a_resource', POINTER(struct_resource)),
    ('a_overlap', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_application), POINTER(struct_partition), POINTER(struct_region), POINTER(struct_region), POINTER(struct_partition))),
    ('a_multioverlap', CFUNCTYPE(UNCHECKED(None), POINTER(struct_application), POINTER(struct_partition), POINTER(struct_bu_ptbl), POINTER(struct_partition))),
    ('a_logoverlap', CFUNCTYPE(UNCHECKED(None), POINTER(struct_application), POINTER(struct_partition), POINTER(struct_bu_ptbl), POINTER(struct_partition))),
    ('a_level', c_int),
    ('a_x', c_int),
    ('a_y', c_int),
    ('a_purpose', String),
    ('a_rbeam', fastf_t),
    ('a_diverge', fastf_t),
    ('a_return', c_int),
    ('a_no_booleans', c_int),
    ('attrs', POINTER(POINTER(c_char))),
    ('a_bot_reverse_normal_disabled', c_int),
    ('a_pixelext', POINTER(struct_pixel_ext)),
    ('a_finished_segs_hdp', POINTER(struct_seg)),
    ('a_Final_Part_hdp', POINTER(struct_partition)),
    ('a_inv_dir', vect_t),
    ('a_user', c_int),
    ('a_uptr', POINTER(None)),
    ('a_spectrum', POINTER(struct_bn_tabdata)),
    ('a_color', fastf_t * int(3)),
    ('a_dist', fastf_t),
    ('a_uvec', vect_t),
    ('a_vvec', vect_t),
    ('a_refrac_index', fastf_t),
    ('a_cumlen', fastf_t),
    ('a_flag', c_int),
    ('a_zero2', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 56
class struct_db_tree_state(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/nongeom.h: 41
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/piece.h: 57
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/piece.h: 84
class struct_rt_piecelist(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 70
class union_cutter(Union):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 46
class struct_cutnode(Structure):
    pass

struct_cutnode.__slots__ = [
    'cn_type',
    'cn_axis',
    'cn_point',
    'cn_l',
    'cn_r',
]
struct_cutnode._fields_ = [
    ('cn_type', c_int),
    ('cn_axis', c_int),
    ('cn_point', fastf_t),
    ('cn_l', POINTER(union_cutter)),
    ('cn_r', POINTER(union_cutter)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 54
class struct_boxnode(Structure):
    pass

struct_boxnode.__slots__ = [
    'bn_type',
    'bn_min',
    'bn_max',
    'bn_list',
    'bn_len',
    'bn_maxlen',
    'bn_piecelist',
    'bn_piecelen',
    'bn_maxpiecelen',
]
struct_boxnode._fields_ = [
    ('bn_type', c_int),
    ('bn_min', fastf_t * int(3)),
    ('bn_max', fastf_t * int(3)),
    ('bn_list', POINTER(POINTER(struct_soltab))),
    ('bn_len', c_size_t),
    ('bn_maxlen', c_size_t),
    ('bn_piecelist', POINTER(struct_rt_piecelist)),
    ('bn_piecelen', c_size_t),
    ('bn_maxpiecelen', c_size_t),
]

union_cutter.__slots__ = [
    'cut_type',
    'cut_forw',
    'cn',
    'bn',
]
union_cutter._fields_ = [
    ('cut_type', c_int),
    ('cut_forw', POINTER(union_cutter)),
    ('cn', struct_cutnode),
    ('bn', struct_boxnode),
]

struct_rt_comb_internal.__slots__ = [
    'magic',
    'tree',
    'region_flag',
    'is_fastgen',
    'region_id',
    'aircode',
    'GIFTmater',
    'los',
    'rgb_valid',
    'rgb',
    'temperature',
    'shader',
    'material',
    'inherit',
]
struct_rt_comb_internal._fields_ = [
    ('magic', c_uint32),
    ('tree', POINTER(union_tree)),
    ('region_flag', c_char),
    ('is_fastgen', c_char),
    ('region_id', c_long),
    ('aircode', c_long),
    ('GIFTmater', c_long),
    ('los', c_long),
    ('rgb_valid', c_char),
    ('rgb', c_ubyte * int(3)),
    ('temperature', c_float),
    ('shader', struct_bu_vls),
    ('material', struct_bu_vls),
    ('inherit', c_char),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/piece.h: 41
class struct_rt_htbl(Structure):
    pass

struct_rt_htbl.__slots__ = [
    'l',
    'end',
    'blen',
    'hits',
]
struct_rt_htbl._fields_ = [
    ('l', struct_bu_list),
    ('end', c_size_t),
    ('blen', c_size_t),
    ('hits', POINTER(struct_hit)),
]

struct_rt_piecestate.__slots__ = [
    'magic',
    'ray_seqno',
    'stp',
    'shot',
    'mindist',
    'maxdist',
    'htab',
    'cutp',
]
struct_rt_piecestate._fields_ = [
    ('magic', c_uint32),
    ('ray_seqno', c_long),
    ('stp', POINTER(struct_soltab)),
    ('shot', POINTER(struct_bu_bitv)),
    ('mindist', fastf_t),
    ('maxdist', fastf_t),
    ('htab', struct_rt_htbl),
    ('cutp', POINTER(union_cutter)),
]

struct_rt_piecelist.__slots__ = [
    'magic',
    'npieces',
    'pieces',
    'stp',
]
struct_rt_piecelist._fields_ = [
    ('magic', c_uint32),
    ('npieces', c_size_t),
    ('pieces', POINTER(c_long)),
    ('stp', POINTER(struct_soltab)),
]

struct_rt_i.__slots__ = [
    'rti_magic',
    'useair',
    'rti_save_overlaps',
    'rti_dont_instance',
    'rti_hasty_prep',
    'rti_nlights',
    'rti_prismtrace',
    'rti_region_fix_file',
    'rti_space_partition',
    'rti_tol',
    'rti_ttol',
    'rti_max_beam_radius',
    'mdl_min',
    'mdl_max',
    'rti_pmin',
    'rti_pmax',
    'rti_radius',
    'rti_dbip',
    'needprep',
    'Regions',
    'HeadRegion',
    'Orca_hash_tbl',
    'delete_regs',
    'nregions',
    'nsolids',
    'rti_nrays',
    'nmiss_model',
    'nshots',
    'nmiss',
    'nhits',
    'nmiss_tree',
    'nmiss_solid',
    'ndup',
    'nempty_cells',
    'rti_CutHead',
    'rti_inf_box',
    'rti_CutFree',
    'rti_busy_cutter_nodes',
    'rti_cuts_waiting',
    'rti_cut_maxlen',
    'rti_ncut_by_type',
    'rti_cut_totobj',
    'rti_cut_maxdepth',
    'rti_sol_by_type',
    'rti_nsol_by_type',
    'rti_maxsol_by_type',
    'rti_air_discards',
    'rti_hist_cellsize',
    'rti_hist_cell_pieces',
    'rti_hist_cutdepth',
    'rti_Solids',
    'rti_solidheads',
    'rti_resources',
    'rti_cutlen',
    'rti_cutdepth',
    'rti_treetop',
    'rti_uses',
    'rti_nsolids_with_pieces',
    'rti_add_to_new_solids_list',
    'rti_new_solids',
]
struct_rt_i._fields_ = [
    ('rti_magic', c_uint32),
    ('useair', c_int),
    ('rti_save_overlaps', c_int),
    ('rti_dont_instance', c_int),
    ('rti_hasty_prep', c_int),
    ('rti_nlights', c_int),
    ('rti_prismtrace', c_int),
    ('rti_region_fix_file', String),
    ('rti_space_partition', c_int),
    ('rti_tol', struct_bn_tol),
    ('rti_ttol', struct_bg_tess_tol),
    ('rti_max_beam_radius', fastf_t),
    ('mdl_min', point_t),
    ('mdl_max', point_t),
    ('rti_pmin', point_t),
    ('rti_pmax', point_t),
    ('rti_radius', c_double),
    ('rti_dbip', POINTER(struct_db_i)),
    ('needprep', c_int),
    ('Regions', POINTER(POINTER(struct_region))),
    ('HeadRegion', struct_bu_list),
    ('Orca_hash_tbl', POINTER(None)),
    ('delete_regs', struct_bu_ptbl),
    ('nregions', c_size_t),
    ('nsolids', c_size_t),
    ('rti_nrays', c_size_t),
    ('nmiss_model', c_size_t),
    ('nshots', c_size_t),
    ('nmiss', c_size_t),
    ('nhits', c_size_t),
    ('nmiss_tree', c_size_t),
    ('nmiss_solid', c_size_t),
    ('ndup', c_size_t),
    ('nempty_cells', c_size_t),
    ('rti_CutHead', union_cutter),
    ('rti_inf_box', union_cutter),
    ('rti_CutFree', POINTER(union_cutter)),
    ('rti_busy_cutter_nodes', struct_bu_ptbl),
    ('rti_cuts_waiting', struct_bu_ptbl),
    ('rti_cut_maxlen', c_int),
    ('rti_ncut_by_type', c_int * int((2 + 1))),
    ('rti_cut_totobj', c_int),
    ('rti_cut_maxdepth', c_int),
    ('rti_sol_by_type', POINTER(POINTER(struct_soltab)) * int((46 + 1))),
    ('rti_nsol_by_type', c_int * int((46 + 1))),
    ('rti_maxsol_by_type', c_int),
    ('rti_air_discards', c_int),
    ('rti_hist_cellsize', struct_bu_hist),
    ('rti_hist_cell_pieces', struct_bu_hist),
    ('rti_hist_cutdepth', struct_bu_hist),
    ('rti_Solids', POINTER(POINTER(struct_soltab))),
    ('rti_solidheads', struct_bu_list * int(8192)),
    ('rti_resources', struct_bu_ptbl),
    ('rti_cutlen', c_size_t),
    ('rti_cutdepth', c_size_t),
    ('rti_treetop', String),
    ('rti_uses', c_size_t),
    ('rti_nsolids_with_pieces', c_size_t),
    ('rti_add_to_new_solids_list', c_int),
    ('rti_new_solids', struct_bu_ptbl),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 49
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 78
class struct_rt_selection(Structure):
    pass

struct_rt_selection.__slots__ = [
    'obj',
]
struct_rt_selection._fields_ = [
    ('obj', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 86
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 117
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 132
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 148
class union_anon_302(Union):
    pass

union_anon_302.__slots__ = [
    'tran',
]
union_anon_302._fields_ = [
    ('tran', struct_rt_selection_translation),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 144
class struct_rt_selection_operation(Structure):
    pass

struct_rt_selection_operation.__slots__ = [
    'type',
    'parameters',
]
struct_rt_selection_operation._fields_ = [
    ('type', c_int),
    ('parameters', union_anon_302),
]

struct_rt_functab.__slots__ = [
    'magic',
    'ft_name',
    'ft_label',
    'ft_use_rpp',
    'ft_prep',
    'ft_shot',
    'ft_print',
    'ft_norm',
    'ft_piece_shot',
    'ft_piece_hitsegs',
    'ft_uv',
    'ft_curve',
    'ft_classify',
    'ft_free',
    'ft_plot',
    'ft_adaptive_plot',
    'ft_vshot',
    'ft_tessellate',
    'ft_tnurb',
    'ft_brep',
    'ft_import5',
    'ft_export5',
    'ft_import4',
    'ft_export4',
    'ft_ifree',
    'ft_describe',
    'ft_xform',
    'ft_parsetab',
    'ft_internal_size',
    'ft_internal_magic',
    'ft_get',
    'ft_adjust',
    'ft_form',
    'ft_make',
    'ft_params',
    'ft_bbox',
    'ft_volume',
    'ft_surf_area',
    'ft_centroid',
    'ft_oriented_bbox',
    'ft_find_selections',
    'ft_evaluate_selection',
    'ft_process_selection',
    'ft_prep_serialize',
]
struct_rt_functab._fields_ = [
    ('magic', c_uint32),
    ('ft_name', c_char * int(17)),
    ('ft_label', c_char * int(9)),
    ('ft_use_rpp', c_int),
    ('ft_prep', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), POINTER(struct_rt_db_internal), POINTER(struct_rt_i))),
    ('ft_shot', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), POINTER(struct_xray), POINTER(struct_application), POINTER(struct_seg))),
    ('ft_print', CFUNCTYPE(UNCHECKED(None), POINTER(struct_soltab))),
    ('ft_norm', CFUNCTYPE(UNCHECKED(None), POINTER(struct_hit), POINTER(struct_soltab), POINTER(struct_xray))),
    ('ft_piece_shot', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_piecestate), POINTER(struct_rt_piecelist), c_double, POINTER(struct_xray), POINTER(struct_application), POINTER(struct_seg))),
    ('ft_piece_hitsegs', CFUNCTYPE(UNCHECKED(None), POINTER(struct_rt_piecestate), POINTER(struct_seg), POINTER(struct_application))),
    ('ft_uv', CFUNCTYPE(UNCHECKED(None), POINTER(struct_application), POINTER(struct_soltab), POINTER(struct_hit), POINTER(struct_uvcoord))),
    ('ft_curve', CFUNCTYPE(UNCHECKED(None), POINTER(struct_curvature), POINTER(struct_hit), POINTER(struct_soltab))),
    ('ft_classify', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), vect_t, vect_t, POINTER(struct_bn_tol))),
    ('ft_free', CFUNCTYPE(UNCHECKED(None), POINTER(struct_soltab))),
    ('ft_plot', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info))),
    ('ft_adaptive_plot', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_rt_view_info))),
    ('ft_vshot', CFUNCTYPE(UNCHECKED(None), POINTER(POINTER(struct_soltab)), POINTER(POINTER(struct_xray)), POINTER(struct_seg), c_int, POINTER(struct_application))),
    ('ft_tessellate', CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol))),
    ('ft_tnurb', CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bn_tol))),
    ('ft_brep', CFUNCTYPE(UNCHECKED(None), POINTER(POINTER(ON_Brep)), POINTER(struct_rt_db_internal), POINTER(struct_bn_tol))),
    ('ft_import5', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_bu_external), mat_t, POINTER(struct_db_i), POINTER(struct_resource))),
    ('ft_export5', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_external), POINTER(struct_rt_db_internal), c_double, POINTER(struct_db_i), POINTER(struct_resource))),
    ('ft_import4', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_bu_external), mat_t, POINTER(struct_db_i), POINTER(struct_resource))),
    ('ft_export4', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_external), POINTER(struct_rt_db_internal), c_double, POINTER(struct_db_i), POINTER(struct_resource))),
    ('ft_ifree', CFUNCTYPE(UNCHECKED(None), POINTER(struct_rt_db_internal))),
    ('ft_describe', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int, c_double)),
    ('ft_xform', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), mat_t, POINTER(struct_rt_db_internal), c_int, POINTER(struct_db_i))),
    ('ft_parsetab', POINTER(struct_bu_structparse)),
    ('ft_internal_size', c_size_t),
    ('ft_internal_magic', c_uint32),
    ('ft_get', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), String)),
    ('ft_adjust', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int, POINTER(POINTER(c_char)))),
    ('ft_form', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_functab))),
    ('ft_make', CFUNCTYPE(UNCHECKED(None), POINTER(struct_rt_functab), POINTER(struct_rt_db_internal))),
    ('ft_params', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_pc_pc_set), POINTER(struct_rt_db_internal))),
    ('ft_bbox', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(point_t), POINTER(point_t), POINTER(struct_bn_tol))),
    ('ft_volume', CFUNCTYPE(UNCHECKED(None), POINTER(fastf_t), POINTER(struct_rt_db_internal))),
    ('ft_surf_area', CFUNCTYPE(UNCHECKED(None), POINTER(fastf_t), POINTER(struct_rt_db_internal))),
    ('ft_centroid', CFUNCTYPE(UNCHECKED(None), POINTER(point_t), POINTER(struct_rt_db_internal))),
    ('ft_oriented_bbox', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_arb_internal), POINTER(struct_rt_db_internal), fastf_t)),
    ('ft_find_selections', CFUNCTYPE(UNCHECKED(POINTER(struct_rt_selection_set)), POINTER(struct_rt_db_internal), POINTER(struct_rt_selection_query))),
    ('ft_evaluate_selection', CFUNCTYPE(UNCHECKED(POINTER(struct_rt_selection)), POINTER(struct_rt_db_internal), c_int, POINTER(struct_rt_selection), POINTER(struct_rt_selection))),
    ('ft_process_selection', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_db_i), POINTER(struct_rt_selection), POINTER(struct_rt_selection_operation))),
    ('ft_prep_serialize', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), POINTER(struct_rt_db_internal), POINTER(struct_bu_external), POINTER(c_size_t))),
]

db_search_callback_t = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(POINTER(c_char)), POINTER(None))# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 40

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/solid.h: 38
class struct_solid(Structure):
    pass

struct_solid.__slots__ = [
    'l',
    's_size',
    's_csize',
    's_center',
    's_vlist',
    's_vlen',
    's_fullpath',
    's_flag',
    's_iflag',
    's_soldash',
    's_Eflag',
    's_uflag',
    's_dflag',
    's_cflag',
    's_wflag',
    's_basecolor',
    's_color',
    's_regionid',
    's_dlist',
    's_transparency',
    's_dmode',
    's_hiddenLine',
    's_mat',
]
struct_solid._fields_ = [
    ('l', struct_bu_list),
    ('s_size', fastf_t),
    ('s_csize', fastf_t),
    ('s_center', vect_t),
    ('s_vlist', struct_bu_list),
    ('s_vlen', c_int),
    ('s_fullpath', struct_db_full_path),
    ('s_flag', c_char),
    ('s_iflag', c_char),
    ('s_soldash', c_char),
    ('s_Eflag', c_char),
    ('s_uflag', c_char),
    ('s_dflag', c_char),
    ('s_cflag', c_char),
    ('s_wflag', c_char),
    ('s_basecolor', c_ubyte * int(3)),
    ('s_color', c_ubyte * int(3)),
    ('s_regionid', c_short),
    ('s_dlist', c_uint),
    ('s_transparency', fastf_t),
    ('s_dmode', c_int),
    ('s_hiddenLine', c_int),
    ('s_mat', mat_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/process.h: 49
class struct_bu_process(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 117
class struct_ged_subprocess(Structure):
    pass

struct_ged_subprocess.__slots__ = [
    'l',
    'p',
    'chan',
    'aborted',
]
struct_ged_subprocess._fields_ = [
    ('l', struct_bu_list),
    ('p', POINTER(struct_bu_process)),
    ('chan', POINTER(None)),
    ('aborted', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 125
class struct_ged_qray_color(Structure):
    pass

struct_ged_qray_color.__slots__ = [
    'r',
    'g',
    'b',
]
struct_ged_qray_color._fields_ = [
    ('r', c_ubyte),
    ('g', c_ubyte),
    ('b', c_ubyte),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 132
class struct_ged_qray_fmt(Structure):
    pass

struct_ged_qray_fmt.__slots__ = [
    'type',
    'fmt',
]
struct_ged_qray_fmt._fields_ = [
    ('type', c_char),
    ('fmt', struct_bu_vls),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 137
class struct_vd_curve(Structure):
    pass

struct_vd_curve.__slots__ = [
    'l',
    'vdc_name',
    'vdc_rgb',
    'vdc_vhd',
]
struct_vd_curve._fields_ = [
    ('l', struct_bu_list),
    ('vdc_name', c_char * int((31 + 1))),
    ('vdc_rgb', c_long),
    ('vdc_vhd', struct_bu_list),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 146
class struct_ged_drawable(Structure):
    pass

struct_ged_drawable.__slots__ = [
    'l',
    'gd_headDisplay',
    'gd_headVDraw',
    'gd_currVHead',
    'gd_freeSolids',
    'gd_rt_cmd',
    'gd_rt_cmd_len',
    'gd_rtCmdNotify',
    'gd_uplotOutputMode',
    'gd_qray_basename',
    'gd_qray_script',
    'gd_qray_effects',
    'gd_qray_cmd_echo',
    'gd_qray_fmts',
    'gd_qray_odd_color',
    'gd_qray_even_color',
    'gd_qray_void_color',
    'gd_qray_overlap_color',
    'gd_shaded_mode',
]
struct_ged_drawable._fields_ = [
    ('l', struct_bu_list),
    ('gd_headDisplay', POINTER(struct_bu_list)),
    ('gd_headVDraw', POINTER(struct_bu_list)),
    ('gd_currVHead', POINTER(struct_vd_curve)),
    ('gd_freeSolids', POINTER(struct_solid)),
    ('gd_rt_cmd', POINTER(POINTER(c_char))),
    ('gd_rt_cmd_len', c_int),
    ('gd_rtCmdNotify', CFUNCTYPE(UNCHECKED(None), c_int)),
    ('gd_uplotOutputMode', c_int),
    ('gd_qray_basename', struct_bu_vls),
    ('gd_qray_script', struct_bu_vls),
    ('gd_qray_effects', c_char),
    ('gd_qray_cmd_echo', c_int),
    ('gd_qray_fmts', POINTER(struct_ged_qray_fmt)),
    ('gd_qray_odd_color', struct_ged_qray_color),
    ('gd_qray_even_color', struct_ged_qray_color),
    ('gd_qray_void_color', struct_ged_qray_color),
    ('gd_qray_overlap_color', struct_ged_qray_color),
    ('gd_shaded_mode', c_int),
]

ged_io_handler_callback_t = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int)# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 174

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 254
class struct_ged_cmd(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 179
class struct_ged_results(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 205
class struct_fbserv_obj(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/ged/defines.h: 181
class struct_ged(Structure):
    pass

struct_ged.__slots__ = [
    'l',
    'ged_wdbp',
    'ged_log',
    'freesolid',
    'ged_result_str',
    'ged_results',
    'ged_gdp',
    'ged_gvp',
    'ged_fbsp',
    'ged_selections',
    'ged_dmp',
    'ged_refresh_clientdata',
    'ged_refresh_handler',
    'ged_output_handler',
    'ged_output_script',
    'ged_create_vlist_solid_callback',
    'ged_create_vlist_callback',
    'ged_free_vlist_callback',
    'ged_internal_call',
    'io_mode',
    'ged_create_io_handler',
    'ged_delete_io_handler',
    'cmds',
    'add',
    '_del',
    'run',
    'gd_headSubprocess',
    'ged_interp',
    'ged_interp_eval',
    'ged_dm_width',
    'ged_dm_height',
    'ged_dmp_is_null',
    'ged_dm_get_display_image',
]
struct_ged._fields_ = [
    ('l', struct_bu_list),
    ('ged_wdbp', POINTER(struct_rt_wdb)),
    ('ged_log', POINTER(struct_bu_vls)),
    ('freesolid', POINTER(struct_solid)),
    ('ged_result_str', POINTER(struct_bu_vls)),
    ('ged_results', POINTER(struct_ged_results)),
    ('ged_gdp', POINTER(struct_ged_drawable)),
    ('ged_gvp', POINTER(struct_bview)),
    ('ged_fbsp', POINTER(struct_fbserv_obj)),
    ('ged_selections', POINTER(struct_bu_hash_tbl)),
    ('ged_dmp', POINTER(None)),
    ('ged_refresh_clientdata', POINTER(None)),
    ('ged_refresh_handler', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('ged_output_handler', CFUNCTYPE(UNCHECKED(None), POINTER(struct_ged), String)),
    ('ged_output_script', String),
    ('ged_create_vlist_solid_callback', CFUNCTYPE(UNCHECKED(None), POINTER(struct_solid))),
    ('ged_create_vlist_callback', CFUNCTYPE(UNCHECKED(None), POINTER(struct_display_list))),
    ('ged_free_vlist_callback', CFUNCTYPE(UNCHECKED(None), c_uint, c_int)),
    ('ged_internal_call', c_int),
    ('io_mode', c_int),
    ('ged_create_io_handler', CFUNCTYPE(UNCHECKED(None), POINTER(POINTER(None)), POINTER(struct_bu_process), c_int, c_int, POINTER(None), ged_io_handler_callback_t)),
    ('ged_delete_io_handler', CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), POINTER(struct_bu_process), c_int, POINTER(None), ged_io_handler_callback_t)),
    ('cmds', POINTER(struct_ged_cmd)),
    ('add', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_ged), POINTER(struct_ged_cmd))),
    ('_del', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_ged), String)),
    ('run', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_ged), c_int, POINTER(POINTER(c_char)))),
    ('gd_headSubprocess', struct_ged_subprocess),
    ('ged_interp', POINTER(None)),
    ('ged_interp_eval', db_search_callback_t),
    ('ged_dm_width', c_int),
    ('ged_dm_height', c_int),
    ('ged_dmp_is_null', c_int),
    ('ged_dm_get_display_image', CFUNCTYPE(UNCHECKED(None), POINTER(struct_ged), POINTER(POINTER(c_ubyte)))),
]

struct_ged_cmd.__slots__ = [
    'l',
    'name',
    'description',
    'manpage',
    'load',
    'unload',
    'exec',
]
struct_ged_cmd._fields_ = [
    ('l', struct_bu_list),
    ('name', String),
    ('description', c_char * int(80)),
    ('manpage', String),
    ('load', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_ged))),
    ('unload', CFUNCTYPE(UNCHECKED(None), POINTER(struct_ged))),
    ('exec', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_ged), c_int, POINTER(POINTER(c_char)))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/ged.h: 56
if _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].has("ged_delay", "cdecl"):
    ged_delay = _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].get("ged_delay", "cdecl")
    ged_delay.argtypes = [POINTER(struct_ged), c_int, POINTER(POINTER(c_char))]
    ged_delay.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/ged.h: 61
if _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].has("ged_echo", "cdecl"):
    ged_echo = _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].get("ged_echo", "cdecl")
    ged_echo.argtypes = [POINTER(struct_ged), c_int, POINTER(POINTER(c_char))]
    ged_echo.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/ged.h: 66
if _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].has("ged_graph", "cdecl"):
    ged_graph = _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].get("ged_graph", "cdecl")
    ged_graph.argtypes = [POINTER(struct_ged), c_int, POINTER(POINTER(c_char))]
    ged_graph.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/ged.h: 71
if _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].has("ged_help", "cdecl"):
    ged_help = _libs["/usr/brlcad/dev-7.31.0/lib/libged.so"].get("ged_help", "cdecl")
    ged_help.argtypes = [POINTER(struct_ged), c_int, POINTER(POINTER(c_char))]
    ged_help.restype = c_int

# No inserted files

# No prefix-stripping

