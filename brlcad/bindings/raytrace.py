r"""Wrapper for raytrace.h

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
_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"] = load_library("/usr/brlcad/dev-7.31.0/lib/librt.so")

# 1 libraries
# End libraries

# Begin modules
from .bu import *
from .bn import *

# 2 modules
# End modules

__off_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 152

__off64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 153

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

off_t = __off64_t# /usr/include/x86_64-linux-gnu/sys/types.h: 87

time_t = __time_t# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 7

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

fastf_t = c_double# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 330

vect2d_t = fastf_t * int(2)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 333

point2d_t = fastf_t * int(2)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 339

vect_t = fastf_t * int(3)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 345

vectp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 348

point_t = fastf_t * int(3)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 351

hvect_t = fastf_t * int(4)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 357

quat_t = hvect_t# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 360

mat_t = fastf_t * int((4 * 4))# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 366

matp_t = POINTER(fastf_t)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 369

plane_t = fastf_t * int(4)# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 393

X = 0# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

Y = 1# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

Z = 2# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 402

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

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/malloc.h: 172
class struct_bu_pool(Structure):
    pass

struct_bu_pool.__slots__ = [
    'block_size',
    'block_pos',
    'alloc_size',
    'block',
]
struct_bu_pool._fields_ = [
    ('block_size', c_size_t),
    ('block_pos', c_size_t),
    ('alloc_size', c_size_t),
    ('block', POINTER(c_uint8)),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/log.h: 147
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bu_log", "cdecl"):
    _func = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bu_log", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String]
    bu_log = _variadic_function(_func,_restype,_argtypes,_errcheck)

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

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/version.h: 37
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_version", "cdecl"):
    bn_version = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_version", "cdecl")
    bn_version.argtypes = []
    bn_version.restype = c_char_p

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

mat3_t = fastf_t * int(9)# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 69

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 155
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_v_permute", "cdecl"):
    anim_v_permute = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_v_permute", "cdecl")
    anim_v_permute.argtypes = [mat_t]
    anim_v_permute.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 165
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_v_unpermute", "cdecl"):
    anim_v_unpermute = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_v_unpermute", "cdecl")
    anim_v_unpermute.argtypes = [mat_t]
    anim_v_unpermute.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 170
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_tran", "cdecl"):
    anim_tran = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_tran", "cdecl")
    anim_tran.argtypes = [mat_t]
    anim_tran.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 180
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_mat2zyx", "cdecl"):
    anim_mat2zyx = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_mat2zyx", "cdecl")
    anim_mat2zyx.argtypes = [mat_t, vect_t]
    anim_mat2zyx.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 192
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_mat2ypr", "cdecl"):
    anim_mat2ypr = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_mat2ypr", "cdecl")
    anim_mat2ypr.argtypes = [mat_t, vect_t]
    anim_mat2ypr.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 203
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_mat2quat", "cdecl"):
    anim_mat2quat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_mat2quat", "cdecl")
    anim_mat2quat.argtypes = [quat_t, mat_t]
    anim_mat2quat.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 211
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_ypr2mat", "cdecl"):
    anim_ypr2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_ypr2mat", "cdecl")
    anim_ypr2mat.argtypes = [mat_t, vect_t]
    anim_ypr2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 226
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_ypr2vmat", "cdecl"):
    anim_ypr2vmat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_ypr2vmat", "cdecl")
    anim_ypr2vmat.argtypes = [mat_t, vect_t]
    anim_ypr2vmat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 234
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_y_p_r2mat", "cdecl"):
    anim_y_p_r2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_y_p_r2mat", "cdecl")
    anim_y_p_r2mat.argtypes = [mat_t, c_double, c_double, c_double]
    anim_y_p_r2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 243
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_dy_p_r2mat", "cdecl"):
    anim_dy_p_r2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_dy_p_r2mat", "cdecl")
    anim_dy_p_r2mat.argtypes = [mat_t, c_double, c_double, c_double]
    anim_dy_p_r2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 253
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_dy_p_r2vmat", "cdecl"):
    anim_dy_p_r2vmat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_dy_p_r2vmat", "cdecl")
    anim_dy_p_r2vmat.argtypes = [mat_t, c_double, c_double, c_double]
    anim_dy_p_r2vmat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 263
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_x_y_z2mat", "cdecl"):
    anim_x_y_z2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_x_y_z2mat", "cdecl")
    anim_x_y_z2mat.argtypes = [mat_t, c_double, c_double, c_double]
    anim_x_y_z2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 273
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_dx_y_z2mat", "cdecl"):
    anim_dx_y_z2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_dx_y_z2mat", "cdecl")
    anim_dx_y_z2mat.argtypes = [mat_t, c_double, c_double, c_double]
    anim_dx_y_z2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 283
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_zyx2mat", "cdecl"):
    anim_zyx2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_zyx2mat", "cdecl")
    anim_zyx2mat.argtypes = [mat_t, vect_t]
    anim_zyx2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 291
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_z_y_x2mat", "cdecl"):
    anim_z_y_x2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_z_y_x2mat", "cdecl")
    anim_z_y_x2mat.argtypes = [mat_t, c_double, c_double, c_double]
    anim_z_y_x2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 302
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_dz_y_x2mat", "cdecl"):
    anim_dz_y_x2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_dz_y_x2mat", "cdecl")
    anim_dz_y_x2mat.argtypes = [mat_t, c_double, c_double, c_double]
    anim_dz_y_x2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 313
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_quat2mat", "cdecl"):
    anim_quat2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_quat2mat", "cdecl")
    anim_quat2mat.argtypes = [mat_t, quat_t]
    anim_quat2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 324
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_dir2mat", "cdecl"):
    anim_dir2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_dir2mat", "cdecl")
    anim_dir2mat.argtypes = [mat_t, vect_t, vect_t]
    anim_dir2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 336
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_dirn2mat", "cdecl"):
    anim_dirn2mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_dirn2mat", "cdecl")
    anim_dirn2mat.argtypes = [mat_t, vect_t, vect_t]
    anim_dirn2mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 348
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_steer_mat", "cdecl"):
    anim_steer_mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_steer_mat", "cdecl")
    anim_steer_mat.argtypes = [mat_t, vect_t, c_int]
    anim_steer_mat.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 358
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_add_trans", "cdecl"):
    anim_add_trans = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_add_trans", "cdecl")
    anim_add_trans.argtypes = [mat_t, vect_t, vect_t]
    anim_add_trans.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 365
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_rotatez", "cdecl"):
    anim_rotatez = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_rotatez", "cdecl")
    anim_rotatez.argtypes = [fastf_t, vect_t]
    anim_rotatez.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 371
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_mat_print", "cdecl"):
    anim_mat_print = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_mat_print", "cdecl")
    anim_mat_print.argtypes = [POINTER(FILE), mat_t, c_int]
    anim_mat_print.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 379
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_mat_printf", "cdecl"):
    anim_mat_printf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_mat_printf", "cdecl")
    anim_mat_printf.argtypes = [POINTER(FILE), mat_t, String, String, String]
    anim_mat_printf.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 389
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("anim_view_rev", "cdecl"):
    anim_view_rev = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("anim_view_rev", "cdecl")
    anim_view_rev.argtypes = [mat_t]
    anim_view_rev.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/complex.h: 41
class struct_bn_complex(Structure):
    pass

struct_bn_complex.__slots__ = [
    're',
    'im',
]
struct_bn_complex._fields_ = [
    ('re', c_double),
    ('im', c_double),
]

bn_complex_t = struct_bn_complex# /usr/brlcad/dev-7.31.0/include/brlcad/bn/complex.h: 41

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/poly.h: 54
class struct_bn_poly(Structure):
    pass

struct_bn_poly.__slots__ = [
    'magic',
    'dgr',
    'cf',
]
struct_bn_poly._fields_ = [
    ('magic', c_uint32),
    ('dgr', c_size_t),
    ('cf', fastf_t * int((6 + 1))),
]

bn_poly_t = struct_bn_poly# /usr/brlcad/dev-7.31.0/include/brlcad/bn/poly.h: 54

# /usr/brlcad/dev-7.31.0/include/brlcad/bu/color.h: 55
class struct_bu_color(Structure):
    pass

struct_bu_color.__slots__ = [
    'buc_rgb',
]
struct_bu_color._fields_ = [
    ('buc_rgb', hvect_t),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 67
class struct_bn_vlist(Structure):
    pass

struct_bn_vlist.__slots__ = [
    'l',
    'nused',
    'cmd',
    'pt',
]
struct_bn_vlist._fields_ = [
    ('l', struct_bu_list),
    ('nused', c_size_t),
    ('cmd', c_int * int(35)),
    ('pt', point_t * int(35)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 184
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_cmd_cnt", "cdecl"):
    bn_vlist_cmd_cnt = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_cmd_cnt", "cdecl")
    bn_vlist_cmd_cnt.argtypes = [POINTER(struct_bn_vlist)]
    bn_vlist_cmd_cnt.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 185
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_bbox", "cdecl"):
    bn_vlist_bbox = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_bbox", "cdecl")
    bn_vlist_bbox.argtypes = [POINTER(struct_bu_list), POINTER(point_t), POINTER(point_t), POINTER(c_int)]
    bn_vlist_bbox.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 193
class struct_bn_vlblock(Structure):
    pass

struct_bn_vlblock.__slots__ = [
    'magic',
    'nused',
    'max',
    'rgb',
    'head',
    'free_vlist_hd',
]
struct_bn_vlblock._fields_ = [
    ('magic', c_uint32),
    ('nused', c_size_t),
    ('max', c_size_t),
    ('rgb', POINTER(c_long)),
    ('head', POINTER(struct_bu_list)),
    ('free_vlist_hd', POINTER(struct_bu_list)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 217
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_3string", "cdecl"):
    bn_vlist_3string = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_3string", "cdecl")
    bn_vlist_3string.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list), String, point_t, mat_t, c_double]
    bn_vlist_3string.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 239
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_2string", "cdecl"):
    bn_vlist_2string = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_2string", "cdecl")
    bn_vlist_2string.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list), String, c_double, c_double, c_double, c_double]
    bn_vlist_2string.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 251
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_get_cmd_description", "cdecl"):
    bn_vlist_get_cmd_description = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_get_cmd_description", "cdecl")
    bn_vlist_get_cmd_description.argtypes = [c_int]
    bn_vlist_get_cmd_description.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 260
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_ck_vlist", "cdecl"):
    bn_ck_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_ck_vlist", "cdecl")
    bn_ck_vlist.argtypes = [POINTER(struct_bu_list)]
    bn_ck_vlist.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 267
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_copy", "cdecl"):
    bn_vlist_copy = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_copy", "cdecl")
    bn_vlist_copy.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list), POINTER(struct_bu_list)]
    bn_vlist_copy.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 279
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_export", "cdecl"):
    bn_vlist_export = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_export", "cdecl")
    bn_vlist_export.argtypes = [POINTER(struct_bu_vls), POINTER(struct_bu_list), String]
    bn_vlist_export.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 288
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_import", "cdecl"):
    bn_vlist_import = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_import", "cdecl")
    bn_vlist_import.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list), POINTER(struct_bu_vls), POINTER(c_ubyte)]
    bn_vlist_import.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 293
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_cleanup", "cdecl"):
    bn_vlist_cleanup = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_cleanup", "cdecl")
    bn_vlist_cleanup.argtypes = [POINTER(struct_bu_list)]
    bn_vlist_cleanup.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 295
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlblock_init", "cdecl"):
    bn_vlblock_init = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlblock_init", "cdecl")
    bn_vlblock_init.argtypes = [POINTER(struct_bu_list), c_int]
    bn_vlblock_init.restype = POINTER(struct_bn_vlblock)

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 298
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlblock_free", "cdecl"):
    bn_vlblock_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlblock_free", "cdecl")
    bn_vlblock_free.argtypes = [POINTER(struct_bn_vlblock)]
    bn_vlblock_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 300
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlblock_find", "cdecl"):
    bn_vlblock_find = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlblock_find", "cdecl")
    bn_vlblock_find.argtypes = [POINTER(struct_bn_vlblock), c_int, c_int, c_int]
    bn_vlblock_find.restype = POINTER(struct_bu_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 306
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_rpp", "cdecl"):
    bn_vlist_rpp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_rpp", "cdecl")
    bn_vlist_rpp.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list), point_t, point_t]
    bn_vlist_rpp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 312
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_plot_vlblock", "cdecl"):
    bn_plot_vlblock = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_plot_vlblock", "cdecl")
    bn_plot_vlblock.argtypes = [POINTER(FILE), POINTER(struct_bn_vlblock)]
    bn_plot_vlblock.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 320
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bn_vlist_to_uplot", "cdecl"):
    bn_vlist_to_uplot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bn_vlist_to_uplot", "cdecl")
    bn_vlist_to_uplot.argtypes = [POINTER(FILE), POINTER(struct_bu_list)]
    bn_vlist_to_uplot.restype = None

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

enum_anon_31 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 60

DB_OP_NULL = 0# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 60

DB_OP_UNION = b'u'# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 60

DB_OP_SUBTRACT = b'-'# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 60

DB_OP_INTERSECT = b'+'# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 60

db_op_t = enum_anon_31# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 60

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 72
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_str2op", "cdecl"):
    db_str2op = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_str2op", "cdecl")
    db_str2op.argtypes = [String]
    db_str2op.restype = db_op_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 56
class struct_db5_ondisk_header(Structure):
    pass

struct_db5_ondisk_header.__slots__ = [
    'db5h_magic1',
    'db5h_hflags',
    'db5h_aflags',
    'db5h_bflags',
    'db5h_major_type',
    'db5h_minor_type',
]
struct_db5_ondisk_header._fields_ = [
    ('db5h_magic1', c_ubyte),
    ('db5h_hflags', c_ubyte),
    ('db5h_aflags', c_ubyte),
    ('db5h_bflags', c_ubyte),
    ('db5h_major_type', c_ubyte),
    ('db5h_minor_type', c_ubyte),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 193
try:
    binu_types = (POINTER(POINTER(c_char))).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "binu_types")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 200
class struct_db5_raw_internal(Structure):
    pass

struct_db5_raw_internal.__slots__ = [
    'magic',
    'h_object_width',
    'h_name_hidden',
    'h_name_present',
    'h_name_width',
    'h_dli',
    'a_width',
    'a_present',
    'a_zzz',
    'b_width',
    'b_present',
    'b_zzz',
    'major_type',
    'minor_type',
    'object_length',
    'name',
    'body',
    'attributes',
    'buf',
]
struct_db5_raw_internal._fields_ = [
    ('magic', c_uint32),
    ('h_object_width', c_ubyte),
    ('h_name_hidden', c_ubyte),
    ('h_name_present', c_ubyte),
    ('h_name_width', c_ubyte),
    ('h_dli', c_ubyte),
    ('a_width', c_ubyte),
    ('a_present', c_ubyte),
    ('a_zzz', c_ubyte),
    ('b_width', c_ubyte),
    ('b_present', c_ubyte),
    ('b_zzz', c_ubyte),
    ('major_type', c_ubyte),
    ('minor_type', c_ubyte),
    ('object_length', c_size_t),
    ('name', struct_bu_external),
    ('body', struct_bu_external),
    ('attributes', struct_bu_external),
    ('buf', POINTER(c_ubyte)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 179
try:
    nmg_debug = (c_uint32).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "nmg_debug")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 188
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

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 264
class struct_shell_a(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 512
class struct_vertexuse(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 252
class struct_shell(Structure):
    pass

struct_shell.__slots__ = [
    'l',
    'r_p',
    'sa_p',
    'fu_hd',
    'lu_hd',
    'eu_hd',
    'vu_p',
    'index',
]
struct_shell._fields_ = [
    ('l', struct_bu_list),
    ('r_p', POINTER(struct_nmgregion)),
    ('sa_p', POINTER(struct_shell_a)),
    ('fu_hd', struct_bu_list),
    ('lu_hd', struct_bu_list),
    ('eu_hd', struct_bu_list),
    ('vu_p', POINTER(struct_vertexuse)),
    ('index', c_long),
]

struct_shell_a.__slots__ = [
    'magic',
    'min_pt',
    'max_pt',
    'index',
]
struct_shell_a._fields_ = [
    ('magic', c_uint32),
    ('min_pt', point_t),
    ('max_pt', point_t),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 319
class struct_faceuse(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 291
class struct_face_g_plane(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 298
class struct_face_g_snurb(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 278
class union_anon_32(Union):
    pass

union_anon_32.__slots__ = [
    'magic_p',
    'plane_p',
    'snurb_p',
]
union_anon_32._fields_ = [
    ('magic_p', POINTER(c_uint32)),
    ('plane_p', POINTER(struct_face_g_plane)),
    ('snurb_p', POINTER(struct_face_g_snurb)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 275
class struct_face(Structure):
    pass

struct_face.__slots__ = [
    'l',
    'fu_p',
    'g',
    'flip',
    'min_pt',
    'max_pt',
    'index',
]
struct_face._fields_ = [
    ('l', struct_bu_list),
    ('fu_p', POINTER(struct_faceuse)),
    ('g', union_anon_32),
    ('flip', c_int),
    ('min_pt', point_t),
    ('max_pt', point_t),
    ('index', c_long),
]

struct_face_g_plane.__slots__ = [
    'magic',
    'f_hd',
    'N',
    'index',
]
struct_face_g_plane._fields_ = [
    ('magic', c_uint32),
    ('f_hd', struct_bu_list),
    ('N', plane_t),
    ('index', c_long),
]

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

struct_faceuse.__slots__ = [
    'l',
    's_p',
    'fumate_p',
    'orientation',
    'outside',
    'f_p',
    'lu_hd',
    'index',
]
struct_faceuse._fields_ = [
    ('l', struct_bu_list),
    ('s_p', POINTER(struct_shell)),
    ('fumate_p', POINTER(struct_faceuse)),
    ('orientation', c_int),
    ('outside', c_int),
    ('f_p', POINTER(struct_face)),
    ('lu_hd', struct_bu_list),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 399
class struct_loopuse(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 392
class struct_loop_g(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 385
class struct_loop(Structure):
    pass

struct_loop.__slots__ = [
    'magic',
    'lu_p',
    'lg_p',
    'index',
]
struct_loop._fields_ = [
    ('magic', c_uint32),
    ('lu_p', POINTER(struct_loopuse)),
    ('lg_p', POINTER(struct_loop_g)),
    ('index', c_long),
]

struct_loop_g.__slots__ = [
    'magic',
    'min_pt',
    'max_pt',
    'index',
]
struct_loop_g._fields_ = [
    ('magic', c_uint32),
    ('min_pt', point_t),
    ('max_pt', point_t),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 401
class union_anon_33(Union):
    pass

union_anon_33.__slots__ = [
    'fu_p',
    's_p',
    'magic_p',
]
union_anon_33._fields_ = [
    ('fu_p', POINTER(struct_faceuse)),
    ('s_p', POINTER(struct_shell)),
    ('magic_p', POINTER(c_uint32)),
]

struct_loopuse.__slots__ = [
    'l',
    'up',
    'lumate_p',
    'orientation',
    'l_p',
    'down_hd',
    'index',
]
struct_loopuse._fields_ = [
    ('l', struct_bu_list),
    ('up', union_anon_33),
    ('lumate_p', POINTER(struct_loopuse)),
    ('orientation', c_int),
    ('l_p', POINTER(struct_loop)),
    ('down_hd', struct_bu_list),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 471
class struct_edgeuse(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 431
class struct_edge(Structure):
    pass

struct_edge.__slots__ = [
    'magic',
    'eu_p',
    'is_real',
    'index',
]
struct_edge._fields_ = [
    ('magic', c_uint32),
    ('eu_p', POINTER(struct_edgeuse)),
    ('is_real', c_long),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 443
class struct_edge_g_lseg(Structure):
    pass

struct_edge_g_lseg.__slots__ = [
    'l',
    'eu_hd2',
    'e_pt',
    'e_dir',
    'index',
]
struct_edge_g_lseg._fields_ = [
    ('l', struct_bu_list),
    ('eu_hd2', struct_bu_list),
    ('e_pt', point_t),
    ('e_dir', vect_t),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 459
class struct_edge_g_cnurb(Structure):
    pass

struct_edge_g_cnurb.__slots__ = [
    'l',
    'eu_hd2',
    'order',
    'k',
    'c_size',
    'pt_type',
    'ctl_points',
    'index',
]
struct_edge_g_cnurb._fields_ = [
    ('l', struct_bu_list),
    ('eu_hd2', struct_bu_list),
    ('order', c_int),
    ('k', struct_knot_vector),
    ('c_size', c_int),
    ('pt_type', c_int),
    ('ctl_points', POINTER(fastf_t)),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 474
class union_anon_34(Union):
    pass

union_anon_34.__slots__ = [
    'lu_p',
    's_p',
    'magic_p',
]
union_anon_34._fields_ = [
    ('lu_p', POINTER(struct_loopuse)),
    ('s_p', POINTER(struct_shell)),
    ('magic_p', POINTER(c_uint32)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 484
class union_anon_35(Union):
    pass

union_anon_35.__slots__ = [
    'magic_p',
    'lseg_p',
    'cnurb_p',
]
union_anon_35._fields_ = [
    ('magic_p', POINTER(c_uint32)),
    ('lseg_p', POINTER(struct_edge_g_lseg)),
    ('cnurb_p', POINTER(struct_edge_g_cnurb)),
]

struct_edgeuse.__slots__ = [
    'l',
    'l2',
    'up',
    'eumate_p',
    'radial_p',
    'e_p',
    'orientation',
    'vu_p',
    'g',
    'index',
]
struct_edgeuse._fields_ = [
    ('l', struct_bu_list),
    ('l2', struct_bu_list),
    ('up', union_anon_34),
    ('eumate_p', POINTER(struct_edgeuse)),
    ('radial_p', POINTER(struct_edgeuse)),
    ('e_p', POINTER(struct_edge)),
    ('orientation', c_int),
    ('vu_p', POINTER(struct_vertexuse)),
    ('g', union_anon_35),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 506
class struct_vertex_g(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 499
class struct_vertex(Structure):
    pass

struct_vertex.__slots__ = [
    'magic',
    'vu_hd',
    'vg_p',
    'index',
]
struct_vertex._fields_ = [
    ('magic', c_uint32),
    ('vu_hd', struct_bu_list),
    ('vg_p', POINTER(struct_vertex_g)),
    ('index', c_long),
]

struct_vertex_g.__slots__ = [
    'magic',
    'coord',
    'index',
]
struct_vertex_g._fields_ = [
    ('magic', c_uint32),
    ('coord', point_t),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 514
class union_anon_36(Union):
    pass

union_anon_36.__slots__ = [
    's_p',
    'lu_p',
    'eu_p',
    'magic_p',
]
union_anon_36._fields_ = [
    ('s_p', POINTER(struct_shell)),
    ('lu_p', POINTER(struct_loopuse)),
    ('eu_p', POINTER(struct_edgeuse)),
    ('magic_p', POINTER(c_uint32)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 529
class struct_vertexuse_a_plane(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 535
class struct_vertexuse_a_cnurb(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 521
class union_anon_37(Union):
    pass

union_anon_37.__slots__ = [
    'magic_p',
    'plane_p',
    'cnurb_p',
]
union_anon_37._fields_ = [
    ('magic_p', POINTER(c_uint32)),
    ('plane_p', POINTER(struct_vertexuse_a_plane)),
    ('cnurb_p', POINTER(struct_vertexuse_a_cnurb)),
]

struct_vertexuse.__slots__ = [
    'l',
    'up',
    'v_p',
    'a',
    'index',
]
struct_vertexuse._fields_ = [
    ('l', struct_bu_list),
    ('up', union_anon_36),
    ('v_p', POINTER(struct_vertex)),
    ('a', union_anon_37),
    ('index', c_long),
]

struct_vertexuse_a_plane.__slots__ = [
    'magic',
    'N',
    'index',
]
struct_vertexuse_a_plane._fields_ = [
    ('magic', c_uint32),
    ('N', vect_t),
    ('index', c_long),
]

struct_vertexuse_a_cnurb.__slots__ = [
    'magic',
    'param',
    'index',
]
struct_vertexuse_a_cnurb._fields_ = [
    ('magic', c_uint32),
    ('param', fastf_t * int(3)),
    ('index', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 545
try:
    nmg_memtrack = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "nmg_memtrack")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 546
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_malloc", "cdecl"):
    nmg_malloc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_malloc", "cdecl")
    nmg_malloc.argtypes = [c_size_t, String]
    nmg_malloc.restype = POINTER(c_ubyte)
    nmg_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 547
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_calloc", "cdecl"):
    nmg_calloc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_calloc", "cdecl")
    nmg_calloc.argtypes = [c_int, c_size_t, String]
    nmg_calloc.restype = POINTER(c_ubyte)
    nmg_calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 548
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_realloc", "cdecl"):
    nmg_realloc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_realloc", "cdecl")
    nmg_realloc.argtypes = [POINTER(None), c_size_t, String]
    nmg_realloc.restype = POINTER(c_ubyte)
    nmg_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 549
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_free", "cdecl"):
    nmg_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_free", "cdecl")
    nmg_free.argtypes = [POINTER(None), String]
    nmg_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 550
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_destroy", "cdecl"):
    nmg_destroy = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_destroy", "cdecl")
    nmg_destroy.argtypes = []
    nmg_destroy.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 647
class struct_nmg_boolstruct(Structure):
    pass

struct_nmg_boolstruct.__slots__ = [
    'ilist',
    'tol',
    'pt',
    'dir',
    'coplanar',
    'vertlist',
    'vlsize',
    'model',
]
struct_nmg_boolstruct._fields_ = [
    ('ilist', struct_bu_ptbl),
    ('tol', fastf_t),
    ('pt', point_t),
    ('dir', vect_t),
    ('coplanar', c_int),
    ('vertlist', String),
    ('vlsize', c_int),
    ('model', POINTER(struct_model)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 669
class struct_nmg_struct_counts(Structure):
    pass

struct_nmg_struct_counts.__slots__ = [
    'model',
    'region',
    'region_a',
    'shell',
    'shell_a',
    'faceuse',
    'face',
    'face_g_plane',
    'face_g_snurb',
    'loopuse',
    'loop',
    'loop_g',
    'edgeuse',
    'edge',
    'edge_g_lseg',
    'edge_g_cnurb',
    'vertexuse',
    'vertexuse_a_plane',
    'vertexuse_a_cnurb',
    'vertex',
    'vertex_g',
    'max_structs',
    'face_loops',
    'face_edges',
    'face_lone_verts',
    'wire_loops',
    'wire_loop_edges',
    'wire_edges',
    'wire_lone_verts',
    'shells_of_lone_vert',
]
struct_nmg_struct_counts._fields_ = [
    ('model', c_long),
    ('region', c_long),
    ('region_a', c_long),
    ('shell', c_long),
    ('shell_a', c_long),
    ('faceuse', c_long),
    ('face', c_long),
    ('face_g_plane', c_long),
    ('face_g_snurb', c_long),
    ('loopuse', c_long),
    ('loop', c_long),
    ('loop_g', c_long),
    ('edgeuse', c_long),
    ('edge', c_long),
    ('edge_g_lseg', c_long),
    ('edge_g_cnurb', c_long),
    ('vertexuse', c_long),
    ('vertexuse_a_plane', c_long),
    ('vertexuse_a_cnurb', c_long),
    ('vertex', c_long),
    ('vertex_g', c_long),
    ('max_structs', c_long),
    ('face_loops', c_long),
    ('face_edges', c_long),
    ('face_lone_verts', c_long),
    ('wire_loops', c_long),
    ('wire_loop_edges', c_long),
    ('wire_edges', c_long),
    ('wire_lone_verts', c_long),
    ('shells_of_lone_vert', c_long),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 769
class struct_nmg_visit_handlers(Structure):
    pass

struct_nmg_visit_handlers.__slots__ = [
    'bef_model',
    'aft_model',
    'bef_region',
    'aft_region',
    'vis_region_a',
    'bef_shell',
    'aft_shell',
    'vis_shell_a',
    'bef_faceuse',
    'aft_faceuse',
    'vis_face',
    'vis_face_g',
    'bef_loopuse',
    'aft_loopuse',
    'vis_loop',
    'vis_loop_g',
    'bef_edgeuse',
    'aft_edgeuse',
    'vis_edge',
    'vis_edge_g',
    'bef_vertexuse',
    'aft_vertexuse',
    'vis_vertexuse_a',
    'vis_vertex',
    'vis_vertex_g',
]
struct_nmg_visit_handlers._fields_ = [
    ('bef_model', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('aft_model', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('bef_region', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('aft_region', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_region_a', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('bef_shell', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('aft_shell', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_shell_a', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('bef_faceuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('aft_faceuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int, POINTER(struct_bu_list))),
    ('vis_face', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_face_g', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('bef_loopuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('aft_loopuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_loop', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_loop_g', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('bef_edgeuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('aft_edgeuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_edge', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_edge_g', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('bef_vertexuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('aft_vertexuse', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_vertexuse_a', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_vertex', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
    ('vis_vertex_g', CFUNCTYPE(UNCHECKED(None), POINTER(c_uint32), POINTER(None), c_int)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 809
class struct_nmg_radial(Structure):
    pass

struct_nmg_radial.__slots__ = [
    'l',
    'eu',
    'fu',
    's',
    'existing_flag',
    'is_crack',
    'is_outie',
    'needs_flip',
    'ang',
]
struct_nmg_radial._fields_ = [
    ('l', struct_bu_list),
    ('eu', POINTER(struct_edgeuse)),
    ('fu', POINTER(struct_faceuse)),
    ('s', POINTER(struct_shell)),
    ('existing_flag', c_int),
    ('is_crack', c_int),
    ('is_outie', c_int),
    ('needs_flip', c_int),
    ('ang', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 822
class struct_nmg_inter_struct(Structure):
    pass

struct_nmg_inter_struct.__slots__ = [
    'magic',
    'l1',
    'l2',
    'mag1',
    'mag2',
    'mag_len',
    's1',
    's2',
    'fu1',
    'fu2',
    'tol',
    'coplanar',
    'on_eg',
    'pt',
    'dir',
    'pt2d',
    'dir2d',
    'vert2d',
    'maxindex',
    'proj',
    'twod',
]
struct_nmg_inter_struct._fields_ = [
    ('magic', c_uint32),
    ('l1', POINTER(struct_bu_ptbl)),
    ('l2', POINTER(struct_bu_ptbl)),
    ('mag1', POINTER(fastf_t)),
    ('mag2', POINTER(fastf_t)),
    ('mag_len', c_size_t),
    ('s1', POINTER(struct_shell)),
    ('s2', POINTER(struct_shell)),
    ('fu1', POINTER(struct_faceuse)),
    ('fu2', POINTER(struct_faceuse)),
    ('tol', struct_bn_tol),
    ('coplanar', c_int),
    ('on_eg', POINTER(struct_edge_g_lseg)),
    ('pt', point_t),
    ('dir', vect_t),
    ('pt2d', point_t),
    ('dir2d', vect_t),
    ('vert2d', POINTER(fastf_t)),
    ('maxindex', c_size_t),
    ('proj', mat_t),
    ('twod', POINTER(c_uint32)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 910
class struct_nmg_nurb_poly(Structure):
    pass

struct_nmg_nurb_poly.__slots__ = [
    'next',
    'ply',
    'uv',
]
struct_nmg_nurb_poly._fields_ = [
    ('next', POINTER(struct_nmg_nurb_poly)),
    ('ply', point_t * int(3)),
    ('uv', (fastf_t * int(2)) * int(3)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 916
class struct_nmg_nurb_uv_hit(Structure):
    pass

struct_nmg_nurb_uv_hit.__slots__ = [
    'next',
    'sub',
    'u',
    'v',
]
struct_nmg_nurb_uv_hit._fields_ = [
    ('next', POINTER(struct_nmg_nurb_uv_hit)),
    ('sub', c_int),
    ('u', fastf_t),
    ('v', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 924
class struct_oslo_mat(Structure):
    pass

struct_oslo_mat.__slots__ = [
    'next',
    'offset',
    'osize',
    'o_vec',
]
struct_oslo_mat._fields_ = [
    ('next', POINTER(struct_oslo_mat)),
    ('offset', c_int),
    ('osize', c_int),
    ('o_vec', POINTER(fastf_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 933
class struct_bezier_2d_list(Structure):
    pass

struct_bezier_2d_list.__slots__ = [
    'l',
    'ctl',
]
struct_bezier_2d_list._fields_ = [
    ('l', struct_bu_list),
    ('ctl', POINTER(point2d_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 943
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bezier", "cdecl"):
    bezier = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bezier", "cdecl")
    bezier.argtypes = [POINTER(point2d_t), c_int, c_double, POINTER(point2d_t), POINTER(point2d_t), point2d_t, point2d_t]
    bezier.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 949
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bezier_roots", "cdecl"):
    bezier_roots = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bezier_roots", "cdecl")
    bezier_roots.argtypes = [POINTER(point2d_t), c_int, POINTER(POINTER(point2d_t)), POINTER(POINTER(point2d_t)), point2d_t, point2d_t, point2d_t, c_int, fastf_t]
    bezier_roots.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 954
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("bezier_subdivide", "cdecl"):
    bezier_subdivide = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("bezier_subdivide", "cdecl")
    bezier_subdivide.argtypes = [POINTER(struct_bezier_2d_list), c_int, fastf_t, c_int]
    bezier_subdivide.restype = POINTER(struct_bezier_2d_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 962
try:
    re_nmgfree = (struct_bu_list).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "re_nmgfree")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1075
class struct_nmg_ray(Structure):
    pass

struct_nmg_ray.__slots__ = [
    'magic',
    'r_pt',
    'r_dir',
    'r_min',
    'r_max',
]
struct_nmg_ray._fields_ = [
    ('magic', c_uint32),
    ('r_pt', point_t),
    ('r_dir', vect_t),
    ('r_min', fastf_t),
    ('r_max', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1083
class struct_nmg_hit(Structure):
    pass

struct_nmg_hit.__slots__ = [
    'hit_magic',
    'hit_dist',
    'hit_point',
    'hit_normal',
    'hit_vpriv',
    'hit_private',
    'hit_surfno',
    'hit_rayp',
]
struct_nmg_hit._fields_ = [
    ('hit_magic', c_uint32),
    ('hit_dist', fastf_t),
    ('hit_point', point_t),
    ('hit_normal', vect_t),
    ('hit_vpriv', vect_t),
    ('hit_private', POINTER(None)),
    ('hit_surfno', c_int),
    ('hit_rayp', POINTER(struct_nmg_ray)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1094
class struct_nmg_seg(Structure):
    pass

struct_nmg_seg.__slots__ = [
    'l',
    'seg_in',
    'seg_out',
    'seg_stp',
]
struct_nmg_seg._fields_ = [
    ('l', struct_bu_list),
    ('seg_in', struct_nmg_hit),
    ('seg_out', struct_nmg_hit),
    ('seg_stp', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1101
class struct_nmg_hitmiss(Structure):
    pass

struct_nmg_hitmiss.__slots__ = [
    'l',
    'hit',
    'dist_in_plane',
    'in_out',
    'inbound_use',
    'inbound_norm',
    'outbound_use',
    'outbound_norm',
    'start_stop',
    'other',
]
struct_nmg_hitmiss._fields_ = [
    ('l', struct_bu_list),
    ('hit', struct_nmg_hit),
    ('dist_in_plane', fastf_t),
    ('in_out', c_int),
    ('inbound_use', POINTER(c_long)),
    ('inbound_norm', vect_t),
    ('outbound_use', POINTER(c_long)),
    ('outbound_norm', vect_t),
    ('start_stop', c_int),
    ('other', POINTER(struct_nmg_hitmiss)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1138
class struct_nmg_ray_data(Structure):
    pass

struct_nmg_ray_data.__slots__ = [
    'magic',
    'rd_m',
    'manifolds',
    'rd_invdir',
    'rp',
    'ap',
    'seghead',
    'stp',
    'tol',
    'hitmiss',
    'rd_hit',
    'rd_miss',
    'plane_pt',
    'ray_dist_to_plane',
    'face_subhit',
    'classifying_ray',
]
struct_nmg_ray_data._fields_ = [
    ('magic', c_uint32),
    ('rd_m', POINTER(struct_model)),
    ('manifolds', String),
    ('rd_invdir', vect_t),
    ('rp', POINTER(struct_nmg_ray)),
    ('ap', POINTER(POINTER(None))),
    ('seghead', POINTER(struct_nmg_seg)),
    ('stp', POINTER(POINTER(None))),
    ('tol', POINTER(struct_bn_tol)),
    ('hitmiss', POINTER(POINTER(struct_nmg_hitmiss))),
    ('rd_hit', struct_bu_list),
    ('rd_miss', struct_bu_list),
    ('plane_pt', point_t),
    ('ray_dist_to_plane', fastf_t),
    ('face_subhit', c_int),
    ('classifying_ray', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1185
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("ray_in_rpp", "cdecl"):
    ray_in_rpp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("ray_in_rpp", "cdecl")
    ray_in_rpp.argtypes = [POINTER(struct_nmg_ray), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t)]
    ray_in_rpp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1193
try:
    nmg_vlblock_anim_upcall = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "nmg_vlblock_anim_upcall")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1198
try:
    nmg_mged_debug_display_hack = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "nmg_mged_debug_display_hack")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1205
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mm", "cdecl"):
    nmg_mm = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mm", "cdecl")
    nmg_mm.argtypes = []
    nmg_mm.restype = POINTER(struct_model)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1206
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mmr", "cdecl"):
    nmg_mmr = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mmr", "cdecl")
    nmg_mmr.argtypes = []
    nmg_mmr.restype = POINTER(struct_model)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1207
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mrsv", "cdecl"):
    nmg_mrsv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mrsv", "cdecl")
    nmg_mrsv.argtypes = [POINTER(struct_model)]
    nmg_mrsv.restype = POINTER(struct_nmgregion)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1208
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_msv", "cdecl"):
    nmg_msv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_msv", "cdecl")
    nmg_msv.argtypes = [POINTER(struct_nmgregion)]
    nmg_msv.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1209
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mf", "cdecl"):
    nmg_mf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mf", "cdecl")
    nmg_mf.argtypes = [POINTER(struct_loopuse)]
    nmg_mf.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1210
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mlv", "cdecl"):
    nmg_mlv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mlv", "cdecl")
    nmg_mlv.argtypes = [POINTER(c_uint32), POINTER(struct_vertex), c_int]
    nmg_mlv.restype = POINTER(struct_loopuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1213
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_me", "cdecl"):
    nmg_me = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_me", "cdecl")
    nmg_me.argtypes = [POINTER(struct_vertex), POINTER(struct_vertex), POINTER(struct_shell)]
    nmg_me.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1216
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_meonvu", "cdecl"):
    nmg_meonvu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_meonvu", "cdecl")
    nmg_meonvu.argtypes = [POINTER(struct_vertexuse)]
    nmg_meonvu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1217
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ml", "cdecl"):
    nmg_ml = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ml", "cdecl")
    nmg_ml.argtypes = [POINTER(struct_shell)]
    nmg_ml.restype = POINTER(struct_loopuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1219
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_keg", "cdecl"):
    nmg_keg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_keg", "cdecl")
    nmg_keg.argtypes = [POINTER(struct_edgeuse)]
    nmg_keg.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1220
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kvu", "cdecl"):
    nmg_kvu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kvu", "cdecl")
    nmg_kvu.argtypes = [POINTER(struct_vertexuse)]
    nmg_kvu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1221
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kfu", "cdecl"):
    nmg_kfu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kfu", "cdecl")
    nmg_kfu.argtypes = [POINTER(struct_faceuse)]
    nmg_kfu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1222
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_klu", "cdecl"):
    nmg_klu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_klu", "cdecl")
    nmg_klu.argtypes = [POINTER(struct_loopuse)]
    nmg_klu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1223
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_keu", "cdecl"):
    nmg_keu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_keu", "cdecl")
    nmg_keu.argtypes = [POINTER(struct_edgeuse)]
    nmg_keu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1224
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_keu_zl", "cdecl"):
    nmg_keu_zl = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_keu_zl", "cdecl")
    nmg_keu_zl.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_keu_zl.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1226
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ks", "cdecl"):
    nmg_ks = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ks", "cdecl")
    nmg_ks.argtypes = [POINTER(struct_shell)]
    nmg_ks.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1227
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kr", "cdecl"):
    nmg_kr = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kr", "cdecl")
    nmg_kr.argtypes = [POINTER(struct_nmgregion)]
    nmg_kr.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1228
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_km", "cdecl"):
    nmg_km = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_km", "cdecl")
    nmg_km.argtypes = [POINTER(struct_model)]
    nmg_km.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1230
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vertex_gv", "cdecl"):
    nmg_vertex_gv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vertex_gv", "cdecl")
    nmg_vertex_gv.argtypes = [POINTER(struct_vertex), point_t]
    nmg_vertex_gv.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1232
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vertex_g", "cdecl"):
    nmg_vertex_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vertex_g", "cdecl")
    nmg_vertex_g.argtypes = [POINTER(struct_vertex), fastf_t, fastf_t, fastf_t]
    nmg_vertex_g.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1236
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vertexuse_nv", "cdecl"):
    nmg_vertexuse_nv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vertexuse_nv", "cdecl")
    nmg_vertexuse_nv.argtypes = [POINTER(struct_vertexuse), vect_t]
    nmg_vertexuse_nv.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1238
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vertexuse_a_cnurb", "cdecl"):
    nmg_vertexuse_a_cnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vertexuse_a_cnurb", "cdecl")
    nmg_vertexuse_a_cnurb.argtypes = [POINTER(struct_vertexuse), POINTER(fastf_t)]
    nmg_vertexuse_a_cnurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1240
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_g", "cdecl"):
    nmg_edge_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_g", "cdecl")
    nmg_edge_g.argtypes = [POINTER(struct_edgeuse)]
    nmg_edge_g.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1241
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_g_cnurb", "cdecl"):
    nmg_edge_g_cnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_g_cnurb", "cdecl")
    nmg_edge_g_cnurb.argtypes = [POINTER(struct_edgeuse), c_int, c_int, POINTER(fastf_t), c_int, c_int, POINTER(fastf_t)]
    nmg_edge_g_cnurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1248
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_g_cnurb_plinear", "cdecl"):
    nmg_edge_g_cnurb_plinear = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_g_cnurb_plinear", "cdecl")
    nmg_edge_g_cnurb_plinear.argtypes = [POINTER(struct_edgeuse)]
    nmg_edge_g_cnurb_plinear.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1249
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_use_edge_g", "cdecl"):
    nmg_use_edge_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_use_edge_g", "cdecl")
    nmg_use_edge_g.argtypes = [POINTER(struct_edgeuse), POINTER(c_uint32)]
    nmg_use_edge_g.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1251
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_g", "cdecl"):
    nmg_loop_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_g", "cdecl")
    nmg_loop_g.argtypes = [POINTER(struct_loop), POINTER(struct_bn_tol)]
    nmg_loop_g.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1253
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_g", "cdecl"):
    nmg_face_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_g", "cdecl")
    nmg_face_g.argtypes = [POINTER(struct_faceuse), plane_t]
    nmg_face_g.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1255
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_new_g", "cdecl"):
    nmg_face_new_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_new_g", "cdecl")
    nmg_face_new_g.argtypes = [POINTER(struct_faceuse), plane_t]
    nmg_face_new_g.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1257
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_g_snurb", "cdecl"):
    nmg_face_g_snurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_g_snurb", "cdecl")
    nmg_face_g_snurb.argtypes = [POINTER(struct_faceuse), c_int, c_int, c_int, c_int, POINTER(fastf_t), POINTER(fastf_t), c_int, c_int, c_int, POINTER(fastf_t)]
    nmg_face_g_snurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1268
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_bb", "cdecl"):
    nmg_face_bb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_bb", "cdecl")
    nmg_face_bb.argtypes = [POINTER(struct_face), POINTER(struct_bn_tol)]
    nmg_face_bb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1270
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_shell_a", "cdecl"):
    nmg_shell_a = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_shell_a", "cdecl")
    nmg_shell_a.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_shell_a.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1272
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_region_a", "cdecl"):
    nmg_region_a = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_region_a", "cdecl")
    nmg_region_a.argtypes = [POINTER(struct_nmgregion), POINTER(struct_bn_tol)]
    nmg_region_a.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1275
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_demote_lu", "cdecl"):
    nmg_demote_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_demote_lu", "cdecl")
    nmg_demote_lu.argtypes = [POINTER(struct_loopuse)]
    nmg_demote_lu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1276
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_demote_eu", "cdecl"):
    nmg_demote_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_demote_eu", "cdecl")
    nmg_demote_eu.argtypes = [POINTER(struct_edgeuse)]
    nmg_demote_eu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1278
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_movevu", "cdecl"):
    nmg_movevu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_movevu", "cdecl")
    nmg_movevu.argtypes = [POINTER(struct_vertexuse), POINTER(struct_vertex)]
    nmg_movevu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1280
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_je", "cdecl"):
    nmg_je = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_je", "cdecl")
    nmg_je.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse)]
    nmg_je.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1282
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_unglueedge", "cdecl"):
    nmg_unglueedge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_unglueedge", "cdecl")
    nmg_unglueedge.argtypes = [POINTER(struct_edgeuse)]
    nmg_unglueedge.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1283
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_jv", "cdecl"):
    nmg_jv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_jv", "cdecl")
    nmg_jv.argtypes = [POINTER(struct_vertex), POINTER(struct_vertex)]
    nmg_jv.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1285
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_jfg", "cdecl"):
    nmg_jfg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_jfg", "cdecl")
    nmg_jfg.argtypes = [POINTER(struct_face), POINTER(struct_face)]
    nmg_jfg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1287
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_jeg", "cdecl"):
    nmg_jeg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_jeg", "cdecl")
    nmg_jeg.argtypes = [POINTER(struct_edge_g_lseg), POINTER(struct_edge_g_lseg)]
    nmg_jeg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1292
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_merge_regions", "cdecl"):
    nmg_merge_regions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_merge_regions", "cdecl")
    nmg_merge_regions.argtypes = [POINTER(struct_nmgregion), POINTER(struct_nmgregion), POINTER(struct_bn_tol)]
    nmg_merge_regions.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1297
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_shell_coplanar_face_merge", "cdecl"):
    nmg_shell_coplanar_face_merge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_shell_coplanar_face_merge", "cdecl")
    nmg_shell_coplanar_face_merge.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol), c_int, POINTER(struct_bu_list)]
    nmg_shell_coplanar_face_merge.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1301
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_simplify_shell", "cdecl"):
    nmg_simplify_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_simplify_shell", "cdecl")
    nmg_simplify_shell.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list)]
    nmg_simplify_shell.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1302
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_rm_redundancies", "cdecl"):
    nmg_rm_redundancies = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_rm_redundancies", "cdecl")
    nmg_rm_redundancies.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_rm_redundancies.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1305
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_sanitize_s_lv", "cdecl"):
    nmg_sanitize_s_lv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_sanitize_s_lv", "cdecl")
    nmg_sanitize_s_lv.argtypes = [POINTER(struct_shell), c_int]
    nmg_sanitize_s_lv.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1307
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_s_split_touchingloops", "cdecl"):
    nmg_s_split_touchingloops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_s_split_touchingloops", "cdecl")
    nmg_s_split_touchingloops.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_s_split_touchingloops.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1309
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_s_join_touchingloops", "cdecl"):
    nmg_s_join_touchingloops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_s_join_touchingloops", "cdecl")
    nmg_s_join_touchingloops.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_s_join_touchingloops.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1311
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_js", "cdecl"):
    nmg_js = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_js", "cdecl")
    nmg_js.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_js.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1315
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_invert_shell", "cdecl"):
    nmg_invert_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_invert_shell", "cdecl")
    nmg_invert_shell.argtypes = [POINTER(struct_shell)]
    nmg_invert_shell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1318
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cmface", "cdecl"):
    nmg_cmface = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cmface", "cdecl")
    nmg_cmface.argtypes = [POINTER(struct_shell), POINTER(POINTER(POINTER(struct_vertex))), c_int]
    nmg_cmface.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1321
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cface", "cdecl"):
    nmg_cface = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cface", "cdecl")
    nmg_cface.argtypes = [POINTER(struct_shell), POINTER(POINTER(struct_vertex)), c_int]
    nmg_cface.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1324
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_add_loop_to_face", "cdecl"):
    nmg_add_loop_to_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_add_loop_to_face", "cdecl")
    nmg_add_loop_to_face.argtypes = [POINTER(struct_shell), POINTER(struct_faceuse), POINTER(POINTER(struct_vertex)), c_int, c_int]
    nmg_add_loop_to_face.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1329
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_fu_planeeqn", "cdecl"):
    nmg_fu_planeeqn = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_fu_planeeqn", "cdecl")
    nmg_fu_planeeqn.argtypes = [POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_fu_planeeqn.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1331
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_gluefaces", "cdecl"):
    nmg_gluefaces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_gluefaces", "cdecl")
    nmg_gluefaces.argtypes = [POINTER(POINTER(struct_faceuse)), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_gluefaces.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1335
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_simplify_face", "cdecl"):
    nmg_simplify_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_simplify_face", "cdecl")
    nmg_simplify_face.argtypes = [POINTER(struct_faceuse), POINTER(struct_bu_list)]
    nmg_simplify_face.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1336
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_reverse_face", "cdecl"):
    nmg_reverse_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_reverse_face", "cdecl")
    nmg_reverse_face.argtypes = [POINTER(struct_faceuse)]
    nmg_reverse_face.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1337
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mv_fu_between_shells", "cdecl"):
    nmg_mv_fu_between_shells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mv_fu_between_shells", "cdecl")
    nmg_mv_fu_between_shells.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_faceuse)]
    nmg_mv_fu_between_shells.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1340
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_jf", "cdecl"):
    nmg_jf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_jf", "cdecl")
    nmg_jf.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse)]
    nmg_jf.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1342
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_dup_face", "cdecl"):
    nmg_dup_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_dup_face", "cdecl")
    nmg_dup_face.argtypes = [POINTER(struct_faceuse), POINTER(struct_shell)]
    nmg_dup_face.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1345
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_jl", "cdecl"):
    nmg_jl = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_jl", "cdecl")
    nmg_jl.argtypes = [POINTER(struct_loopuse), POINTER(struct_edgeuse)]
    nmg_jl.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1347
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_join_2loops", "cdecl"):
    nmg_join_2loops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_join_2loops", "cdecl")
    nmg_join_2loops.argtypes = [POINTER(struct_vertexuse), POINTER(struct_vertexuse)]
    nmg_join_2loops.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1349
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_join_singvu_loop", "cdecl"):
    nmg_join_singvu_loop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_join_singvu_loop", "cdecl")
    nmg_join_singvu_loop.argtypes = [POINTER(struct_vertexuse), POINTER(struct_vertexuse)]
    nmg_join_singvu_loop.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1351
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_join_2singvu_loops", "cdecl"):
    nmg_join_2singvu_loops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_join_2singvu_loops", "cdecl")
    nmg_join_2singvu_loops.argtypes = [POINTER(struct_vertexuse), POINTER(struct_vertexuse)]
    nmg_join_2singvu_loops.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1353
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cut_loop", "cdecl"):
    nmg_cut_loop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cut_loop", "cdecl")
    nmg_cut_loop.argtypes = [POINTER(struct_vertexuse), POINTER(struct_vertexuse), POINTER(struct_bu_list)]
    nmg_cut_loop.restype = POINTER(struct_loopuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1356
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_split_lu_at_vu", "cdecl"):
    nmg_split_lu_at_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_split_lu_at_vu", "cdecl")
    nmg_split_lu_at_vu.argtypes = [POINTER(struct_loopuse), POINTER(struct_vertexuse)]
    nmg_split_lu_at_vu.restype = POINTER(struct_loopuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1358
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_repeated_v_in_lu", "cdecl"):
    nmg_find_repeated_v_in_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_repeated_v_in_lu", "cdecl")
    nmg_find_repeated_v_in_lu.argtypes = [POINTER(struct_vertexuse)]
    nmg_find_repeated_v_in_lu.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1359
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_split_touchingloops", "cdecl"):
    nmg_split_touchingloops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_split_touchingloops", "cdecl")
    nmg_split_touchingloops.argtypes = [POINTER(struct_loopuse), POINTER(struct_bn_tol)]
    nmg_split_touchingloops.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1361
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_join_touchingloops", "cdecl"):
    nmg_join_touchingloops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_join_touchingloops", "cdecl")
    nmg_join_touchingloops.argtypes = [POINTER(struct_loopuse)]
    nmg_join_touchingloops.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1362
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_get_touching_jaunts", "cdecl"):
    nmg_get_touching_jaunts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_get_touching_jaunts", "cdecl")
    nmg_get_touching_jaunts.argtypes = [POINTER(struct_loopuse), POINTER(struct_bu_ptbl), POINTER(c_int)]
    nmg_get_touching_jaunts.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1365
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kill_accordions", "cdecl"):
    nmg_kill_accordions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kill_accordions", "cdecl")
    nmg_kill_accordions.argtypes = [POINTER(struct_loopuse)]
    nmg_kill_accordions.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1366
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_split_at_touching_jaunt", "cdecl"):
    nmg_loop_split_at_touching_jaunt = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_split_at_touching_jaunt", "cdecl")
    nmg_loop_split_at_touching_jaunt.argtypes = [POINTER(struct_loopuse), POINTER(struct_bn_tol)]
    nmg_loop_split_at_touching_jaunt.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1368
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_simplify_loop", "cdecl"):
    nmg_simplify_loop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_simplify_loop", "cdecl")
    nmg_simplify_loop.argtypes = [POINTER(struct_loopuse), POINTER(struct_bu_list)]
    nmg_simplify_loop.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1369
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kill_snakes", "cdecl"):
    nmg_kill_snakes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kill_snakes", "cdecl")
    nmg_kill_snakes.argtypes = [POINTER(struct_loopuse), POINTER(struct_bu_list)]
    nmg_kill_snakes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1370
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mv_lu_between_shells", "cdecl"):
    nmg_mv_lu_between_shells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mv_lu_between_shells", "cdecl")
    nmg_mv_lu_between_shells.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_loopuse)]
    nmg_mv_lu_between_shells.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1373
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_moveltof", "cdecl"):
    nmg_moveltof = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_moveltof", "cdecl")
    nmg_moveltof.argtypes = [POINTER(struct_faceuse), POINTER(struct_shell)]
    nmg_moveltof.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1375
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_dup_loop", "cdecl"):
    nmg_dup_loop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_dup_loop", "cdecl")
    nmg_dup_loop.argtypes = [POINTER(struct_loopuse), POINTER(c_uint32), POINTER(POINTER(c_long))]
    nmg_dup_loop.restype = POINTER(struct_loopuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1378
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_set_lu_orientation", "cdecl"):
    nmg_set_lu_orientation = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_set_lu_orientation", "cdecl")
    nmg_set_lu_orientation.argtypes = [POINTER(struct_loopuse), c_int]
    nmg_set_lu_orientation.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1380
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_lu_reorient", "cdecl"):
    nmg_lu_reorient = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_lu_reorient", "cdecl")
    nmg_lu_reorient.argtypes = [POINTER(struct_loopuse)]
    nmg_lu_reorient.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1382
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eusplit", "cdecl"):
    nmg_eusplit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eusplit", "cdecl")
    nmg_eusplit.argtypes = [POINTER(struct_vertex), POINTER(struct_edgeuse), c_int]
    nmg_eusplit.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1385
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_esplit", "cdecl"):
    nmg_esplit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_esplit", "cdecl")
    nmg_esplit.argtypes = [POINTER(struct_vertex), POINTER(struct_edgeuse), c_int]
    nmg_esplit.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1388
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ebreak", "cdecl"):
    nmg_ebreak = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ebreak", "cdecl")
    nmg_ebreak.argtypes = [POINTER(struct_vertex), POINTER(struct_edgeuse)]
    nmg_ebreak.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1390
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ebreaker", "cdecl"):
    nmg_ebreaker = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ebreaker", "cdecl")
    nmg_ebreaker.argtypes = [POINTER(struct_vertex), POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_ebreaker.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1393
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_e2break", "cdecl"):
    nmg_e2break = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_e2break", "cdecl")
    nmg_e2break.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse)]
    nmg_e2break.restype = POINTER(struct_vertex)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1395
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_unbreak_edge", "cdecl"):
    nmg_unbreak_edge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_unbreak_edge", "cdecl")
    nmg_unbreak_edge.argtypes = [POINTER(struct_edgeuse)]
    nmg_unbreak_edge.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1396
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_unbreak_shell_edge_unsafe", "cdecl"):
    nmg_unbreak_shell_edge_unsafe = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_unbreak_shell_edge_unsafe", "cdecl")
    nmg_unbreak_shell_edge_unsafe.argtypes = [POINTER(struct_edgeuse)]
    nmg_unbreak_shell_edge_unsafe.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1397
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eins", "cdecl"):
    nmg_eins = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eins", "cdecl")
    nmg_eins.argtypes = [POINTER(struct_edgeuse)]
    nmg_eins.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1398
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mv_eu_between_shells", "cdecl"):
    nmg_mv_eu_between_shells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mv_eu_between_shells", "cdecl")
    nmg_mv_eu_between_shells.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_edgeuse)]
    nmg_mv_eu_between_shells.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1402
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mv_vu_between_shells", "cdecl"):
    nmg_mv_vu_between_shells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mv_vu_between_shells", "cdecl")
    nmg_mv_vu_between_shells.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_vertexuse)]
    nmg_mv_vu_between_shells.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1408
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_model", "cdecl"):
    nmg_find_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_model", "cdecl")
    nmg_find_model.argtypes = [POINTER(c_uint32)]
    nmg_find_model.restype = POINTER(struct_model)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1409
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_shell", "cdecl"):
    nmg_find_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_shell", "cdecl")
    nmg_find_shell.argtypes = [POINTER(c_uint32)]
    nmg_find_shell.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1410
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_model_bb", "cdecl"):
    nmg_model_bb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_model_bb", "cdecl")
    nmg_model_bb.argtypes = [point_t, point_t, POINTER(struct_model)]
    nmg_model_bb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1416
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_shell_is_empty", "cdecl"):
    nmg_shell_is_empty = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_shell_is_empty", "cdecl")
    nmg_shell_is_empty.argtypes = [POINTER(struct_shell)]
    nmg_shell_is_empty.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1417
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_s_of_lu", "cdecl"):
    nmg_find_s_of_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_s_of_lu", "cdecl")
    nmg_find_s_of_lu.argtypes = [POINTER(struct_loopuse)]
    nmg_find_s_of_lu.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1418
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_s_of_eu", "cdecl"):
    nmg_find_s_of_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_s_of_eu", "cdecl")
    nmg_find_s_of_eu.argtypes = [POINTER(struct_edgeuse)]
    nmg_find_s_of_eu.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1419
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_s_of_vu", "cdecl"):
    nmg_find_s_of_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_s_of_vu", "cdecl")
    nmg_find_s_of_vu.argtypes = [POINTER(struct_vertexuse)]
    nmg_find_s_of_vu.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1422
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_fu_of_eu", "cdecl"):
    nmg_find_fu_of_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_fu_of_eu", "cdecl")
    nmg_find_fu_of_eu.argtypes = [POINTER(struct_edgeuse)]
    nmg_find_fu_of_eu.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1423
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_fu_of_lu", "cdecl"):
    nmg_find_fu_of_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_fu_of_lu", "cdecl")
    nmg_find_fu_of_lu.argtypes = [POINTER(struct_loopuse)]
    nmg_find_fu_of_lu.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1424
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_fu_of_vu", "cdecl"):
    nmg_find_fu_of_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_fu_of_vu", "cdecl")
    nmg_find_fu_of_vu.argtypes = [POINTER(struct_vertexuse)]
    nmg_find_fu_of_vu.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1425
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_fu_with_fg_in_s", "cdecl"):
    nmg_find_fu_with_fg_in_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_fu_with_fg_in_s", "cdecl")
    nmg_find_fu_with_fg_in_s.argtypes = [POINTER(struct_shell), POINTER(struct_faceuse)]
    nmg_find_fu_with_fg_in_s.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1427
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_measure_fu_angle", "cdecl"):
    nmg_measure_fu_angle = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_measure_fu_angle", "cdecl")
    nmg_measure_fu_angle.argtypes = [POINTER(struct_edgeuse), vect_t, vect_t, vect_t]
    nmg_measure_fu_angle.restype = c_double

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1433
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_lu_of_vu", "cdecl"):
    nmg_find_lu_of_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_lu_of_vu", "cdecl")
    nmg_find_lu_of_vu.argtypes = [POINTER(struct_vertexuse)]
    nmg_find_lu_of_vu.restype = POINTER(struct_loopuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1434
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_is_a_crack", "cdecl"):
    nmg_loop_is_a_crack = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_is_a_crack", "cdecl")
    nmg_loop_is_a_crack.argtypes = [POINTER(struct_loopuse)]
    nmg_loop_is_a_crack.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1435
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_is_ccw", "cdecl"):
    nmg_loop_is_ccw = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_is_ccw", "cdecl")
    nmg_loop_is_ccw.argtypes = [POINTER(struct_loopuse), plane_t, POINTER(struct_bn_tol)]
    nmg_loop_is_ccw.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1438
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_touches_self", "cdecl"):
    nmg_loop_touches_self = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_touches_self", "cdecl")
    nmg_loop_touches_self.argtypes = [POINTER(struct_loopuse)]
    nmg_loop_touches_self.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1439
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_2lu_identical", "cdecl"):
    nmg_2lu_identical = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_2lu_identical", "cdecl")
    nmg_2lu_identical.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse)]
    nmg_2lu_identical.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1443
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_matching_eu_in_s", "cdecl"):
    nmg_find_matching_eu_in_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_matching_eu_in_s", "cdecl")
    nmg_find_matching_eu_in_s.argtypes = [POINTER(struct_edgeuse), POINTER(struct_shell)]
    nmg_find_matching_eu_in_s.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1445
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_findeu", "cdecl"):
    nmg_findeu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_findeu", "cdecl")
    nmg_findeu.argtypes = [POINTER(struct_vertex), POINTER(struct_vertex), POINTER(struct_shell), POINTER(struct_edgeuse), c_int]
    nmg_findeu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1450
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_eu_in_face", "cdecl"):
    nmg_find_eu_in_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_eu_in_face", "cdecl")
    nmg_find_eu_in_face.argtypes = [POINTER(struct_vertex), POINTER(struct_vertex), POINTER(struct_faceuse), POINTER(struct_edgeuse), c_int]
    nmg_find_eu_in_face.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1455
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_e", "cdecl"):
    nmg_find_e = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_e", "cdecl")
    nmg_find_e.argtypes = [POINTER(struct_vertex), POINTER(struct_vertex), POINTER(struct_shell), POINTER(struct_edge)]
    nmg_find_e.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1459
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_eu_of_vu", "cdecl"):
    nmg_find_eu_of_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_eu_of_vu", "cdecl")
    nmg_find_eu_of_vu.argtypes = [POINTER(struct_vertexuse)]
    nmg_find_eu_of_vu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1460
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_eu_with_vu_in_lu", "cdecl"):
    nmg_find_eu_with_vu_in_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_eu_with_vu_in_lu", "cdecl")
    nmg_find_eu_with_vu_in_lu.argtypes = [POINTER(struct_loopuse), POINTER(struct_vertexuse)]
    nmg_find_eu_with_vu_in_lu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1462
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_faceradial", "cdecl"):
    nmg_faceradial = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_faceradial", "cdecl")
    nmg_faceradial.argtypes = [POINTER(struct_edgeuse)]
    nmg_faceradial.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1463
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_face_edge_in_shell", "cdecl"):
    nmg_radial_face_edge_in_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_face_edge_in_shell", "cdecl")
    nmg_radial_face_edge_in_shell.argtypes = [POINTER(struct_edgeuse)]
    nmg_radial_face_edge_in_shell.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1464
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_edge_between_2fu", "cdecl"):
    nmg_find_edge_between_2fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_edge_between_2fu", "cdecl")
    nmg_find_edge_between_2fu.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_find_edge_between_2fu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1468
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_e_nearest_pt2", "cdecl"):
    nmg_find_e_nearest_pt2 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_e_nearest_pt2", "cdecl")
    nmg_find_e_nearest_pt2.argtypes = [POINTER(c_uint32), point_t, mat_t, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_find_e_nearest_pt2.restype = POINTER(struct_edge)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1473
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_matching_eu_in_s", "cdecl"):
    nmg_find_matching_eu_in_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_matching_eu_in_s", "cdecl")
    nmg_find_matching_eu_in_s.argtypes = [POINTER(struct_edgeuse), POINTER(struct_shell)]
    nmg_find_matching_eu_in_s.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1475
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eu_2vecs_perp", "cdecl"):
    nmg_eu_2vecs_perp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eu_2vecs_perp", "cdecl")
    nmg_eu_2vecs_perp.argtypes = [vect_t, vect_t, vect_t, POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_eu_2vecs_perp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1480
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_eu_leftvec", "cdecl"):
    nmg_find_eu_leftvec = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_eu_leftvec", "cdecl")
    nmg_find_eu_leftvec.argtypes = [vect_t, POINTER(struct_edgeuse)]
    nmg_find_eu_leftvec.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1482
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_eu_left_non_unit", "cdecl"):
    nmg_find_eu_left_non_unit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_eu_left_non_unit", "cdecl")
    nmg_find_eu_left_non_unit.argtypes = [vect_t, POINTER(struct_edgeuse)]
    nmg_find_eu_left_non_unit.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1484
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_ot_same_eu_of_e", "cdecl"):
    nmg_find_ot_same_eu_of_e = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_ot_same_eu_of_e", "cdecl")
    nmg_find_ot_same_eu_of_e.argtypes = [POINTER(struct_edge)]
    nmg_find_ot_same_eu_of_e.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1487
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_v_in_face", "cdecl"):
    nmg_find_v_in_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_v_in_face", "cdecl")
    nmg_find_v_in_face.argtypes = [POINTER(struct_vertex), POINTER(struct_faceuse)]
    nmg_find_v_in_face.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1489
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_v_in_shell", "cdecl"):
    nmg_find_v_in_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_v_in_shell", "cdecl")
    nmg_find_v_in_shell.argtypes = [POINTER(struct_vertex), POINTER(struct_shell), c_int]
    nmg_find_v_in_shell.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1492
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_pnt_in_lu", "cdecl"):
    nmg_find_pnt_in_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_pnt_in_lu", "cdecl")
    nmg_find_pnt_in_lu.argtypes = [POINTER(struct_loopuse), point_t, POINTER(struct_bn_tol)]
    nmg_find_pnt_in_lu.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1495
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_pnt_in_face", "cdecl"):
    nmg_find_pnt_in_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_pnt_in_face", "cdecl")
    nmg_find_pnt_in_face.argtypes = [POINTER(struct_faceuse), point_t, POINTER(struct_bn_tol)]
    nmg_find_pnt_in_face.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1498
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_pnt_in_shell", "cdecl"):
    nmg_find_pnt_in_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_pnt_in_shell", "cdecl")
    nmg_find_pnt_in_shell.argtypes = [POINTER(struct_shell), point_t, POINTER(struct_bn_tol)]
    nmg_find_pnt_in_shell.restype = POINTER(struct_vertex)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1501
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_pnt_in_model", "cdecl"):
    nmg_find_pnt_in_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_pnt_in_model", "cdecl")
    nmg_find_pnt_in_model.argtypes = [POINTER(struct_model), point_t, POINTER(struct_bn_tol)]
    nmg_find_pnt_in_model.restype = POINTER(struct_vertex)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1504
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_vertex_in_edgelist", "cdecl"):
    nmg_is_vertex_in_edgelist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_vertex_in_edgelist", "cdecl")
    nmg_is_vertex_in_edgelist.argtypes = [POINTER(struct_vertex), POINTER(struct_bu_list)]
    nmg_is_vertex_in_edgelist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1506
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_vertex_in_looplist", "cdecl"):
    nmg_is_vertex_in_looplist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_vertex_in_looplist", "cdecl")
    nmg_is_vertex_in_looplist.argtypes = [POINTER(struct_vertex), POINTER(struct_bu_list), c_int]
    nmg_is_vertex_in_looplist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1509
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_vertex_in_face", "cdecl"):
    nmg_is_vertex_in_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_vertex_in_face", "cdecl")
    nmg_is_vertex_in_face.argtypes = [POINTER(struct_vertex), POINTER(struct_face)]
    nmg_is_vertex_in_face.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1511
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_vertex_a_selfloop_in_shell", "cdecl"):
    nmg_is_vertex_a_selfloop_in_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_vertex_a_selfloop_in_shell", "cdecl")
    nmg_is_vertex_a_selfloop_in_shell.argtypes = [POINTER(struct_vertex), POINTER(struct_shell)]
    nmg_is_vertex_a_selfloop_in_shell.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1513
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_vertex_in_facelist", "cdecl"):
    nmg_is_vertex_in_facelist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_vertex_in_facelist", "cdecl")
    nmg_is_vertex_in_facelist.argtypes = [POINTER(struct_vertex), POINTER(struct_bu_list)]
    nmg_is_vertex_in_facelist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1515
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_edge_in_edgelist", "cdecl"):
    nmg_is_edge_in_edgelist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_edge_in_edgelist", "cdecl")
    nmg_is_edge_in_edgelist.argtypes = [POINTER(struct_edge), POINTER(struct_bu_list)]
    nmg_is_edge_in_edgelist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1517
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_edge_in_looplist", "cdecl"):
    nmg_is_edge_in_looplist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_edge_in_looplist", "cdecl")
    nmg_is_edge_in_looplist.argtypes = [POINTER(struct_edge), POINTER(struct_bu_list)]
    nmg_is_edge_in_looplist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1519
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_edge_in_facelist", "cdecl"):
    nmg_is_edge_in_facelist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_edge_in_facelist", "cdecl")
    nmg_is_edge_in_facelist.argtypes = [POINTER(struct_edge), POINTER(struct_bu_list)]
    nmg_is_edge_in_facelist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1521
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_loop_in_facelist", "cdecl"):
    nmg_is_loop_in_facelist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_loop_in_facelist", "cdecl")
    nmg_is_loop_in_facelist.argtypes = [POINTER(struct_loop), POINTER(struct_bu_list)]
    nmg_is_loop_in_facelist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1525
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vertex_tabulate", "cdecl"):
    nmg_vertex_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vertex_tabulate", "cdecl")
    nmg_vertex_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_vertex_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1528
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vertexuse_normal_tabulate", "cdecl"):
    nmg_vertexuse_normal_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vertexuse_normal_tabulate", "cdecl")
    nmg_vertexuse_normal_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_vertexuse_normal_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1531
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edgeuse_tabulate", "cdecl"):
    nmg_edgeuse_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edgeuse_tabulate", "cdecl")
    nmg_edgeuse_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_edgeuse_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1534
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_tabulate", "cdecl"):
    nmg_edge_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_tabulate", "cdecl")
    nmg_edge_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_edge_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1537
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_g_tabulate", "cdecl"):
    nmg_edge_g_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_g_tabulate", "cdecl")
    nmg_edge_g_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_edge_g_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1540
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_tabulate", "cdecl"):
    nmg_face_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_tabulate", "cdecl")
    nmg_face_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_face_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1543
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edgeuse_with_eg_tabulate", "cdecl"):
    nmg_edgeuse_with_eg_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edgeuse_with_eg_tabulate", "cdecl")
    nmg_edgeuse_with_eg_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(struct_edge_g_lseg)]
    nmg_edgeuse_with_eg_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1545
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edgeuse_on_line_tabulate", "cdecl"):
    nmg_edgeuse_on_line_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edgeuse_on_line_tabulate", "cdecl")
    nmg_edgeuse_on_line_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(c_uint32), point_t, vect_t, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_edgeuse_on_line_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1551
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_e_and_v_tabulate", "cdecl"):
    nmg_e_and_v_tabulate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_e_and_v_tabulate", "cdecl")
    nmg_e_and_v_tabulate.argtypes = [POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl), POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_e_and_v_tabulate.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1555
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_2edgeuse_g_coincident", "cdecl"):
    nmg_2edgeuse_g_coincident = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_2edgeuse_g_coincident", "cdecl")
    nmg_2edgeuse_g_coincident.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_2edgeuse_g_coincident.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1560
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_translate_face", "cdecl"):
    nmg_translate_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_translate_face", "cdecl")
    nmg_translate_face.argtypes = [POINTER(struct_faceuse), vect_t, POINTER(struct_bu_list)]
    nmg_translate_face.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1561
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_extrude_face", "cdecl"):
    nmg_extrude_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_extrude_face", "cdecl")
    nmg_extrude_face.argtypes = [POINTER(struct_faceuse), vect_t, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_extrude_face.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1562
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_vertex_in_lu", "cdecl"):
    nmg_find_vertex_in_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_vertex_in_lu", "cdecl")
    nmg_find_vertex_in_lu.argtypes = [POINTER(struct_vertex), POINTER(struct_loopuse)]
    nmg_find_vertex_in_lu.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1563
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_fix_overlapping_loops", "cdecl"):
    nmg_fix_overlapping_loops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_fix_overlapping_loops", "cdecl")
    nmg_fix_overlapping_loops.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_fix_overlapping_loops.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1564
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_crossed_loops", "cdecl"):
    nmg_break_crossed_loops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_crossed_loops", "cdecl")
    nmg_break_crossed_loops.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_break_crossed_loops.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1565
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_extrude_cleanup", "cdecl"):
    nmg_extrude_cleanup = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_extrude_cleanup", "cdecl")
    nmg_extrude_cleanup.argtypes = [POINTER(struct_shell), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_extrude_cleanup.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1566
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_hollow_shell", "cdecl"):
    nmg_hollow_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_hollow_shell", "cdecl")
    nmg_hollow_shell.argtypes = [POINTER(struct_shell), fastf_t, c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_hollow_shell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1567
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_extrude_shell", "cdecl"):
    nmg_extrude_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_extrude_shell", "cdecl")
    nmg_extrude_shell.argtypes = [POINTER(struct_shell), fastf_t, c_int, c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_extrude_shell.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1570
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_orientation", "cdecl"):
    nmg_orientation = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_orientation", "cdecl")
    nmg_orientation.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        nmg_orientation.restype = ReturnString
    else:
        nmg_orientation.restype = String
        nmg_orientation.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1571
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_orient", "cdecl"):
    nmg_pr_orient = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_orient", "cdecl")
    nmg_pr_orient.argtypes = [c_int, String]
    nmg_pr_orient.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1573
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_m", "cdecl"):
    nmg_pr_m = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_m", "cdecl")
    nmg_pr_m.argtypes = [POINTER(struct_model)]
    nmg_pr_m.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1574
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_r", "cdecl"):
    nmg_pr_r = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_r", "cdecl")
    nmg_pr_r.argtypes = [POINTER(struct_nmgregion), String]
    nmg_pr_r.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1576
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_sa", "cdecl"):
    nmg_pr_sa = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_sa", "cdecl")
    nmg_pr_sa.argtypes = [POINTER(struct_shell_a), String]
    nmg_pr_sa.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1578
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_lg", "cdecl"):
    nmg_pr_lg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_lg", "cdecl")
    nmg_pr_lg.argtypes = [POINTER(struct_loop_g), String]
    nmg_pr_lg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1580
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_fg", "cdecl"):
    nmg_pr_fg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_fg", "cdecl")
    nmg_pr_fg.argtypes = [POINTER(c_uint32), String]
    nmg_pr_fg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1582
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_s", "cdecl"):
    nmg_pr_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_s", "cdecl")
    nmg_pr_s.argtypes = [POINTER(struct_shell), String]
    nmg_pr_s.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1584
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_s_briefly", "cdecl"):
    nmg_pr_s_briefly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_s_briefly", "cdecl")
    nmg_pr_s_briefly.argtypes = [POINTER(struct_shell), String]
    nmg_pr_s_briefly.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1586
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_f", "cdecl"):
    nmg_pr_f = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_f", "cdecl")
    nmg_pr_f.argtypes = [POINTER(struct_face), String]
    nmg_pr_f.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1588
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_fu", "cdecl"):
    nmg_pr_fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_fu", "cdecl")
    nmg_pr_fu.argtypes = [POINTER(struct_faceuse), String]
    nmg_pr_fu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1590
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_fu_briefly", "cdecl"):
    nmg_pr_fu_briefly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_fu_briefly", "cdecl")
    nmg_pr_fu_briefly.argtypes = [POINTER(struct_faceuse), String]
    nmg_pr_fu_briefly.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1592
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_l", "cdecl"):
    nmg_pr_l = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_l", "cdecl")
    nmg_pr_l.argtypes = [POINTER(struct_loop), String]
    nmg_pr_l.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1594
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_lu", "cdecl"):
    nmg_pr_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_lu", "cdecl")
    nmg_pr_lu.argtypes = [POINTER(struct_loopuse), String]
    nmg_pr_lu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1596
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_lu_briefly", "cdecl"):
    nmg_pr_lu_briefly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_lu_briefly", "cdecl")
    nmg_pr_lu_briefly.argtypes = [POINTER(struct_loopuse), String]
    nmg_pr_lu_briefly.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1598
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_eg", "cdecl"):
    nmg_pr_eg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_eg", "cdecl")
    nmg_pr_eg.argtypes = [POINTER(c_uint32), String]
    nmg_pr_eg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1600
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_e", "cdecl"):
    nmg_pr_e = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_e", "cdecl")
    nmg_pr_e.argtypes = [POINTER(struct_edge), String]
    nmg_pr_e.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1602
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_eu", "cdecl"):
    nmg_pr_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_eu", "cdecl")
    nmg_pr_eu.argtypes = [POINTER(struct_edgeuse), String]
    nmg_pr_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1604
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_eu_briefly", "cdecl"):
    nmg_pr_eu_briefly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_eu_briefly", "cdecl")
    nmg_pr_eu_briefly.argtypes = [POINTER(struct_edgeuse), String]
    nmg_pr_eu_briefly.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1606
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_eu_endpoints", "cdecl"):
    nmg_pr_eu_endpoints = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_eu_endpoints", "cdecl")
    nmg_pr_eu_endpoints.argtypes = [POINTER(struct_edgeuse), String]
    nmg_pr_eu_endpoints.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1608
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_vg", "cdecl"):
    nmg_pr_vg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_vg", "cdecl")
    nmg_pr_vg.argtypes = [POINTER(struct_vertex_g), String]
    nmg_pr_vg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1610
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_v", "cdecl"):
    nmg_pr_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_v", "cdecl")
    nmg_pr_v.argtypes = [POINTER(struct_vertex), String]
    nmg_pr_v.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1612
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_vu", "cdecl"):
    nmg_pr_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_vu", "cdecl")
    nmg_pr_vu.argtypes = [POINTER(struct_vertexuse), String]
    nmg_pr_vu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1614
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_vu_briefly", "cdecl"):
    nmg_pr_vu_briefly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_vu_briefly", "cdecl")
    nmg_pr_vu_briefly.argtypes = [POINTER(struct_vertexuse), String]
    nmg_pr_vu_briefly.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1616
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_vua", "cdecl"):
    nmg_pr_vua = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_vua", "cdecl")
    nmg_pr_vua.argtypes = [POINTER(c_uint32), String]
    nmg_pr_vua.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1618
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_euprint", "cdecl"):
    nmg_euprint = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_euprint", "cdecl")
    nmg_euprint.argtypes = [String, POINTER(struct_edgeuse)]
    nmg_euprint.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1620
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_ptbl", "cdecl"):
    nmg_pr_ptbl = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_ptbl", "cdecl")
    nmg_pr_ptbl.argtypes = [String, POINTER(struct_bu_ptbl), c_int]
    nmg_pr_ptbl.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1623
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_ptbl_vert_list", "cdecl"):
    nmg_pr_ptbl_vert_list = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_ptbl_vert_list", "cdecl")
    nmg_pr_ptbl_vert_list.argtypes = [String, POINTER(struct_bu_ptbl), POINTER(fastf_t)]
    nmg_pr_ptbl_vert_list.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1626
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_one_eu_vecs", "cdecl"):
    nmg_pr_one_eu_vecs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_one_eu_vecs", "cdecl")
    nmg_pr_one_eu_vecs.argtypes = [POINTER(struct_edgeuse), vect_t, vect_t, vect_t, POINTER(struct_bn_tol)]
    nmg_pr_one_eu_vecs.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1631
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_fu_around_eu_vecs", "cdecl"):
    nmg_pr_fu_around_eu_vecs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_fu_around_eu_vecs", "cdecl")
    nmg_pr_fu_around_eu_vecs.argtypes = [POINTER(struct_edgeuse), vect_t, vect_t, vect_t, POINTER(struct_bn_tol)]
    nmg_pr_fu_around_eu_vecs.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1636
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_fu_around_eu", "cdecl"):
    nmg_pr_fu_around_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_fu_around_eu", "cdecl")
    nmg_pr_fu_around_eu.argtypes = [POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_pr_fu_around_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1638
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_lu_around_eu", "cdecl"):
    nmg_pl_lu_around_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_lu_around_eu", "cdecl")
    nmg_pl_lu_around_eu.argtypes = [POINTER(struct_edgeuse), POINTER(struct_bu_list)]
    nmg_pl_lu_around_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1639
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_fus_in_fg", "cdecl"):
    nmg_pr_fus_in_fg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_fus_in_fg", "cdecl")
    nmg_pr_fus_in_fg.argtypes = [POINTER(c_uint32)]
    nmg_pr_fus_in_fg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1642
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_snurb_calc_lu_uv_orient", "cdecl"):
    nmg_snurb_calc_lu_uv_orient = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_snurb_calc_lu_uv_orient", "cdecl")
    nmg_snurb_calc_lu_uv_orient.argtypes = [POINTER(struct_loopuse)]
    nmg_snurb_calc_lu_uv_orient.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1643
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_snurb_fu_eval", "cdecl"):
    nmg_snurb_fu_eval = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_snurb_fu_eval", "cdecl")
    nmg_snurb_fu_eval.argtypes = [POINTER(struct_faceuse), fastf_t, fastf_t, point_t]
    nmg_snurb_fu_eval.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1647
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_snurb_fu_get_norm", "cdecl"):
    nmg_snurb_fu_get_norm = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_snurb_fu_get_norm", "cdecl")
    nmg_snurb_fu_get_norm.argtypes = [POINTER(struct_faceuse), fastf_t, fastf_t, vect_t]
    nmg_snurb_fu_get_norm.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1651
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_snurb_fu_get_norm_at_vu", "cdecl"):
    nmg_snurb_fu_get_norm_at_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_snurb_fu_get_norm_at_vu", "cdecl")
    nmg_snurb_fu_get_norm_at_vu.argtypes = [POINTER(struct_faceuse), POINTER(struct_vertexuse), vect_t]
    nmg_snurb_fu_get_norm_at_vu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1654
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_zero_length_edges", "cdecl"):
    nmg_find_zero_length_edges = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_zero_length_edges", "cdecl")
    nmg_find_zero_length_edges.argtypes = [POINTER(struct_model), POINTER(struct_bu_list)]
    nmg_find_zero_length_edges.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1655
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_top_face_in_dir", "cdecl"):
    nmg_find_top_face_in_dir = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_top_face_in_dir", "cdecl")
    nmg_find_top_face_in_dir.argtypes = [POINTER(struct_shell), c_int, POINTER(c_long)]
    nmg_find_top_face_in_dir.restype = POINTER(struct_face)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1657
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_top_face", "cdecl"):
    nmg_find_top_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_top_face", "cdecl")
    nmg_find_top_face.argtypes = [POINTER(struct_shell), POINTER(c_int), POINTER(c_long)]
    nmg_find_top_face.restype = POINTER(struct_face)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1660
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_outer_and_void_shells", "cdecl"):
    nmg_find_outer_and_void_shells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_outer_and_void_shells", "cdecl")
    nmg_find_outer_and_void_shells.argtypes = [POINTER(struct_nmgregion), POINTER(POINTER(POINTER(struct_bu_ptbl))), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_find_outer_and_void_shells.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1664
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mark_edges_real", "cdecl"):
    nmg_mark_edges_real = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mark_edges_real", "cdecl")
    nmg_mark_edges_real.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_mark_edges_real.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1665
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_tabulate_face_g_verts", "cdecl"):
    nmg_tabulate_face_g_verts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_tabulate_face_g_verts", "cdecl")
    nmg_tabulate_face_g_verts.argtypes = [POINTER(struct_bu_ptbl), POINTER(struct_face_g_plane)]
    nmg_tabulate_face_g_verts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1667
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_shell_self", "cdecl"):
    nmg_isect_shell_self = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_shell_self", "cdecl")
    nmg_isect_shell_self.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_isect_shell_self.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1670
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_next_radial_eu", "cdecl"):
    nmg_next_radial_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_next_radial_eu", "cdecl")
    nmg_next_radial_eu.argtypes = [POINTER(struct_edgeuse), POINTER(struct_shell), c_int]
    nmg_next_radial_eu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1673
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_prev_radial_eu", "cdecl"):
    nmg_prev_radial_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_prev_radial_eu", "cdecl")
    nmg_prev_radial_eu.argtypes = [POINTER(struct_edgeuse), POINTER(struct_shell), c_int]
    nmg_prev_radial_eu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1676
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_face_count", "cdecl"):
    nmg_radial_face_count = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_face_count", "cdecl")
    nmg_radial_face_count.argtypes = [POINTER(struct_edgeuse), POINTER(struct_shell)]
    nmg_radial_face_count.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1678
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_check_closed_shell", "cdecl"):
    nmg_check_closed_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_check_closed_shell", "cdecl")
    nmg_check_closed_shell.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_check_closed_shell.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1680
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_move_lu_between_fus", "cdecl"):
    nmg_move_lu_between_fus = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_move_lu_between_fus", "cdecl")
    nmg_move_lu_between_fus.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_loopuse)]
    nmg_move_lu_between_fus.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1683
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_plane_newell", "cdecl"):
    nmg_loop_plane_newell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_plane_newell", "cdecl")
    nmg_loop_plane_newell.argtypes = [POINTER(struct_loopuse), plane_t]
    nmg_loop_plane_newell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1685
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_plane_area", "cdecl"):
    nmg_loop_plane_area = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_plane_area", "cdecl")
    nmg_loop_plane_area.argtypes = [POINTER(struct_loopuse), plane_t]
    nmg_loop_plane_area.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1687
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_plane_area2", "cdecl"):
    nmg_loop_plane_area2 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_plane_area2", "cdecl")
    nmg_loop_plane_area2.argtypes = [POINTER(struct_loopuse), plane_t, POINTER(struct_bn_tol)]
    nmg_loop_plane_area2.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1690
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_calc_face_plane", "cdecl"):
    nmg_calc_face_plane = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_calc_face_plane", "cdecl")
    nmg_calc_face_plane.argtypes = [POINTER(struct_faceuse), plane_t, POINTER(struct_bu_list)]
    nmg_calc_face_plane.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1692
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_calc_face_g", "cdecl"):
    nmg_calc_face_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_calc_face_g", "cdecl")
    nmg_calc_face_g.argtypes = [POINTER(struct_faceuse), POINTER(struct_bu_list)]
    nmg_calc_face_g.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1693
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_faceuse_area", "cdecl"):
    nmg_faceuse_area = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_faceuse_area", "cdecl")
    nmg_faceuse_area.argtypes = [POINTER(struct_faceuse)]
    nmg_faceuse_area.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1694
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_shell_area", "cdecl"):
    nmg_shell_area = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_shell_area", "cdecl")
    nmg_shell_area.argtypes = [POINTER(struct_shell)]
    nmg_shell_area.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1695
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_region_area", "cdecl"):
    nmg_region_area = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_region_area", "cdecl")
    nmg_region_area.argtypes = [POINTER(struct_nmgregion)]
    nmg_region_area.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1696
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_model_area", "cdecl"):
    nmg_model_area = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_model_area", "cdecl")
    nmg_model_area.argtypes = [POINTER(struct_model)]
    nmg_model_area.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1698
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_purge_unwanted_intersection_points", "cdecl"):
    nmg_purge_unwanted_intersection_points = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_purge_unwanted_intersection_points", "cdecl")
    nmg_purge_unwanted_intersection_points.argtypes = [POINTER(struct_bu_ptbl), POINTER(fastf_t), POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_purge_unwanted_intersection_points.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1702
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_in_or_ref", "cdecl"):
    nmg_in_or_ref = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_in_or_ref", "cdecl")
    nmg_in_or_ref.argtypes = [POINTER(struct_vertexuse), POINTER(struct_bu_ptbl)]
    nmg_in_or_ref.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1704
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_rebound", "cdecl"):
    nmg_rebound = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_rebound", "cdecl")
    nmg_rebound.argtypes = [POINTER(struct_model), POINTER(struct_bn_tol)]
    nmg_rebound.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1706
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_count_shell_kids", "cdecl"):
    nmg_count_shell_kids = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_count_shell_kids", "cdecl")
    nmg_count_shell_kids.argtypes = [POINTER(struct_model), POINTER(c_size_t), POINTER(c_size_t), POINTER(c_size_t)]
    nmg_count_shell_kids.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1710
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_close_shell", "cdecl"):
    nmg_close_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_close_shell", "cdecl")
    nmg_close_shell.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_close_shell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1712
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_dup_shell", "cdecl"):
    nmg_dup_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_dup_shell", "cdecl")
    nmg_dup_shell.argtypes = [POINTER(struct_shell), POINTER(POINTER(POINTER(c_long))), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_dup_shell.restype = POINTER(struct_shell)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1716
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pop_eu", "cdecl"):
    nmg_pop_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pop_eu", "cdecl")
    nmg_pop_eu.argtypes = [POINTER(struct_bu_ptbl)]
    nmg_pop_eu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1717
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_reverse_radials", "cdecl"):
    nmg_reverse_radials = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_reverse_radials", "cdecl")
    nmg_reverse_radials.argtypes = [POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_reverse_radials.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1719
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_reverse_face_and_radials", "cdecl"):
    nmg_reverse_face_and_radials = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_reverse_face_and_radials", "cdecl")
    nmg_reverse_face_and_radials.argtypes = [POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_reverse_face_and_radials.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1721
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_shell_is_void", "cdecl"):
    nmg_shell_is_void = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_shell_is_void", "cdecl")
    nmg_shell_is_void.argtypes = [POINTER(struct_shell)]
    nmg_shell_is_void.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1722
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_propagate_normals", "cdecl"):
    nmg_propagate_normals = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_propagate_normals", "cdecl")
    nmg_propagate_normals.argtypes = [POINTER(struct_faceuse), POINTER(c_long), POINTER(struct_bn_tol)]
    nmg_propagate_normals.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1725
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_connect_same_fu_orients", "cdecl"):
    nmg_connect_same_fu_orients = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_connect_same_fu_orients", "cdecl")
    nmg_connect_same_fu_orients.argtypes = [POINTER(struct_shell)]
    nmg_connect_same_fu_orients.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1726
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_fix_decomposed_shell_normals", "cdecl"):
    nmg_fix_decomposed_shell_normals = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_fix_decomposed_shell_normals", "cdecl")
    nmg_fix_decomposed_shell_normals.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_fix_decomposed_shell_normals.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1728
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mk_model_from_region", "cdecl"):
    nmg_mk_model_from_region = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mk_model_from_region", "cdecl")
    nmg_mk_model_from_region.argtypes = [POINTER(struct_nmgregion), c_int, POINTER(struct_bu_list)]
    nmg_mk_model_from_region.restype = POINTER(struct_model)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1730
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_fix_normals", "cdecl"):
    nmg_fix_normals = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_fix_normals", "cdecl")
    nmg_fix_normals.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_fix_normals.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1733
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_long_edges", "cdecl"):
    nmg_break_long_edges = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_long_edges", "cdecl")
    nmg_break_long_edges.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_break_long_edges.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1735
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mk_new_face_from_loop", "cdecl"):
    nmg_mk_new_face_from_loop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mk_new_face_from_loop", "cdecl")
    nmg_mk_new_face_from_loop.argtypes = [POINTER(struct_loopuse)]
    nmg_mk_new_face_from_loop.restype = POINTER(struct_faceuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1736
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_split_loops_into_faces", "cdecl"):
    nmg_split_loops_into_faces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_split_loops_into_faces", "cdecl")
    nmg_split_loops_into_faces.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_split_loops_into_faces.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1738
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_decompose_shell", "cdecl"):
    nmg_decompose_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_decompose_shell", "cdecl")
    nmg_decompose_shell.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_decompose_shell.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1740
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_unbreak_region_edges", "cdecl"):
    nmg_unbreak_region_edges = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_unbreak_region_edges", "cdecl")
    nmg_unbreak_region_edges.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list)]
    nmg_unbreak_region_edges.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1741
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlist_to_eu", "cdecl"):
    nmg_vlist_to_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlist_to_eu", "cdecl")
    nmg_vlist_to_eu.argtypes = [POINTER(struct_bu_list), POINTER(struct_shell)]
    nmg_vlist_to_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1743
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mv_shell_to_region", "cdecl"):
    nmg_mv_shell_to_region = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mv_shell_to_region", "cdecl")
    nmg_mv_shell_to_region.argtypes = [POINTER(struct_shell), POINTER(struct_nmgregion)]
    nmg_mv_shell_to_region.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1745
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_isect_faces", "cdecl"):
    nmg_find_isect_faces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_isect_faces", "cdecl")
    nmg_find_isect_faces.argtypes = [POINTER(struct_vertex), POINTER(struct_bu_ptbl), POINTER(c_int), POINTER(struct_bn_tol)]
    nmg_find_isect_faces.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1749
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_simple_vertex_solve", "cdecl"):
    nmg_simple_vertex_solve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_simple_vertex_solve", "cdecl")
    nmg_simple_vertex_solve.argtypes = [POINTER(struct_vertex), POINTER(struct_bu_ptbl), POINTER(struct_bn_tol)]
    nmg_simple_vertex_solve.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1752
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_vert_on_fus", "cdecl"):
    nmg_ck_vert_on_fus = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_vert_on_fus", "cdecl")
    nmg_ck_vert_on_fus.argtypes = [POINTER(struct_vertex), POINTER(struct_bn_tol)]
    nmg_ck_vert_on_fus.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1754
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_make_faces_at_vert", "cdecl"):
    nmg_make_faces_at_vert = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_make_faces_at_vert", "cdecl")
    nmg_make_faces_at_vert.argtypes = [POINTER(struct_vertex), POINTER(struct_bu_ptbl), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_make_faces_at_vert.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1758
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kill_cracks_at_vertex", "cdecl"):
    nmg_kill_cracks_at_vertex = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kill_cracks_at_vertex", "cdecl")
    nmg_kill_cracks_at_vertex.argtypes = [POINTER(struct_vertex)]
    nmg_kill_cracks_at_vertex.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1759
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_complex_vertex_solve", "cdecl"):
    nmg_complex_vertex_solve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_complex_vertex_solve", "cdecl")
    nmg_complex_vertex_solve.argtypes = [POINTER(struct_vertex), POINTER(struct_bu_ptbl), c_int, c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_complex_vertex_solve.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1765
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_bad_face_normals", "cdecl"):
    nmg_bad_face_normals = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_bad_face_normals", "cdecl")
    nmg_bad_face_normals.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_bad_face_normals.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1767
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_faces_are_radial", "cdecl"):
    nmg_faces_are_radial = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_faces_are_radial", "cdecl")
    nmg_faces_are_radial.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse)]
    nmg_faces_are_radial.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1769
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_move_edge_thru_pnt", "cdecl"):
    nmg_move_edge_thru_pnt = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_move_edge_thru_pnt", "cdecl")
    nmg_move_edge_thru_pnt.argtypes = [POINTER(struct_edgeuse), point_t, POINTER(struct_bn_tol)]
    nmg_move_edge_thru_pnt.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1772
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlist_to_wire_edges", "cdecl"):
    nmg_vlist_to_wire_edges = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlist_to_wire_edges", "cdecl")
    nmg_vlist_to_wire_edges.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list)]
    nmg_vlist_to_wire_edges.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1774
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_follow_free_edges_to_vertex", "cdecl"):
    nmg_follow_free_edges_to_vertex = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_follow_free_edges_to_vertex", "cdecl")
    nmg_follow_free_edges_to_vertex.argtypes = [POINTER(struct_vertex), POINTER(struct_vertex), POINTER(struct_bu_ptbl), POINTER(struct_shell), POINTER(struct_edgeuse), POINTER(struct_bu_ptbl), POINTER(c_int)]
    nmg_follow_free_edges_to_vertex.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1781
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_glue_face_in_shell", "cdecl"):
    nmg_glue_face_in_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_glue_face_in_shell", "cdecl")
    nmg_glue_face_in_shell.argtypes = [POINTER(struct_faceuse), POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_glue_face_in_shell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1784
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_open_shells_connect", "cdecl"):
    nmg_open_shells_connect = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_open_shells_connect", "cdecl")
    nmg_open_shells_connect.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(POINTER(c_long)), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_open_shells_connect.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1789
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_in_vert", "cdecl"):
    nmg_in_vert = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_in_vert", "cdecl")
    nmg_in_vert.argtypes = [POINTER(struct_vertex), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_in_vert.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1793
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mirror_model", "cdecl"):
    nmg_mirror_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mirror_model", "cdecl")
    nmg_mirror_model.argtypes = [POINTER(struct_model), POINTER(struct_bu_list)]
    nmg_mirror_model.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1794
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kill_cracks", "cdecl"):
    nmg_kill_cracks = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kill_cracks", "cdecl")
    nmg_kill_cracks.argtypes = [POINTER(struct_shell)]
    nmg_kill_cracks.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1795
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_kill_zero_length_edgeuses", "cdecl"):
    nmg_kill_zero_length_edgeuses = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_kill_zero_length_edgeuses", "cdecl")
    nmg_kill_zero_length_edgeuses.argtypes = [POINTER(struct_model)]
    nmg_kill_zero_length_edgeuses.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1796
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_make_faces_within_tol", "cdecl"):
    nmg_make_faces_within_tol = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_make_faces_within_tol", "cdecl")
    nmg_make_faces_within_tol.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_make_faces_within_tol.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1799
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_intersect_loops_self", "cdecl"):
    nmg_intersect_loops_self = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_intersect_loops_self", "cdecl")
    nmg_intersect_loops_self.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_intersect_loops_self.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1801
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_join_cnurbs", "cdecl"):
    nmg_join_cnurbs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_join_cnurbs", "cdecl")
    nmg_join_cnurbs.argtypes = [POINTER(struct_bu_list)]
    nmg_join_cnurbs.restype = POINTER(struct_edge_g_cnurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1802
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_arc2d_to_cnurb", "cdecl"):
    nmg_arc2d_to_cnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_arc2d_to_cnurb", "cdecl")
    nmg_arc2d_to_cnurb.argtypes = [point_t, point_t, point_t, c_int, POINTER(struct_bn_tol)]
    nmg_arc2d_to_cnurb.restype = POINTER(struct_edge_g_cnurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1807
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_edge_at_verts", "cdecl"):
    nmg_break_edge_at_verts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_edge_at_verts", "cdecl")
    nmg_break_edge_at_verts.argtypes = [POINTER(struct_edge), POINTER(struct_bu_ptbl), POINTER(struct_bn_tol)]
    nmg_break_edge_at_verts.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1810
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_loop_plane_area", "cdecl"):
    nmg_loop_plane_area = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_loop_plane_area", "cdecl")
    nmg_loop_plane_area.argtypes = [POINTER(struct_loopuse), plane_t]
    nmg_loop_plane_area.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1812
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_edges", "cdecl"):
    nmg_break_edges = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_edges", "cdecl")
    nmg_break_edges.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_break_edges.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1814
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_lu_is_convex", "cdecl"):
    nmg_lu_is_convex = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_lu_is_convex", "cdecl")
    nmg_lu_is_convex.argtypes = [POINTER(struct_loopuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_lu_is_convex.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1817
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_simplify_shell_edges", "cdecl"):
    nmg_simplify_shell_edges = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_simplify_shell_edges", "cdecl")
    nmg_simplify_shell_edges.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_simplify_shell_edges.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1819
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_collapse", "cdecl"):
    nmg_edge_collapse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_collapse", "cdecl")
    nmg_edge_collapse.argtypes = [POINTER(struct_model), POINTER(struct_bn_tol), fastf_t, fastf_t, POINTER(struct_bu_list)]
    nmg_edge_collapse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1826
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_clone_model", "cdecl"):
    nmg_clone_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_clone_model", "cdecl")
    nmg_clone_model.argtypes = [POINTER(struct_model)]
    nmg_clone_model.restype = POINTER(struct_model)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1829
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_triangulate_shell", "cdecl"):
    nmg_triangulate_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_triangulate_shell", "cdecl")
    nmg_triangulate_shell.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_triangulate_shell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1834
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_triangulate_model", "cdecl"):
    nmg_triangulate_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_triangulate_model", "cdecl")
    nmg_triangulate_model.argtypes = [POINTER(struct_model), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_triangulate_model.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1837
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_triangulate_fu", "cdecl"):
    nmg_triangulate_fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_triangulate_fu", "cdecl")
    nmg_triangulate_fu.argtypes = [POINTER(struct_faceuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_triangulate_fu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1840
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_dump_model", "cdecl"):
    nmg_dump_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_dump_model", "cdecl")
    nmg_dump_model.argtypes = [POINTER(struct_model)]
    nmg_dump_model.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1843
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_dangling_face", "cdecl"):
    nmg_dangling_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_dangling_face", "cdecl")
    nmg_dangling_face.argtypes = [POINTER(struct_faceuse), String]
    nmg_dangling_face.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1849
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_shell_manifolds", "cdecl"):
    nmg_shell_manifolds = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_shell_manifolds", "cdecl")
    nmg_shell_manifolds.argtypes = [POINTER(struct_shell), String]
    if sizeof(c_int) == sizeof(c_void_p):
        nmg_shell_manifolds.restype = ReturnString
    else:
        nmg_shell_manifolds.restype = String
        nmg_shell_manifolds.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1851
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_manifolds", "cdecl"):
    nmg_manifolds = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_manifolds", "cdecl")
    nmg_manifolds.argtypes = [POINTER(struct_model)]
    if sizeof(c_int) == sizeof(c_void_p):
        nmg_manifolds.restype = ReturnString
    else:
        nmg_manifolds.restype = String
        nmg_manifolds.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1854
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_common_bigloop", "cdecl"):
    nmg_is_common_bigloop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_common_bigloop", "cdecl")
    nmg_is_common_bigloop.argtypes = [POINTER(struct_face), POINTER(struct_face)]
    nmg_is_common_bigloop.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1856
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_region_v_unique", "cdecl"):
    nmg_region_v_unique = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_region_v_unique", "cdecl")
    nmg_region_v_unique.argtypes = [POINTER(struct_nmgregion), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_region_v_unique.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1858
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ptbl_vfuse", "cdecl"):
    nmg_ptbl_vfuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ptbl_vfuse", "cdecl")
    nmg_ptbl_vfuse.argtypes = [POINTER(struct_bu_ptbl), POINTER(struct_bn_tol)]
    nmg_ptbl_vfuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1860
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_region_both_vfuse", "cdecl"):
    nmg_region_both_vfuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_region_both_vfuse", "cdecl")
    nmg_region_both_vfuse.argtypes = [POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl), POINTER(struct_bn_tol)]
    nmg_region_both_vfuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1864
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vertex_fuse", "cdecl"):
    nmg_vertex_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vertex_fuse", "cdecl")
    nmg_vertex_fuse.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_vertex_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1866
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cnurb_is_linear", "cdecl"):
    nmg_cnurb_is_linear = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cnurb_is_linear", "cdecl")
    nmg_cnurb_is_linear.argtypes = [POINTER(struct_edge_g_cnurb)]
    nmg_cnurb_is_linear.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1867
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_snurb_is_planar", "cdecl"):
    nmg_snurb_is_planar = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_snurb_is_planar", "cdecl")
    nmg_snurb_is_planar.argtypes = [POINTER(struct_face_g_snurb), POINTER(struct_bn_tol)]
    nmg_snurb_is_planar.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1869
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eval_linear_trim_curve", "cdecl"):
    nmg_eval_linear_trim_curve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eval_linear_trim_curve", "cdecl")
    nmg_eval_linear_trim_curve.argtypes = [POINTER(struct_face_g_snurb), fastf_t * int(3), point_t]
    nmg_eval_linear_trim_curve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1872
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eval_trim_curve", "cdecl"):
    nmg_eval_trim_curve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eval_trim_curve", "cdecl")
    nmg_eval_trim_curve.argtypes = [POINTER(struct_edge_g_cnurb), POINTER(struct_face_g_snurb), fastf_t, point_t]
    nmg_eval_trim_curve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1876
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eval_trim_to_tol", "cdecl"):
    nmg_eval_trim_to_tol = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eval_trim_to_tol", "cdecl")
    nmg_eval_trim_to_tol.argtypes = [POINTER(struct_edge_g_cnurb), POINTER(struct_face_g_snurb), fastf_t, fastf_t, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_eval_trim_to_tol.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1883
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eval_linear_trim_to_tol", "cdecl"):
    nmg_eval_linear_trim_to_tol = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eval_linear_trim_to_tol", "cdecl")
    nmg_eval_linear_trim_to_tol.argtypes = [POINTER(struct_edge_g_cnurb), POINTER(struct_face_g_snurb), fastf_t * int(3), fastf_t * int(3), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_eval_linear_trim_to_tol.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1889
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cnurb_lseg_coincident", "cdecl"):
    nmg_cnurb_lseg_coincident = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cnurb_lseg_coincident", "cdecl")
    nmg_cnurb_lseg_coincident.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edge_g_cnurb), POINTER(struct_face_g_snurb), point_t, point_t, POINTER(struct_bn_tol)]
    nmg_cnurb_lseg_coincident.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1895
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cnurb_is_on_crv", "cdecl"):
    nmg_cnurb_is_on_crv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cnurb_is_on_crv", "cdecl")
    nmg_cnurb_is_on_crv.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edge_g_cnurb), POINTER(struct_face_g_snurb), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_cnurb_is_on_crv.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1900
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_fuse", "cdecl"):
    nmg_edge_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_fuse", "cdecl")
    nmg_edge_fuse.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_edge_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1902
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_edge_g_fuse", "cdecl"):
    nmg_edge_g_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_edge_g_fuse", "cdecl")
    nmg_edge_g_fuse.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_edge_g_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1904
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_fu_verts", "cdecl"):
    nmg_ck_fu_verts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_fu_verts", "cdecl")
    nmg_ck_fu_verts.argtypes = [POINTER(struct_faceuse), POINTER(struct_face), POINTER(struct_bn_tol)]
    nmg_ck_fu_verts.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1907
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_fg_verts", "cdecl"):
    nmg_ck_fg_verts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_fg_verts", "cdecl")
    nmg_ck_fg_verts.argtypes = [POINTER(struct_faceuse), POINTER(struct_face), POINTER(struct_bn_tol)]
    nmg_ck_fg_verts.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1910
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_two_face_fuse", "cdecl"):
    nmg_two_face_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_two_face_fuse", "cdecl")
    nmg_two_face_fuse.argtypes = [POINTER(struct_face), POINTER(struct_face), POINTER(struct_bn_tol)]
    nmg_two_face_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1913
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_model_face_fuse", "cdecl"):
    nmg_model_face_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_model_face_fuse", "cdecl")
    nmg_model_face_fuse.argtypes = [POINTER(struct_model), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_model_face_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1915
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_all_es_on_v", "cdecl"):
    nmg_break_all_es_on_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_all_es_on_v", "cdecl")
    nmg_break_all_es_on_v.argtypes = [POINTER(c_uint32), POINTER(struct_vertex), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_break_all_es_on_v.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1918
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_e_on_v", "cdecl"):
    nmg_break_e_on_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_e_on_v", "cdecl")
    nmg_break_e_on_v.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_break_e_on_v.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1921
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_model_break_e_on_v", "cdecl"):
    nmg_model_break_e_on_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_model_break_e_on_v", "cdecl")
    nmg_model_break_e_on_v.argtypes = [POINTER(c_uint32), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_model_break_e_on_v.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1924
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_model_fuse", "cdecl"):
    nmg_model_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_model_fuse", "cdecl")
    nmg_model_fuse.argtypes = [POINTER(struct_model), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_model_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1929
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_sorted_list_insert", "cdecl"):
    nmg_radial_sorted_list_insert = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_sorted_list_insert", "cdecl")
    nmg_radial_sorted_list_insert.argtypes = [POINTER(struct_bu_list), POINTER(struct_nmg_radial)]
    nmg_radial_sorted_list_insert.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1931
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_verify_pointers", "cdecl"):
    nmg_radial_verify_pointers = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_verify_pointers", "cdecl")
    nmg_radial_verify_pointers.argtypes = [POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_radial_verify_pointers.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1933
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_verify_monotone", "cdecl"):
    nmg_radial_verify_monotone = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_verify_monotone", "cdecl")
    nmg_radial_verify_monotone.argtypes = [POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_radial_verify_monotone.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1935
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_insure_radial_list_is_increasing", "cdecl"):
    nmg_insure_radial_list_is_increasing = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_insure_radial_list_is_increasing", "cdecl")
    nmg_insure_radial_list_is_increasing.argtypes = [POINTER(struct_bu_list), fastf_t, fastf_t]
    nmg_insure_radial_list_is_increasing.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1937
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_build_list", "cdecl"):
    nmg_radial_build_list = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_build_list", "cdecl")
    nmg_radial_build_list.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_ptbl), c_int, POINTER(struct_edgeuse), vect_t, vect_t, vect_t, POINTER(struct_bn_tol)]
    nmg_radial_build_list.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1945
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_merge_lists", "cdecl"):
    nmg_radial_merge_lists = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_merge_lists", "cdecl")
    nmg_radial_merge_lists.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_radial_merge_lists.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1948
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_crack_outie", "cdecl"):
    nmg_is_crack_outie = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_crack_outie", "cdecl")
    nmg_is_crack_outie.argtypes = [POINTER(struct_edgeuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_is_crack_outie.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1951
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_radial_eu", "cdecl"):
    nmg_find_radial_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_radial_eu", "cdecl")
    nmg_find_radial_eu.argtypes = [POINTER(struct_bu_list), POINTER(struct_edgeuse)]
    nmg_find_radial_eu.restype = POINTER(struct_nmg_radial)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1953
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_next_use_of_2e_in_lu", "cdecl"):
    nmg_find_next_use_of_2e_in_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_next_use_of_2e_in_lu", "cdecl")
    nmg_find_next_use_of_2e_in_lu.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edge), POINTER(struct_edge)]
    nmg_find_next_use_of_2e_in_lu.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1956
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_mark_cracks", "cdecl"):
    nmg_radial_mark_cracks = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_mark_cracks", "cdecl")
    nmg_radial_mark_cracks.argtypes = [POINTER(struct_bu_list), POINTER(struct_edge), POINTER(struct_edge), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_radial_mark_cracks.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1961
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_find_an_original", "cdecl"):
    nmg_radial_find_an_original = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_find_an_original", "cdecl")
    nmg_radial_find_an_original.argtypes = [POINTER(struct_bu_list), POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_radial_find_an_original.restype = POINTER(struct_nmg_radial)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1964
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_mark_flips", "cdecl"):
    nmg_radial_mark_flips = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_mark_flips", "cdecl")
    nmg_radial_mark_flips.argtypes = [POINTER(struct_bu_list), POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_radial_mark_flips.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1967
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_check_parity", "cdecl"):
    nmg_radial_check_parity = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_check_parity", "cdecl")
    nmg_radial_check_parity.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_ptbl), POINTER(struct_bn_tol)]
    nmg_radial_check_parity.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1970
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_implement_decisions", "cdecl"):
    nmg_radial_implement_decisions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_implement_decisions", "cdecl")
    nmg_radial_implement_decisions.argtypes = [POINTER(struct_bu_list), POINTER(struct_bn_tol), POINTER(struct_edgeuse), vect_t, vect_t, vect_t]
    nmg_radial_implement_decisions.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1976
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_radial", "cdecl"):
    nmg_pr_radial = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_radial", "cdecl")
    nmg_pr_radial.argtypes = [String, POINTER(struct_nmg_radial)]
    nmg_pr_radial.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1978
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_radial_list", "cdecl"):
    nmg_pr_radial_list = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_radial_list", "cdecl")
    nmg_pr_radial_list.argtypes = [POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_pr_radial_list.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1980
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_do_radial_flips", "cdecl"):
    nmg_do_radial_flips = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_do_radial_flips", "cdecl")
    nmg_do_radial_flips.argtypes = [POINTER(struct_bu_list)]
    nmg_do_radial_flips.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1981
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_do_radial_join", "cdecl"):
    nmg_do_radial_join = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_do_radial_join", "cdecl")
    nmg_do_radial_join.argtypes = [POINTER(struct_bu_list), POINTER(struct_edgeuse), vect_t, vect_t, vect_t, POINTER(struct_bn_tol)]
    nmg_do_radial_join.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1985
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_join_eu_NEW", "cdecl"):
    nmg_radial_join_eu_NEW = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_join_eu_NEW", "cdecl")
    nmg_radial_join_eu_NEW.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_radial_join_eu_NEW.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1988
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_exchange_marked", "cdecl"):
    nmg_radial_exchange_marked = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_exchange_marked", "cdecl")
    nmg_radial_exchange_marked.argtypes = [POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_radial_exchange_marked.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1990
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_s_radial_harmonize", "cdecl"):
    nmg_s_radial_harmonize = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_s_radial_harmonize", "cdecl")
    nmg_s_radial_harmonize.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_s_radial_harmonize.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1993
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_s_radial_check", "cdecl"):
    nmg_s_radial_check = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_s_radial_check", "cdecl")
    nmg_s_radial_check.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_s_radial_check.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1996
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_r_radial_check", "cdecl"):
    nmg_r_radial_check = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_r_radial_check", "cdecl")
    nmg_r_radial_check.argtypes = [POINTER(struct_nmgregion), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_r_radial_check.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2001
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pick_best_edge_g", "cdecl"):
    nmg_pick_best_edge_g = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pick_best_edge_g", "cdecl")
    nmg_pick_best_edge_g.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_pick_best_edge_g.restype = POINTER(struct_edge_g_lseg)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2006
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_vertex", "cdecl"):
    nmg_visit_vertex = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_vertex", "cdecl")
    nmg_visit_vertex.argtypes = [POINTER(struct_vertex), POINTER(struct_nmg_visit_handlers), POINTER(None)]
    nmg_visit_vertex.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2009
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_vertexuse", "cdecl"):
    nmg_visit_vertexuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_vertexuse", "cdecl")
    nmg_visit_vertexuse.argtypes = [POINTER(struct_vertexuse), POINTER(struct_nmg_visit_handlers), POINTER(None)]
    nmg_visit_vertexuse.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2012
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_edge", "cdecl"):
    nmg_visit_edge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_edge", "cdecl")
    nmg_visit_edge.argtypes = [POINTER(struct_edge), POINTER(struct_nmg_visit_handlers), POINTER(None)]
    nmg_visit_edge.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2015
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_edgeuse", "cdecl"):
    nmg_visit_edgeuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_edgeuse", "cdecl")
    nmg_visit_edgeuse.argtypes = [POINTER(struct_edgeuse), POINTER(struct_nmg_visit_handlers), POINTER(None)]
    nmg_visit_edgeuse.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2018
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_loop", "cdecl"):
    nmg_visit_loop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_loop", "cdecl")
    nmg_visit_loop.argtypes = [POINTER(struct_loop), POINTER(struct_nmg_visit_handlers), POINTER(None)]
    nmg_visit_loop.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2021
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_loopuse", "cdecl"):
    nmg_visit_loopuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_loopuse", "cdecl")
    nmg_visit_loopuse.argtypes = [POINTER(struct_loopuse), POINTER(struct_nmg_visit_handlers), POINTER(None)]
    nmg_visit_loopuse.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2024
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_face", "cdecl"):
    nmg_visit_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_face", "cdecl")
    nmg_visit_face.argtypes = [POINTER(struct_face), POINTER(struct_nmg_visit_handlers), POINTER(None)]
    nmg_visit_face.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2027
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_faceuse", "cdecl"):
    nmg_visit_faceuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_faceuse", "cdecl")
    nmg_visit_faceuse.argtypes = [POINTER(struct_faceuse), POINTER(struct_nmg_visit_handlers), POINTER(None), POINTER(struct_bu_list)]
    nmg_visit_faceuse.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2031
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_shell", "cdecl"):
    nmg_visit_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_shell", "cdecl")
    nmg_visit_shell.argtypes = [POINTER(struct_shell), POINTER(struct_nmg_visit_handlers), POINTER(None), POINTER(struct_bu_list)]
    nmg_visit_shell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2035
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_region", "cdecl"):
    nmg_visit_region = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_region", "cdecl")
    nmg_visit_region.argtypes = [POINTER(struct_nmgregion), POINTER(struct_nmg_visit_handlers), POINTER(None), POINTER(struct_bu_list)]
    nmg_visit_region.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2039
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit_model", "cdecl"):
    nmg_visit_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit_model", "cdecl")
    nmg_visit_model.argtypes = [POINTER(struct_model), POINTER(struct_nmg_visit_handlers), POINTER(None), POINTER(struct_bu_list)]
    nmg_visit_model.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2043
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_visit", "cdecl"):
    nmg_visit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_visit", "cdecl")
    nmg_visit.argtypes = [POINTER(c_uint32), POINTER(struct_nmg_visit_handlers), POINTER(None), POINTER(struct_bu_list)]
    nmg_visit.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2050
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_classify_pnt_loop", "cdecl"):
    nmg_classify_pnt_loop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_classify_pnt_loop", "cdecl")
    nmg_classify_pnt_loop.argtypes = [point_t, POINTER(struct_loopuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_classify_pnt_loop.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2055
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_classify_s_vs_s", "cdecl"):
    nmg_classify_s_vs_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_classify_s_vs_s", "cdecl")
    nmg_classify_s_vs_s.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_classify_s_vs_s.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2060
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_classify_lu_lu", "cdecl"):
    nmg_classify_lu_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_classify_lu_lu", "cdecl")
    nmg_classify_lu_lu.argtypes = [POINTER(struct_loopuse), POINTER(struct_loopuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_classify_lu_lu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2065
for _lib in _libs.values():
    if not _lib.has("nmg_class_pnt_f", "cdecl"):
        continue
    nmg_class_pnt_f = _lib.get("nmg_class_pnt_f", "cdecl")
    nmg_class_pnt_f.argtypes = [point_t, POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_class_pnt_f.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2068
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_class_pnt_s", "cdecl"):
    nmg_class_pnt_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_class_pnt_s", "cdecl")
    nmg_class_pnt_s.argtypes = [point_t, POINTER(struct_shell), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_class_pnt_s.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2075
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eu_is_part_of_crack", "cdecl"):
    nmg_eu_is_part_of_crack = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eu_is_part_of_crack", "cdecl")
    nmg_eu_is_part_of_crack.argtypes = [POINTER(struct_edgeuse)]
    nmg_eu_is_part_of_crack.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2077
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_class_pnt_lu_except", "cdecl"):
    nmg_class_pnt_lu_except = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_class_pnt_lu_except", "cdecl")
    nmg_class_pnt_lu_except.argtypes = [point_t, POINTER(struct_loopuse), POINTER(struct_edge), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_class_pnt_lu_except.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2083
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_class_pnt_fu_except", "cdecl"):
    nmg_class_pnt_fu_except = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_class_pnt_fu_except", "cdecl")
    nmg_class_pnt_fu_except.argtypes = [point_t, POINTER(struct_faceuse), POINTER(struct_loopuse), CFUNCTYPE(UNCHECKED(None), POINTER(struct_edgeuse), point_t, String, POINTER(struct_bu_list)), CFUNCTYPE(UNCHECKED(None), POINTER(struct_vertexuse), point_t, String), String, c_int, c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_class_pnt_fu_except.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2095
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_shell", "cdecl"):
    nmg_pl_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_shell", "cdecl")
    nmg_pl_shell.argtypes = [POINTER(FILE), POINTER(struct_shell), c_int, POINTER(struct_bu_list)]
    nmg_pl_shell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2100
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vu_to_vlist", "cdecl"):
    nmg_vu_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vu_to_vlist", "cdecl")
    nmg_vu_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_vertexuse), POINTER(struct_bu_list)]
    nmg_vu_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2103
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eu_to_vlist", "cdecl"):
    nmg_eu_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eu_to_vlist", "cdecl")
    nmg_eu_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list), POINTER(struct_bu_list)]
    nmg_eu_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2106
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_lu_to_vlist", "cdecl"):
    nmg_lu_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_lu_to_vlist", "cdecl")
    nmg_lu_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_loopuse), c_int, vectp_t, POINTER(struct_bu_list)]
    nmg_lu_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2111
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_snurb_fu_to_vlist", "cdecl"):
    nmg_snurb_fu_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_snurb_fu_to_vlist", "cdecl")
    nmg_snurb_fu_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_faceuse), c_int, POINTER(struct_bu_list)]
    nmg_snurb_fu_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2115
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_s_to_vlist", "cdecl"):
    nmg_s_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_s_to_vlist", "cdecl")
    nmg_s_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_shell), c_int, POINTER(struct_bu_list)]
    nmg_s_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2119
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_r_to_vlist", "cdecl"):
    nmg_r_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_r_to_vlist", "cdecl")
    nmg_r_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_nmgregion), c_int, POINTER(struct_bu_list)]
    nmg_r_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2123
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_m_to_vlist", "cdecl"):
    nmg_m_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_m_to_vlist", "cdecl")
    nmg_m_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_model), c_int, POINTER(struct_bu_list)]
    nmg_m_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2127
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_offset_eu_vert", "cdecl"):
    nmg_offset_eu_vert = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_offset_eu_vert", "cdecl")
    nmg_offset_eu_vert.argtypes = [point_t, POINTER(struct_edgeuse), vect_t, c_int]
    nmg_offset_eu_vert.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2132
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_v", "cdecl"):
    nmg_pl_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_v", "cdecl")
    nmg_pl_v.argtypes = [POINTER(FILE), POINTER(struct_vertex), POINTER(c_long)]
    nmg_pl_v.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2135
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_e", "cdecl"):
    nmg_pl_e = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_e", "cdecl")
    nmg_pl_e.argtypes = [POINTER(FILE), POINTER(struct_edge), POINTER(c_long), c_int, c_int, c_int]
    nmg_pl_e.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2141
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_eu", "cdecl"):
    nmg_pl_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_eu", "cdecl")
    nmg_pl_eu.argtypes = [POINTER(FILE), POINTER(struct_edgeuse), POINTER(c_long), c_int, c_int, c_int]
    nmg_pl_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2147
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_lu", "cdecl"):
    nmg_pl_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_lu", "cdecl")
    nmg_pl_lu.argtypes = [POINTER(FILE), POINTER(struct_loopuse), POINTER(c_long), c_int, c_int, c_int, POINTER(struct_bu_list)]
    nmg_pl_lu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2154
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_fu", "cdecl"):
    nmg_pl_fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_fu", "cdecl")
    nmg_pl_fu.argtypes = [POINTER(FILE), POINTER(struct_faceuse), POINTER(c_long), c_int, c_int, c_int, POINTER(struct_bu_list)]
    nmg_pl_fu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2161
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_s", "cdecl"):
    nmg_pl_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_s", "cdecl")
    nmg_pl_s.argtypes = [POINTER(FILE), POINTER(struct_shell), POINTER(struct_bu_list)]
    nmg_pl_s.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2164
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_r", "cdecl"):
    nmg_pl_r = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_r", "cdecl")
    nmg_pl_r.argtypes = [POINTER(FILE), POINTER(struct_nmgregion), POINTER(struct_bu_list)]
    nmg_pl_r.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2167
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_m", "cdecl"):
    nmg_pl_m = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_m", "cdecl")
    nmg_pl_m.argtypes = [POINTER(FILE), POINTER(struct_model), POINTER(struct_bu_list)]
    nmg_pl_m.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2170
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_v", "cdecl"):
    nmg_vlblock_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_v", "cdecl")
    nmg_vlblock_v.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_vertex), POINTER(c_long), POINTER(struct_bu_list)]
    nmg_vlblock_v.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2174
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_e", "cdecl"):
    nmg_vlblock_e = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_e", "cdecl")
    nmg_vlblock_e.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_edge), POINTER(c_long), c_int, c_int, c_int, POINTER(struct_bu_list)]
    nmg_vlblock_e.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2181
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_eu", "cdecl"):
    nmg_vlblock_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_eu", "cdecl")
    nmg_vlblock_eu.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_edgeuse), POINTER(c_long), c_int, c_int, c_int, c_int, POINTER(struct_bu_list)]
    nmg_vlblock_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2189
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_euleft", "cdecl"):
    nmg_vlblock_euleft = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_euleft", "cdecl")
    nmg_vlblock_euleft.argtypes = [POINTER(struct_bu_list), POINTER(struct_edgeuse), point_t, mat_t, vect_t, vect_t, c_double, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_vlblock_euleft.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2198
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_around_eu", "cdecl"):
    nmg_vlblock_around_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_around_eu", "cdecl")
    nmg_vlblock_around_eu.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_edgeuse), POINTER(c_long), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_vlblock_around_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2204
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_lu", "cdecl"):
    nmg_vlblock_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_lu", "cdecl")
    nmg_vlblock_lu.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_loopuse), POINTER(c_long), c_int, c_int, c_int, c_int, POINTER(struct_bu_list)]
    nmg_vlblock_lu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2212
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_fu", "cdecl"):
    nmg_vlblock_fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_fu", "cdecl")
    nmg_vlblock_fu.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_faceuse), POINTER(c_long), c_int, POINTER(struct_bu_list)]
    nmg_vlblock_fu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2215
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_s", "cdecl"):
    nmg_vlblock_s = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_s", "cdecl")
    nmg_vlblock_s.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_shell), c_int, POINTER(struct_bu_list)]
    nmg_vlblock_s.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2219
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_r", "cdecl"):
    nmg_vlblock_r = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_r", "cdecl")
    nmg_vlblock_r.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_nmgregion), c_int, POINTER(struct_bu_list)]
    nmg_vlblock_r.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2223
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlblock_m", "cdecl"):
    nmg_vlblock_m = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlblock_m", "cdecl")
    nmg_vlblock_m.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_model), c_int, POINTER(struct_bu_list)]
    nmg_vlblock_m.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2229
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_edges_in_2_shells", "cdecl"):
    nmg_pl_edges_in_2_shells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_edges_in_2_shells", "cdecl")
    nmg_pl_edges_in_2_shells.argtypes = [POINTER(struct_bn_vlblock), POINTER(c_long), POINTER(struct_edgeuse), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_pl_edges_in_2_shells.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2235
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_isect", "cdecl"):
    nmg_pl_isect = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_isect", "cdecl")
    nmg_pl_isect.argtypes = [String, POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_pl_isect.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2239
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_comb_fu", "cdecl"):
    nmg_pl_comb_fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_comb_fu", "cdecl")
    nmg_pl_comb_fu.argtypes = [c_int, c_int, POINTER(struct_faceuse), POINTER(struct_bu_list)]
    nmg_pl_comb_fu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2243
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pl_2fu", "cdecl"):
    nmg_pl_2fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pl_2fu", "cdecl")
    nmg_pl_2fu.argtypes = [String, POINTER(struct_faceuse), POINTER(struct_faceuse), c_int, POINTER(struct_bu_list)]
    nmg_pl_2fu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2249
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_show_broken_classifier_stuff", "cdecl"):
    nmg_show_broken_classifier_stuff = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_show_broken_classifier_stuff", "cdecl")
    nmg_show_broken_classifier_stuff.argtypes = [POINTER(c_uint32), POINTER(POINTER(c_char)), c_int, c_int, String, POINTER(struct_bu_list)]
    nmg_show_broken_classifier_stuff.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2255
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_plot", "cdecl"):
    nmg_face_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_plot", "cdecl")
    nmg_face_plot.argtypes = [POINTER(struct_faceuse), POINTER(struct_bu_list)]
    nmg_face_plot.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2256
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_2face_plot", "cdecl"):
    nmg_2face_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_2face_plot", "cdecl")
    nmg_2face_plot.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_list)]
    nmg_2face_plot.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2259
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_lu_plot", "cdecl"):
    nmg_face_lu_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_lu_plot", "cdecl")
    nmg_face_lu_plot.argtypes = [POINTER(struct_loopuse), POINTER(struct_vertexuse), POINTER(struct_vertexuse), POINTER(struct_bu_list)]
    nmg_face_lu_plot.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2263
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_plot_lu_ray", "cdecl"):
    nmg_plot_lu_ray = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_plot_lu_ray", "cdecl")
    nmg_plot_lu_ray.argtypes = [POINTER(struct_loopuse), POINTER(struct_vertexuse), POINTER(struct_vertexuse), vect_t, POINTER(struct_bu_list)]
    nmg_plot_lu_ray.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2268
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_plot_ray_face", "cdecl"):
    nmg_plot_ray_face = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_plot_ray_face", "cdecl")
    nmg_plot_ray_face.argtypes = [String, point_t, vect_t, POINTER(struct_faceuse), POINTER(struct_bu_list)]
    nmg_plot_ray_face.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2273
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_plot_lu_around_eu", "cdecl"):
    nmg_plot_lu_around_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_plot_lu_around_eu", "cdecl")
    nmg_plot_lu_around_eu.argtypes = [String, POINTER(struct_edgeuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_plot_lu_around_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2277
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_snurb_to_vlist", "cdecl"):
    nmg_snurb_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_snurb_to_vlist", "cdecl")
    nmg_snurb_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_face_g_snurb), c_int, POINTER(struct_bu_list)]
    nmg_snurb_to_vlist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2281
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cnurb_to_vlist", "cdecl"):
    nmg_cnurb_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cnurb_to_vlist", "cdecl")
    nmg_cnurb_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_edgeuse), c_int, c_int, POINTER(struct_bu_list)]
    nmg_cnurb_to_vlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2290
try:
    nmg_eue_dist = (c_double).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "nmg_eue_dist")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2294
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mesh_two_faces", "cdecl"):
    nmg_mesh_two_faces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mesh_two_faces", "cdecl")
    nmg_mesh_two_faces.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_mesh_two_faces.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2297
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_radial_join_eu", "cdecl"):
    nmg_radial_join_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_radial_join_eu", "cdecl")
    nmg_radial_join_eu.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_radial_join_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2300
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mesh_faces", "cdecl"):
    nmg_mesh_faces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mesh_faces", "cdecl")
    nmg_mesh_faces.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_mesh_faces.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2304
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mesh_face_shell", "cdecl"):
    nmg_mesh_face_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mesh_face_shell", "cdecl")
    nmg_mesh_face_shell.argtypes = [POINTER(struct_faceuse), POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_mesh_face_shell.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2307
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mesh_shell_shell", "cdecl"):
    nmg_mesh_shell_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mesh_shell_shell", "cdecl")
    nmg_mesh_shell_shell.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_mesh_shell_shell.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2311
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_measure_fu_angle", "cdecl"):
    nmg_measure_fu_angle = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_measure_fu_angle", "cdecl")
    nmg_measure_fu_angle.argtypes = [POINTER(struct_edgeuse), vect_t, vect_t, vect_t]
    nmg_measure_fu_angle.restype = c_double

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2317
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_do_bool", "cdecl"):
    nmg_do_bool = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_do_bool", "cdecl")
    nmg_do_bool.argtypes = [POINTER(struct_nmgregion), POINTER(struct_nmgregion), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_do_bool.restype = POINTER(struct_nmgregion)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2320
for _lib in _libs.values():
    if not _lib.has("nmg_two_region_vertex_fuse", "cdecl"):
        continue
    nmg_two_region_vertex_fuse = _lib.get("nmg_two_region_vertex_fuse", "cdecl")
    nmg_two_region_vertex_fuse.argtypes = [POINTER(struct_nmgregion), POINTER(struct_nmgregion), POINTER(struct_bn_tol)]
    nmg_two_region_vertex_fuse.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2326
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_class_shells", "cdecl"):
    nmg_class_shells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_class_shells", "cdecl")
    nmg_class_shells.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(POINTER(c_char)), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_class_shells.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2334
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_vu_ptbl", "cdecl"):
    nmg_ck_vu_ptbl = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_vu_ptbl", "cdecl")
    nmg_ck_vu_ptbl.argtypes = [POINTER(struct_bu_ptbl), POINTER(struct_faceuse)]
    nmg_ck_vu_ptbl.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2336
for _lib in _libs.values():
    if not _lib.has("nmg_vu_angle_measure", "cdecl"):
        continue
    nmg_vu_angle_measure = _lib.get("nmg_vu_angle_measure", "cdecl")
    nmg_vu_angle_measure.argtypes = [POINTER(struct_vertexuse), vect_t, vect_t, c_int, c_int]
    nmg_vu_angle_measure.restype = c_double
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2341
for _lib in _libs.values():
    if not _lib.has("nmg_wedge_class", "cdecl"):
        continue
    nmg_wedge_class = _lib.get("nmg_wedge_class", "cdecl")
    nmg_wedge_class.argtypes = [c_int, c_double, c_double]
    nmg_wedge_class.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2344
for _lib in _libs.values():
    if not _lib.has("nmg_sanitize_fu", "cdecl"):
        continue
    nmg_sanitize_fu = _lib.get("nmg_sanitize_fu", "cdecl")
    nmg_sanitize_fu.argtypes = [POINTER(struct_faceuse)]
    nmg_sanitize_fu.restype = None
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2345
for _lib in _libs.values():
    if not _lib.has("nmg_unlist_v", "cdecl"):
        continue
    nmg_unlist_v = _lib.get("nmg_unlist_v", "cdecl")
    nmg_unlist_v.argtypes = [POINTER(struct_bu_ptbl), POINTER(fastf_t), POINTER(struct_vertex)]
    nmg_unlist_v.restype = None
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2348
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_face_cutjoin", "cdecl"):
    nmg_face_cutjoin = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_face_cutjoin", "cdecl")
    nmg_face_cutjoin.argtypes = [POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl), POINTER(fastf_t), POINTER(fastf_t), POINTER(struct_faceuse), POINTER(struct_faceuse), point_t, vect_t, POINTER(struct_edge_g_lseg), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_face_cutjoin.restype = POINTER(struct_edge_g_lseg)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2359
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_fcut_face_2d", "cdecl"):
    nmg_fcut_face_2d = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_fcut_face_2d", "cdecl")
    nmg_fcut_face_2d.argtypes = [POINTER(struct_bu_ptbl), POINTER(fastf_t), POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_fcut_face_2d.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2365
for _lib in _libs.values():
    if not _lib.has("nmg_insert_vu_if_on_edge", "cdecl"):
        continue
    nmg_insert_vu_if_on_edge = _lib.get("nmg_insert_vu_if_on_edge", "cdecl")
    nmg_insert_vu_if_on_edge.argtypes = [POINTER(struct_vertexuse), POINTER(struct_vertexuse), POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_insert_vu_if_on_edge.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2374
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_lu_orientation", "cdecl"):
    nmg_ck_lu_orientation = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_lu_orientation", "cdecl")
    nmg_ck_lu_orientation.argtypes = [POINTER(struct_loopuse), POINTER(struct_bn_tol)]
    nmg_ck_lu_orientation.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2376
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_class_name", "cdecl"):
    nmg_class_name = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_class_name", "cdecl")
    nmg_class_name.argtypes = [c_int]
    nmg_class_name.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2377
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_evaluate_boolean", "cdecl"):
    nmg_evaluate_boolean = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_evaluate_boolean", "cdecl")
    nmg_evaluate_boolean.argtypes = [POINTER(struct_shell), POINTER(struct_shell), c_int, POINTER(POINTER(c_char)), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_evaluate_boolean.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2392
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vvg", "cdecl"):
    nmg_vvg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vvg", "cdecl")
    nmg_vvg.argtypes = [POINTER(struct_vertex_g)]
    nmg_vvg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2393
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vvertex", "cdecl"):
    nmg_vvertex = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vvertex", "cdecl")
    nmg_vvertex.argtypes = [POINTER(struct_vertex), POINTER(struct_vertexuse)]
    nmg_vvertex.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2395
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vvua", "cdecl"):
    nmg_vvua = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vvua", "cdecl")
    nmg_vvua.argtypes = [POINTER(c_uint32)]
    nmg_vvua.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2396
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vvu", "cdecl"):
    nmg_vvu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vvu", "cdecl")
    nmg_vvu.argtypes = [POINTER(struct_vertexuse), POINTER(c_uint32)]
    nmg_vvu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2398
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_veg", "cdecl"):
    nmg_veg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_veg", "cdecl")
    nmg_veg.argtypes = [POINTER(c_uint32)]
    nmg_veg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2399
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vedge", "cdecl"):
    nmg_vedge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vedge", "cdecl")
    nmg_vedge.argtypes = [POINTER(struct_edge), POINTER(struct_edgeuse)]
    nmg_vedge.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2401
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_veu", "cdecl"):
    nmg_veu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_veu", "cdecl")
    nmg_veu.argtypes = [POINTER(struct_bu_list), POINTER(c_uint32)]
    nmg_veu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2403
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlg", "cdecl"):
    nmg_vlg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlg", "cdecl")
    nmg_vlg.argtypes = [POINTER(struct_loop_g)]
    nmg_vlg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2404
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vloop", "cdecl"):
    nmg_vloop = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vloop", "cdecl")
    nmg_vloop.argtypes = [POINTER(struct_loop), POINTER(struct_loopuse)]
    nmg_vloop.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2406
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vlu", "cdecl"):
    nmg_vlu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vlu", "cdecl")
    nmg_vlu.argtypes = [POINTER(struct_bu_list), POINTER(c_uint32)]
    nmg_vlu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2408
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vfg", "cdecl"):
    nmg_vfg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vfg", "cdecl")
    nmg_vfg.argtypes = [POINTER(struct_face_g_plane)]
    nmg_vfg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2409
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vface", "cdecl"):
    nmg_vface = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vface", "cdecl")
    nmg_vface.argtypes = [POINTER(struct_face), POINTER(struct_faceuse)]
    nmg_vface.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2411
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vfu", "cdecl"):
    nmg_vfu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vfu", "cdecl")
    nmg_vfu.argtypes = [POINTER(struct_bu_list), POINTER(struct_shell)]
    nmg_vfu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2413
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vsshell", "cdecl"):
    nmg_vsshell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vsshell", "cdecl")
    nmg_vsshell.argtypes = [POINTER(struct_shell), POINTER(struct_nmgregion)]
    nmg_vsshell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2415
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vshell", "cdecl"):
    nmg_vshell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vshell", "cdecl")
    nmg_vshell.argtypes = [POINTER(struct_bu_list), POINTER(struct_nmgregion)]
    nmg_vshell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2417
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vregion", "cdecl"):
    nmg_vregion = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vregion", "cdecl")
    nmg_vregion.argtypes = [POINTER(struct_bu_list), POINTER(struct_model)]
    nmg_vregion.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2419
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vmodel", "cdecl"):
    nmg_vmodel = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vmodel", "cdecl")
    nmg_vmodel.argtypes = [POINTER(struct_model)]
    nmg_vmodel.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2422
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_e", "cdecl"):
    nmg_ck_e = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_e", "cdecl")
    nmg_ck_e.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edge), String]
    nmg_ck_e.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2425
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_vu", "cdecl"):
    nmg_ck_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_vu", "cdecl")
    nmg_ck_vu.argtypes = [POINTER(c_uint32), POINTER(struct_vertexuse), String]
    nmg_ck_vu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2428
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_eu", "cdecl"):
    nmg_ck_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_eu", "cdecl")
    nmg_ck_eu.argtypes = [POINTER(c_uint32), POINTER(struct_edgeuse), String]
    nmg_ck_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2431
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_lg", "cdecl"):
    nmg_ck_lg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_lg", "cdecl")
    nmg_ck_lg.argtypes = [POINTER(struct_loop), POINTER(struct_loop_g), String]
    nmg_ck_lg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2434
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_l", "cdecl"):
    nmg_ck_l = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_l", "cdecl")
    nmg_ck_l.argtypes = [POINTER(struct_loopuse), POINTER(struct_loop), String]
    nmg_ck_l.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2437
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_lu", "cdecl"):
    nmg_ck_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_lu", "cdecl")
    nmg_ck_lu.argtypes = [POINTER(c_uint32), POINTER(struct_loopuse), String]
    nmg_ck_lu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2440
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_fg", "cdecl"):
    nmg_ck_fg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_fg", "cdecl")
    nmg_ck_fg.argtypes = [POINTER(struct_face), POINTER(struct_face_g_plane), String]
    nmg_ck_fg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2443
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_f", "cdecl"):
    nmg_ck_f = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_f", "cdecl")
    nmg_ck_f.argtypes = [POINTER(struct_faceuse), POINTER(struct_face), String]
    nmg_ck_f.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2446
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_fu", "cdecl"):
    nmg_ck_fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_fu", "cdecl")
    nmg_ck_fu.argtypes = [POINTER(struct_shell), POINTER(struct_faceuse), String]
    nmg_ck_fu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2449
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_eg_verts", "cdecl"):
    nmg_ck_eg_verts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_eg_verts", "cdecl")
    nmg_ck_eg_verts.argtypes = [POINTER(struct_edge_g_lseg), POINTER(struct_bn_tol)]
    nmg_ck_eg_verts.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2451
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_geometry", "cdecl"):
    nmg_ck_geometry = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_geometry", "cdecl")
    nmg_ck_geometry.argtypes = [POINTER(struct_model), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_ck_geometry.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2454
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_face_worthless_edges", "cdecl"):
    nmg_ck_face_worthless_edges = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_face_worthless_edges", "cdecl")
    nmg_ck_face_worthless_edges.argtypes = [POINTER(struct_faceuse)]
    nmg_ck_face_worthless_edges.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2455
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_lueu", "cdecl"):
    nmg_ck_lueu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_lueu", "cdecl")
    nmg_ck_lueu.argtypes = [POINTER(struct_loopuse), String]
    nmg_ck_lueu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2456
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_check_radial", "cdecl"):
    nmg_check_radial = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_check_radial", "cdecl")
    nmg_check_radial.argtypes = [POINTER(struct_edgeuse), POINTER(struct_bn_tol)]
    nmg_check_radial.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2457
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_eu_2s_orient_bad", "cdecl"):
    nmg_eu_2s_orient_bad = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_eu_2s_orient_bad", "cdecl")
    nmg_eu_2s_orient_bad.argtypes = [POINTER(struct_edgeuse), POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_eu_2s_orient_bad.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2461
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_closed_surf", "cdecl"):
    nmg_ck_closed_surf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_closed_surf", "cdecl")
    nmg_ck_closed_surf.argtypes = [POINTER(struct_shell), POINTER(struct_bn_tol)]
    nmg_ck_closed_surf.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2463
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_closed_region", "cdecl"):
    nmg_ck_closed_region = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_closed_region", "cdecl")
    nmg_ck_closed_region.argtypes = [POINTER(struct_nmgregion), POINTER(struct_bn_tol)]
    nmg_ck_closed_region.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2465
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_v_in_2fus", "cdecl"):
    nmg_ck_v_in_2fus = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_v_in_2fus", "cdecl")
    nmg_ck_v_in_2fus.argtypes = [POINTER(struct_vertex), POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_ck_v_in_2fus.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2469
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ck_vs_in_region", "cdecl"):
    nmg_ck_vs_in_region = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ck_vs_in_region", "cdecl")
    nmg_ck_vs_in_region.argtypes = [POINTER(struct_nmgregion), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_ck_vs_in_region.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2475
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_make_dualvu", "cdecl"):
    nmg_make_dualvu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_make_dualvu", "cdecl")
    nmg_make_dualvu.argtypes = [POINTER(struct_vertex), POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_make_dualvu.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2478
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_enlist_vu", "cdecl"):
    nmg_enlist_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_enlist_vu", "cdecl")
    nmg_enlist_vu.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_vertexuse), POINTER(struct_vertexuse), fastf_t]
    nmg_enlist_vu.restype = POINTER(struct_vertexuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2482
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect2d_prep", "cdecl"):
    nmg_isect2d_prep = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect2d_prep", "cdecl")
    nmg_isect2d_prep.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(c_uint32)]
    nmg_isect2d_prep.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2484
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect2d_cleanup", "cdecl"):
    nmg_isect2d_cleanup = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect2d_cleanup", "cdecl")
    nmg_isect2d_cleanup.argtypes = [POINTER(struct_nmg_inter_struct)]
    nmg_isect2d_cleanup.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2485
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect2d_final_cleanup", "cdecl"):
    nmg_isect2d_final_cleanup = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect2d_final_cleanup", "cdecl")
    nmg_isect2d_final_cleanup.argtypes = []
    nmg_isect2d_final_cleanup.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2486
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_2faceuse", "cdecl"):
    nmg_isect_2faceuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_2faceuse", "cdecl")
    nmg_isect_2faceuse.argtypes = [point_t, vect_t, POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bn_tol)]
    nmg_isect_2faceuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2491
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_vert2p_face2p", "cdecl"):
    nmg_isect_vert2p_face2p = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_vert2p_face2p", "cdecl")
    nmg_isect_vert2p_face2p.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_vertexuse), POINTER(struct_faceuse)]
    nmg_isect_vert2p_face2p.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2494
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_eu_on_v", "cdecl"):
    nmg_break_eu_on_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_eu_on_v", "cdecl")
    nmg_break_eu_on_v.argtypes = [POINTER(struct_edgeuse), POINTER(struct_vertex), POINTER(struct_faceuse), POINTER(struct_nmg_inter_struct)]
    nmg_break_eu_on_v.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2498
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_break_eg_on_v", "cdecl"):
    nmg_break_eg_on_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_break_eg_on_v", "cdecl")
    nmg_break_eg_on_v.argtypes = [POINTER(struct_edge_g_lseg), POINTER(struct_vertex), POINTER(struct_bn_tol)]
    nmg_break_eg_on_v.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2501
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_2colinear_edge2p", "cdecl"):
    nmg_isect_2colinear_edge2p = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_2colinear_edge2p", "cdecl")
    nmg_isect_2colinear_edge2p.argtypes = [POINTER(struct_edgeuse), POINTER(struct_edgeuse), POINTER(struct_faceuse), POINTER(struct_nmg_inter_struct), POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl)]
    nmg_isect_2colinear_edge2p.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2507
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_edge2p_edge2p", "cdecl"):
    nmg_isect_edge2p_edge2p = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_edge2p_edge2p", "cdecl")
    nmg_isect_edge2p_edge2p.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_edgeuse), POINTER(struct_edgeuse), POINTER(struct_faceuse), POINTER(struct_faceuse)]
    nmg_isect_edge2p_edge2p.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2512
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_construct_nice_ray", "cdecl"):
    nmg_isect_construct_nice_ray = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_construct_nice_ray", "cdecl")
    nmg_isect_construct_nice_ray.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_faceuse)]
    nmg_isect_construct_nice_ray.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2514
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_enlist_one_vu", "cdecl"):
    nmg_enlist_one_vu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_enlist_one_vu", "cdecl")
    nmg_enlist_one_vu.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_vertexuse), fastf_t]
    nmg_enlist_one_vu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2517
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_line2_edge2p", "cdecl"):
    nmg_isect_line2_edge2p = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_line2_edge2p", "cdecl")
    nmg_isect_line2_edge2p.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_bu_ptbl), POINTER(struct_edgeuse), POINTER(struct_faceuse), POINTER(struct_faceuse)]
    nmg_isect_line2_edge2p.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2522
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_line2_vertex2", "cdecl"):
    nmg_isect_line2_vertex2 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_line2_vertex2", "cdecl")
    nmg_isect_line2_vertex2.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_vertexuse), POINTER(struct_faceuse)]
    nmg_isect_line2_vertex2.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2525
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_two_ptbls", "cdecl"):
    nmg_isect_two_ptbls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_two_ptbls", "cdecl")
    nmg_isect_two_ptbls.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl)]
    nmg_isect_two_ptbls.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2528
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_eg_on_line", "cdecl"):
    nmg_find_eg_on_line = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_eg_on_line", "cdecl")
    nmg_find_eg_on_line.argtypes = [POINTER(c_uint32), point_t, vect_t, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_find_eg_on_line.restype = POINTER(struct_edge_g_lseg)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2533
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_k0eu", "cdecl"):
    nmg_k0eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_k0eu", "cdecl")
    nmg_k0eu.argtypes = [POINTER(struct_vertex)]
    nmg_k0eu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2534
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_repair_v_near_v", "cdecl"):
    nmg_repair_v_near_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_repair_v_near_v", "cdecl")
    nmg_repair_v_near_v.argtypes = [POINTER(struct_vertex), POINTER(struct_vertex), POINTER(struct_edge_g_lseg), POINTER(struct_edge_g_lseg), c_int, POINTER(struct_bn_tol)]
    nmg_repair_v_near_v.restype = POINTER(struct_vertex)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2540
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_search_v_eg", "cdecl"):
    nmg_search_v_eg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_search_v_eg", "cdecl")
    nmg_search_v_eg.argtypes = [POINTER(struct_edgeuse), c_int, POINTER(struct_edge_g_lseg), POINTER(struct_edge_g_lseg), POINTER(struct_vertex), POINTER(struct_bn_tol)]
    nmg_search_v_eg.restype = POINTER(struct_vertex)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2546
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_common_v_2eg", "cdecl"):
    nmg_common_v_2eg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_common_v_2eg", "cdecl")
    nmg_common_v_2eg.argtypes = [POINTER(struct_edge_g_lseg), POINTER(struct_edge_g_lseg), POINTER(struct_bn_tol)]
    nmg_common_v_2eg.restype = POINTER(struct_vertex)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2549
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_vertex_on_inter", "cdecl"):
    nmg_is_vertex_on_inter = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_vertex_on_inter", "cdecl")
    nmg_is_vertex_on_inter.argtypes = [POINTER(struct_vertex), POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_nmg_inter_struct), POINTER(struct_bu_list)]
    nmg_is_vertex_on_inter.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2554
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_eu_verts", "cdecl"):
    nmg_isect_eu_verts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_eu_verts", "cdecl")
    nmg_isect_eu_verts.argtypes = [POINTER(struct_edgeuse), POINTER(struct_vertex_g), POINTER(struct_vertex_g), POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl), POINTER(struct_bn_tol)]
    nmg_isect_eu_verts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2560
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_eu_eu", "cdecl"):
    nmg_isect_eu_eu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_eu_eu", "cdecl")
    nmg_isect_eu_eu.argtypes = [POINTER(struct_edgeuse), POINTER(struct_vertex_g), POINTER(struct_vertex_g), vect_t, POINTER(struct_edgeuse), POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl), POINTER(struct_bn_tol)]
    nmg_isect_eu_eu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2568
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_eu_fu", "cdecl"):
    nmg_isect_eu_fu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_eu_fu", "cdecl")
    nmg_isect_eu_fu.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_bu_ptbl), POINTER(struct_edgeuse), POINTER(struct_faceuse), POINTER(struct_bu_list)]
    nmg_isect_eu_fu.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2573
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_fu_jra", "cdecl"):
    nmg_isect_fu_jra = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_fu_jra", "cdecl")
    nmg_isect_fu_jra.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl), POINTER(struct_bu_list)]
    nmg_isect_fu_jra.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2579
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_line2_face2pNEW", "cdecl"):
    nmg_isect_line2_face2pNEW = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_line2_face2pNEW", "cdecl")
    nmg_isect_line2_face2pNEW.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_ptbl), POINTER(struct_bu_ptbl), POINTER(struct_bu_list)]
    nmg_isect_line2_face2pNEW.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2584
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_is_eu_on_line3", "cdecl"):
    nmg_is_eu_on_line3 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_is_eu_on_line3", "cdecl")
    nmg_is_eu_on_line3.argtypes = [POINTER(struct_edgeuse), point_t, vect_t, POINTER(struct_bn_tol)]
    nmg_is_eu_on_line3.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2588
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_eg_between_2fg", "cdecl"):
    nmg_find_eg_between_2fg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_eg_between_2fg", "cdecl")
    nmg_find_eg_between_2fg.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_find_eg_between_2fg.restype = POINTER(struct_edge_g_lseg)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2592
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_does_fu_use_eg", "cdecl"):
    nmg_does_fu_use_eg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_does_fu_use_eg", "cdecl")
    nmg_does_fu_use_eg.argtypes = [POINTER(struct_faceuse), POINTER(c_uint32)]
    nmg_does_fu_use_eg.restype = POINTER(struct_edgeuse)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2594
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_line_on_plane", "cdecl"):
    rt_line_on_plane = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_line_on_plane", "cdecl")
    rt_line_on_plane.argtypes = [point_t, vect_t, plane_t, POINTER(struct_bn_tol)]
    rt_line_on_plane.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2598
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_cut_lu_into_coplanar_and_non", "cdecl"):
    nmg_cut_lu_into_coplanar_and_non = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_cut_lu_into_coplanar_and_non", "cdecl")
    nmg_cut_lu_into_coplanar_and_non.argtypes = [POINTER(struct_loopuse), plane_t, POINTER(struct_nmg_inter_struct), POINTER(struct_bu_list)]
    nmg_cut_lu_into_coplanar_and_non.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2602
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_check_radial_angles", "cdecl"):
    nmg_check_radial_angles = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_check_radial_angles", "cdecl")
    nmg_check_radial_angles.argtypes = [String, POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_check_radial_angles.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2606
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_faces_can_be_intersected", "cdecl"):
    nmg_faces_can_be_intersected = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_faces_can_be_intersected", "cdecl")
    nmg_faces_can_be_intersected.argtypes = [POINTER(struct_nmg_inter_struct), POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_faces_can_be_intersected.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2611
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_two_generic_faces", "cdecl"):
    nmg_isect_two_generic_faces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_two_generic_faces", "cdecl")
    nmg_isect_two_generic_faces.argtypes = [POINTER(struct_faceuse), POINTER(struct_faceuse), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_isect_two_generic_faces.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2615
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_crackshells", "cdecl"):
    nmg_crackshells = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_crackshells", "cdecl")
    nmg_crackshells.argtypes = [POINTER(struct_shell), POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_crackshells.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2619
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_fu_touchingloops", "cdecl"):
    nmg_fu_touchingloops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_fu_touchingloops", "cdecl")
    nmg_fu_touchingloops.argtypes = [POINTER(struct_faceuse)]
    nmg_fu_touchingloops.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2623
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_index_of_struct", "cdecl"):
    nmg_index_of_struct = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_index_of_struct", "cdecl")
    nmg_index_of_struct.argtypes = [POINTER(c_uint32)]
    nmg_index_of_struct.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2624
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_m_set_high_bit", "cdecl"):
    nmg_m_set_high_bit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_m_set_high_bit", "cdecl")
    nmg_m_set_high_bit.argtypes = [POINTER(struct_model)]
    nmg_m_set_high_bit.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2625
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_m_reindex", "cdecl"):
    nmg_m_reindex = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_m_reindex", "cdecl")
    nmg_m_reindex.argtypes = [POINTER(struct_model), c_long]
    nmg_m_reindex.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2626
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_vls_struct_counts", "cdecl"):
    nmg_vls_struct_counts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_vls_struct_counts", "cdecl")
    nmg_vls_struct_counts.argtypes = [POINTER(struct_bu_vls), POINTER(struct_nmg_struct_counts)]
    nmg_vls_struct_counts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2628
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_struct_counts", "cdecl"):
    nmg_pr_struct_counts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_struct_counts", "cdecl")
    nmg_pr_struct_counts.argtypes = [POINTER(struct_nmg_struct_counts), String]
    nmg_pr_struct_counts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2630
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_m_struct_count", "cdecl"):
    nmg_m_struct_count = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_m_struct_count", "cdecl")
    nmg_m_struct_count.argtypes = [POINTER(struct_nmg_struct_counts), POINTER(struct_model)]
    nmg_m_struct_count.restype = POINTER(POINTER(c_uint32))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2632
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_pr_m_struct_counts", "cdecl"):
    nmg_pr_m_struct_counts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_pr_m_struct_counts", "cdecl")
    nmg_pr_m_struct_counts.argtypes = [POINTER(struct_model), String]
    nmg_pr_m_struct_counts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2634
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_merge_models", "cdecl"):
    nmg_merge_models = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_merge_models", "cdecl")
    nmg_merge_models.argtypes = [POINTER(struct_model), POINTER(struct_model)]
    nmg_merge_models.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2636
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_find_max_index", "cdecl"):
    nmg_find_max_index = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_find_max_index", "cdecl")
    nmg_find_max_index.argtypes = [POINTER(struct_model)]
    nmg_find_max_index.restype = c_long

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2639
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_rt_inout_str", "cdecl"):
    nmg_rt_inout_str = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_rt_inout_str", "cdecl")
    nmg_rt_inout_str.argtypes = [c_int]
    nmg_rt_inout_str.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2641
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_rt_print_hitlist", "cdecl"):
    nmg_rt_print_hitlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_rt_print_hitlist", "cdecl")
    nmg_rt_print_hitlist.argtypes = [POINTER(struct_bu_list)]
    nmg_rt_print_hitlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2643
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_rt_print_hitmiss", "cdecl"):
    nmg_rt_print_hitmiss = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_rt_print_hitmiss", "cdecl")
    nmg_rt_print_hitmiss.argtypes = [POINTER(struct_nmg_hitmiss)]
    nmg_rt_print_hitmiss.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2645
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_class_ray_vs_shell", "cdecl"):
    nmg_class_ray_vs_shell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_class_ray_vs_shell", "cdecl")
    nmg_class_ray_vs_shell.argtypes = [POINTER(struct_nmg_ray), POINTER(struct_shell), c_int, POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_class_ray_vs_shell.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2651
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_isect_ray_model", "cdecl"):
    nmg_isect_ray_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_isect_ray_model", "cdecl")
    nmg_isect_ray_model.argtypes = [POINTER(struct_nmg_ray_data), POINTER(struct_bu_list)]
    nmg_isect_ray_model.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2659
class struct_nmg_curvature(Structure):
    pass

struct_nmg_curvature.__slots__ = [
    'crv_pdir',
    'crv_c1',
    'crv_c2',
]
struct_nmg_curvature._fields_ = [
    ('crv_pdir', vect_t),
    ('crv_c1', fastf_t),
    ('crv_c2', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2666
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_basis_eval", "cdecl"):
    nmg_nurb_basis_eval = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_basis_eval", "cdecl")
    nmg_nurb_basis_eval.argtypes = [POINTER(struct_knot_vector), c_int, c_int, fastf_t]
    nmg_nurb_basis_eval.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2670
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_bezier", "cdecl"):
    nmg_nurb_bezier = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_bezier", "cdecl")
    nmg_nurb_bezier.argtypes = [POINTER(struct_bu_list), POINTER(struct_face_g_snurb)]
    nmg_nurb_bezier.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2671
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_bez_check", "cdecl"):
    nmg_bez_check = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_bez_check", "cdecl")
    nmg_bez_check.argtypes = [POINTER(struct_face_g_snurb)]
    nmg_bez_check.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2672
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nurb_crv_is_bezier", "cdecl"):
    nurb_crv_is_bezier = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nurb_crv_is_bezier", "cdecl")
    nurb_crv_is_bezier.argtypes = [POINTER(struct_edge_g_cnurb)]
    nurb_crv_is_bezier.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2673
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nurb_c_to_bezier", "cdecl"):
    nurb_c_to_bezier = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nurb_c_to_bezier", "cdecl")
    nurb_c_to_bezier.argtypes = [POINTER(struct_bu_list), POINTER(struct_edge_g_cnurb)]
    nurb_c_to_bezier.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2676
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_bound", "cdecl"):
    nmg_nurb_s_bound = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_bound", "cdecl")
    nmg_nurb_s_bound.argtypes = [POINTER(struct_face_g_snurb), point_t, point_t]
    nmg_nurb_s_bound.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2677
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_bound", "cdecl"):
    nmg_nurb_c_bound = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_bound", "cdecl")
    nmg_nurb_c_bound.argtypes = [POINTER(struct_edge_g_cnurb), point_t, point_t]
    nmg_nurb_c_bound.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2678
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_check", "cdecl"):
    nmg_nurb_s_check = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_check", "cdecl")
    nmg_nurb_s_check.argtypes = [POINTER(struct_face_g_snurb)]
    nmg_nurb_s_check.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2679
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_check", "cdecl"):
    nmg_nurb_c_check = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_check", "cdecl")
    nmg_nurb_c_check.argtypes = [POINTER(struct_edge_g_cnurb)]
    nmg_nurb_c_check.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2682
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_scopy", "cdecl"):
    nmg_nurb_scopy = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_scopy", "cdecl")
    nmg_nurb_scopy.argtypes = [POINTER(struct_face_g_snurb)]
    nmg_nurb_scopy.restype = POINTER(struct_face_g_snurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2683
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_crv_copy", "cdecl"):
    nmg_nurb_crv_copy = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_crv_copy", "cdecl")
    nmg_nurb_crv_copy.argtypes = [POINTER(struct_edge_g_cnurb)]
    nmg_nurb_crv_copy.restype = POINTER(struct_edge_g_cnurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2686
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_diff", "cdecl"):
    nmg_nurb_s_diff = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_diff", "cdecl")
    nmg_nurb_s_diff.argtypes = [POINTER(struct_face_g_snurb), c_int]
    nmg_nurb_s_diff.restype = POINTER(struct_face_g_snurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2687
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_diff", "cdecl"):
    nmg_nurb_c_diff = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_diff", "cdecl")
    nmg_nurb_c_diff.argtypes = [POINTER(struct_edge_g_cnurb)]
    nmg_nurb_c_diff.restype = POINTER(struct_edge_g_cnurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2688
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_mesh_diff", "cdecl"):
    nmg_nurb_mesh_diff = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_mesh_diff", "cdecl")
    nmg_nurb_mesh_diff.argtypes = [c_int, POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_int, c_int, c_int, c_int]
    nmg_nurb_mesh_diff.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2694
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_eval", "cdecl"):
    nmg_nurb_s_eval = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_eval", "cdecl")
    nmg_nurb_s_eval.argtypes = [POINTER(struct_face_g_snurb), fastf_t, fastf_t, POINTER(fastf_t)]
    nmg_nurb_s_eval.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2695
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_eval", "cdecl"):
    nmg_nurb_c_eval = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_eval", "cdecl")
    nmg_nurb_c_eval.argtypes = [POINTER(struct_edge_g_cnurb), fastf_t, POINTER(fastf_t)]
    nmg_nurb_c_eval.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2696
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_eval_crv", "cdecl"):
    nmg_nurb_eval_crv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_eval_crv", "cdecl")
    nmg_nurb_eval_crv.argtypes = [POINTER(fastf_t), c_int, fastf_t, POINTER(struct_knot_vector), c_int, c_int]
    nmg_nurb_eval_crv.restype = POINTER(fastf_t)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2699
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_pr_crv", "cdecl"):
    nmg_nurb_pr_crv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_pr_crv", "cdecl")
    nmg_nurb_pr_crv.argtypes = [POINTER(fastf_t), c_int, c_int]
    nmg_nurb_pr_crv.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2702
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_flat", "cdecl"):
    nmg_nurb_s_flat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_flat", "cdecl")
    nmg_nurb_s_flat.argtypes = [POINTER(struct_face_g_snurb), fastf_t]
    nmg_nurb_s_flat.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2703
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_crv_flat", "cdecl"):
    nmg_nurb_crv_flat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_crv_flat", "cdecl")
    nmg_nurb_crv_flat.argtypes = [POINTER(fastf_t), c_int, c_int]
    nmg_nurb_crv_flat.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2706
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvknot", "cdecl"):
    nmg_nurb_kvknot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvknot", "cdecl")
    nmg_nurb_kvknot.argtypes = [POINTER(struct_knot_vector), c_int, fastf_t, fastf_t, c_int]
    nmg_nurb_kvknot.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2708
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvmult", "cdecl"):
    nmg_nurb_kvmult = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvmult", "cdecl")
    nmg_nurb_kvmult.argtypes = [POINTER(struct_knot_vector), POINTER(struct_knot_vector), c_int, fastf_t]
    nmg_nurb_kvmult.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2711
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvgen", "cdecl"):
    nmg_nurb_kvgen = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvgen", "cdecl")
    nmg_nurb_kvgen.argtypes = [POINTER(struct_knot_vector), fastf_t, fastf_t, c_int]
    nmg_nurb_kvgen.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2713
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvmerge", "cdecl"):
    nmg_nurb_kvmerge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvmerge", "cdecl")
    nmg_nurb_kvmerge.argtypes = [POINTER(struct_knot_vector), POINTER(struct_knot_vector), POINTER(struct_knot_vector)]
    nmg_nurb_kvmerge.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2716
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvcheck", "cdecl"):
    nmg_nurb_kvcheck = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvcheck", "cdecl")
    nmg_nurb_kvcheck.argtypes = [fastf_t, POINTER(struct_knot_vector)]
    nmg_nurb_kvcheck.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2717
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvextract", "cdecl"):
    nmg_nurb_kvextract = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvextract", "cdecl")
    nmg_nurb_kvextract.argtypes = [POINTER(struct_knot_vector), POINTER(struct_knot_vector), c_int, c_int]
    nmg_nurb_kvextract.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2720
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvcopy", "cdecl"):
    nmg_nurb_kvcopy = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvcopy", "cdecl")
    nmg_nurb_kvcopy.argtypes = [POINTER(struct_knot_vector), POINTER(struct_knot_vector)]
    nmg_nurb_kvcopy.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2722
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_kvnorm", "cdecl"):
    nmg_nurb_kvnorm = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_kvnorm", "cdecl")
    nmg_nurb_kvnorm.argtypes = [POINTER(struct_knot_vector)]
    nmg_nurb_kvnorm.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2723
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_knot_index", "cdecl"):
    nmg_nurb_knot_index = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_knot_index", "cdecl")
    nmg_nurb_knot_index.argtypes = [POINTER(struct_knot_vector), fastf_t, c_int]
    nmg_nurb_knot_index.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2724
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_gen_knot_vector", "cdecl"):
    nmg_nurb_gen_knot_vector = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_gen_knot_vector", "cdecl")
    nmg_nurb_gen_knot_vector.argtypes = [POINTER(struct_knot_vector), c_int, fastf_t, fastf_t]
    nmg_nurb_gen_knot_vector.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2728
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_norm", "cdecl"):
    nmg_nurb_s_norm = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_norm", "cdecl")
    nmg_nurb_s_norm.argtypes = [POINTER(struct_face_g_snurb), fastf_t, fastf_t, POINTER(fastf_t)]
    nmg_nurb_s_norm.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2731
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_curvature", "cdecl"):
    nmg_nurb_curvature = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_curvature", "cdecl")
    nmg_nurb_curvature.argtypes = [POINTER(struct_nmg_curvature), POINTER(struct_face_g_snurb), fastf_t, fastf_t]
    nmg_nurb_curvature.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2735
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_plot_snurb", "cdecl"):
    nmg_nurb_plot_snurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_plot_snurb", "cdecl")
    nmg_nurb_plot_snurb.argtypes = [POINTER(FILE), POINTER(struct_face_g_snurb)]
    nmg_nurb_plot_snurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2736
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_plot_cnurb", "cdecl"):
    nmg_nurb_plot_cnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_plot_cnurb", "cdecl")
    nmg_nurb_plot_cnurb.argtypes = [POINTER(FILE), POINTER(struct_edge_g_cnurb)]
    nmg_nurb_plot_cnurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2737
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_plot", "cdecl"):
    nmg_nurb_s_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_plot", "cdecl")
    nmg_nurb_s_plot.argtypes = [POINTER(struct_face_g_snurb)]
    nmg_nurb_s_plot.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2740
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_cinterp", "cdecl"):
    nmg_nurb_cinterp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_cinterp", "cdecl")
    nmg_nurb_cinterp.argtypes = [POINTER(struct_edge_g_cnurb), c_int, POINTER(fastf_t), c_int]
    nmg_nurb_cinterp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2742
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_sinterp", "cdecl"):
    nmg_nurb_sinterp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_sinterp", "cdecl")
    nmg_nurb_sinterp.argtypes = [POINTER(struct_face_g_snurb), c_int, POINTER(fastf_t), c_int, c_int]
    nmg_nurb_sinterp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2746
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_to_poly", "cdecl"):
    nmg_nurb_to_poly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_to_poly", "cdecl")
    nmg_nurb_to_poly.argtypes = [POINTER(struct_face_g_snurb)]
    nmg_nurb_to_poly.restype = POINTER(struct_nmg_nurb_poly)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2747
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_mk_poly", "cdecl"):
    nmg_nurb_mk_poly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_mk_poly", "cdecl")
    nmg_nurb_mk_poly.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), fastf_t * int(2), fastf_t * int(2), fastf_t * int(2)]
    nmg_nurb_mk_poly.restype = POINTER(struct_nmg_nurb_poly)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2751
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_project_srf", "cdecl"):
    nmg_nurb_project_srf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_project_srf", "cdecl")
    nmg_nurb_project_srf.argtypes = [POINTER(struct_face_g_snurb), plane_t, plane_t]
    nmg_nurb_project_srf.restype = POINTER(struct_face_g_snurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2753
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_clip_srf", "cdecl"):
    nmg_nurb_clip_srf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_clip_srf", "cdecl")
    nmg_nurb_clip_srf.argtypes = [POINTER(struct_face_g_snurb), c_int, POINTER(fastf_t), POINTER(fastf_t)]
    nmg_nurb_clip_srf.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2755
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_region_from_srf", "cdecl"):
    nmg_nurb_region_from_srf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_region_from_srf", "cdecl")
    nmg_nurb_region_from_srf.argtypes = [POINTER(struct_face_g_snurb), c_int, fastf_t, fastf_t]
    nmg_nurb_region_from_srf.restype = POINTER(struct_face_g_snurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2757
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_intersect", "cdecl"):
    nmg_nurb_intersect = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_intersect", "cdecl")
    nmg_nurb_intersect.argtypes = [POINTER(struct_face_g_snurb), plane_t, plane_t, c_double, POINTER(struct_bu_list)]
    nmg_nurb_intersect.restype = POINTER(struct_nmg_nurb_uv_hit)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2761
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_refine", "cdecl"):
    nmg_nurb_s_refine = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_refine", "cdecl")
    nmg_nurb_s_refine.argtypes = [POINTER(struct_face_g_snurb), c_int, POINTER(struct_knot_vector)]
    nmg_nurb_s_refine.restype = POINTER(struct_face_g_snurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2763
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_refine", "cdecl"):
    nmg_nurb_c_refine = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_refine", "cdecl")
    nmg_nurb_c_refine.argtypes = [POINTER(struct_edge_g_cnurb), POINTER(struct_knot_vector)]
    nmg_nurb_c_refine.restype = POINTER(struct_edge_g_cnurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2767
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_solve", "cdecl"):
    nmg_nurb_solve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_solve", "cdecl")
    nmg_nurb_solve.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_int, c_int]
    nmg_nurb_solve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2769
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_doolittle", "cdecl"):
    nmg_nurb_doolittle = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_doolittle", "cdecl")
    nmg_nurb_doolittle.argtypes = [POINTER(fastf_t), POINTER(fastf_t), c_int, c_int]
    nmg_nurb_doolittle.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2771
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_forw_solve", "cdecl"):
    nmg_nurb_forw_solve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_forw_solve", "cdecl")
    nmg_nurb_forw_solve.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_int]
    nmg_nurb_forw_solve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2773
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_back_solve", "cdecl"):
    nmg_nurb_back_solve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_back_solve", "cdecl")
    nmg_nurb_back_solve.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_int]
    nmg_nurb_back_solve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2775
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_p_mat", "cdecl"):
    nmg_nurb_p_mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_p_mat", "cdecl")
    nmg_nurb_p_mat.argtypes = [POINTER(fastf_t), c_int]
    nmg_nurb_p_mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2778
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_split", "cdecl"):
    nmg_nurb_s_split = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_split", "cdecl")
    nmg_nurb_s_split.argtypes = [POINTER(struct_bu_list), POINTER(struct_face_g_snurb), c_int]
    nmg_nurb_s_split.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2780
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_split", "cdecl"):
    nmg_nurb_c_split = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_split", "cdecl")
    nmg_nurb_c_split.argtypes = [POINTER(struct_bu_list), POINTER(struct_edge_g_cnurb)]
    nmg_nurb_c_split.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2783
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_uv_in_lu", "cdecl"):
    nmg_uv_in_lu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_uv_in_lu", "cdecl")
    nmg_uv_in_lu.argtypes = [fastf_t, fastf_t, POINTER(struct_loopuse)]
    nmg_uv_in_lu.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2786
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_new_snurb", "cdecl"):
    nmg_nurb_new_snurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_new_snurb", "cdecl")
    nmg_nurb_new_snurb.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
    nmg_nurb_new_snurb.restype = POINTER(struct_face_g_snurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2789
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_new_cnurb", "cdecl"):
    nmg_nurb_new_cnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_new_cnurb", "cdecl")
    nmg_nurb_new_cnurb.argtypes = [c_int, c_int, c_int, c_int]
    nmg_nurb_new_cnurb.restype = POINTER(struct_edge_g_cnurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2791
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_free_snurb", "cdecl"):
    nmg_nurb_free_snurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_free_snurb", "cdecl")
    nmg_nurb_free_snurb.argtypes = [POINTER(struct_face_g_snurb)]
    nmg_nurb_free_snurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2792
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_free_cnurb", "cdecl"):
    nmg_nurb_free_cnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_free_cnurb", "cdecl")
    nmg_nurb_free_cnurb.argtypes = [POINTER(struct_edge_g_cnurb)]
    nmg_nurb_free_cnurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2793
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_print", "cdecl"):
    nmg_nurb_c_print = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_print", "cdecl")
    nmg_nurb_c_print.argtypes = [POINTER(struct_edge_g_cnurb)]
    nmg_nurb_c_print.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2794
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_print", "cdecl"):
    nmg_nurb_s_print = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_print", "cdecl")
    nmg_nurb_s_print.argtypes = [String, POINTER(struct_face_g_snurb)]
    nmg_nurb_s_print.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2795
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_pr_kv", "cdecl"):
    nmg_nurb_pr_kv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_pr_kv", "cdecl")
    nmg_nurb_pr_kv.argtypes = [POINTER(struct_knot_vector)]
    nmg_nurb_pr_kv.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2796
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_pr_mesh", "cdecl"):
    nmg_nurb_pr_mesh = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_pr_mesh", "cdecl")
    nmg_nurb_pr_mesh.argtypes = [POINTER(struct_face_g_snurb)]
    nmg_nurb_pr_mesh.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2797
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_print_pnt_type", "cdecl"):
    nmg_nurb_print_pnt_type = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_print_pnt_type", "cdecl")
    nmg_nurb_print_pnt_type.argtypes = [c_int]
    nmg_nurb_print_pnt_type.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2798
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_clean_cnurb", "cdecl"):
    nmg_nurb_clean_cnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_clean_cnurb", "cdecl")
    nmg_nurb_clean_cnurb.argtypes = [POINTER(struct_edge_g_cnurb)]
    nmg_nurb_clean_cnurb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2801
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_s_xsplit", "cdecl"):
    nmg_nurb_s_xsplit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_s_xsplit", "cdecl")
    nmg_nurb_s_xsplit.argtypes = [POINTER(struct_face_g_snurb), fastf_t, c_int]
    nmg_nurb_s_xsplit.restype = POINTER(struct_face_g_snurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2803
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_c_xsplit", "cdecl"):
    nmg_nurb_c_xsplit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_c_xsplit", "cdecl")
    nmg_nurb_c_xsplit.argtypes = [POINTER(struct_edge_g_cnurb), fastf_t]
    nmg_nurb_c_xsplit.restype = POINTER(struct_edge_g_cnurb)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2806
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_calc_oslo", "cdecl"):
    nmg_nurb_calc_oslo = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_calc_oslo", "cdecl")
    nmg_nurb_calc_oslo.argtypes = [c_int, POINTER(struct_knot_vector), POINTER(struct_knot_vector)]
    nmg_nurb_calc_oslo.restype = POINTER(struct_oslo_mat)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2809
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_pr_oslo", "cdecl"):
    nmg_nurb_pr_oslo = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_pr_oslo", "cdecl")
    nmg_nurb_pr_oslo.argtypes = [POINTER(struct_oslo_mat)]
    nmg_nurb_pr_oslo.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2810
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_free_oslo", "cdecl"):
    nmg_nurb_free_oslo = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_free_oslo", "cdecl")
    nmg_nurb_free_oslo.argtypes = [POINTER(struct_oslo_mat)]
    nmg_nurb_free_oslo.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2813
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_nurb_map_oslo", "cdecl"):
    nmg_nurb_map_oslo = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_nurb_map_oslo", "cdecl")
    nmg_nurb_map_oslo.argtypes = [POINTER(struct_oslo_mat), POINTER(fastf_t), POINTER(fastf_t), c_int, c_int, c_int, c_int, c_int]
    nmg_nurb_map_oslo.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2819
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_cnurb_par_edge", "cdecl"):
    rt_cnurb_par_edge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_cnurb_par_edge", "cdecl")
    rt_cnurb_par_edge.argtypes = [POINTER(struct_edge_g_cnurb), fastf_t]
    rt_cnurb_par_edge.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/pc.h: 82
class union_anon_38(Union):
    pass

union_anon_38.__slots__ = [
    'expression',
    'ptr',
]
union_anon_38._fields_ = [
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
    ('data', union_anon_38),
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
class union_anon_39(Union):
    pass

union_anon_39.__slots__ = [
    'expression',
    'cf',
]
union_anon_39._fields_ = [
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
    ('data', union_anon_39),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 60
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 79
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 96
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 111
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 156
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 169
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 203
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 217
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 229
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 244
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 263
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 268
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 281
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 297
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 46
class struct_rt_db_internal(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 323
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 349
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 373
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 403
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 416
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 423
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 438
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 459
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 474
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 490
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 506
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 523
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 539
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 556
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 597
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 609
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 616
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 630
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 642
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 651
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h: 63
class struct_db_i(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 676
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 695
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 720
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 744
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 761
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 828
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

enum_anon_58 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_PNT = 0# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_COL = (0 + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_SCA = (0 + 2)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_NRM = (0 + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_COL_SCA = ((0 + 1) + 2)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_COL_NRM = ((0 + 1) + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_SCA_NRM = ((0 + 2) + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_TYPE_COL_SCA_NRM = (((0 + 1) + 2) + 4)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

RT_PNT_UNKNOWN = 8# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

rt_pnt_type = enum_anon_58# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 899

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 901
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 905
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 910
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 915
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 920
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 926
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 932
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 938
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 947
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 971
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 981
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1005
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_txt_pos_flag", "cdecl"):
    rt_txt_pos_flag = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_txt_pos_flag", "cdecl")
    rt_txt_pos_flag.argtypes = [POINTER(c_int), c_int, c_int]
    rt_txt_pos_flag.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1010
class struct_rt_annot_internal(Structure):
    pass

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1054
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1073
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1087
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 75
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_full_path_init", "cdecl"):
    db_full_path_init = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_full_path_init", "cdecl")
    db_full_path_init.argtypes = [POINTER(struct_db_full_path)]
    db_full_path_init.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 77
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_add_node_to_full_path", "cdecl"):
    db_add_node_to_full_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_add_node_to_full_path", "cdecl")
    db_add_node_to_full_path.argtypes = [POINTER(struct_db_full_path), POINTER(struct_directory)]
    db_add_node_to_full_path.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 80
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dup_full_path", "cdecl"):
    db_dup_full_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dup_full_path", "cdecl")
    db_dup_full_path.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_full_path)]
    db_dup_full_path.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 88
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_extend_full_path", "cdecl"):
    db_extend_full_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_extend_full_path", "cdecl")
    db_extend_full_path.argtypes = [POINTER(struct_db_full_path), c_size_t]
    db_extend_full_path.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 91
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_append_full_path", "cdecl"):
    db_append_full_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_append_full_path", "cdecl")
    db_append_full_path.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_full_path)]
    db_append_full_path.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 97
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dup_path_tail", "cdecl"):
    db_dup_path_tail = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dup_path_tail", "cdecl")
    db_dup_path_tail.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_full_path), off_t]
    db_dup_path_tail.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 106
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_path_to_string", "cdecl"):
    db_path_to_string = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_path_to_string", "cdecl")
    db_path_to_string.argtypes = [POINTER(struct_db_full_path)]
    if sizeof(c_int) == sizeof(c_void_p):
        db_path_to_string.restype = ReturnString
    else:
        db_path_to_string.restype = String
        db_path_to_string.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 112
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_path_to_vls", "cdecl"):
    db_path_to_vls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_path_to_vls", "cdecl")
    db_path_to_vls.argtypes = [POINTER(struct_bu_vls), POINTER(struct_db_full_path)]
    db_path_to_vls.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 122
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_fullpath_to_vls", "cdecl"):
    db_fullpath_to_vls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_fullpath_to_vls", "cdecl")
    db_fullpath_to_vls.argtypes = [POINTER(struct_bu_vls), POINTER(struct_db_full_path), POINTER(struct_db_i), c_int]
    db_fullpath_to_vls.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 128
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_pr_full_path", "cdecl"):
    db_pr_full_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_pr_full_path", "cdecl")
    db_pr_full_path.argtypes = [String, POINTER(struct_db_full_path)]
    db_pr_full_path.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 142
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_string_to_path", "cdecl"):
    db_string_to_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_string_to_path", "cdecl")
    db_string_to_path.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_i), String]
    db_string_to_path.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 157
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_argv_to_path", "cdecl"):
    db_argv_to_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_argv_to_path", "cdecl")
    db_argv_to_path.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_i), c_int, POINTER(POINTER(c_char))]
    db_argv_to_path.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 167
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_free_full_path", "cdecl"):
    db_free_full_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_free_full_path", "cdecl")
    db_free_full_path.argtypes = [POINTER(struct_db_full_path)]
    db_free_full_path.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 175
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_identical_full_paths", "cdecl"):
    db_identical_full_paths = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_identical_full_paths", "cdecl")
    db_identical_full_paths.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_full_path)]
    db_identical_full_paths.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 184
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_full_path_subset", "cdecl"):
    db_full_path_subset = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_full_path_subset", "cdecl")
    db_full_path_subset.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_full_path), c_int]
    db_full_path_subset.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 195
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_full_path_match_top", "cdecl"):
    db_full_path_match_top = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_full_path_match_top", "cdecl")
    db_full_path_match_top.argtypes = [POINTER(struct_db_full_path), POINTER(struct_db_full_path)]
    db_full_path_match_top.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 204
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_full_path_search", "cdecl"):
    db_full_path_search = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_full_path_search", "cdecl")
    db_full_path_search.argtypes = [POINTER(struct_db_full_path), POINTER(struct_directory)]
    db_full_path_search.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 224
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_full_path_cyclic", "cdecl"):
    db_full_path_cyclic = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_full_path_cyclic", "cdecl")
    db_full_path_cyclic.argtypes = [POINTER(struct_db_full_path), String, c_int]
    db_full_path_cyclic.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 236
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_path_to_mat", "cdecl"):
    db_path_to_mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_path_to_mat", "cdecl")
    db_path_to_mat.argtypes = [POINTER(struct_db_i), POINTER(struct_db_full_path), mat_t, c_int, POINTER(struct_resource)]
    db_path_to_mat.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 133
try:
    rt_debug = (c_uint).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "rt_debug")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/tol.h: 89
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_tol_default", "cdecl"):
    rt_tol_default = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_tol_default", "cdecl")
    rt_tol_default.argtypes = [POINTER(struct_bn_tol)]
    rt_tol_default.restype = POINTER(struct_bn_tol)

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 56
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_memalloc", "cdecl"):
    rt_memalloc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_memalloc", "cdecl")
    rt_memalloc.argtypes = [POINTER(POINTER(struct_mem_map)), c_size_t]
    rt_memalloc.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 69
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_memalloc_nosplit", "cdecl"):
    rt_memalloc_nosplit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_memalloc_nosplit", "cdecl")
    rt_memalloc_nosplit.argtypes = [POINTER(POINTER(struct_mem_map)), c_size_t]
    rt_memalloc_nosplit.restype = POINTER(struct_mem_map)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 81
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_memfree", "cdecl"):
    rt_memfree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_memfree", "cdecl")
    rt_memfree.argtypes = [POINTER(POINTER(struct_mem_map)), c_size_t, off_t]
    rt_memfree.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 89
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_mempurge", "cdecl"):
    rt_mempurge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_mempurge", "cdecl")
    rt_mempurge.argtypes = [POINTER(POINTER(struct_mem_map))]
    rt_mempurge.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 94
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_memclose", "cdecl"):
    rt_memclose = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_memclose", "cdecl")
    rt_memclose.argtypes = []
    rt_memclose.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 50
class struct_mater(Structure):
    pass

struct_mater.__slots__ = [
    'mt_low',
    'mt_high',
    'mt_r',
    'mt_g',
    'mt_b',
    'mt_daddr',
    'mt_forw',
]
struct_mater._fields_ = [
    ('mt_low', c_short),
    ('mt_high', c_short),
    ('mt_r', c_ubyte),
    ('mt_g', c_ubyte),
    ('mt_b', c_ubyte),
    ('mt_daddr', off_t),
    ('mt_forw', POINTER(struct_mater)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 63
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_region_color_map", "cdecl"):
    rt_region_color_map = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_region_color_map", "cdecl")
    rt_region_color_map.argtypes = [POINTER(struct_region)]
    rt_region_color_map.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 66
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_color_addrec", "cdecl"):
    rt_color_addrec = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_color_addrec", "cdecl")
    rt_color_addrec.argtypes = [c_int, c_int, c_int, c_int, c_int, off_t]
    rt_color_addrec.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 72
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_insert_color", "cdecl"):
    rt_insert_color = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_insert_color", "cdecl")
    rt_insert_color.argtypes = [POINTER(struct_mater)]
    rt_insert_color.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 73
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_vls_color_map", "cdecl"):
    rt_vls_color_map = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_vls_color_map", "cdecl")
    rt_vls_color_map.argtypes = [POINTER(struct_bu_vls)]
    rt_vls_color_map.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 74
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_material_head", "cdecl"):
    rt_material_head = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_material_head", "cdecl")
    rt_material_head.argtypes = []
    rt_material_head.restype = POINTER(struct_mater)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 75
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_new_material_head", "cdecl"):
    rt_new_material_head = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_new_material_head", "cdecl")
    rt_new_material_head.argtypes = [POINTER(struct_mater)]
    rt_new_material_head.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 76
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_dup_material_head", "cdecl"):
    rt_dup_material_head = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_dup_material_head", "cdecl")
    rt_dup_material_head.argtypes = []
    rt_dup_material_head.restype = POINTER(struct_mater)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 77
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_color_free", "cdecl"):
    rt_color_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_color_free", "cdecl")
    rt_color_free.argtypes = []
    rt_color_free.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 100
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_parse_1anim", "cdecl"):
    db_parse_1anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_parse_1anim", "cdecl")
    db_parse_1anim.argtypes = [POINTER(struct_db_i), c_int, POINTER(POINTER(c_char))]
    db_parse_1anim.restype = POINTER(struct_animate)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 109
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_parse_anim", "cdecl"):
    db_parse_anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_parse_anim", "cdecl")
    db_parse_anim.argtypes = [POINTER(struct_db_i), c_int, POINTER(POINTER(c_char))]
    db_parse_anim.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 123
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_add_anim", "cdecl"):
    db_add_anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_add_anim", "cdecl")
    db_add_anim.argtypes = [POINTER(struct_db_i), POINTER(struct_animate), c_int]
    db_add_anim.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 134
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_do_anim", "cdecl"):
    db_do_anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_do_anim", "cdecl")
    db_do_anim.argtypes = [POINTER(struct_animate), mat_t, mat_t, POINTER(struct_mater_info)]
    db_do_anim.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 144
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_free_anim", "cdecl"):
    db_free_anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_free_anim", "cdecl")
    db_free_anim.argtypes = [POINTER(struct_db_i)]
    db_free_anim.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 157
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_write_anim", "cdecl"):
    db_write_anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_write_anim", "cdecl")
    db_write_anim.argtypes = [POINTER(FILE), POINTER(struct_animate)]
    db_write_anim.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 166
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_parse_1anim", "cdecl"):
    db_parse_1anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_parse_1anim", "cdecl")
    db_parse_1anim.argtypes = [POINTER(struct_db_i), c_int, POINTER(POINTER(c_char))]
    db_parse_1anim.restype = POINTER(struct_animate)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 174
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_free_1anim", "cdecl"):
    db_free_1anim = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_free_1anim", "cdecl")
    db_free_1anim.argtypes = [POINTER(struct_animate)]
    db_free_1anim.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 182
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_apply_anims", "cdecl"):
    db_apply_anims = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_apply_anims", "cdecl")
    db_apply_anims.argtypes = [POINTER(struct_db_full_path), POINTER(struct_directory), mat_t, mat_t, POINTER(struct_mater_info)]
    db_apply_anims.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 62
class union_anon_59(Union):
    pass

union_anon_59.__slots__ = [
    'file_offset',
    'ptr',
]
union_anon_59._fields_ = [
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
    ('d_un', union_anon_59),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 141
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_argv_to_dpv", "cdecl"):
    db_argv_to_dpv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_argv_to_dpv", "cdecl")
    db_argv_to_dpv.argtypes = [POINTER(struct_db_i), POINTER(POINTER(c_char))]
    db_argv_to_dpv.restype = POINTER(POINTER(struct_directory))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 148
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dpv_to_argv", "cdecl"):
    db_dpv_to_argv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dpv_to_argv", "cdecl")
    db_dpv_to_argv.argtypes = [POINTER(POINTER(struct_directory))]
    db_dpv_to_argv.restype = POINTER(POINTER(c_char))

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 103
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_region", "cdecl"):
    rt_pr_region = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_region", "cdecl")
    rt_pr_region.argtypes = [POINTER(struct_region)]
    rt_pr_region.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 113
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_region_mat", "cdecl"):
    db_region_mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_region_mat", "cdecl")
    db_region_mat.argtypes = [mat_t, POINTER(struct_db_i), String, POINTER(struct_resource)]
    db_region_mat.restype = c_int

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 101
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_free_soltab", "cdecl"):
    rt_free_soltab = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_free_soltab", "cdecl")
    rt_free_soltab.argtypes = [POINTER(struct_soltab)]
    rt_free_soltab.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 104
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_soltab", "cdecl"):
    rt_pr_soltab = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_soltab", "cdecl")
    rt_pr_soltab.argtypes = [POINTER(struct_soltab)]
    rt_pr_soltab.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 57
class struct_xrays(Structure):
    pass

struct_xrays.__slots__ = [
    'l',
    'ray',
]
struct_xrays._fields_ = [
    ('l', struct_bu_list),
    ('ray', struct_xray),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 172
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_hit", "cdecl"):
    rt_pr_hit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_hit", "cdecl")
    rt_pr_hit.argtypes = [String, POINTER(struct_hit)]
    rt_pr_hit.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 174
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_hit_vls", "cdecl"):
    rt_pr_hit_vls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_hit_vls", "cdecl")
    rt_pr_hit_vls.argtypes = [POINTER(struct_bu_vls), String, POINTER(struct_hit)]
    rt_pr_hit_vls.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 177
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_hitarray_vls", "cdecl"):
    rt_pr_hitarray_vls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_hitarray_vls", "cdecl")
    rt_pr_hitarray_vls.argtypes = [POINTER(struct_bu_vls), String, POINTER(struct_hit), c_int]
    rt_pr_hitarray_vls.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/seg.h: 101
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_seg", "cdecl"):
    rt_pr_seg = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_seg", "cdecl")
    rt_pr_seg.argtypes = [POINTER(struct_seg)]
    rt_pr_seg.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/seg.h: 102
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_seg_vls", "cdecl"):
    rt_pr_seg_vls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_seg_vls", "cdecl")
    rt_pr_seg_vls.argtypes = [POINTER(struct_bu_vls), POINTER(struct_seg)]
    rt_pr_seg_vls.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 136
class struct_partition_list(Structure):
    pass

struct_partition_list.__slots__ = [
    'l',
    'ap',
    'PartHeadp',
    'segHeadp',
    'userptr',
]
struct_partition_list._fields_ = [
    ('l', struct_bu_list),
    ('ap', POINTER(struct_application)),
    ('PartHeadp', struct_partition),
    ('segHeadp', struct_seg),
    ('userptr', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 149
class struct_partition_bundle(Structure):
    pass

struct_partition_bundle.__slots__ = [
    'hits',
    'misses',
    'list',
    'ap',
]
struct_partition_bundle._fields_ = [
    ('hits', c_int),
    ('misses', c_int),
    ('list', POINTER(struct_partition_list)),
    ('ap', POINTER(struct_application)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 160
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_partition_len", "cdecl"):
    rt_partition_len = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_partition_len", "cdecl")
    rt_partition_len.argtypes = [POINTER(struct_partition)]
    rt_partition_len.restype = c_int

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/application.h: 176
class struct_application_bundle(Structure):
    pass

struct_application_bundle.__slots__ = [
    'b_magic',
    'b_rays',
    'b_ap',
    'b_hit',
    'b_miss',
    'b_user',
    'b_uptr',
    'b_return',
]
struct_application_bundle._fields_ = [
    ('b_magic', c_uint32),
    ('b_rays', struct_xrays),
    ('b_ap', struct_application),
    ('b_hit', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_application_bundle), POINTER(struct_partition_bundle))),
    ('b_miss', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_application_bundle))),
    ('b_user', c_int),
    ('b_uptr', POINTER(None)),
    ('b_return', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 43
class struct_hitmiss(Structure):
    pass

struct_hitmiss.__slots__ = [
    'l',
    'hit',
    'dist_in_plane',
    'in_out',
    'inbound_use',
    'inbound_norm',
    'outbound_use',
    'outbound_norm',
    'start_stop',
    'other',
]
struct_hitmiss._fields_ = [
    ('l', struct_bu_list),
    ('hit', struct_hit),
    ('dist_in_plane', fastf_t),
    ('in_out', c_int),
    ('inbound_use', POINTER(c_long)),
    ('inbound_norm', vect_t),
    ('outbound_use', POINTER(c_long)),
    ('outbound_norm', vect_t),
    ('start_stop', c_int),
    ('other', POINTER(struct_hitmiss)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 82
class struct_ray_data(Structure):
    pass

struct_ray_data.__slots__ = [
    'magic',
    'rd_m',
    'manifolds',
    'rd_invdir',
    'rp',
    'ap',
    'seghead',
    'stp',
    'tol',
    'hitmiss',
    'rd_hit',
    'rd_miss',
    'plane_pt',
    'ray_dist_to_plane',
    'face_subhit',
    'classifying_ray',
]
struct_ray_data._fields_ = [
    ('magic', c_uint32),
    ('rd_m', POINTER(struct_model)),
    ('manifolds', String),
    ('rd_invdir', vect_t),
    ('rp', POINTER(struct_xray)),
    ('ap', POINTER(struct_application)),
    ('seghead', POINTER(struct_seg)),
    ('stp', POINTER(struct_soltab)),
    ('tol', POINTER(struct_bn_tol)),
    ('hitmiss', POINTER(POINTER(struct_hitmiss))),
    ('rd_hit', struct_bu_list),
    ('rd_miss', struct_bu_list),
    ('plane_pt', point_t),
    ('ray_dist_to_plane', fastf_t),
    ('face_subhit', c_int),
    ('classifying_ray', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 135
try:
    nmg_plot_anim_upcall = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "nmg_plot_anim_upcall")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 139
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_nmg_print_hitlist", "cdecl"):
    rt_nmg_print_hitlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_nmg_print_hitlist", "cdecl")
    rt_nmg_print_hitlist.argtypes = [POINTER(struct_bu_list)]
    rt_nmg_print_hitlist.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 140
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_nmg_print_hitmiss", "cdecl"):
    rt_nmg_print_hitmiss = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_nmg_print_hitmiss", "cdecl")
    rt_nmg_print_hitmiss.argtypes = [POINTER(struct_hitmiss)]
    rt_nmg_print_hitmiss.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 141
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_isect_ray_model", "cdecl"):
    rt_isect_ray_model = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_isect_ray_model", "cdecl")
    rt_isect_ray_model.argtypes = [POINTER(struct_ray_data), POINTER(struct_bu_list)]
    rt_isect_ray_model.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 151
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_ray_segs", "cdecl"):
    nmg_ray_segs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_ray_segs", "cdecl")
    nmg_ray_segs.argtypes = [POINTER(struct_ray_data), POINTER(struct_bu_list)]
    nmg_ray_segs.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 153
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_to_arb", "cdecl"):
    nmg_to_arb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_to_arb", "cdecl")
    nmg_to_arb.argtypes = [POINTER(struct_model), POINTER(struct_rt_arb_internal)]
    nmg_to_arb.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 155
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_to_tgc", "cdecl"):
    nmg_to_tgc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_to_tgc", "cdecl")
    nmg_to_tgc.argtypes = [POINTER(struct_model), POINTER(struct_rt_tgc_internal), POINTER(struct_bn_tol)]
    nmg_to_tgc.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 158
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_to_poly", "cdecl"):
    nmg_to_poly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_to_poly", "cdecl")
    nmg_to_poly.argtypes = [POINTER(struct_model), POINTER(struct_rt_pg_internal), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_to_poly.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 162
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_bot", "cdecl"):
    nmg_bot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_bot", "cdecl")
    nmg_bot.argtypes = [POINTER(struct_shell), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_bot.restype = POINTER(struct_rt_bot_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 165
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mdl_to_bot", "cdecl"):
    nmg_mdl_to_bot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mdl_to_bot", "cdecl")
    nmg_mdl_to_bot.argtypes = [POINTER(struct_model), POINTER(struct_bu_list), POINTER(struct_bn_tol)]
    nmg_mdl_to_bot.restype = POINTER(struct_rt_bot_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 56
class struct_db_tree_state(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 169
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_booltree_leaf_tess", "cdecl"):
    nmg_booltree_leaf_tess = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_booltree_leaf_tess", "cdecl")
    nmg_booltree_leaf_tess.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_rt_db_internal), POINTER(None)]
    nmg_booltree_leaf_tess.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 173
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_booltree_leaf_tnurb", "cdecl"):
    nmg_booltree_leaf_tnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_booltree_leaf_tnurb", "cdecl")
    nmg_booltree_leaf_tnurb.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_rt_db_internal), POINTER(None)]
    nmg_booltree_leaf_tnurb.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 177
try:
    nmg_bool_eval_silent = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "nmg_bool_eval_silent")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 178
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_booltree_evaluate", "cdecl"):
    nmg_booltree_evaluate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_booltree_evaluate", "cdecl")
    nmg_booltree_evaluate.argtypes = [POINTER(union_tree), POINTER(struct_bu_list), POINTER(struct_bn_tol), POINTER(struct_resource)]
    nmg_booltree_evaluate.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 182
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_boolean", "cdecl"):
    nmg_boolean = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_boolean", "cdecl")
    nmg_boolean.argtypes = [POINTER(union_tree), POINTER(struct_model), POINTER(struct_bu_list), POINTER(struct_bn_tol), POINTER(struct_resource)]
    nmg_boolean.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 192
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_triangulate_model_mc", "cdecl"):
    nmg_triangulate_model_mc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_triangulate_model_mc", "cdecl")
    nmg_triangulate_model_mc.argtypes = [POINTER(struct_model), POINTER(struct_bn_tol)]
    nmg_triangulate_model_mc.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 194
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mc_realize_cube", "cdecl"):
    nmg_mc_realize_cube = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mc_realize_cube", "cdecl")
    nmg_mc_realize_cube.argtypes = [POINTER(struct_shell), c_int, POINTER(point_t), POINTER(struct_bn_tol)]
    nmg_mc_realize_cube.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 198
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_mc_evaluate", "cdecl"):
    nmg_mc_evaluate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_mc_evaluate", "cdecl")
    nmg_mc_evaluate.argtypes = [POINTER(struct_shell), POINTER(struct_rt_i), POINTER(struct_db_full_path), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    nmg_mc_evaluate.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 206
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("nmg_stash_model_to_file", "cdecl"):
    nmg_stash_model_to_file = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("nmg_stash_model_to_file", "cdecl")
    nmg_stash_model_to_file.argtypes = [String, POINTER(struct_model), String]
    nmg_stash_model_to_file.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 110
try:
    rt_initial_tree_state = (struct_db_tree_state).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "rt_initial_tree_state")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 115
class struct_db_traverse(Structure):
    pass

struct_db_traverse.__slots__ = [
    'magic',
    'dbip',
    'comb_enter_func',
    'comb_exit_func',
    'leaf_func',
    'resp',
    'client_data',
]
struct_db_traverse._fields_ = [
    ('magic', c_uint32),
    ('dbip', POINTER(struct_db_i)),
    ('comb_enter_func', CFUNCTYPE(UNCHECKED(None), POINTER(struct_db_i), POINTER(struct_directory), POINTER(None))),
    ('comb_exit_func', CFUNCTYPE(UNCHECKED(None), POINTER(struct_db_i), POINTER(struct_directory), POINTER(None))),
    ('leaf_func', CFUNCTYPE(UNCHECKED(None), POINTER(struct_db_i), POINTER(struct_directory), POINTER(None))),
    ('resp', POINTER(struct_resource)),
    ('client_data', POINTER(None)),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 227
class struct_rt_tree_array(Structure):
    pass

struct_rt_tree_array.__slots__ = [
    'tl_tree',
    'tl_op',
]
struct_rt_tree_array._fields_ = [
    ('tl_tree', POINTER(union_tree)),
    ('tl_op', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 279
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_tree", "cdecl"):
    rt_pr_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_tree", "cdecl")
    rt_pr_tree.argtypes = [POINTER(union_tree), c_int]
    rt_pr_tree.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 281
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_tree_vls", "cdecl"):
    rt_pr_tree_vls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_tree_vls", "cdecl")
    rt_pr_tree_vls.argtypes = [POINTER(struct_bu_vls), POINTER(union_tree)]
    rt_pr_tree_vls.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 283
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_tree_str", "cdecl"):
    rt_pr_tree_str = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_tree_str", "cdecl")
    rt_pr_tree_str.argtypes = [POINTER(union_tree)]
    if sizeof(c_int) == sizeof(c_void_p):
        rt_pr_tree_str.restype = ReturnString
    else:
        rt_pr_tree_str.restype = String
        rt_pr_tree_str.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 286
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_tree_val", "cdecl"):
    rt_pr_tree_val = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_tree_val", "cdecl")
    rt_pr_tree_val.argtypes = [POINTER(union_tree), POINTER(struct_partition), c_int, c_int]
    rt_pr_tree_val.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 295
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dup_db_tree_state", "cdecl"):
    db_dup_db_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dup_db_tree_state", "cdecl")
    db_dup_db_tree_state.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_tree_state)]
    db_dup_db_tree_state.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 302
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_free_db_tree_state", "cdecl"):
    db_free_db_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_free_db_tree_state", "cdecl")
    db_free_db_tree_state.argtypes = [POINTER(struct_db_tree_state)]
    db_free_db_tree_state.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 309
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_init_db_tree_state", "cdecl"):
    db_init_db_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_init_db_tree_state", "cdecl")
    db_init_db_tree_state.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_i), POINTER(struct_resource)]
    db_init_db_tree_state.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 312
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_new_combined_tree_state", "cdecl"):
    db_new_combined_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_new_combined_tree_state", "cdecl")
    db_new_combined_tree_state.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path)]
    db_new_combined_tree_state.restype = POINTER(struct_combined_tree_state)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 314
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dup_combined_tree_state", "cdecl"):
    db_dup_combined_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dup_combined_tree_state", "cdecl")
    db_dup_combined_tree_state.argtypes = [POINTER(struct_combined_tree_state)]
    db_dup_combined_tree_state.restype = POINTER(struct_combined_tree_state)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 315
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_free_combined_tree_state", "cdecl"):
    db_free_combined_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_free_combined_tree_state", "cdecl")
    db_free_combined_tree_state.argtypes = [POINTER(struct_combined_tree_state)]
    db_free_combined_tree_state.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 316
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_pr_tree_state", "cdecl"):
    db_pr_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_pr_tree_state", "cdecl")
    db_pr_tree_state.argtypes = [POINTER(struct_db_tree_state)]
    db_pr_tree_state.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 317
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_pr_combined_tree_state", "cdecl"):
    db_pr_combined_tree_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_pr_combined_tree_state", "cdecl")
    db_pr_combined_tree_state.argtypes = [POINTER(struct_combined_tree_state)]
    db_pr_combined_tree_state.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 329
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_apply_state_from_comb", "cdecl"):
    db_apply_state_from_comb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_apply_state_from_comb", "cdecl")
    db_apply_state_from_comb.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_rt_comb_internal)]
    db_apply_state_from_comb.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 341
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_apply_state_from_memb", "cdecl"):
    db_apply_state_from_memb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_apply_state_from_memb", "cdecl")
    db_apply_state_from_memb.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(union_tree)]
    db_apply_state_from_memb.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 351
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_apply_state_from_one_member", "cdecl"):
    db_apply_state_from_one_member = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_apply_state_from_one_member", "cdecl")
    db_apply_state_from_one_member.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), String, c_int, POINTER(union_tree)]
    db_apply_state_from_one_member.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 364
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_find_named_leaf", "cdecl"):
    db_find_named_leaf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_find_named_leaf", "cdecl")
    db_find_named_leaf.argtypes = [POINTER(union_tree), String]
    db_find_named_leaf.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 376
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_find_named_leafs_parent", "cdecl"):
    db_find_named_leafs_parent = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_find_named_leafs_parent", "cdecl")
    db_find_named_leafs_parent.argtypes = [POINTER(c_int), POINTER(union_tree), String]
    db_find_named_leafs_parent.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 379
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_del_lhs", "cdecl"):
    db_tree_del_lhs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_del_lhs", "cdecl")
    db_tree_del_lhs.argtypes = [POINTER(union_tree), POINTER(struct_resource)]
    db_tree_del_lhs.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 381
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_del_rhs", "cdecl"):
    db_tree_del_rhs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_del_rhs", "cdecl")
    db_tree_del_rhs.argtypes = [POINTER(union_tree), POINTER(struct_resource)]
    db_tree_del_rhs.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 404
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_del_dbleaf", "cdecl"):
    db_tree_del_dbleaf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_del_dbleaf", "cdecl")
    db_tree_del_dbleaf.argtypes = [POINTER(POINTER(union_tree)), String, POINTER(struct_resource), c_int]
    db_tree_del_dbleaf.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 413
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_mul_dbleaf", "cdecl"):
    db_tree_mul_dbleaf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_mul_dbleaf", "cdecl")
    db_tree_mul_dbleaf.argtypes = [POINTER(union_tree), mat_t]
    db_tree_mul_dbleaf.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 423
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_funcleaf", "cdecl"):
    db_tree_funcleaf = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_funcleaf", "cdecl")
    db_tree_funcleaf.argtypes = [POINTER(struct_db_i), POINTER(struct_rt_comb_internal), POINTER(union_tree), CFUNCTYPE(UNCHECKED(None), POINTER(struct_db_i), POINTER(struct_rt_comb_internal), POINTER(union_tree), POINTER(None), POINTER(None), POINTER(None), POINTER(None)), POINTER(None), POINTER(None), POINTER(None), POINTER(None)]
    db_tree_funcleaf.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 452
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_follow_path", "cdecl"):
    db_follow_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_follow_path", "cdecl")
    db_follow_path.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_db_full_path), c_int, c_long]
    db_follow_path.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 468
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_follow_path_for_state", "cdecl"):
    db_follow_path_for_state = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_follow_path_for_state", "cdecl")
    db_follow_path_for_state.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), String, c_int]
    db_follow_path_for_state.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 479
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_recurse", "cdecl"):
    db_recurse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_recurse", "cdecl")
    db_recurse.argtypes = [POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(POINTER(struct_combined_tree_state)), POINTER(None)]
    db_recurse.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 483
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dup_subtree", "cdecl"):
    db_dup_subtree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dup_subtree", "cdecl")
    db_dup_subtree.argtypes = [POINTER(union_tree), POINTER(struct_resource)]
    db_dup_subtree.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 485
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_ck_tree", "cdecl"):
    db_ck_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_ck_tree", "cdecl")
    db_ck_tree.argtypes = [POINTER(union_tree)]
    db_ck_tree.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 492
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_free_tree", "cdecl"):
    db_free_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_free_tree", "cdecl")
    db_free_tree.argtypes = [POINTER(union_tree), POINTER(struct_resource)]
    db_free_tree.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 501
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_left_hvy_node", "cdecl"):
    db_left_hvy_node = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_left_hvy_node", "cdecl")
    db_left_hvy_node.argtypes = [POINTER(union_tree)]
    db_left_hvy_node.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 510
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_non_union_push", "cdecl"):
    db_non_union_push = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_non_union_push", "cdecl")
    db_non_union_push.argtypes = [POINTER(union_tree), POINTER(struct_resource)]
    db_non_union_push.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 517
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_count_tree_nodes", "cdecl"):
    db_count_tree_nodes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_count_tree_nodes", "cdecl")
    db_count_tree_nodes.argtypes = [POINTER(union_tree), c_int]
    db_count_tree_nodes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 526
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_is_tree_all_unions", "cdecl"):
    db_is_tree_all_unions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_is_tree_all_unions", "cdecl")
    db_is_tree_all_unions.argtypes = [POINTER(union_tree)]
    db_is_tree_all_unions.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 527
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_count_subtree_regions", "cdecl"):
    db_count_subtree_regions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_count_subtree_regions", "cdecl")
    db_count_subtree_regions.argtypes = [POINTER(union_tree)]
    db_count_subtree_regions.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 528
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tally_subtree_regions", "cdecl"):
    db_tally_subtree_regions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tally_subtree_regions", "cdecl")
    db_tally_subtree_regions.argtypes = [POINTER(union_tree), POINTER(POINTER(union_tree)), c_int, c_int, POINTER(struct_resource)]
    db_tally_subtree_regions.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 586
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_walk_tree", "cdecl"):
    db_walk_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_walk_tree", "cdecl")
    db_walk_tree.argtypes = [POINTER(struct_db_i), c_int, POINTER(POINTER(c_char)), c_int, POINTER(struct_db_tree_state), CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_rt_comb_internal), POINTER(None)), CFUNCTYPE(UNCHECKED(POINTER(union_tree)), POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(union_tree), POINTER(None)), CFUNCTYPE(UNCHECKED(POINTER(union_tree)), POINTER(struct_db_tree_state), POINTER(struct_db_full_path), POINTER(struct_rt_db_internal), POINTER(None)), POINTER(None)]
    db_walk_tree.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 629
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_list", "cdecl"):
    db_tree_list = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_list", "cdecl")
    db_tree_list.argtypes = [POINTER(struct_bu_vls), POINTER(union_tree)]
    db_tree_list.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 635
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_parse", "cdecl"):
    db_tree_parse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_parse", "cdecl")
    db_tree_parse.argtypes = [POINTER(struct_bu_vls), String, POINTER(struct_resource)]
    db_tree_parse.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 644
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_functree", "cdecl"):
    db_functree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_functree", "cdecl")
    db_functree.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), CFUNCTYPE(UNCHECKED(None), POINTER(struct_db_i), POINTER(struct_directory), POINTER(None)), CFUNCTYPE(UNCHECKED(None), POINTER(struct_db_i), POINTER(struct_directory), POINTER(None)), POINTER(struct_resource), POINTER(None)]
    db_functree.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 671
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bound_tree", "cdecl"):
    rt_bound_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bound_tree", "cdecl")
    rt_bound_tree.argtypes = [POINTER(union_tree), vect_t, vect_t]
    rt_bound_tree.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 687
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_tree_elim_nops", "cdecl"):
    rt_tree_elim_nops = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_tree_elim_nops", "cdecl")
    rt_tree_elim_nops.argtypes = [POINTER(union_tree), POINTER(struct_resource)]
    rt_tree_elim_nops.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 693
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_nleaves", "cdecl"):
    db_tree_nleaves = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_nleaves", "cdecl")
    db_tree_nleaves.argtypes = [POINTER(union_tree)]
    db_tree_nleaves.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 709
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_flatten_tree", "cdecl"):
    db_flatten_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_flatten_tree", "cdecl")
    db_flatten_tree.argtypes = [POINTER(struct_rt_tree_array), POINTER(union_tree), c_int, c_int, POINTER(struct_resource)]
    db_flatten_tree.restype = POINTER(struct_rt_tree_array)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 716
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_flatten_describe", "cdecl"):
    db_tree_flatten_describe = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_flatten_describe", "cdecl")
    db_tree_flatten_describe.argtypes = [POINTER(struct_bu_vls), POINTER(union_tree), c_int, c_int, c_double, POINTER(struct_resource)]
    db_tree_flatten_describe.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 723
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_tree_describe", "cdecl"):
    db_tree_describe = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_tree_describe", "cdecl")
    db_tree_describe.argtypes = [POINTER(struct_bu_vls), POINTER(union_tree), c_int, c_int, c_double]
    db_tree_describe.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 738
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_ck_left_heavy_tree", "cdecl"):
    db_ck_left_heavy_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_ck_left_heavy_tree", "cdecl")
    db_ck_left_heavy_tree.argtypes = [POINTER(union_tree), c_int]
    db_ck_left_heavy_tree.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 755
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_ck_v4gift_tree", "cdecl"):
    db_ck_v4gift_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_ck_v4gift_tree", "cdecl")
    db_ck_v4gift_tree.argtypes = [POINTER(union_tree)]
    db_ck_v4gift_tree.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 764
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_mkbool_tree", "cdecl"):
    db_mkbool_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_mkbool_tree", "cdecl")
    db_mkbool_tree.argtypes = [POINTER(struct_rt_tree_array), c_size_t, POINTER(struct_resource)]
    db_mkbool_tree.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 768
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_mkgift_tree", "cdecl"):
    db_mkgift_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_mkgift_tree", "cdecl")
    db_mkgift_tree.argtypes = [POINTER(struct_rt_tree_array), c_size_t, POINTER(struct_resource)]
    db_mkgift_tree.restype = POINTER(union_tree)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 773
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_optim_tree", "cdecl"):
    rt_optim_tree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_optim_tree", "cdecl")
    rt_optim_tree.argtypes = [POINTER(union_tree), POINTER(struct_resource)]
    rt_optim_tree.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 109
try:
    rt_uniresource = (struct_resource).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "rt_uniresource")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 119
try:
    RT_SEM_WORKER = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RT_SEM_WORKER")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 120
try:
    RT_SEM_MODEL = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RT_SEM_MODEL")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 121
try:
    RT_SEM_RESULTS = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RT_SEM_RESULTS")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 122
try:
    RT_SEM_TREE0 = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RT_SEM_TREE0")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 123
try:
    RT_SEM_TREE1 = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RT_SEM_TREE1")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 124
try:
    RT_SEM_TREE2 = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RT_SEM_TREE2")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 125
try:
    RT_SEM_TREE3 = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RT_SEM_TREE3")
except:
    pass

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 73
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_get_internal", "cdecl"):
    rt_db_get_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_get_internal", "cdecl")
    rt_db_get_internal.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_directory), POINTER(struct_db_i), mat_t, POINTER(struct_resource)]
    rt_db_get_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 88
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_put_internal", "cdecl"):
    rt_db_put_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_put_internal", "cdecl")
    rt_db_put_internal.argtypes = [POINTER(struct_directory), POINTER(struct_db_i), POINTER(struct_rt_db_internal), POINTER(struct_resource)]
    rt_db_put_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 106
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_fwrite_internal", "cdecl"):
    rt_fwrite_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_fwrite_internal", "cdecl")
    rt_fwrite_internal.argtypes = [POINTER(FILE), String, POINTER(struct_rt_db_internal), c_double]
    rt_fwrite_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 110
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_free_internal", "cdecl"):
    rt_db_free_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_free_internal", "cdecl")
    rt_db_free_internal.argtypes = [POINTER(struct_rt_db_internal)]
    rt_db_free_internal.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 120
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_lookup_internal", "cdecl"):
    rt_db_lookup_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_lookup_internal", "cdecl")
    rt_db_lookup_internal.argtypes = [POINTER(struct_db_i), String, POINTER(POINTER(struct_directory)), POINTER(struct_rt_db_internal), c_int, POINTER(struct_resource)]
    rt_db_lookup_internal.restype = c_int

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 85
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_cut", "cdecl"):
    rt_pr_cut = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_cut", "cdecl")
    rt_pr_cut.argtypes = [POINTER(union_cutter), c_int]
    rt_pr_cut.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 91
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_cut_info", "cdecl"):
    rt_pr_cut_info = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_cut_info", "cdecl")
    rt_pr_cut_info.argtypes = [POINTER(struct_rt_i), String]
    rt_pr_cut_info.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 93
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("remove_from_bsp", "cdecl"):
    remove_from_bsp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("remove_from_bsp", "cdecl")
    remove_from_bsp.argtypes = [POINTER(struct_soltab), POINTER(union_cutter), POINTER(struct_bn_tol)]
    remove_from_bsp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 96
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("insert_in_bsp", "cdecl"):
    insert_in_bsp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("insert_in_bsp", "cdecl")
    insert_in_bsp.argtypes = [POINTER(struct_soltab), POINTER(union_cutter)]
    insert_in_bsp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 98
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("fill_out_bsp", "cdecl"):
    fill_out_bsp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("fill_out_bsp", "cdecl")
    fill_out_bsp.argtypes = [POINTER(struct_rt_i), POINTER(union_cutter), POINTER(struct_resource), fastf_t * int(6)]
    fill_out_bsp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 103
class struct_bvh_build_node(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 104
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("hlbvh_create", "cdecl"):
    hlbvh_create = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("hlbvh_create", "cdecl")
    hlbvh_create.argtypes = [c_long, POINTER(struct_bu_pool), POINTER(fastf_t), POINTER(fastf_t), POINTER(c_long), c_long, POINTER(POINTER(c_long))]
    hlbvh_create.restype = POINTER(struct_bvh_build_node)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 117
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_cut_extend", "cdecl"):
    rt_cut_extend = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_cut_extend", "cdecl")
    rt_cut_extend.argtypes = [POINTER(union_cutter), POINTER(struct_soltab), POINTER(struct_rt_i)]
    rt_cut_extend.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 126
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_cell_n_on_ray", "cdecl"):
    rt_cell_n_on_ray = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_cell_n_on_ray", "cdecl")
    rt_cell_n_on_ray.argtypes = [POINTER(struct_application), c_int]
    rt_cell_n_on_ray.restype = POINTER(union_cutter)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 134
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_cut_clean", "cdecl"):
    rt_cut_clean = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_cut_clean", "cdecl")
    rt_cut_clean.argtypes = [POINTER(struct_rt_i)]
    rt_cut_clean.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/nongeom.h: 107
class union_anon_60(Union):
    pass

union_anon_60.__slots__ = [
    'flt',
    'dbl',
    'int8',
    'int16',
    'int32',
    'int64',
    'uint8',
    'uint16',
    'uint32',
    'uint64',
]
union_anon_60._fields_ = [
    ('flt', POINTER(c_float)),
    ('dbl', POINTER(c_double)),
    ('int8', String),
    ('int16', POINTER(c_short)),
    ('int32', POINTER(c_int)),
    ('int64', POINTER(c_long)),
    ('uint8', POINTER(c_ubyte)),
    ('uint16', POINTER(c_ushort)),
    ('uint32', POINTER(c_uint)),
    ('uint64', POINTER(c_ulong)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/nongeom.h: 103
class struct_rt_binunif_internal(Structure):
    pass

struct_rt_binunif_internal.__slots__ = [
    'magic',
    'type',
    'count',
    'u',
]
struct_rt_binunif_internal._fields_ = [
    ('magic', c_uint32),
    ('type', c_int),
    ('count', c_size_t),
    ('u', union_anon_60),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/nongeom.h: 127
class struct_rt_constraint_internal(Structure):
    pass

struct_rt_constraint_internal.__slots__ = [
    'magic',
    'id',
    'type',
    'expression',
]
struct_rt_constraint_internal._fields_ = [
    ('magic', c_uint32),
    ('id', c_int),
    ('type', c_int),
    ('expression', struct_bu_vls),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 92
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_fopen", "cdecl"):
    wdb_fopen = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_fopen", "cdecl")
    wdb_fopen.argtypes = [String]
    wdb_fopen.restype = POINTER(struct_rt_wdb)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 104
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_fopen_v", "cdecl"):
    wdb_fopen_v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_fopen_v", "cdecl")
    wdb_fopen_v.argtypes = [String, c_int]
    wdb_fopen_v.restype = POINTER(struct_rt_wdb)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 117
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_dbopen", "cdecl"):
    wdb_dbopen = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_dbopen", "cdecl")
    wdb_dbopen.argtypes = [POINTER(struct_db_i), c_int]
    wdb_dbopen.restype = POINTER(struct_rt_wdb)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 131
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_import", "cdecl"):
    wdb_import = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_import", "cdecl")
    wdb_import.argtypes = [POINTER(struct_rt_wdb), POINTER(struct_rt_db_internal), String, mat_t]
    wdb_import.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 144
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_export_external", "cdecl"):
    wdb_export_external = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_export_external", "cdecl")
    wdb_export_external.argtypes = [POINTER(struct_rt_wdb), POINTER(struct_bu_external), String, c_int, c_ubyte]
    wdb_export_external.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 166
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_put_internal", "cdecl"):
    wdb_put_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_put_internal", "cdecl")
    wdb_put_internal.argtypes = [POINTER(struct_rt_wdb), String, POINTER(struct_rt_db_internal), c_double]
    wdb_put_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 190
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_export", "cdecl"):
    wdb_export = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_export", "cdecl")
    wdb_export.argtypes = [POINTER(struct_rt_wdb), String, POINTER(None), c_int, c_double]
    wdb_export.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 195
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_init", "cdecl"):
    wdb_init = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_init", "cdecl")
    wdb_init.argtypes = [POINTER(struct_rt_wdb), POINTER(struct_db_i), c_int]
    wdb_init.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 204
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_close", "cdecl"):
    wdb_close = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_close", "cdecl")
    wdb_close.argtypes = [POINTER(struct_rt_wdb)]
    wdb_close.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 215
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_import_from_path", "cdecl"):
    wdb_import_from_path = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_import_from_path", "cdecl")
    wdb_import_from_path.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), String, POINTER(struct_rt_wdb)]
    wdb_import_from_path.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 231
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("wdb_import_from_path2", "cdecl"):
    wdb_import_from_path2 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("wdb_import_from_path2", "cdecl")
    wdb_import_from_path2.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), String, POINTER(struct_rt_wdb), matp_t]
    wdb_import_from_path2.restype = c_int

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/global.h: 39
class struct_rt_g(Structure):
    pass

struct_rt_g.__slots__ = [
    'rtg_parallel',
    'rtg_vlfree',
    'rtg_headwdb',
]
struct_rt_g._fields_ = [
    ('rtg_parallel', c_int8),
    ('rtg_vlfree', struct_bu_list),
    ('rtg_headwdb', struct_rt_wdb),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/global.h: 50
try:
    RTG = (struct_rt_g).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "RTG")
except:
    pass

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 157
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_new_rti", "cdecl"):
    rt_new_rti = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_new_rti", "cdecl")
    rt_new_rti.argtypes = [POINTER(struct_db_i)]
    rt_new_rti.restype = POINTER(struct_rt_i)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 158
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_free_rti", "cdecl"):
    rt_free_rti = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_free_rti", "cdecl")
    rt_free_rti.argtypes = [POINTER(struct_rt_i)]
    rt_free_rti.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 159
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_prep", "cdecl"):
    rt_prep = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_prep", "cdecl")
    rt_prep.argtypes = [POINTER(struct_rt_i)]
    rt_prep.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 160
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_prep_parallel", "cdecl"):
    rt_prep_parallel = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_prep_parallel", "cdecl")
    rt_prep_parallel.argtypes = [POINTER(struct_rt_i), c_int]
    rt_prep_parallel.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 176
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gettree", "cdecl"):
    rt_gettree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gettree", "cdecl")
    rt_gettree.argtypes = [POINTER(struct_rt_i), String]
    rt_gettree.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 178
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gettrees", "cdecl"):
    rt_gettrees = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gettrees", "cdecl")
    rt_gettrees.argtypes = [POINTER(struct_rt_i), c_int, POINTER(POINTER(c_char)), c_int]
    rt_gettrees.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 200
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gettrees_and_attrs", "cdecl"):
    rt_gettrees_and_attrs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gettrees_and_attrs", "cdecl")
    rt_gettrees_and_attrs.argtypes = [POINTER(struct_rt_i), POINTER(POINTER(c_char)), c_int, POINTER(POINTER(c_char)), c_int]
    rt_gettrees_and_attrs.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 237
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gettrees_muves", "cdecl"):
    rt_gettrees_muves = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gettrees_muves", "cdecl")
    rt_gettrees_muves.argtypes = [POINTER(struct_rt_i), POINTER(POINTER(c_char)), c_int, POINTER(POINTER(c_char)), c_int]
    rt_gettrees_muves.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 243
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_load_attrs", "cdecl"):
    rt_load_attrs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_load_attrs", "cdecl")
    rt_load_attrs.argtypes = [POINTER(struct_rt_i), POINTER(POINTER(c_char))]
    rt_load_attrs.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 248
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_partitions", "cdecl"):
    rt_pr_partitions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_partitions", "cdecl")
    rt_pr_partitions.argtypes = [POINTER(struct_rt_i), POINTER(struct_partition), String]
    rt_pr_partitions.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 260
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_find_solid", "cdecl"):
    rt_find_solid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_find_solid", "cdecl")
    rt_find_solid.argtypes = [POINTER(struct_rt_i), String]
    rt_find_solid.restype = POINTER(struct_soltab)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 279
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_init_resource", "cdecl"):
    rt_init_resource = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_init_resource", "cdecl")
    rt_init_resource.argtypes = [POINTER(struct_resource), c_int, POINTER(struct_rt_i)]
    rt_init_resource.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 282
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_clean_resource", "cdecl"):
    rt_clean_resource = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_clean_resource", "cdecl")
    rt_clean_resource.argtypes = [POINTER(struct_rt_i), POINTER(struct_resource)]
    rt_clean_resource.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 284
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_clean_resource_complete", "cdecl"):
    rt_clean_resource_complete = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_clean_resource_complete", "cdecl")
    rt_clean_resource_complete.argtypes = [POINTER(struct_rt_i), POINTER(struct_resource)]
    rt_clean_resource_complete.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 289
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_plot_solid", "cdecl"):
    rt_plot_solid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_plot_solid", "cdecl")
    rt_plot_solid.argtypes = [POINTER(FILE), POINTER(struct_rt_i), POINTER(struct_soltab), POINTER(struct_resource)]
    rt_plot_solid.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 296
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_clean", "cdecl"):
    rt_clean = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_clean", "cdecl")
    rt_clean.argtypes = [POINTER(struct_rt_i)]
    rt_clean.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 297
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_del_regtree", "cdecl"):
    rt_del_regtree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_del_regtree", "cdecl")
    rt_del_regtree.argtypes = [POINTER(struct_rt_i), POINTER(struct_region), POINTER(struct_resource)]
    rt_del_regtree.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 301
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_ck", "cdecl"):
    rt_ck = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_ck", "cdecl")
    rt_ck.argtypes = [POINTER(struct_rt_i)]
    rt_ck.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 304
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_tree_val", "cdecl"):
    rt_pr_tree_val = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_tree_val", "cdecl")
    rt_pr_tree_val.argtypes = [POINTER(union_tree), POINTER(struct_partition), c_int, c_int]
    rt_pr_tree_val.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 308
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_partition", "cdecl"):
    rt_pr_partition = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_partition", "cdecl")
    rt_pr_partition.argtypes = [POINTER(struct_rt_i), POINTER(struct_partition)]
    rt_pr_partition.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 310
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_partition_vls", "cdecl"):
    rt_pr_partition_vls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_partition_vls", "cdecl")
    rt_pr_partition_vls.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_i), POINTER(struct_partition)]
    rt_pr_partition_vls.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 324
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_cut_it", "cdecl"):
    rt_cut_it = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_cut_it", "cdecl")
    rt_cut_it.argtypes = [POINTER(struct_rt_i), c_int]
    rt_cut_it.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 333
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_fr_cut", "cdecl"):
    rt_fr_cut = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_fr_cut", "cdecl")
    rt_fr_cut.argtypes = [POINTER(struct_rt_i), POINTER(union_cutter)]
    rt_fr_cut.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 343
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_regionfix", "cdecl"):
    rt_regionfix = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_regionfix", "cdecl")
    rt_regionfix.argtypes = [POINTER(struct_rt_i)]
    rt_regionfix.restype = None

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 104
class struct_rt_object_selections(Structure):
    pass

struct_rt_object_selections.__slots__ = [
    'sets',
]
struct_rt_object_selections._fields_ = [
    ('sets', POINTER(struct_bu_hash_tbl)),
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
class union_anon_61(Union):
    pass

union_anon_61.__slots__ = [
    'tran',
]
union_anon_61._fields_ = [
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
    ('parameters', union_anon_61),
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 270
try:
    OBJ = (POINTER(struct_rt_functab)).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "OBJ")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 274
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_get_functab_by_label", "cdecl"):
    rt_get_functab_by_label = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_get_functab_by_label", "cdecl")
    rt_get_functab_by_label.argtypes = [String]
    rt_get_functab_by_label.restype = POINTER(struct_rt_functab)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 63
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_prep", "cdecl"):
    rt_obj_prep = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_prep", "cdecl")
    rt_obj_prep.argtypes = [POINTER(struct_soltab), POINTER(struct_rt_db_internal), POINTER(struct_rt_i)]
    rt_obj_prep.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 68
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_shot", "cdecl"):
    rt_obj_shot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_shot", "cdecl")
    rt_obj_shot.argtypes = [POINTER(struct_soltab), POINTER(struct_xray), POINTER(struct_application), POINTER(struct_seg)]
    rt_obj_shot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 73
for _lib in _libs.values():
    if not _lib.has("rt_obj_piece_shot", "cdecl"):
        continue
    rt_obj_piece_shot = _lib.get("rt_obj_piece_shot", "cdecl")
    rt_obj_piece_shot.argtypes = [POINTER(struct_rt_piecestate), POINTER(struct_rt_piecelist), c_double, POINTER(struct_xray), POINTER(struct_application), POINTER(struct_seg)]
    rt_obj_piece_shot.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 78
for _lib in _libs.values():
    if not _lib.has("rt_obj_piece_hitsegs", "cdecl"):
        continue
    rt_obj_piece_hitsegs = _lib.get("rt_obj_piece_hitsegs", "cdecl")
    rt_obj_piece_hitsegs.argtypes = [POINTER(struct_rt_piecestate), POINTER(struct_seg), POINTER(struct_application)]
    rt_obj_piece_hitsegs.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 83
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_print", "cdecl"):
    rt_obj_print = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_print", "cdecl")
    rt_obj_print.argtypes = [POINTER(struct_soltab)]
    rt_obj_print.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 88
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_norm", "cdecl"):
    rt_obj_norm = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_norm", "cdecl")
    rt_obj_norm.argtypes = [POINTER(struct_hit), POINTER(struct_soltab), POINTER(struct_xray)]
    rt_obj_norm.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 93
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_uv", "cdecl"):
    rt_obj_uv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_uv", "cdecl")
    rt_obj_uv.argtypes = [POINTER(struct_application), POINTER(struct_soltab), POINTER(struct_hit), POINTER(struct_uvcoord)]
    rt_obj_uv.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 98
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_curve", "cdecl"):
    rt_obj_curve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_curve", "cdecl")
    rt_obj_curve.argtypes = [POINTER(struct_curvature), POINTER(struct_hit), POINTER(struct_soltab)]
    rt_obj_curve.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 103
for _lib in _libs.values():
    if not _lib.has("rt_obj_class", "cdecl"):
        continue
    rt_obj_class = _lib.get("rt_obj_class", "cdecl")
    rt_obj_class.argtypes = []
    rt_obj_class.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 108
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_free", "cdecl"):
    rt_obj_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_free", "cdecl")
    rt_obj_free.argtypes = [POINTER(struct_soltab)]
    rt_obj_free.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 113
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_plot", "cdecl"):
    rt_obj_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_plot", "cdecl")
    rt_obj_plot.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_obj_plot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 118
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_vshot", "cdecl"):
    rt_obj_vshot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_vshot", "cdecl")
    rt_obj_vshot.argtypes = [POINTER(POINTER(struct_soltab)), POINTER(POINTER(struct_xray)), POINTER(struct_seg), c_int, POINTER(struct_application)]
    rt_obj_vshot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 123
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_tess", "cdecl"):
    rt_obj_tess = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_tess", "cdecl")
    rt_obj_tess.argtypes = [POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_obj_tess.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 128
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_tnurb", "cdecl"):
    rt_obj_tnurb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_tnurb", "cdecl")
    rt_obj_tnurb.argtypes = [POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bn_tol)]
    rt_obj_tnurb.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 133
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_import", "cdecl"):
    rt_obj_import = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_import", "cdecl")
    rt_obj_import.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_bu_external), mat_t, POINTER(struct_db_i), POINTER(struct_resource)]
    rt_obj_import.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 138
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_export", "cdecl"):
    rt_obj_export = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_export", "cdecl")
    rt_obj_export.argtypes = [POINTER(struct_bu_external), POINTER(struct_rt_db_internal), c_double, POINTER(struct_db_i), POINTER(struct_resource)]
    rt_obj_export.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 143
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_ifree", "cdecl"):
    rt_obj_ifree = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_ifree", "cdecl")
    rt_obj_ifree.argtypes = [POINTER(struct_rt_db_internal)]
    rt_obj_ifree.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 148
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_get", "cdecl"):
    rt_obj_get = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_get", "cdecl")
    rt_obj_get.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), String]
    rt_obj_get.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 153
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_adjust", "cdecl"):
    rt_obj_adjust = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_adjust", "cdecl")
    rt_obj_adjust.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int, POINTER(POINTER(c_char))]
    rt_obj_adjust.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 158
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_describe", "cdecl"):
    rt_obj_describe = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_describe", "cdecl")
    rt_obj_describe.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int, c_double]
    rt_obj_describe.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 163
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_make", "cdecl"):
    rt_obj_make = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_make", "cdecl")
    rt_obj_make.argtypes = [POINTER(struct_rt_functab), POINTER(struct_rt_db_internal)]
    rt_obj_make.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 168
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_xform", "cdecl"):
    rt_obj_xform = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_xform", "cdecl")
    rt_obj_xform.argtypes = [POINTER(struct_rt_db_internal), mat_t, POINTER(struct_rt_db_internal), c_int, POINTER(struct_db_i)]
    rt_obj_xform.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 173
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_params", "cdecl"):
    rt_obj_params = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_params", "cdecl")
    rt_obj_params.argtypes = [POINTER(struct_pc_pc_set), POINTER(struct_rt_db_internal)]
    rt_obj_params.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 178
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_mirror", "cdecl"):
    rt_obj_mirror = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_mirror", "cdecl")
    rt_obj_mirror.argtypes = [POINTER(struct_rt_db_internal), POINTER(plane_t)]
    rt_obj_mirror.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/func.h: 183
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_obj_prep_serialize", "cdecl"):
    rt_obj_prep_serialize = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_obj_prep_serialize", "cdecl")
    rt_obj_prep_serialize.argtypes = [POINTER(struct_soltab), POINTER(struct_rt_db_internal), POINTER(struct_bu_external), POINTER(c_size_t)]
    rt_obj_prep_serialize.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/private.h: 42
class struct_rt_pnt_node(Structure):
    pass

struct_rt_pnt_node.__slots__ = [
    'p',
    'next',
]
struct_rt_pnt_node._fields_ = [
    ('p', point_t),
    ('next', POINTER(struct_rt_pnt_node)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/private.h: 51
class struct_rt_shootray_status(Structure):
    pass

struct_rt_shootray_status.__slots__ = [
    'dist_corr',
    'odist_corr',
    'box_start',
    'obox_start',
    'box_end',
    'obox_end',
    'model_start',
    'model_end',
    'newray',
    'ap',
    'resp',
    'inv_dir',
    'abs_inv_dir',
    'rstep',
    'lastcut',
    'lastcell',
    'curcut',
    'curmin',
    'curmax',
    'igrid',
    'tv',
    'out_axis',
    'old_status',
    'box_num',
]
struct_rt_shootray_status._fields_ = [
    ('dist_corr', fastf_t),
    ('odist_corr', fastf_t),
    ('box_start', fastf_t),
    ('obox_start', fastf_t),
    ('box_end', fastf_t),
    ('obox_end', fastf_t),
    ('model_start', fastf_t),
    ('model_end', fastf_t),
    ('newray', struct_xray),
    ('ap', POINTER(struct_application)),
    ('resp', POINTER(struct_resource)),
    ('inv_dir', vect_t),
    ('abs_inv_dir', vect_t),
    ('rstep', c_int * int(3)),
    ('lastcut', POINTER(union_cutter)),
    ('lastcell', POINTER(union_cutter)),
    ('curcut', POINTER(union_cutter)),
    ('curmin', point_t),
    ('curmax', point_t),
    ('igrid', c_int * int(3)),
    ('tv', vect_t),
    ('out_axis', c_int),
    ('old_status', POINTER(struct_rt_shootray_status)),
    ('box_num', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/overlap.h: 60
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_default_multioverlap", "cdecl"):
    rt_default_multioverlap = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_default_multioverlap", "cdecl")
    rt_default_multioverlap.argtypes = [POINTER(struct_application), POINTER(struct_partition), POINTER(struct_bu_ptbl), POINTER(struct_partition)]
    rt_default_multioverlap.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/overlap.h: 69
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_silent_logoverlap", "cdecl"):
    rt_silent_logoverlap = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_silent_logoverlap", "cdecl")
    rt_silent_logoverlap.argtypes = [POINTER(struct_application), POINTER(struct_partition), POINTER(struct_bu_ptbl), POINTER(struct_partition)]
    rt_silent_logoverlap.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/overlap.h: 80
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_default_logoverlap", "cdecl"):
    rt_default_logoverlap = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_default_logoverlap", "cdecl")
    rt_default_logoverlap.argtypes = [POINTER(struct_application), POINTER(struct_partition), POINTER(struct_bu_ptbl), POINTER(struct_partition)]
    rt_default_logoverlap.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/overlap.h: 89
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_rebuild_overlaps", "cdecl"):
    rt_rebuild_overlaps = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_rebuild_overlaps", "cdecl")
    rt_rebuild_overlaps.argtypes = [POINTER(struct_partition), POINTER(struct_application), c_int]
    rt_rebuild_overlaps.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/overlap.h: 101
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_defoverlap", "cdecl"):
    rt_defoverlap = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_defoverlap", "cdecl")
    rt_defoverlap.argtypes = [POINTER(struct_application), POINTER(struct_partition), POINTER(struct_region), POINTER(struct_region), POINTER(struct_partition)]
    rt_defoverlap.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 45
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_raybundle_maker", "cdecl"):
    rt_raybundle_maker = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_raybundle_maker", "cdecl")
    rt_raybundle_maker.argtypes = [POINTER(struct_xray), c_double, POINTER(fastf_t), POINTER(fastf_t), c_int, c_int]
    rt_raybundle_maker.restype = c_int

enum_anon_62 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_RECT_ORTHOGRID = 0# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_RECT_PERSPGRID = (RT_PATTERN_RECT_ORTHOGRID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_CIRC_ORTHOGRID = (RT_PATTERN_RECT_PERSPGRID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_CIRC_PERSPGRID = (RT_PATTERN_CIRC_ORTHOGRID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_CIRC_SPIRAL = (RT_PATTERN_CIRC_PERSPGRID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_ELLIPSE_ORTHOGRID = (RT_PATTERN_CIRC_SPIRAL + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_ELLIPSE_PERSPGRID = (RT_PATTERN_ELLIPSE_ORTHOGRID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_CIRC_LAYERS = (RT_PATTERN_ELLIPSE_PERSPGRID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_SPH_LAYERS = (RT_PATTERN_CIRC_LAYERS + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_SPH_QRAND = (RT_PATTERN_SPH_LAYERS + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

RT_PATTERN_UNKNOWN = (RT_PATTERN_SPH_QRAND + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

rt_pattern_t = enum_anon_62# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 61

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 68
class struct_rt_pattern_data(Structure):
    pass

struct_rt_pattern_data.__slots__ = [
    'rays',
    'ray_cnt',
    'center_pt',
    'center_dir',
    'vn',
    'n_vec',
    'pn',
    'n_p',
]
struct_rt_pattern_data._fields_ = [
    ('rays', POINTER(fastf_t)),
    ('ray_cnt', c_size_t),
    ('center_pt', point_t),
    ('center_dir', vect_t),
    ('vn', c_size_t),
    ('n_vec', POINTER(vect_t)),
    ('pn', c_size_t),
    ('n_p', POINTER(fastf_t)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 224
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pattern", "cdecl"):
    rt_pattern = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pattern", "cdecl")
    rt_pattern.argtypes = [POINTER(struct_rt_pattern_data), rt_pattern_t]
    rt_pattern.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 235
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gen_elliptical_grid", "cdecl"):
    rt_gen_elliptical_grid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gen_elliptical_grid", "cdecl")
    rt_gen_elliptical_grid.argtypes = [POINTER(struct_xrays), POINTER(struct_xray), POINTER(fastf_t), POINTER(fastf_t), fastf_t]
    rt_gen_elliptical_grid.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 248
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gen_circular_grid", "cdecl"):
    rt_gen_circular_grid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gen_circular_grid", "cdecl")
    rt_gen_circular_grid.argtypes = [POINTER(struct_xrays), POINTER(struct_xray), fastf_t, POINTER(fastf_t), fastf_t]
    rt_gen_circular_grid.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 262
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gen_conic", "cdecl"):
    rt_gen_conic = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gen_conic", "cdecl")
    rt_gen_conic.argtypes = [POINTER(struct_xrays), POINTER(struct_xray), fastf_t, vect_t, c_int]
    rt_gen_conic.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 276
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gen_frustum", "cdecl"):
    rt_gen_frustum = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gen_frustum", "cdecl")
    rt_gen_frustum.argtypes = [POINTER(struct_xrays), POINTER(struct_xray), vect_t, vect_t, fastf_t, fastf_t, fastf_t, fastf_t]
    rt_gen_frustum.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 293
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_gen_rect", "cdecl"):
    rt_gen_rect = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_gen_rect", "cdecl")
    rt_gen_rect.argtypes = [POINTER(struct_xrays), POINTER(struct_xray), vect_t, vect_t, fastf_t, fastf_t]
    rt_gen_rect.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 93
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_shootray", "cdecl"):
    rt_shootray = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_shootray", "cdecl")
    rt_shootray.argtypes = [POINTER(struct_application)]
    rt_shootray.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 122
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_shootrays", "cdecl"):
    rt_shootrays = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_shootrays", "cdecl")
    rt_shootrays.argtypes = [POINTER(struct_application_bundle)]
    rt_shootrays.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 132
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_shootray_simple", "cdecl"):
    rt_shootray_simple = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_shootray_simple", "cdecl")
    rt_shootray_simple.argtypes = [POINTER(struct_application), point_t, vect_t]
    rt_shootray_simple.restype = POINTER(struct_partition)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 141
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_shootray_bundle", "cdecl"):
    rt_shootray_bundle = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_shootray_bundle", "cdecl")
    rt_shootray_bundle.argtypes = [POINTER(struct_application), POINTER(struct_xray), c_int]
    rt_shootray_bundle.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 151
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_add_res_stats", "cdecl"):
    rt_add_res_stats = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_add_res_stats", "cdecl")
    rt_add_res_stats.argtypes = [POINTER(struct_rt_i), POINTER(struct_resource)]
    rt_add_res_stats.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 154
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_zero_res_stats", "cdecl"):
    rt_zero_res_stats = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_zero_res_stats", "cdecl")
    rt_zero_res_stats.argtypes = [POINTER(struct_resource)]
    rt_zero_res_stats.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 157
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_res_pieces_clean", "cdecl"):
    rt_res_pieces_clean = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_res_pieces_clean", "cdecl")
    rt_res_pieces_clean.argtypes = [POINTER(struct_resource), POINTER(struct_rt_i)]
    rt_res_pieces_clean.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 165
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_res_pieces_init", "cdecl"):
    rt_res_pieces_init = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_res_pieces_init", "cdecl")
    rt_res_pieces_init.argtypes = [POINTER(struct_resource), POINTER(struct_rt_i)]
    rt_res_pieces_init.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/shoot.h: 167
for _lib in _libs.values():
    if not _lib.has("rt_vstub", "cdecl"):
        continue
    rt_vstub = _lib.get("rt_vstub", "cdecl")
    rt_vstub.argtypes = [POINTER(POINTER(struct_soltab)), POINTER(POINTER(struct_xray)), POINTER(struct_seg), c_int, POINTER(struct_application)]
    rt_vstub.restype = None
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/timer.h: 60
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_prep_timer", "cdecl"):
    rt_prep_timer = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_prep_timer", "cdecl")
    rt_prep_timer.argtypes = []
    rt_prep_timer.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/timer.h: 68
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_get_timer", "cdecl"):
    rt_get_timer = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_get_timer", "cdecl")
    rt_get_timer.argtypes = [POINTER(struct_bu_vls), POINTER(c_double)]
    rt_get_timer.restype = c_double

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/timer.h: 74
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_read_timer", "cdecl"):
    rt_read_timer = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_read_timer", "cdecl")
    rt_read_timer.argtypes = [String, c_int]
    rt_read_timer.restype = c_double

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/boolweave.h: 76
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_boolweave", "cdecl"):
    rt_boolweave = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_boolweave", "cdecl")
    rt_boolweave.argtypes = [POINTER(struct_seg), POINTER(struct_seg), POINTER(struct_partition), POINTER(struct_application)]
    rt_boolweave.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/boolweave.h: 155
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_boolfinal", "cdecl"):
    rt_boolfinal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_boolfinal", "cdecl")
    rt_boolfinal.argtypes = [POINTER(struct_partition), POINTER(struct_partition), fastf_t, fastf_t, POINTER(struct_bu_ptbl), POINTER(struct_application), POINTER(struct_bu_bitv)]
    rt_boolfinal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/boolweave.h: 170
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bool_growstack", "cdecl"):
    rt_bool_growstack = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bool_growstack", "cdecl")
    rt_bool_growstack.argtypes = [POINTER(struct_resource)]
    rt_bool_growstack.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 50
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_matrix_transform", "cdecl"):
    rt_matrix_transform = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_matrix_transform", "cdecl")
    rt_matrix_transform.argtypes = [POINTER(struct_rt_db_internal), mat_t, POINTER(struct_rt_db_internal), c_int, POINTER(struct_db_i), POINTER(struct_resource)]
    rt_matrix_transform.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 60
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_rpp_region", "cdecl"):
    rt_rpp_region = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_rpp_region", "cdecl")
    rt_rpp_region.argtypes = [POINTER(struct_rt_i), String, POINTER(fastf_t), POINTER(fastf_t)]
    rt_rpp_region.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 87
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_in_rpp", "cdecl"):
    rt_in_rpp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_in_rpp", "cdecl")
    rt_in_rpp.argtypes = [POINTER(struct_xray), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t)]
    rt_in_rpp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 114
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bound_internal", "cdecl"):
    rt_bound_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bound_internal", "cdecl")
    rt_bound_internal.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), point_t, point_t]
    rt_bound_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 133
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_shader_mat", "cdecl"):
    rt_shader_mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_shader_mat", "cdecl")
    rt_shader_mat.argtypes = [mat_t, POINTER(struct_rt_i), POINTER(struct_region), point_t, point_t, POINTER(struct_resource)]
    rt_shader_mat.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 141
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_mirror", "cdecl"):
    rt_mirror = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_mirror", "cdecl")
    rt_mirror.argtypes = [POINTER(struct_db_i), POINTER(struct_rt_db_internal), point_t, vect_t, POINTER(struct_resource)]
    rt_mirror.restype = POINTER(struct_rt_db_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 148
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_plot_all_bboxes", "cdecl"):
    rt_plot_all_bboxes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_plot_all_bboxes", "cdecl")
    rt_plot_all_bboxes.argtypes = [POINTER(FILE), POINTER(struct_rt_i)]
    rt_plot_all_bboxes.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 150
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_plot_all_solids", "cdecl"):
    rt_plot_all_solids = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_plot_all_solids", "cdecl")
    rt_plot_all_solids.argtypes = [POINTER(FILE), POINTER(struct_rt_i), POINTER(struct_resource)]
    rt_plot_all_solids.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 157
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_fallback_angle", "cdecl"):
    rt_pr_fallback_angle = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_fallback_angle", "cdecl")
    rt_pr_fallback_angle.argtypes = [POINTER(struct_bu_vls), String, c_double * int(5)]
    rt_pr_fallback_angle.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 160
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_find_fallback_angle", "cdecl"):
    rt_find_fallback_angle = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_find_fallback_angle", "cdecl")
    rt_find_fallback_angle.argtypes = [c_double * int(5), vect_t]
    rt_find_fallback_angle.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 162
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pr_tol", "cdecl"):
    rt_pr_tol = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pr_tol", "cdecl")
    rt_pr_tol.argtypes = [POINTER(struct_bn_tol)]
    rt_pr_tol.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/calc.h: 178
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_poly_roots", "cdecl"):
    rt_poly_roots = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_poly_roots", "cdecl")
    rt_poly_roots.argtypes = [POINTER(bn_poly_t), POINTER(bn_complex_t), String]
    rt_poly_roots.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/cmd.h: 42
class struct_command_tab(Structure):
    pass

struct_command_tab.__slots__ = [
    'ct_cmd',
    'ct_parms',
    'ct_comment',
    'ct_func',
    'ct_min',
    'ct_max',
]
struct_command_tab._fields_ = [
    ('ct_cmd', String),
    ('ct_parms', String),
    ('ct_comment', String),
    ('ct_func', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(POINTER(c_char)))),
    ('ct_min', c_int),
    ('ct_max', c_int),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/cmd.h: 63
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_read_cmd", "cdecl"):
    rt_read_cmd = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_read_cmd", "cdecl")
    rt_read_cmd.argtypes = [POINTER(FILE)]
    if sizeof(c_int) == sizeof(c_void_p):
        rt_read_cmd.restype = ReturnString
    else:
        rt_read_cmd.restype = String
        rt_read_cmd.errcheck = ReturnString

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/cmd.h: 78
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_do_cmd", "cdecl"):
    rt_do_cmd = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_do_cmd", "cdecl")
    rt_do_cmd.argtypes = [POINTER(struct_rt_i), String, POINTER(struct_command_tab)]
    rt_do_cmd.restype = c_int

db_search_callback_t = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(POINTER(c_char)), POINTER(None))# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 40

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 45
class struct_db_search_context(Structure):
    pass

struct_db_search_context.__slots__ = [
    '_e_callback',
    '_e_userdata',
]
struct_db_search_context._fields_ = [
    ('_e_callback', db_search_callback_t),
    ('_e_userdata', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 53
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_search_context_create", "cdecl"):
    db_search_context_create = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_search_context_create", "cdecl")
    db_search_context_create.argtypes = []
    db_search_context_create.restype = POINTER(struct_db_search_context)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 58
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_search_context_destroy", "cdecl"):
    db_search_context_destroy = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_search_context_destroy", "cdecl")
    db_search_context_destroy.argtypes = [POINTER(struct_db_search_context)]
    db_search_context_destroy.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 63
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_search_register_exec", "cdecl"):
    db_search_register_exec = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_search_register_exec", "cdecl")
    db_search_register_exec.argtypes = [POINTER(struct_db_search_context), db_search_callback_t]
    db_search_register_exec.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 68
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_search_register_data", "cdecl"):
    db_search_register_data = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_search_register_data", "cdecl")
    db_search_register_data.argtypes = [POINTER(struct_db_search_context), POINTER(None)]
    db_search_register_data.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 136
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_search", "cdecl"):
    db_search = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_search", "cdecl")
    db_search.argtypes = [POINTER(struct_bu_ptbl), c_int, String, c_int, POINTER(POINTER(struct_directory)), POINTER(struct_db_i), POINTER(struct_db_search_context)]
    db_search.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 157
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_search_free", "cdecl"):
    db_search_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_search_free", "cdecl")
    db_search_free.argtypes = [POINTER(struct_bu_ptbl)]
    db_search_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 175
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_ls", "cdecl"):
    db_ls = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_ls", "cdecl")
    db_ls.argtypes = [POINTER(struct_db_i), c_int, String, POINTER(POINTER(POINTER(struct_directory)))]
    db_ls.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 49
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_sync", "cdecl"):
    db_sync = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_sync", "cdecl")
    db_sync.argtypes = [POINTER(struct_db_i)]
    db_sync.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 83
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_open", "cdecl"):
    db_open = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_open", "cdecl")
    db_open.argtypes = [String, String]
    db_open.restype = POINTER(struct_db_i)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 100
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_create", "cdecl"):
    db_create = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_create", "cdecl")
    db_create.argtypes = [String, c_int]
    db_create.restype = POINTER(struct_db_i)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 108
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_close_client", "cdecl"):
    db_close_client = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_close_client", "cdecl")
    db_close_client.argtypes = [POINTER(struct_db_i), POINTER(c_long)]
    db_close_client.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 115
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_close", "cdecl"):
    db_close = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_close", "cdecl")
    db_close.argtypes = [POINTER(struct_db_i)]
    db_close.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 129
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dump", "cdecl"):
    db_dump = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dump", "cdecl")
    db_dump.argtypes = [POINTER(struct_rt_wdb), POINTER(struct_db_i)]
    db_dump.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 136
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_clone_dbi", "cdecl"):
    db_clone_dbi = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_clone_dbi", "cdecl")
    db_clone_dbi.argtypes = [POINTER(struct_db_i), POINTER(c_long)]
    db_clone_dbi.restype = POINTER(struct_db_i)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 152
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_write_free", "cdecl"):
    db5_write_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_write_free", "cdecl")
    db5_write_free.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), c_size_t]
    db5_write_free.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 178
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_realloc", "cdecl"):
    db5_realloc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_realloc", "cdecl")
    db5_realloc.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), POINTER(struct_bu_external)]
    db5_realloc.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 189
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_export_object3", "cdecl"):
    db5_export_object3 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_export_object3", "cdecl")
    db5_export_object3.argtypes = [POINTER(struct_bu_external), c_int, String, c_ubyte, POINTER(struct_bu_external), POINTER(struct_bu_external), c_int, c_int, c_int, c_int]
    db5_export_object3.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 219
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_cvt_to_external5", "cdecl"):
    rt_db_cvt_to_external5 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_cvt_to_external5", "cdecl")
    rt_db_cvt_to_external5.argtypes = [POINTER(struct_bu_external), String, POINTER(struct_rt_db_internal), c_double, POINTER(struct_db_i), POINTER(struct_resource), c_int]
    rt_db_cvt_to_external5.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 231
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_wrap_v5_external", "cdecl"):
    db_wrap_v5_external = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_wrap_v5_external", "cdecl")
    db_wrap_v5_external.argtypes = [POINTER(struct_bu_external), String]
    db_wrap_v5_external.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 246
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_get_internal5", "cdecl"):
    rt_db_get_internal5 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_get_internal5", "cdecl")
    rt_db_get_internal5.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_directory), POINTER(struct_db_i), mat_t, POINTER(struct_resource)]
    rt_db_get_internal5.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 267
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_put_internal5", "cdecl"):
    rt_db_put_internal5 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_put_internal5", "cdecl")
    rt_db_put_internal5.argtypes = [POINTER(struct_directory), POINTER(struct_db_i), POINTER(struct_rt_db_internal), POINTER(struct_resource), c_int]
    rt_db_put_internal5.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 279
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_make_free_object_hdr", "cdecl"):
    db5_make_free_object_hdr = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_make_free_object_hdr", "cdecl")
    db5_make_free_object_hdr.argtypes = [POINTER(struct_bu_external), c_size_t]
    db5_make_free_object_hdr.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 287
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_make_free_object", "cdecl"):
    db5_make_free_object = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_make_free_object", "cdecl")
    db5_make_free_object.argtypes = [POINTER(struct_bu_external), c_size_t]
    db5_make_free_object.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 304
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_decode_signed", "cdecl"):
    db5_decode_signed = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_decode_signed", "cdecl")
    db5_decode_signed.argtypes = [POINTER(c_size_t), POINTER(c_ubyte), c_int]
    db5_decode_signed.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 317
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_decode_length", "cdecl"):
    db5_decode_length = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_decode_length", "cdecl")
    db5_decode_length.argtypes = [POINTER(c_size_t), POINTER(c_ubyte), c_int]
    db5_decode_length.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 332
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_select_length_encoding", "cdecl"):
    db5_select_length_encoding = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_select_length_encoding", "cdecl")
    db5_select_length_encoding.argtypes = [c_size_t]
    db5_select_length_encoding.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 335
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_import_color_table", "cdecl"):
    db5_import_color_table = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_import_color_table", "cdecl")
    db5_import_color_table.argtypes = [String]
    db5_import_color_table.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 344
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_encode_length", "cdecl"):
    db5_encode_length = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_encode_length", "cdecl")
    db5_encode_length.argtypes = [POINTER(c_ubyte), c_size_t, c_int]
    db5_encode_length.restype = POINTER(c_ubyte)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 356
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_get_raw_internal_ptr", "cdecl"):
    db5_get_raw_internal_ptr = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_get_raw_internal_ptr", "cdecl")
    db5_get_raw_internal_ptr.argtypes = [POINTER(struct_db5_raw_internal), POINTER(c_ubyte)]
    db5_get_raw_internal_ptr.restype = POINTER(c_ubyte)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 369
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_get_raw_internal_fp", "cdecl"):
    db5_get_raw_internal_fp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_get_raw_internal_fp", "cdecl")
    db5_get_raw_internal_fp.argtypes = [POINTER(struct_db5_raw_internal), POINTER(FILE)]
    db5_get_raw_internal_fp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 380
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_header_is_valid", "cdecl"):
    db5_header_is_valid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_header_is_valid", "cdecl")
    db5_header_is_valid.argtypes = [POINTER(c_ubyte)]
    db5_header_is_valid.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 391
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_fwrite_ident", "cdecl"):
    db5_fwrite_ident = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_fwrite_ident", "cdecl")
    db5_fwrite_ident.argtypes = [POINTER(FILE), String, c_double]
    db5_fwrite_ident.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 418
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_put_external5", "cdecl"):
    db_put_external5 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_put_external5", "cdecl")
    db_put_external5.argtypes = [POINTER(struct_bu_external), POINTER(struct_directory), POINTER(struct_db_i)]
    db_put_external5.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 427
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_wrap_v4_external", "cdecl"):
    db_wrap_v4_external = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_wrap_v4_external", "cdecl")
    db_wrap_v4_external.argtypes = [POINTER(struct_bu_external), String]
    db_wrap_v4_external.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 432
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_write", "cdecl"):
    db_write = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_write", "cdecl")
    db_write.argtypes = [POINTER(struct_db_i), POINTER(None), c_size_t, off_t]
    db_write.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 456
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_fwrite_external", "cdecl"):
    db_fwrite_external = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_fwrite_external", "cdecl")
    db_fwrite_external.argtypes = [POINTER(FILE), String, POINTER(struct_bu_external)]
    db_fwrite_external.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 421
class union_record(Union):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 474
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_getmrec", "cdecl"):
    db_getmrec = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_getmrec", "cdecl")
    db_getmrec.argtypes = [POINTER(struct_db_i), POINTER(struct_directory)]
    db_getmrec.restype = POINTER(union_record)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 486
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_get", "cdecl"):
    db_get = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_get", "cdecl")
    db_get.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), POINTER(union_record), off_t, c_size_t]
    db_get.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 501
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_put", "cdecl"):
    db_put = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_put", "cdecl")
    db_put.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), POINTER(union_record), off_t, c_size_t]
    db_put.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 520
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_get_external", "cdecl"):
    db_get_external = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_get_external", "cdecl")
    db_get_external.argtypes = [POINTER(struct_bu_external), POINTER(struct_directory), POINTER(struct_db_i)]
    db_get_external.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 542
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_put_external", "cdecl"):
    db_put_external = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_put_external", "cdecl")
    db_put_external.argtypes = [POINTER(struct_bu_external), POINTER(struct_directory), POINTER(struct_db_i)]
    db_put_external.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 548
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_scan", "cdecl"):
    db_scan = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_scan", "cdecl")
    db_scan.argtypes = [POINTER(struct_db_i), CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_db_i), String, off_t, c_size_t, c_int, POINTER(None)), c_int, POINTER(None)]
    db_scan.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 570
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_update_ident", "cdecl"):
    db_update_ident = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_update_ident", "cdecl")
    db_update_ident.argtypes = [POINTER(struct_db_i), String, c_double]
    db_update_ident.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 603
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_fwrite_ident", "cdecl"):
    db_fwrite_ident = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_fwrite_ident", "cdecl")
    db_fwrite_ident.argtypes = [POINTER(FILE), String, c_double]
    db_fwrite_ident.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 610
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_conversions", "cdecl"):
    db_conversions = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_conversions", "cdecl")
    db_conversions.argtypes = [POINTER(struct_db_i), c_int]
    db_conversions.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 622
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_v4_get_units_code", "cdecl"):
    db_v4_get_units_code = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_v4_get_units_code", "cdecl")
    db_v4_get_units_code.argtypes = [String]
    db_v4_get_units_code.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 641
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dirbuild", "cdecl"):
    db_dirbuild = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dirbuild", "cdecl")
    db_dirbuild.argtypes = [POINTER(struct_db_i)]
    db_dirbuild.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 642
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_diradd", "cdecl"):
    db5_diradd = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_diradd", "cdecl")
    db5_diradd.argtypes = [POINTER(struct_db_i), POINTER(struct_db5_raw_internal), off_t, POINTER(None)]
    db5_diradd.restype = POINTER(struct_directory)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 654
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_scan", "cdecl"):
    db5_scan = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_scan", "cdecl")
    db5_scan.argtypes = [POINTER(struct_db_i), CFUNCTYPE(UNCHECKED(None), POINTER(struct_db_i), POINTER(struct_db5_raw_internal), off_t, POINTER(None)), POINTER(None)]
    db5_scan.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 666
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_version", "cdecl"):
    db_version = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_version", "cdecl")
    db_version.argtypes = [POINTER(struct_db_i)]
    db_version.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 680
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_db_flip_endian", "cdecl"):
    rt_db_flip_endian = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_db_flip_endian", "cdecl")
    rt_db_flip_endian.argtypes = [POINTER(struct_db_i)]
    rt_db_flip_endian.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 688
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_open_inmem", "cdecl"):
    db_open_inmem = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_open_inmem", "cdecl")
    db_open_inmem.argtypes = []
    db_open_inmem.restype = POINTER(struct_db_i)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 696
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_create_inmem", "cdecl"):
    db_create_inmem = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_create_inmem", "cdecl")
    db_create_inmem.argtypes = []
    db_create_inmem.restype = POINTER(struct_db_i)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 703
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_inmem", "cdecl"):
    db_inmem = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_inmem", "cdecl")
    db_inmem.argtypes = [POINTER(struct_directory), POINTER(struct_bu_external), c_int, POINTER(struct_db_i)]
    db_inmem.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 714
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_directory_size", "cdecl"):
    db_directory_size = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_directory_size", "cdecl")
    db_directory_size.argtypes = [POINTER(struct_db_i)]
    db_directory_size.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 720
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_ck_directory", "cdecl"):
    db_ck_directory = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_ck_directory", "cdecl")
    db_ck_directory.argtypes = [POINTER(struct_db_i)]
    db_ck_directory.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 728
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_is_directory_non_empty", "cdecl"):
    db_is_directory_non_empty = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_is_directory_non_empty", "cdecl")
    db_is_directory_non_empty.argtypes = [POINTER(struct_db_i)]
    db_is_directory_non_empty.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 734
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dirhash", "cdecl"):
    db_dirhash = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dirhash", "cdecl")
    db_dirhash.argtypes = [String]
    db_dirhash.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 755
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dircheck", "cdecl"):
    db_dircheck = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dircheck", "cdecl")
    db_dircheck.argtypes = [POINTER(struct_db_i), POINTER(struct_bu_vls), c_int, POINTER(POINTER(POINTER(struct_directory)))]
    db_dircheck.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 780
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_lookup", "cdecl"):
    db_lookup = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_lookup", "cdecl")
    db_lookup.argtypes = [POINTER(struct_db_i), String, c_int]
    db_lookup.restype = POINTER(struct_directory)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 806
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_diradd", "cdecl"):
    db_diradd = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_diradd", "cdecl")
    db_diradd.argtypes = [POINTER(struct_db_i), String, off_t, c_size_t, c_int, POINTER(None)]
    db_diradd.restype = POINTER(struct_directory)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 812
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_diradd5", "cdecl"):
    db_diradd5 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_diradd5", "cdecl")
    db_diradd5.argtypes = [POINTER(struct_db_i), String, off_t, c_ubyte, c_ubyte, c_ubyte, c_size_t, POINTER(struct_bu_attribute_value_set)]
    db_diradd5.restype = POINTER(struct_directory)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 834
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_dirdelete", "cdecl"):
    db_dirdelete = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_dirdelete", "cdecl")
    db_dirdelete.argtypes = [POINTER(struct_db_i), POINTER(struct_directory)]
    db_dirdelete.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 836
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_fwrite_ident", "cdecl"):
    db_fwrite_ident = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_fwrite_ident", "cdecl")
    db_fwrite_ident.argtypes = [POINTER(FILE), String, c_double]
    db_fwrite_ident.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 843
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_pr_dir", "cdecl"):
    db_pr_dir = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_pr_dir", "cdecl")
    db_pr_dir.argtypes = [POINTER(struct_db_i)]
    db_pr_dir.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 853
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_rename", "cdecl"):
    db_rename = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_rename", "cdecl")
    db_rename.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), String]
    db_rename.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 863
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_update_nref", "cdecl"):
    db_update_nref = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_update_nref", "cdecl")
    db_update_nref.argtypes = [POINTER(struct_db_i), POINTER(struct_resource)]
    db_update_nref.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 874
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_flags_internal", "cdecl"):
    db_flags_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_flags_internal", "cdecl")
    db_flags_internal.argtypes = [POINTER(struct_rt_db_internal)]
    db_flags_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 883
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_flags_raw_internal", "cdecl"):
    db_flags_raw_internal = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_flags_raw_internal", "cdecl")
    db_flags_raw_internal.argtypes = [POINTER(struct_db5_raw_internal)]
    db_flags_raw_internal.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 888
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_alloc", "cdecl"):
    db_alloc = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_alloc", "cdecl")
    db_alloc.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), c_size_t]
    db_alloc.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 892
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_delrec", "cdecl"):
    db_delrec = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_delrec", "cdecl")
    db_delrec.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), c_int]
    db_delrec.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 896
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_delete", "cdecl"):
    db_delete = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_delete", "cdecl")
    db_delete.argtypes = [POINTER(struct_db_i), POINTER(struct_directory)]
    db_delete.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 899
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_zapper", "cdecl"):
    db_zapper = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_zapper", "cdecl")
    db_zapper.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), c_size_t]
    db_zapper.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 908
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_alloc_directory_block", "cdecl"):
    db_alloc_directory_block = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_alloc_directory_block", "cdecl")
    db_alloc_directory_block.argtypes = [POINTER(struct_resource)]
    db_alloc_directory_block.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 917
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_alloc_seg_block", "cdecl"):
    rt_alloc_seg_block = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_alloc_seg_block", "cdecl")
    rt_alloc_seg_block.argtypes = [POINTER(struct_resource)]
    rt_alloc_seg_block.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 924
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_dirbuild", "cdecl"):
    rt_dirbuild = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_dirbuild", "cdecl")
    rt_dirbuild.argtypes = [String, String, c_int]
    rt_dirbuild.restype = POINTER(struct_rt_i)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 928
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_tag_from_major", "cdecl"):
    db5_type_tag_from_major = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_tag_from_major", "cdecl")
    db5_type_tag_from_major.argtypes = [POINTER(POINTER(c_char)), c_int]
    db5_type_tag_from_major.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 931
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_descrip_from_major", "cdecl"):
    db5_type_descrip_from_major = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_descrip_from_major", "cdecl")
    db5_type_descrip_from_major.argtypes = [POINTER(POINTER(c_char)), c_int]
    db5_type_descrip_from_major.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 934
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_tag_from_codes", "cdecl"):
    db5_type_tag_from_codes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_tag_from_codes", "cdecl")
    db5_type_tag_from_codes.argtypes = [POINTER(POINTER(c_char)), c_int, c_int]
    db5_type_tag_from_codes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 938
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_descrip_from_codes", "cdecl"):
    db5_type_descrip_from_codes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_descrip_from_codes", "cdecl")
    db5_type_descrip_from_codes.argtypes = [POINTER(POINTER(c_char)), c_int, c_int]
    db5_type_descrip_from_codes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 942
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_codes_from_tag", "cdecl"):
    db5_type_codes_from_tag = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_codes_from_tag", "cdecl")
    db5_type_codes_from_tag.argtypes = [POINTER(c_int), POINTER(c_int), String]
    db5_type_codes_from_tag.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 946
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_codes_from_descrip", "cdecl"):
    db5_type_codes_from_descrip = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_codes_from_descrip", "cdecl")
    db5_type_codes_from_descrip.argtypes = [POINTER(c_int), POINTER(c_int), String]
    db5_type_codes_from_descrip.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 950
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_sizeof_h_binu", "cdecl"):
    db5_type_sizeof_h_binu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_sizeof_h_binu", "cdecl")
    db5_type_sizeof_h_binu.argtypes = [c_int]
    db5_type_sizeof_h_binu.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 952
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_type_sizeof_n_binu", "cdecl"):
    db5_type_sizeof_n_binu = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_type_sizeof_n_binu", "cdecl")
    db5_type_sizeof_n_binu.argtypes = [c_int]
    db5_type_sizeof_n_binu.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 38
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_get_cgtype", "cdecl"):
    rt_arb_get_cgtype = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_get_cgtype", "cdecl")
    rt_arb_get_cgtype.argtypes = [POINTER(c_int), POINTER(struct_rt_arb_internal), POINTER(struct_bn_tol), POINTER(c_int), POINTER(c_int)]
    rt_arb_get_cgtype.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 44
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_std_type", "cdecl"):
    rt_arb_std_type = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_std_type", "cdecl")
    rt_arb_std_type.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_bn_tol)]
    rt_arb_std_type.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 46
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_centroid", "cdecl"):
    rt_arb_centroid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_centroid", "cdecl")
    rt_arb_centroid.argtypes = [POINTER(point_t), POINTER(struct_rt_db_internal)]
    rt_arb_centroid.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 48
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_calc_points", "cdecl"):
    rt_arb_calc_points = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_calc_points", "cdecl")
    rt_arb_calc_points.argtypes = [POINTER(struct_rt_arb_internal), c_int, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_calc_points.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 49
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_check_points", "cdecl"):
    rt_arb_check_points = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_check_points", "cdecl")
    rt_arb_check_points.argtypes = [POINTER(struct_rt_arb_internal), c_int, POINTER(struct_bn_tol)]
    rt_arb_check_points.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 52
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_3face_intersect", "cdecl"):
    rt_arb_3face_intersect = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_3face_intersect", "cdecl")
    rt_arb_3face_intersect.argtypes = [point_t, plane_t * int(6), c_int, c_int]
    rt_arb_3face_intersect.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 56
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_calc_planes", "cdecl"):
    rt_arb_calc_planes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_calc_planes", "cdecl")
    rt_arb_calc_planes.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_arb_internal), c_int, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_calc_planes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 61
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_move_edge", "cdecl"):
    rt_arb_move_edge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_move_edge", "cdecl")
    rt_arb_move_edge.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_arb_internal), vect_t, c_int, c_int, c_int, c_int, vect_t, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_move_edge.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 71
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_edit", "cdecl"):
    rt_arb_edit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_edit", "cdecl")
    rt_arb_edit.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_arb_internal), c_int, c_int, vect_t, plane_t * int(6), POINTER(struct_bn_tol)]
    rt_arb_edit.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/arb8.h: 78
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_arb_find_e_nearest_pt2", "cdecl"):
    rt_arb_find_e_nearest_pt2 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_arb_find_e_nearest_pt2", "cdecl")
    rt_arb_find_e_nearest_pt2.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_rt_db_internal), point_t, mat_t, fastf_t]
    rt_arb_find_e_nearest_pt2.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/epa.h: 33
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_ell", "cdecl"):
    rt_ell = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_ell", "cdecl")
    rt_ell.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_int]
    rt_ell.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/pipe.h: 35
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_vls_pipe_pnt", "cdecl"):
    rt_vls_pipe_pnt = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_vls_pipe_pnt", "cdecl")
    rt_vls_pipe_pnt.argtypes = [POINTER(struct_bu_vls), c_int, POINTER(struct_rt_db_internal), c_double]
    rt_vls_pipe_pnt.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/pipe.h: 39
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pipe_pnt_print", "cdecl"):
    rt_pipe_pnt_print = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pipe_pnt_print", "cdecl")
    rt_pipe_pnt_print.argtypes = [POINTER(struct_wdb_pipe_pnt), c_double]
    rt_pipe_pnt_print.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/pipe.h: 40
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pipe_ck", "cdecl"):
    rt_pipe_ck = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pipe_ck", "cdecl")
    rt_pipe_ck.argtypes = [POINTER(struct_bu_list)]
    rt_pipe_ck.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 35
for _lib in _libs.values():
    if not _lib.has("rt_vls_metaball_pnt", "cdecl"):
        continue
    rt_vls_metaball_pnt = _lib.get("rt_vls_metaball_pnt", "cdecl")
    rt_vls_metaball_pnt.argtypes = [POINTER(struct_bu_vls), c_int, POINTER(struct_rt_db_internal), c_double]
    rt_vls_metaball_pnt.restype = None
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 39
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_metaball_pnt_print", "cdecl"):
    rt_metaball_pnt_print = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_metaball_pnt_print", "cdecl")
    rt_metaball_pnt_print.argtypes = [POINTER(struct_wdb_metaball_pnt), c_double]
    rt_metaball_pnt_print.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 40
for _lib in _libs.values():
    if not _lib.has("rt_metaball_ck", "cdecl"):
        continue
    rt_metaball_ck = _lib.get("rt_metaball_ck", "cdecl")
    rt_metaball_ck.argtypes = [POINTER(struct_bu_list)]
    rt_metaball_ck.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 41
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_metaball_point_value", "cdecl"):
    rt_metaball_point_value = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_metaball_point_value", "cdecl")
    rt_metaball_point_value.argtypes = [POINTER(point_t), POINTER(struct_rt_metaball_internal)]
    rt_metaball_point_value.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 43
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_metaball_point_inside", "cdecl"):
    rt_metaball_point_inside = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_metaball_point_inside", "cdecl")
    rt_metaball_point_inside.argtypes = [POINTER(point_t), POINTER(struct_rt_metaball_internal)]
    rt_metaball_point_inside.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 45
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_metaball_lookup_type_id", "cdecl"):
    rt_metaball_lookup_type_id = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_metaball_lookup_type_id", "cdecl")
    rt_metaball_lookup_type_id.argtypes = [String]
    rt_metaball_lookup_type_id.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 46
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_metaball_lookup_type_name", "cdecl"):
    rt_metaball_lookup_type_name = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_metaball_lookup_type_name", "cdecl")
    rt_metaball_lookup_type_name.argtypes = [c_int]
    rt_metaball_lookup_type_name.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/metaball.h: 47
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_metaball_add_point", "cdecl"):
    rt_metaball_add_point = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_metaball_add_point", "cdecl")
    rt_metaball_add_point.argtypes = [POINTER(struct_rt_metaball_internal), POINTER(point_t), fastf_t, fastf_t]
    rt_metaball_add_point.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/rpc.h: 33
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_mk_parabola", "cdecl"):
    rt_mk_parabola = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_mk_parabola", "cdecl")
    rt_mk_parabola.argtypes = [POINTER(struct_rt_pnt_node), fastf_t, fastf_t, fastf_t, fastf_t]
    rt_mk_parabola.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/pg.h: 35
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pg_to_bot", "cdecl"):
    rt_pg_to_bot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pg_to_bot", "cdecl")
    rt_pg_to_bot.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_bn_tol), POINTER(struct_resource)]
    rt_pg_to_bot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/pg.h: 38
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pg_plot", "cdecl"):
    rt_pg_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pg_plot", "cdecl")
    rt_pg_plot.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_pg_plot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/pg.h: 43
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pg_plot_poly", "cdecl"):
    rt_pg_plot_poly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pg_plot_poly", "cdecl")
    rt_pg_plot_poly.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_pg_plot_poly.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/hf.h: 33
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_hf_to_dsp", "cdecl"):
    rt_hf_to_dsp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_hf_to_dsp", "cdecl")
    rt_hf_to_dsp.argtypes = [POINTER(struct_rt_db_internal)]
    rt_hf_to_dsp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/dsp.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("dsp_pos", "cdecl"):
    dsp_pos = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("dsp_pos", "cdecl")
    dsp_pos.argtypes = [point_t, POINTER(struct_soltab), point_t]
    dsp_pos.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/ell.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_ell_16pnts", "cdecl"):
    rt_ell_16pnts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_ell_16pnts", "cdecl")
    rt_ell_16pnts.argtypes = [POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t)]
    rt_ell_16pnts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/tgc.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_pnt_sort", "cdecl"):
    rt_pnt_sort = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_pnt_sort", "cdecl")
    rt_pnt_sort.argtypes = [POINTER(fastf_t), c_int]
    rt_pnt_sort.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 36
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("curve_to_vlist", "cdecl"):
    curve_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("curve_to_vlist", "cdecl")
    curve_to_vlist.argtypes = [POINTER(struct_bu_list), POINTER(struct_bg_tess_tol), point_t, vect_t, vect_t, POINTER(struct_rt_sketch_internal), POINTER(struct_rt_curve)]
    curve_to_vlist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 44
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_check_curve", "cdecl"):
    rt_check_curve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_check_curve", "cdecl")
    rt_check_curve.argtypes = [POINTER(struct_rt_curve), POINTER(struct_rt_sketch_internal), c_int]
    rt_check_curve.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 48
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_curve_reverse_segment", "cdecl"):
    rt_curve_reverse_segment = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_curve_reverse_segment", "cdecl")
    rt_curve_reverse_segment.argtypes = [POINTER(c_uint32)]
    rt_curve_reverse_segment.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 49
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_curve_order_segments", "cdecl"):
    rt_curve_order_segments = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_curve_order_segments", "cdecl")
    rt_curve_order_segments.argtypes = [POINTER(struct_rt_curve)]
    rt_curve_order_segments.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 51
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_copy_curve", "cdecl"):
    rt_copy_curve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_copy_curve", "cdecl")
    rt_copy_curve.argtypes = [POINTER(struct_rt_curve), POINTER(struct_rt_curve)]
    rt_copy_curve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 54
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_curve_free", "cdecl"):
    rt_curve_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_curve_free", "cdecl")
    rt_curve_free.argtypes = [POINTER(struct_rt_curve)]
    rt_curve_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 55
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_copy_curve", "cdecl"):
    rt_copy_curve = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_copy_curve", "cdecl")
    rt_copy_curve.argtypes = [POINTER(struct_rt_curve), POINTER(struct_rt_curve)]
    rt_copy_curve.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 57
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_copy_sketch", "cdecl"):
    rt_copy_sketch = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_copy_sketch", "cdecl")
    rt_copy_sketch.argtypes = [POINTER(struct_rt_sketch_internal)]
    rt_copy_sketch.restype = POINTER(struct_rt_sketch_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/sketch.h: 58
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("curve_to_tcl_list", "cdecl"):
    curve_to_tcl_list = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("curve_to_tcl_list", "cdecl")
    curve_to_tcl_list.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_curve)]
    curve_to_tcl_list.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/annot.h: 36
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_copy_annot", "cdecl"):
    rt_copy_annot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_copy_annot", "cdecl")
    rt_copy_annot.argtypes = [POINTER(struct_rt_annot_internal)]
    rt_copy_annot.restype = POINTER(struct_rt_annot_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 57
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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 76
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_prep_pieces", "cdecl"):
    rt_bot_prep_pieces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_prep_pieces", "cdecl")
    rt_bot_prep_pieces.argtypes = [POINTER(struct_bot_specific), POINTER(struct_soltab), c_size_t, POINTER(struct_bn_tol)]
    rt_bot_prep_pieces.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 81
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_botface", "cdecl"):
    rt_botface = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_botface", "cdecl")
    rt_botface.argtypes = [POINTER(struct_soltab), POINTER(struct_bot_specific), POINTER(fastf_t), POINTER(fastf_t), POINTER(fastf_t), c_size_t, POINTER(struct_bn_tol)]
    rt_botface.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 91
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_get_edge_list", "cdecl"):
    rt_bot_get_edge_list = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_get_edge_list", "cdecl")
    rt_bot_get_edge_list.argtypes = [POINTER(struct_rt_bot_internal), POINTER(POINTER(c_size_t))]
    rt_bot_get_edge_list.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 93
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_edge_in_list", "cdecl"):
    rt_bot_edge_in_list = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_edge_in_list", "cdecl")
    rt_bot_edge_in_list.argtypes = [c_size_t, c_size_t, POINTER(c_size_t), c_size_t]
    rt_bot_edge_in_list.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 97
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_plot", "cdecl"):
    rt_bot_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_plot", "cdecl")
    rt_bot_plot.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_bot_plot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 102
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_plot_poly", "cdecl"):
    rt_bot_plot_poly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_plot_poly", "cdecl")
    rt_bot_plot_poly.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_bot_plot_poly.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 106
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_find_v_nearest_pt2", "cdecl"):
    rt_bot_find_v_nearest_pt2 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_find_v_nearest_pt2", "cdecl")
    rt_bot_find_v_nearest_pt2.argtypes = [POINTER(struct_rt_bot_internal), point_t, mat_t]
    rt_bot_find_v_nearest_pt2.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 109
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_find_e_nearest_pt2", "cdecl"):
    rt_bot_find_e_nearest_pt2 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_find_e_nearest_pt2", "cdecl")
    rt_bot_find_e_nearest_pt2.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(struct_rt_bot_internal), point_t, mat_t]
    rt_bot_find_e_nearest_pt2.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 110
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_propget", "cdecl"):
    rt_bot_propget = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_propget", "cdecl")
    rt_bot_propget.argtypes = [POINTER(struct_rt_bot_internal), String]
    rt_bot_propget.restype = fastf_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 112
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_vertex_fuse", "cdecl"):
    rt_bot_vertex_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_vertex_fuse", "cdecl")
    rt_bot_vertex_fuse.argtypes = [POINTER(struct_rt_bot_internal), POINTER(struct_bn_tol)]
    rt_bot_vertex_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 114
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_face_fuse", "cdecl"):
    rt_bot_face_fuse = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_face_fuse", "cdecl")
    rt_bot_face_fuse.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_face_fuse.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 115
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_condense", "cdecl"):
    rt_bot_condense = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_condense", "cdecl")
    rt_bot_condense.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_condense.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 116
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_smooth", "cdecl"):
    rt_bot_smooth = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_smooth", "cdecl")
    rt_bot_smooth.argtypes = [POINTER(struct_rt_bot_internal), String, POINTER(struct_db_i), fastf_t]
    rt_bot_smooth.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 120
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_flip", "cdecl"):
    rt_bot_flip = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_flip", "cdecl")
    rt_bot_flip.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_flip.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 121
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_sync", "cdecl"):
    rt_bot_sync = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_sync", "cdecl")
    rt_bot_sync.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_sync.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 122
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_split", "cdecl"):
    rt_bot_split = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_split", "cdecl")
    rt_bot_split.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_split.restype = POINTER(struct_rt_bot_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 123
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_patches", "cdecl"):
    rt_bot_patches = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_patches", "cdecl")
    rt_bot_patches.argtypes = [POINTER(struct_rt_bot_internal)]
    rt_bot_patches.restype = POINTER(struct_rt_bot_list)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 124
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_list_free", "cdecl"):
    rt_bot_list_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_list_free", "cdecl")
    rt_bot_list_free.argtypes = [POINTER(struct_rt_bot_list), c_int]
    rt_bot_list_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 127
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_same_orientation", "cdecl"):
    rt_bot_same_orientation = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_same_orientation", "cdecl")
    rt_bot_same_orientation.argtypes = [POINTER(c_int), POINTER(c_int)]
    rt_bot_same_orientation.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 130
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_tess", "cdecl"):
    rt_bot_tess = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_tess", "cdecl")
    rt_bot_tess.argtypes = [POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol)]
    rt_bot_tess.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 136
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_merge", "cdecl"):
    rt_bot_merge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_merge", "cdecl")
    rt_bot_merge.argtypes = [c_size_t, POINTER(POINTER(struct_rt_bot_internal))]
    rt_bot_merge.restype = POINTER(struct_rt_bot_internal)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 141
try:
    rt_bot_minpieces = (c_size_t).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "rt_bot_minpieces")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 142
try:
    rt_bot_tri_per_piece = (c_size_t).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "rt_bot_tri_per_piece")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 143
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_sort_faces", "cdecl"):
    rt_bot_sort_faces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_sort_faces", "cdecl")
    rt_bot_sort_faces.argtypes = [POINTER(struct_rt_bot_internal), c_size_t]
    rt_bot_sort_faces.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 145
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_decimate", "cdecl"):
    rt_bot_decimate = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_decimate", "cdecl")
    rt_bot_decimate.argtypes = [POINTER(struct_rt_bot_internal), fastf_t, fastf_t, fastf_t]
    rt_bot_decimate.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 149
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_bot_decimate_gct", "cdecl"):
    rt_bot_decimate_gct = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_bot_decimate_gct", "cdecl")
    rt_bot_decimate_gct.argtypes = [POINTER(struct_rt_bot_internal), fastf_t]
    rt_bot_decimate_gct.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 37
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_brep_plot", "cdecl"):
    rt_brep_plot = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_brep_plot", "cdecl")
    rt_brep_plot.argtypes = [POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_brep_plot.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 42
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_brep_plot_poly", "cdecl"):
    rt_brep_plot_poly = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_brep_plot_poly", "cdecl")
    rt_brep_plot_poly.argtypes = [POINTER(struct_bu_list), POINTER(struct_db_full_path), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info)]
    rt_brep_plot_poly.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 52
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_brep_valid", "cdecl"):
    rt_brep_valid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_brep_valid", "cdecl")
    rt_brep_valid.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int]
    rt_brep_valid.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 57
for _lib in _libs.values():
    if not _lib.has("rt_brep_normalize", "cdecl"):
        continue
    rt_brep_normalize = _lib.get("rt_brep_normalize", "cdecl")
    rt_brep_normalize.argtypes = [POINTER(struct_rt_db_internal), c_double]
    rt_brep_normalize.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 62
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_brep_plate_mode", "cdecl"):
    rt_brep_plate_mode = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_brep_plate_mode", "cdecl")
    rt_brep_plate_mode.argtypes = [POINTER(struct_rt_db_internal)]
    rt_brep_plate_mode.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 67
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_brep_plate_mode_getvals", "cdecl"):
    rt_brep_plate_mode_getvals = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_brep_plate_mode_getvals", "cdecl")
    rt_brep_plate_mode_getvals.argtypes = [POINTER(c_double), POINTER(c_int), POINTER(struct_rt_db_internal)]
    rt_brep_plate_mode_getvals.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/tor.h: 32
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_num_circular_segments", "cdecl"):
    rt_num_circular_segments = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_num_circular_segments", "cdecl")
    rt_num_circular_segments.argtypes = [c_double, c_double]
    rt_num_circular_segments.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/rhc.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_mk_hyperbola", "cdecl"):
    rt_mk_hyperbola = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_mk_hyperbola", "cdecl")
    rt_mk_hyperbola.argtypes = [POINTER(struct_rt_pnt_node), fastf_t, fastf_t, fastf_t, fastf_t, fastf_t]
    rt_mk_hyperbola.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/cline.h: 38
try:
    rt_cline_radius = (fastf_t).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "rt_cline_radius")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 44
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_comb_import4", "cdecl"):
    rt_comb_import4 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_comb_import4", "cdecl")
    rt_comb_import4.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_bu_external), mat_t, POINTER(struct_db_i), POINTER(struct_resource)]
    rt_comb_import4.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 50
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_comb_export4", "cdecl"):
    rt_comb_export4 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_comb_export4", "cdecl")
    rt_comb_export4.argtypes = [POINTER(struct_bu_external), POINTER(struct_rt_db_internal), c_double, POINTER(struct_db_i), POINTER(struct_resource)]
    rt_comb_export4.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 57
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_comb_describe", "cdecl"):
    db_comb_describe = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_comb_describe", "cdecl")
    db_comb_describe.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_comb_internal), c_int, c_double]
    db_comb_describe.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 65
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_comb_describe", "cdecl"):
    rt_comb_describe = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_comb_describe", "cdecl")
    rt_comb_describe.argtypes = [POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int, c_double]
    rt_comb_describe.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 78
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_comb_get_color", "cdecl"):
    rt_comb_get_color = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_comb_get_color", "cdecl")
    rt_comb_get_color.argtypes = [c_ubyte * int(3), POINTER(struct_rt_comb_internal)]
    rt_comb_get_color.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 88
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_comb_mvall", "cdecl"):
    db_comb_mvall = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_comb_mvall", "cdecl")
    db_comb_mvall.argtypes = [POINTER(struct_directory), POINTER(struct_db_i), String, String, POINTER(struct_bu_ptbl)]
    db_comb_mvall.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 109
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_comb_import5", "cdecl"):
    rt_comb_import5 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_comb_import5", "cdecl")
    rt_comb_import5.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_bu_external), mat_t, POINTER(struct_db_i), POINTER(struct_resource)]
    rt_comb_import5.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/comb.h: 156
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_comb_children", "cdecl"):
    db_comb_children = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_comb_children", "cdecl")
    db_comb_children.argtypes = [POINTER(struct_db_i), POINTER(struct_rt_comb_internal), POINTER(POINTER(POINTER(struct_directory))), POINTER(POINTER(c_int)), POINTER(POINTER(matp_t))]
    db_comb_children.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 34
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_find_paths", "cdecl"):
    rt_find_paths = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_find_paths", "cdecl")
    rt_find_paths.argtypes = [POINTER(struct_db_i), POINTER(struct_directory), POINTER(struct_directory), POINTER(struct_bu_ptbl), POINTER(struct_resource)]
    rt_find_paths.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 40
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_get_solidbitv", "cdecl"):
    rt_get_solidbitv = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_get_solidbitv", "cdecl")
    rt_get_solidbitv.argtypes = [c_size_t, POINTER(struct_resource)]
    rt_get_solidbitv.restype = POINTER(struct_bu_bitv)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 44
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_id_solid", "cdecl"):
    rt_id_solid = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_id_solid", "cdecl")
    rt_id_solid.argtypes = [POINTER(struct_bu_external)]
    rt_id_solid.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 52
class struct_rt_point_labels(Structure):
    pass

struct_rt_point_labels.__slots__ = [
    'str',
    'pt',
]
struct_rt_point_labels._fields_ = [
    ('str', c_char * int(8)),
    ('pt', point_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 60
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_reduce_obj", "cdecl"):
    rt_reduce_obj = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_reduce_obj", "cdecl")
    rt_reduce_obj.argtypes = [POINTER(struct_rt_db_internal), POINTER(struct_rt_db_internal), fastf_t, c_uint]
    rt_reduce_obj.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 67
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_reduce_db", "cdecl"):
    rt_reduce_db = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_reduce_db", "cdecl")
    rt_reduce_db.argtypes = [POINTER(struct_db_i), c_size_t, POINTER(POINTER(c_char)), POINTER(struct_bu_ptbl)]
    rt_reduce_db.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 71
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_generic_xform", "cdecl"):
    rt_generic_xform = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_generic_xform", "cdecl")
    rt_generic_xform.argtypes = [POINTER(struct_rt_db_internal), mat_t, POINTER(struct_rt_db_internal), c_int, POINTER(struct_db_i)]
    rt_generic_xform.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 76
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_generic_make", "cdecl"):
    rt_generic_make = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_generic_make", "cdecl")
    rt_generic_make.argtypes = [POINTER(struct_rt_functab), POINTER(struct_rt_db_internal)]
    rt_generic_make.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/prep.h: 40
class struct_rt_reprep_obj_list(Structure):
    pass

struct_rt_reprep_obj_list.__slots__ = [
    'ntopobjs',
    'topobjs',
    'nunprepped',
    'unprepped',
    'paths',
    'tsp',
    'unprep_regions',
    'old_nsolids',
    'old_nregions',
    'nsolids_unprepped',
    'nregions_unprepped',
]
struct_rt_reprep_obj_list._fields_ = [
    ('ntopobjs', c_size_t),
    ('topobjs', POINTER(POINTER(c_char))),
    ('nunprepped', c_size_t),
    ('unprepped', POINTER(POINTER(c_char))),
    ('paths', struct_bu_ptbl),
    ('tsp', POINTER(POINTER(struct_db_tree_state))),
    ('unprep_regions', struct_bu_ptbl),
    ('old_nsolids', c_size_t),
    ('old_nregions', c_size_t),
    ('nsolids_unprepped', c_size_t),
    ('nregions_unprepped', c_size_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/prep.h: 57
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_unprep", "cdecl"):
    rt_unprep = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_unprep", "cdecl")
    rt_unprep.argtypes = [POINTER(struct_rt_i), POINTER(struct_rt_reprep_obj_list), POINTER(struct_resource)]
    rt_unprep.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/prep.h: 60
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_reprep", "cdecl"):
    rt_reprep = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_reprep", "cdecl")
    rt_reprep.argtypes = [POINTER(struct_rt_i), POINTER(struct_rt_reprep_obj_list), POINTER(struct_resource)]
    rt_reprep.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/prep.h: 63
for _lib in _libs.values():
    if not _lib.has("re_prep_solids", "cdecl"):
        continue
    re_prep_solids = _lib.get("re_prep_solids", "cdecl")
    re_prep_solids.argtypes = [POINTER(struct_rt_i), c_int, POINTER(POINTER(c_char)), POINTER(struct_resource)]
    re_prep_solids.restype = c_int
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 43
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_vlist_copy", "cdecl"):
    rt_vlist_copy = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_vlist_copy", "cdecl")
    rt_vlist_copy.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_list)]
    rt_vlist_copy.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 45
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_vlist_cleanup", "cdecl"):
    rt_vlist_cleanup = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_vlist_cleanup", "cdecl")
    rt_vlist_cleanup.argtypes = []
    rt_vlist_cleanup.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 46
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_vlist_import", "cdecl"):
    rt_vlist_import = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_vlist_import", "cdecl")
    rt_vlist_import.argtypes = [POINTER(struct_bu_list), POINTER(struct_bu_vls), POINTER(c_ubyte)]
    rt_vlist_import.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 49
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_vlblock_init", "cdecl"):
    rt_vlblock_init = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_vlblock_init", "cdecl")
    rt_vlblock_init.argtypes = []
    rt_vlblock_init.restype = POINTER(struct_bn_vlblock)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 59
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_process_uplot_value", "cdecl"):
    rt_process_uplot_value = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_process_uplot_value", "cdecl")
    rt_process_uplot_value.argtypes = [POINTER(POINTER(struct_bu_list)), POINTER(struct_bn_vlblock), POINTER(FILE), c_int, c_double, c_int]
    rt_process_uplot_value.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 72
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_uplot_to_vlist", "cdecl"):
    rt_uplot_to_vlist = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_uplot_to_vlist", "cdecl")
    rt_uplot_to_vlist.argtypes = [POINTER(struct_bn_vlblock), POINTER(FILE), c_double, c_int]
    rt_uplot_to_vlist.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 81
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_label_vlist_verts", "cdecl"):
    rt_label_vlist_verts = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_label_vlist_verts", "cdecl")
    rt_label_vlist_verts.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_bu_list), mat_t, c_double, c_double]
    rt_label_vlist_verts.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/vlist.h: 90
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_label_vlist_faces", "cdecl"):
    rt_label_vlist_faces = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_label_vlist_faces", "cdecl")
    rt_label_vlist_faces.argtypes = [POINTER(struct_bn_vlblock), POINTER(struct_bu_list), mat_t, c_double, c_double]
    rt_label_vlist_faces.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/htbl.h: 35
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_htbl_init", "cdecl"):
    rt_htbl_init = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_htbl_init", "cdecl")
    rt_htbl_init.argtypes = [POINTER(struct_rt_htbl), c_size_t, String]
    rt_htbl_init.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/htbl.h: 40
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_htbl_reset", "cdecl"):
    rt_htbl_reset = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_htbl_reset", "cdecl")
    rt_htbl_reset.argtypes = [POINTER(struct_rt_htbl)]
    rt_htbl_reset.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/htbl.h: 46
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_htbl_free", "cdecl"):
    rt_htbl_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_htbl_free", "cdecl")
    rt_htbl_free.argtypes = [POINTER(struct_rt_htbl)]
    rt_htbl_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/htbl.h: 51
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_htbl_get", "cdecl"):
    rt_htbl_get = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_htbl_get", "cdecl")
    rt_htbl_get.argtypes = [POINTER(struct_rt_htbl)]
    rt_htbl_get.restype = POINTER(struct_hit)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/dspline.h: 38
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_dspline_matrix", "cdecl"):
    rt_dspline_matrix = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_dspline_matrix", "cdecl")
    rt_dspline_matrix.argtypes = [mat_t, String, c_double, c_double]
    rt_dspline_matrix.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/dspline.h: 50
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_dspline4", "cdecl"):
    rt_dspline4 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_dspline4", "cdecl")
    rt_dspline4.argtypes = [mat_t, c_double, c_double, c_double, c_double, c_double]
    rt_dspline4.restype = c_double

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/dspline.h: 67
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_dspline4v", "cdecl"):
    rt_dspline4v = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_dspline4v", "cdecl")
    rt_dspline4v.argtypes = [POINTER(c_double), mat_t, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_double]
    rt_dspline4v.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/dspline.h: 101
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_dspline_n", "cdecl"):
    rt_dspline_n = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_dspline_n", "cdecl")
    rt_dspline_n.argtypes = [POINTER(c_double), mat_t, POINTER(c_double), c_int, c_int, c_double]
    rt_dspline_n.restype = None

enum_anon_63 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_REGION = 0# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_REGION_ID = (ATTR_REGION + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_MATERIAL_ID = (ATTR_REGION_ID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_AIR = (ATTR_MATERIAL_ID + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_LOS = (ATTR_AIR + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_COLOR = (ATTR_LOS + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_SHADER = (ATTR_COLOR + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_INHERIT = (ATTR_SHADER + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_TIMESTAMP = (ATTR_INHERIT + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

ATTR_NULL = (ATTR_TIMESTAMP + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 44

enum_anon_64 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 58

ATTR_STANDARD = 0# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 58

ATTR_USER_DEFINED = (ATTR_STANDARD + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 58

ATTR_UNKNOWN_ORIGIN = (ATTR_USER_DEFINED + 1)# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 58

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 64
class struct_db5_attr_ctype(Structure):
    pass

struct_db5_attr_ctype.__slots__ = [
    'attr_type',
    'is_binary',
    'attr_subtype',
    'name',
    'description',
    'examples',
    'aliases',
    'property',
    'long_description',
]
struct_db5_attr_ctype._fields_ = [
    ('attr_type', c_int),
    ('is_binary', c_int),
    ('attr_subtype', c_int),
    ('name', String),
    ('description', String),
    ('examples', String),
    ('aliases', String),
    ('property', String),
    ('long_description', String),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 83
try:
    db5_attr_std = (POINTER(struct_db5_attr_ctype)).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "db5_attr_std")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 86
class struct_db5_registry(Structure):
    pass

struct_db5_registry.__slots__ = [
    'internal',
]
struct_db5_registry._fields_ = [
    ('internal', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 96
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_attr_registry_init", "cdecl"):
    db5_attr_registry_init = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_attr_registry_init", "cdecl")
    db5_attr_registry_init.argtypes = [POINTER(struct_db5_registry)]
    db5_attr_registry_init.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 104
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_attr_registry_free", "cdecl"):
    db5_attr_registry_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_attr_registry_free", "cdecl")
    db5_attr_registry_free.argtypes = [POINTER(struct_db5_registry)]
    db5_attr_registry_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 112
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_attr_create", "cdecl"):
    db5_attr_create = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_attr_create", "cdecl")
    db5_attr_create.argtypes = [POINTER(struct_db5_registry), c_int, c_int, c_int, String, String, String, String, String, String]
    db5_attr_create.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 129
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_attr_register", "cdecl"):
    db5_attr_register = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_attr_register", "cdecl")
    db5_attr_register.argtypes = [POINTER(struct_db5_registry), POINTER(struct_db5_attr_ctype)]
    db5_attr_register.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 138
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_attr_deregister", "cdecl"):
    db5_attr_deregister = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_attr_deregister", "cdecl")
    db5_attr_deregister.argtypes = [POINTER(struct_db5_registry), String]
    db5_attr_deregister.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 147
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_attr_get", "cdecl"):
    db5_attr_get = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_attr_get", "cdecl")
    db5_attr_get.argtypes = [POINTER(struct_db5_registry), String]
    db5_attr_get.restype = POINTER(struct_db5_attr_ctype)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 156
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_attr_dump", "cdecl"):
    db5_attr_dump = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_attr_dump", "cdecl")
    db5_attr_dump.argtypes = [POINTER(struct_db5_registry)]
    db5_attr_dump.restype = POINTER(POINTER(struct_db5_attr_ctype))

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 169
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_standard_attribute", "cdecl"):
    db5_standard_attribute = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_standard_attribute", "cdecl")
    db5_standard_attribute.argtypes = [c_int]
    db5_standard_attribute.restype = c_char_p

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 183
for _lib in _libs.values():
    if not _lib.has("db5_standard_attribute_def", "cdecl"):
        continue
    db5_standard_attribute_def = _lib.get("db5_standard_attribute_def", "cdecl")
    db5_standard_attribute_def.argtypes = [c_int]
    db5_standard_attribute_def.restype = c_char_p
    break

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 194
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_is_standard_attribute", "cdecl"):
    db5_is_standard_attribute = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_is_standard_attribute", "cdecl")
    db5_is_standard_attribute.argtypes = [String]
    db5_is_standard_attribute.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 209
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_standardize_avs", "cdecl"):
    db5_standardize_avs = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_standardize_avs", "cdecl")
    db5_standardize_avs.argtypes = [POINTER(struct_bu_attribute_value_set)]
    db5_standardize_avs.restype = c_size_t

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 215
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_standardize_attribute", "cdecl"):
    db5_standardize_attribute = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_standardize_attribute", "cdecl")
    db5_standardize_attribute.argtypes = [String]
    db5_standardize_attribute.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 220
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_sync_attr_to_comb", "cdecl"):
    db5_sync_attr_to_comb = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_sync_attr_to_comb", "cdecl")
    db5_sync_attr_to_comb.argtypes = [POINTER(struct_rt_comb_internal), POINTER(struct_bu_attribute_value_set), POINTER(struct_directory)]
    db5_sync_attr_to_comb.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 225
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_sync_comb_to_attr", "cdecl"):
    db5_sync_comb_to_attr = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_sync_comb_to_attr", "cdecl")
    db5_sync_comb_to_attr.argtypes = [POINTER(struct_bu_attribute_value_set), POINTER(struct_rt_comb_internal)]
    db5_sync_comb_to_attr.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 247
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_import_attributes", "cdecl"):
    db5_import_attributes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_import_attributes", "cdecl")
    db5_import_attributes.argtypes = [POINTER(struct_bu_attribute_value_set), POINTER(struct_bu_external)]
    db5_import_attributes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 265
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_export_attributes", "cdecl"):
    db5_export_attributes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_export_attributes", "cdecl")
    db5_export_attributes.argtypes = [POINTER(struct_bu_external), POINTER(struct_bu_attribute_value_set)]
    db5_export_attributes.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 291
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_lookup_by_attr", "cdecl"):
    db_lookup_by_attr = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_lookup_by_attr", "cdecl")
    db_lookup_by_attr.argtypes = [POINTER(struct_db_i), c_int, POINTER(struct_bu_attribute_value_set), c_int]
    db_lookup_by_attr.restype = POINTER(struct_bu_ptbl)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 303
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_put_color_table", "cdecl"):
    db5_put_color_table = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_put_color_table", "cdecl")
    db5_put_color_table.argtypes = [POINTER(struct_db_i)]
    db5_put_color_table.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 304
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_update_ident", "cdecl"):
    db5_update_ident = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_update_ident", "cdecl")
    db5_update_ident.argtypes = [POINTER(struct_db_i), String, c_double]
    db5_update_ident.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 321
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_update_attributes", "cdecl"):
    db5_update_attributes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_update_attributes", "cdecl")
    db5_update_attributes.argtypes = [POINTER(struct_directory), POINTER(struct_bu_attribute_value_set), POINTER(struct_db_i)]
    db5_update_attributes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 332
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_update_attribute", "cdecl"):
    db5_update_attribute = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_update_attribute", "cdecl")
    db5_update_attribute.argtypes = [String, String, String, POINTER(struct_db_i)]
    db5_update_attribute.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 348
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_replace_attributes", "cdecl"):
    db5_replace_attributes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_replace_attributes", "cdecl")
    db5_replace_attributes.argtypes = [POINTER(struct_directory), POINTER(struct_bu_attribute_value_set), POINTER(struct_db_i)]
    db5_replace_attributes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 360
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db5_get_attributes", "cdecl"):
    db5_get_attributes = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db5_get_attributes", "cdecl")
    db5_get_attributes.argtypes = [POINTER(struct_db_i), POINTER(struct_bu_attribute_value_set), POINTER(struct_directory)]
    db5_get_attributes.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/binunif.h: 35
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_mk_binunif", "cdecl"):
    rt_mk_binunif = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_mk_binunif", "cdecl")
    rt_mk_binunif.argtypes = [POINTER(struct_rt_wdb), String, String, c_uint, c_size_t]
    rt_mk_binunif.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/binunif.h: 47
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_binunif_free", "cdecl"):
    rt_binunif_free = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_binunif_free", "cdecl")
    rt_binunif_free.argtypes = [POINTER(struct_rt_binunif_internal)]
    rt_binunif_free.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/binunif.h: 52
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_binunif_dump", "cdecl"):
    rt_binunif_dump = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_binunif_dump", "cdecl")
    rt_binunif_dump.argtypes = [POINTER(struct_rt_binunif_internal)]
    rt_binunif_dump.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/version.h: 37
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_version", "cdecl"):
    rt_version = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_version", "cdecl")
    rt_version.argtypes = []
    rt_version.restype = c_char_p

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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 51
class struct_diff_avp(Structure):
    pass

struct_diff_avp.__slots__ = [
    'name',
    'state',
    'left_value',
    'ancestor_value',
    'right_value',
]
struct_diff_avp._fields_ = [
    ('name', String),
    ('state', c_int),
    ('left_value', String),
    ('ancestor_value', String),
    ('right_value', String),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 58
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("diff_init_avp", "cdecl"):
    diff_init_avp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("diff_init_avp", "cdecl")
    diff_init_avp.argtypes = [POINTER(struct_diff_avp)]
    diff_init_avp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 59
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("diff_free_avp", "cdecl"):
    diff_free_avp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("diff_free_avp", "cdecl")
    diff_free_avp.argtypes = [POINTER(struct_diff_avp)]
    diff_free_avp.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 60
class struct_diff_result(Structure):
    pass

struct_diff_result.__slots__ = [
    'obj_name',
    'diff_tol',
    'dp_left',
    'dp_ancestor',
    'dp_right',
    'param_state',
    'attr_state',
    'param_diffs',
    'attr_diffs',
]
struct_diff_result._fields_ = [
    ('obj_name', String),
    ('diff_tol', POINTER(struct_bn_tol)),
    ('dp_left', POINTER(struct_directory)),
    ('dp_ancestor', POINTER(struct_directory)),
    ('dp_right', POINTER(struct_directory)),
    ('param_state', c_int),
    ('attr_state', c_int),
    ('param_diffs', POINTER(struct_bu_ptbl)),
    ('attr_diffs', POINTER(struct_bu_ptbl)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 71
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("diff_init_result", "cdecl"):
    diff_init_result = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("diff_init_result", "cdecl")
    diff_init_result.argtypes = [POINTER(struct_diff_result), POINTER(struct_bn_tol), String]
    diff_init_result.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 72
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("diff_free_result", "cdecl"):
    diff_free_result = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("diff_free_result", "cdecl")
    diff_free_result.argtypes = [POINTER(struct_diff_result)]
    diff_free_result.restype = None

enum_anon_65 = c_int# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 84

DB_COMPARE_ALL = 0# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 84

DB_COMPARE_PARAM = 1# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 84

DB_COMPARE_ATTRS = 2# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 84

db_compare_criteria_t = enum_anon_65# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 84

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 92
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_avs_diff", "cdecl"):
    db_avs_diff = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_avs_diff", "cdecl")
    db_avs_diff.argtypes = [POINTER(struct_bu_attribute_value_set), POINTER(struct_bu_attribute_value_set), POINTER(struct_bn_tol), CFUNCTYPE(UNCHECKED(c_int), String, String, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), String, String, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), String, String, String, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), String, String, POINTER(None)), POINTER(None)]
    db_avs_diff.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 105
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_avs_diff3", "cdecl"):
    db_avs_diff3 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_avs_diff3", "cdecl")
    db_avs_diff3.argtypes = [POINTER(struct_bu_attribute_value_set), POINTER(struct_bu_attribute_value_set), POINTER(struct_bu_attribute_value_set), POINTER(struct_bn_tol), CFUNCTYPE(UNCHECKED(c_int), String, String, String, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), String, String, String, String, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), String, String, String, String, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), String, String, String, String, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), String, String, POINTER(None)), POINTER(None)]
    db_avs_diff3.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 157
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_diff_dp", "cdecl"):
    db_diff_dp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_diff_dp", "cdecl")
    db_diff_dp.argtypes = [POINTER(struct_db_i), POINTER(struct_db_i), POINTER(struct_directory), POINTER(struct_directory), POINTER(struct_bn_tol), db_compare_criteria_t, POINTER(struct_diff_result)]
    db_diff_dp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 185
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_diff3_dp", "cdecl"):
    db_diff3_dp = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_diff3_dp", "cdecl")
    db_diff3_dp.argtypes = [POINTER(struct_db_i), POINTER(struct_db_i), POINTER(struct_db_i), POINTER(struct_directory), POINTER(struct_directory), POINTER(struct_directory), POINTER(struct_bn_tol), db_compare_criteria_t, POINTER(struct_diff_result)]
    db_diff3_dp.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 214
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_diff", "cdecl"):
    db_diff = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_diff", "cdecl")
    db_diff.argtypes = [POINTER(struct_db_i), POINTER(struct_db_i), POINTER(struct_bn_tol), db_compare_criteria_t, POINTER(struct_bu_ptbl)]
    db_diff.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 234
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("db_diff3", "cdecl"):
    db_diff3 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("db_diff3", "cdecl")
    db_diff3.argtypes = [POINTER(struct_db_i), POINTER(struct_db_i), POINTER(struct_db_i), POINTER(struct_bn_tol), db_compare_criteria_t, POINTER(struct_bu_ptbl)]
    db_diff3.restype = c_int

TFLOAT = c_double# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 65

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 78
class struct_TIE_3_s(Structure):
    pass

struct_TIE_3_s.__slots__ = [
    'v',
]
struct_TIE_3_s._fields_ = [
    ('v', TFLOAT * int(3)),
]

TIE_3 = struct_TIE_3_s# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 78

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 80
class struct_tie_ray_s(Structure):
    pass

struct_tie_ray_s.__slots__ = [
    'pos',
    'dir',
    'depth',
    'kdtree_depth',
]
struct_tie_ray_s._fields_ = [
    ('pos', point_t),
    ('dir', vect_t),
    ('depth', c_short),
    ('kdtree_depth', c_short),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 87
class struct_tie_id_s(Structure):
    pass

struct_tie_id_s.__slots__ = [
    'pos',
    'norm',
    'dist',
    'alpha',
    'beta',
]
struct_tie_id_s._fields_ = [
    ('pos', point_t),
    ('norm', vect_t),
    ('dist', fastf_t),
    ('alpha', fastf_t),
    ('beta', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 95
class struct_tie_tri_s(Structure):
    pass

struct_tie_tri_s.__slots__ = [
    'data',
    'v',
    'ptr',
    'b',
]
struct_tie_tri_s._fields_ = [
    ('data', TIE_3 * int(3)),
    ('v', TFLOAT * int(2)),
    ('ptr', POINTER(None)),
    ('b', c_uint32),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 107
class struct_tie_kdtree_s(Structure):
    pass

struct_tie_kdtree_s.__slots__ = [
    'axis',
    'b',
    'data',
]
struct_tie_kdtree_s._fields_ = [
    ('axis', c_float),
    ('b', c_uint32),
    ('data', POINTER(None)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 114
class struct_tie_s(Structure):
    pass

struct_tie_s.__slots__ = [
    'rays_fired',
    'kdtree',
    'max_depth',
    'tri_num',
    'tri_num_alloc',
    'tri_list',
    'stat',
    'kdmethod',
    'min',
    'max',
    'amin',
    'amax',
    'mid',
    'radius',
]
struct_tie_s._fields_ = [
    ('rays_fired', c_uint64),
    ('kdtree', POINTER(struct_tie_kdtree_s)),
    ('max_depth', c_uint),
    ('tri_num', c_uint),
    ('tri_num_alloc', c_uint),
    ('tri_list', POINTER(struct_tie_tri_s)),
    ('stat', c_int),
    ('kdmethod', c_uint),
    ('min', point_t),
    ('max', point_t),
    ('amin', vect_t),
    ('amax', vect_t),
    ('mid', vect_t),
    ('radius', fastf_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 128
try:
    tie_check_degenerate = (c_int).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "tie_check_degenerate")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 129
try:
    TIE_PREC = (fastf_t).in_dll(_libs["/usr/brlcad/dev-7.31.0/lib/librt.so"], "TIE_PREC")
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 139
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("tie_init_double", "cdecl"):
    tie_init_double = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("tie_init_double", "cdecl")
    tie_init_double.argtypes = [POINTER(struct_tie_s), c_uint, c_uint]
    tie_init_double.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 140
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("tie_free_double", "cdecl"):
    tie_free_double = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("tie_free_double", "cdecl")
    tie_free_double.argtypes = [POINTER(struct_tie_s)]
    tie_free_double.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 141
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("tie_prep_double", "cdecl"):
    tie_prep_double = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("tie_prep_double", "cdecl")
    tie_prep_double.argtypes = [POINTER(struct_tie_s)]
    tie_prep_double.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 142
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("tie_work_double", "cdecl"):
    tie_work_double = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("tie_work_double", "cdecl")
    tie_work_double.argtypes = [POINTER(struct_tie_s), POINTER(struct_tie_ray_s), POINTER(struct_tie_id_s), CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(struct_tie_ray_s), POINTER(struct_tie_id_s), POINTER(struct_tie_tri_s), POINTER(None)), POINTER(None)]
    tie_work_double.restype = POINTER(c_ubyte)
    tie_work_double.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 143
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("tie_push_double", "cdecl"):
    tie_push_double = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("tie_push_double", "cdecl")
    tie_push_double.argtypes = [POINTER(struct_tie_s), POINTER(POINTER(TIE_3)), c_uint, POINTER(None), c_uint]
    tie_push_double.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 144
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("tie_kdtree_free_double", "cdecl"):
    tie_kdtree_free_double = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("tie_kdtree_free_double", "cdecl")
    tie_kdtree_free_double.argtypes = [POINTER(struct_tie_s)]
    tie_kdtree_free_double.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 145
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("tie_kdtree_prep_double", "cdecl"):
    tie_kdtree_prep_double = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("tie_kdtree_prep_double", "cdecl")
    tie_kdtree_prep_double.argtypes = [POINTER(struct_tie_s)]
    tie_kdtree_prep_double.restype = None

dbfloat_t = c_float# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 83

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 88
class struct_ident(Structure):
    pass

struct_ident.__slots__ = [
    'i_id',
    'i_units',
    'i_version',
    'i_title',
    'i_byteorder',
    'i_floattype',
]
struct_ident._fields_ = [
    ('i_id', c_char),
    ('i_units', c_char),
    ('i_version', c_char * int(6)),
    ('i_title', c_char * int(72)),
    ('i_byteorder', c_char),
    ('i_floattype', c_char),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 119
class struct_solidrec(Structure):
    pass

struct_solidrec.__slots__ = [
    's_id',
    's_type',
    's_name',
    's_cgtype',
    's_values',
]
struct_solidrec._fields_ = [
    ('s_id', c_char),
    ('s_type', c_char),
    ('s_name', c_char * int(16)),
    ('s_cgtype', c_short),
    ('s_values', dbfloat_t * int(24)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 194
class struct_combination(Structure):
    pass

struct_combination.__slots__ = [
    'c_id',
    'c_flags',
    'c_name',
    'c_regionid',
    'c_aircode',
    'c_pad1',
    'c_pad2',
    'c_material',
    'c_los',
    'c_override',
    'c_rgb',
    'c_matname',
    'c_matparm',
    'c_inherit',
]
struct_combination._fields_ = [
    ('c_id', c_char),
    ('c_flags', c_char),
    ('c_name', c_char * int(16)),
    ('c_regionid', c_short),
    ('c_aircode', c_short),
    ('c_pad1', c_short),
    ('c_pad2', c_short),
    ('c_material', c_short),
    ('c_los', c_short),
    ('c_override', c_char),
    ('c_rgb', c_ubyte * int(3)),
    ('c_matname', c_char * int(32)),
    ('c_matparm', c_char * int(60)),
    ('c_inherit', c_char),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 218
class struct_member(Structure):
    pass

struct_member.__slots__ = [
    'm_id',
    'm_relation',
    'm_brname',
    'm_instname',
    'm_pad1',
    'm_mat',
    'm_pad2',
]
struct_member._fields_ = [
    ('m_id', c_char),
    ('m_relation', c_char),
    ('m_brname', c_char * int(16)),
    ('m_instname', c_char * int(16)),
    ('m_pad1', c_short),
    ('m_mat', dbfloat_t * int(16)),
    ('m_pad2', c_short),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 228
class struct_material_rec(Structure):
    pass

struct_material_rec.__slots__ = [
    'md_id',
    'md_flags',
    'md_low',
    'md_hi',
    'md_r',
    'md_g',
    'md_b',
    'md_material',
]
struct_material_rec._fields_ = [
    ('md_id', c_char),
    ('md_flags', c_char),
    ('md_low', c_short),
    ('md_hi', c_short),
    ('md_r', c_ubyte),
    ('md_g', c_ubyte),
    ('md_b', c_ubyte),
    ('md_material', c_char * int(100)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 239
class struct_B_solid(Structure):
    pass

struct_B_solid.__slots__ = [
    'B_id',
    'B_pad',
    'B_name',
    'B_nsurf',
    'B_unused',
]
struct_B_solid._fields_ = [
    ('B_id', c_char),
    ('B_pad', c_char),
    ('B_name', c_char * int(16)),
    ('B_nsurf', c_short),
    ('B_unused', dbfloat_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 247
class struct_b_surf(Structure):
    pass

struct_b_surf.__slots__ = [
    'd_id',
    'd_order',
    'd_kv_size',
    'd_ctl_size',
    'd_geom_type',
    'd_nknots',
    'd_nctls',
]
struct_b_surf._fields_ = [
    ('d_id', c_char),
    ('d_order', c_short * int(2)),
    ('d_kv_size', c_short * int(2)),
    ('d_ctl_size', c_short * int(2)),
    ('d_geom_type', c_short),
    ('d_nknots', c_short),
    ('d_nctls', c_short),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 257
class struct_polyhead(Structure):
    pass

struct_polyhead.__slots__ = [
    'p_id',
    'p_pad1',
    'p_name',
]
struct_polyhead._fields_ = [
    ('p_id', c_char),
    ('p_pad1', c_char),
    ('p_name', c_char * int(16)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 263
class struct_polydata(Structure):
    pass

struct_polydata.__slots__ = [
    'q_id',
    'q_count',
    'q_verts',
    'q_norms',
]
struct_polydata._fields_ = [
    ('q_id', c_char),
    ('q_count', c_char),
    ('q_verts', (dbfloat_t * int(3)) * int(5)),
    ('q_norms', (dbfloat_t * int(3)) * int(5)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 270
class struct_ars_rec(Structure):
    pass

struct_ars_rec.__slots__ = [
    'a_id',
    'a_type',
    'a_name',
    'a_m',
    'a_n',
    'a_curlen',
    'a_totlen',
    'a_pad',
    'a_xmax',
    'a_xmin',
    'a_ymax',
    'a_ymin',
    'a_zmax',
    'a_zmin',
]
struct_ars_rec._fields_ = [
    ('a_id', c_char),
    ('a_type', c_char),
    ('a_name', c_char * int(16)),
    ('a_m', c_short),
    ('a_n', c_short),
    ('a_curlen', c_short),
    ('a_totlen', c_short),
    ('a_pad', c_short),
    ('a_xmax', dbfloat_t),
    ('a_xmin', dbfloat_t),
    ('a_ymax', dbfloat_t),
    ('a_ymin', dbfloat_t),
    ('a_zmax', dbfloat_t),
    ('a_zmin', dbfloat_t),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 289
class struct_ars_ext(Structure):
    pass

struct_ars_ext.__slots__ = [
    'b_id',
    'b_type',
    'b_n',
    'b_ngranule',
    'b_pad',
    'b_values',
]
struct_ars_ext._fields_ = [
    ('b_id', c_char),
    ('b_type', c_char),
    ('b_n', c_short),
    ('b_ngranule', c_short),
    ('b_pad', c_short),
    ('b_values', dbfloat_t * int((8 * 3))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 298
class struct_strsol(Structure):
    pass

struct_strsol.__slots__ = [
    'ss_id',
    'ss_pad',
    'ss_name',
    'ss_keyword',
    'ss_args',
]
struct_strsol._fields_ = [
    ('ss_id', c_char),
    ('ss_pad', c_char),
    ('ss_name', c_char * int(16)),
    ('ss_keyword', c_char * int(16)),
    ('ss_args', c_char * int(4)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 308
class struct_arbn_rec(Structure):
    pass

struct_arbn_rec.__slots__ = [
    'n_id',
    'n_pad',
    'n_name',
    'n_neqn',
    'n_grans',
]
struct_arbn_rec._fields_ = [
    ('n_id', c_char),
    ('n_pad', c_char),
    ('n_name', c_char * int(16)),
    ('n_neqn', c_ubyte * int(4)),
    ('n_grans', c_ubyte * int(4)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 317
class struct_exported_pipe_pnt(Structure):
    pass

struct_exported_pipe_pnt.__slots__ = [
    'epp_coord',
    'epp_bendradius',
    'epp_id',
    'epp_od',
]
struct_exported_pipe_pnt._fields_ = [
    ('epp_coord', c_ubyte * int((8 * 3))),
    ('epp_bendradius', c_ubyte * int(8)),
    ('epp_id', c_ubyte * int(8)),
    ('epp_od', c_ubyte * int(8)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 324
class struct_pipewire_rec(Structure):
    pass

struct_pipewire_rec.__slots__ = [
    'pwr_id',
    'pwr_pad',
    'pwr_name',
    'pwr_pt_count',
    'pwr_count',
    'pwr_data',
]
struct_pipewire_rec._fields_ = [
    ('pwr_id', c_char),
    ('pwr_pad', c_char),
    ('pwr_name', c_char * int(16)),
    ('pwr_pt_count', c_ubyte * int(4)),
    ('pwr_count', c_ubyte * int(4)),
    ('pwr_data', struct_exported_pipe_pnt * int(1)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 333
class struct_particle_rec(Structure):
    pass

struct_particle_rec.__slots__ = [
    'p_id',
    'p_pad',
    'p_name',
    'p_v',
    'p_h',
    'p_vrad',
    'p_hrad',
]
struct_particle_rec._fields_ = [
    ('p_id', c_char),
    ('p_pad', c_char),
    ('p_name', c_char * int(16)),
    ('p_v', c_ubyte * int((8 * 3))),
    ('p_h', c_ubyte * int((8 * 3))),
    ('p_vrad', c_ubyte * int(8)),
    ('p_hrad', c_ubyte * int(8)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 343
class struct_nmg_rec(Structure):
    pass

struct_nmg_rec.__slots__ = [
    'N_id',
    'N_version',
    'N_name',
    'N_pad2',
    'N_count',
    'N_structs',
]
struct_nmg_rec._fields_ = [
    ('N_id', c_char),
    ('N_version', c_char),
    ('N_name', c_char * int(16)),
    ('N_pad2', c_char * int(2)),
    ('N_count', c_ubyte * int(4)),
    ('N_structs', c_ubyte * int((26 * 4))),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 352
class struct_extr_rec(Structure):
    pass

struct_extr_rec.__slots__ = [
    'ex_id',
    'ex_pad',
    'ex_name',
    'ex_V',
    'ex_h',
    'ex_uvec',
    'ex_vvec',
    'ex_key',
    'ex_count',
]
struct_extr_rec._fields_ = [
    ('ex_id', c_char),
    ('ex_pad', c_char),
    ('ex_name', c_char * int(16)),
    ('ex_V', c_ubyte * int((8 * 3))),
    ('ex_h', c_ubyte * int((8 * 3))),
    ('ex_uvec', c_ubyte * int((8 * 3))),
    ('ex_vvec', c_ubyte * int((8 * 3))),
    ('ex_key', c_ubyte * int(4)),
    ('ex_count', c_ubyte * int(4)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 365
class struct_sketch_rec(Structure):
    pass

struct_sketch_rec.__slots__ = [
    'skt_id',
    'skt_pad',
    'skt_name',
    'skt_V',
    'skt_uvec',
    'skt_vvec',
    'skt_vert_count',
    'skt_seg_count',
    'skt_count',
]
struct_sketch_rec._fields_ = [
    ('skt_id', c_char),
    ('skt_pad', c_char),
    ('skt_name', c_char * int(16)),
    ('skt_V', c_ubyte * int((8 * 3))),
    ('skt_uvec', c_ubyte * int((8 * 3))),
    ('skt_vvec', c_ubyte * int((8 * 3))),
    ('skt_vert_count', c_ubyte * int(4)),
    ('skt_seg_count', c_ubyte * int(4)),
    ('skt_count', c_ubyte * int(4)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 377
class struct_annot_rec(Structure):
    pass

struct_annot_rec.__slots__ = [
    'ant_id',
    'ant_pad',
    'ant_name',
    'ant_V',
    'ant_vert_count',
    'ant_seg_count',
    'ant_count',
]
struct_annot_rec._fields_ = [
    ('ant_id', c_char),
    ('ant_pad', c_char),
    ('ant_name', c_char * int(16)),
    ('ant_V', c_ubyte * int((8 * 3))),
    ('ant_vert_count', c_ubyte * int(4)),
    ('ant_seg_count', c_ubyte * int(4)),
    ('ant_count', c_ubyte * int(4)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 387
class struct_script_rec(Structure):
    pass

struct_script_rec.__slots__ = [
    'script_id',
    'script_pad',
    'script_name',
]
struct_script_rec._fields_ = [
    ('script_id', c_char),
    ('script_pad', c_char),
    ('script_name', c_char * int(16)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 393
class struct_cline_rec(Structure):
    pass

struct_cline_rec.__slots__ = [
    'cli_id',
    'cli_pad',
    'cli_name',
    'cli_V',
    'cli_h',
    'cli_radius',
    'cli_thick',
]
struct_cline_rec._fields_ = [
    ('cli_id', c_char),
    ('cli_pad', c_char),
    ('cli_name', c_char * int(16)),
    ('cli_V', c_ubyte * int((8 * 3))),
    ('cli_h', c_ubyte * int((8 * 3))),
    ('cli_radius', c_ubyte * int(8)),
    ('cli_thick', c_ubyte * int(8)),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 403
class struct_bot_rec(Structure):
    pass

struct_bot_rec.__slots__ = [
    'bot_id',
    'bot_pad',
    'bot_name',
    'bot_nrec',
    'bot_orientation',
    'bot_mode',
    'bot_err_mode',
    'bot_num_verts',
    'bot_num_triangles',
    'bot_data',
]
struct_bot_rec._fields_ = [
    ('bot_id', c_char),
    ('bot_pad', c_char),
    ('bot_name', c_char * int(16)),
    ('bot_nrec', c_ubyte * int(4)),
    ('bot_orientation', c_ubyte),
    ('bot_mode', c_ubyte),
    ('bot_err_mode', c_ubyte),
    ('bot_num_verts', c_ubyte * int(4)),
    ('bot_num_triangles', c_ubyte * int(4)),
    ('bot_data', c_ubyte * int(1)),
]

union_record.__slots__ = [
    'u_id',
    'u_size',
    'i',
    's',
    'c',
    'M',
    'md',
    'B',
    'd',
    'p',
    'q',
    'a',
    'b',
    'ss',
    'n',
    'pwr',
    'part',
    'nmg',
    'extr',
    'skt',
    'ant',
    'scr',
    'cli',
    'bot',
]
union_record._fields_ = [
    ('u_id', c_char),
    ('u_size', c_char * int(128)),
    ('i', struct_ident),
    ('s', struct_solidrec),
    ('c', struct_combination),
    ('M', struct_member),
    ('md', struct_material_rec),
    ('B', struct_B_solid),
    ('d', struct_b_surf),
    ('p', struct_polyhead),
    ('q', struct_polydata),
    ('a', struct_ars_rec),
    ('b', struct_ars_ext),
    ('ss', struct_strsol),
    ('n', struct_arbn_rec),
    ('pwr', struct_pipewire_rec),
    ('part', struct_particle_rec),
    ('nmg', struct_nmg_rec),
    ('extr', struct_extr_rec),
    ('skt', struct_sketch_rec),
    ('ant', struct_annot_rec),
    ('scr', struct_script_rec),
    ('cli', struct_cline_rec),
    ('bot', struct_bot_rec),
]

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 505
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_fastf_float", "cdecl"):
    rt_fastf_float = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_fastf_float", "cdecl")
    rt_fastf_float.argtypes = [POINTER(fastf_t), POINTER(dbfloat_t), c_int, c_int]
    rt_fastf_float.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 508
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_mat_dbmat", "cdecl"):
    rt_mat_dbmat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_mat_dbmat", "cdecl")
    rt_mat_dbmat.argtypes = [POINTER(fastf_t), POINTER(dbfloat_t), c_int]
    rt_mat_dbmat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 511
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("rt_dbmat_mat", "cdecl"):
    rt_dbmat_mat = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("rt_dbmat_mat", "cdecl")
    rt_dbmat_mat.argtypes = [POINTER(dbfloat_t), POINTER(fastf_t)]
    rt_dbmat_mat.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/arb_edit.h: 382
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("ext4to6", "cdecl"):
    ext4to6 = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("ext4to6", "cdecl")
    ext4to6.argtypes = [c_int, c_int, c_int, POINTER(struct_rt_arb_internal), (fastf_t * int(4)) * int(7)]
    ext4to6.restype = None

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/arb_edit.h: 393
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("mv_edge", "cdecl"):
    mv_edge = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("mv_edge", "cdecl")
    mv_edge.argtypes = [POINTER(struct_rt_arb_internal), vect_t, c_int, c_int, c_int, c_int, vect_t, POINTER(struct_bn_tol), (fastf_t * int(4)) * int(7)]
    mv_edge.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/arb_edit.h: 403
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("arb_extrude", "cdecl"):
    arb_extrude = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("arb_extrude", "cdecl")
    arb_extrude.argtypes = [POINTER(struct_rt_arb_internal), c_int, fastf_t, POINTER(struct_bn_tol), (fastf_t * int(4)) * int(7)]
    arb_extrude.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/arb_edit.h: 424
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("arb_permute", "cdecl"):
    arb_permute = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("arb_permute", "cdecl")
    arb_permute.argtypes = [POINTER(struct_rt_arb_internal), String, POINTER(struct_bn_tol)]
    arb_permute.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/arb_edit.h: 429
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("arb_mirror_face_axis", "cdecl"):
    arb_mirror_face_axis = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("arb_mirror_face_axis", "cdecl")
    arb_mirror_face_axis.argtypes = [POINTER(struct_rt_arb_internal), (fastf_t * int(4)) * int(7), c_int, String, POINTER(struct_bn_tol)]
    arb_mirror_face_axis.restype = c_int

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/arb_edit.h: 439
if _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].has("arb_edit", "cdecl"):
    arb_edit = _libs["/usr/brlcad/dev-7.31.0/lib/librt.so"].get("arb_edit", "cdecl")
    arb_edit.argtypes = [POINTER(struct_rt_arb_internal), (fastf_t * int(4)) * int(7), c_int, c_int, vect_t, POINTER(struct_bn_tol)]
    arb_edit.restype = c_int

# /usr/include/linux/limits.h: 13
try:
    PATH_MAX = 4096
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/common.h: 341
def LIKELY(expression):
    return expression

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

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 236
try:
    SMALL_FASTF = 1e-77
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 461
def NEAR_ZERO(val, epsilon):
    return ((val > (-epsilon)) and (val < epsilon))

# /usr/brlcad/dev-7.31.0/include/brlcad/vmath.h: 527
def NEAR_EQUAL(_a, _b, _tol):
    return (NEAR_ZERO ((_a - _b), _tol))

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

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 47
try:
    ANIM_STEER_NEW = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/anim.h: 48
try:
    ANIM_STEER_END = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 65
try:
    BN_VLIST_CHUNK = 35
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 73
try:
    BN_VLIST_NULL = cast(0, POINTER(struct_bn_vlist))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 78
try:
    BN_VLIST_LINE_MOVE = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 79
try:
    BN_VLIST_LINE_DRAW = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 80
try:
    BN_VLIST_POLY_START = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 81
try:
    BN_VLIST_POLY_MOVE = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 82
try:
    BN_VLIST_POLY_DRAW = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 83
try:
    BN_VLIST_POLY_END = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 84
try:
    BN_VLIST_POLY_VERTNORM = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 85
try:
    BN_VLIST_TRI_START = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 86
try:
    BN_VLIST_TRI_MOVE = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 87
try:
    BN_VLIST_TRI_DRAW = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 88
try:
    BN_VLIST_TRI_END = 10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 89
try:
    BN_VLIST_TRI_VERTNORM = 11
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 90
try:
    BN_VLIST_POINT_DRAW = 12
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 91
try:
    BN_VLIST_POINT_SIZE = 13
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 92
try:
    BN_VLIST_LINE_WIDTH = 14
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 93
try:
    BN_VLIST_DISPLAY_MAT = 15
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 94
try:
    BN_VLIST_MODEL_MAT = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 95
try:
    BN_VLIST_CMD_MAX = 16
except:
    pass

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 76
try:
    ID_NULL = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 77
try:
    ID_TOR = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 78
try:
    ID_TGC = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 79
try:
    ID_ELL = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 80
try:
    ID_ARB8 = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 81
try:
    ID_ARS = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 82
try:
    ID_HALF = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 83
try:
    ID_REC = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 84
try:
    ID_POLY = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 85
try:
    ID_BSPLINE = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 86
try:
    ID_SPH = 10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 87
try:
    ID_NMG = 11
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 88
try:
    ID_EBM = 12
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 89
try:
    ID_VOL = 13
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 90
try:
    ID_ARBN = 14
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 91
try:
    ID_PIPE = 15
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 92
try:
    ID_PARTICLE = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 93
try:
    ID_RPC = 17
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 94
try:
    ID_RHC = 18
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 95
try:
    ID_EPA = 19
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 96
try:
    ID_EHY = 20
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 97
try:
    ID_ETO = 21
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 98
try:
    ID_GRIP = 22
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 99
try:
    ID_JOINT = 23
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 100
try:
    ID_HF = 24
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 101
try:
    ID_DSP = 25
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 102
try:
    ID_SKETCH = 26
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 103
try:
    ID_EXTRUDE = 27
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 104
try:
    ID_SUBMODEL = 28
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 105
try:
    ID_CLINE = 29
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 106
try:
    ID_BOT = 30
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 112
try:
    ID_MAX_SOLID = 46
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 117
try:
    ID_COMBINATION = 31
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 118
try:
    ID_UNUSED1 = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 119
try:
    ID_BINUNIF = 33
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 120
try:
    ID_UNUSED2 = 34
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 121
try:
    ID_CONSTRAINT = 39
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 125
try:
    ID_SUPERELL = 35
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 126
try:
    ID_METABALL = 36
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 127
try:
    ID_BREP = 37
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 128
try:
    ID_HYP = 38
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 129
try:
    ID_REVOLVE = 40
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 130
try:
    ID_PNTS = 41
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 131
try:
    ID_ANNOT = 42
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 132
try:
    ID_HRT = 43
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 133
try:
    ID_DATUM = 44
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 134
try:
    ID_SCRIPT = 45
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 135
try:
    ID_MAXIMUM = 46
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 147
try:
    RT_DBNHASH = 8192
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 165
def RT_DBHASH(sum):
    return ((c_size_t (ord_if_char(sum))).value & (RT_DBNHASH - 1))

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 169
try:
    RT_DEFAULT_MINPIECES = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 170
try:
    RT_DEFAULT_TRIS_PER_PIECE = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 171
try:
    RT_DEFAULT_MINTIE = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 174
try:
    BACKING_DIST = (-2.0)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 175
try:
    OFFSET_DIST = 0.01
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 180
def RT_BADNUM(n):
    return (not ((n >= (-INFINITY)) and (n <= INFINITY)))

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 181
def RT_BADVEC(v):
    return (((RT_BADNUM ((v [X]))) or (RT_BADNUM ((v [Y])))) or (RT_BADNUM ((v [Z]))))

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 184
try:
    RT_MAXLINE = 10240
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/defines.h: 186
try:
    RT_PART_NUBSPT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 36
def MKOP(x):
    return x

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 38
try:
    OP_SOLID = (MKOP (1))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 39
try:
    OP_UNION = (MKOP (2))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 40
try:
    OP_INTERSECT = (MKOP (3))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 41
try:
    OP_SUBTRACT = (MKOP (4))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 42
try:
    OP_XOR = (MKOP (5))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 43
try:
    OP_REGION = (MKOP (6))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 44
try:
    OP_NOP = (MKOP (7))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 46
try:
    OP_NOT = (MKOP (8))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 47
try:
    OP_GUARD = (MKOP (9))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 48
try:
    OP_XNOP = (MKOP (10))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 49
try:
    OP_NMG_TESS = (MKOP (11))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 51
try:
    OP_DB_LEAF = (MKOP (12))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/op.h: 52
try:
    OP_FREE = (MKOP (13))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 67
try:
    DB5HDR_MAGIC1 = 118
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 68
try:
    DB5HDR_MAGIC2 = 53
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 71
try:
    DB5HDR_HFLAGS_DLI_MASK = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 72
try:
    DB5HDR_HFLAGS_DLI_APPLICATION_DATA_OBJECT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 73
try:
    DB5HDR_HFLAGS_DLI_HEADER_OBJECT = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 74
try:
    DB5HDR_HFLAGS_DLI_FREE_STORAGE = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 75
try:
    DB5HDR_HFLAGS_HIDDEN_OBJECT = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 76
try:
    DB5HDR_HFLAGS_NAME_PRESENT = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 77
try:
    DB5HDR_HFLAGS_OBJECT_WIDTH_MASK = 192
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 78
try:
    DB5HDR_HFLAGS_OBJECT_WIDTH_SHIFT = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 79
try:
    DB5HDR_HFLAGS_NAME_WIDTH_MASK = 24
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 80
try:
    DB5HDR_HFLAGS_NAME_WIDTH_SHIFT = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 82
try:
    DB5HDR_WIDTHCODE_8BIT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 83
try:
    DB5HDR_WIDTHCODE_16BIT = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 84
try:
    DB5HDR_WIDTHCODE_32BIT = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 85
try:
    DB5HDR_WIDTHCODE_64BIT = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 88
try:
    DB5HDR_AFLAGS_ZZZ_MASK = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 89
try:
    DB5HDR_AFLAGS_PRESENT = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 90
try:
    DB5HDR_AFLAGS_WIDTH_MASK = 192
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 91
try:
    DB5HDR_AFLAGS_WIDTH_SHIFT = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 94
try:
    DB5HDR_BFLAGS_ZZZ_MASK = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 95
try:
    DB5HDR_BFLAGS_PRESENT = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 96
try:
    DB5HDR_BFLAGS_WIDTH_MASK = 192
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 97
try:
    DB5HDR_BFLAGS_WIDTH_SHIFT = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 108
try:
    DB5_GLOBAL_OBJECT_NAME = '_GLOBAL'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 111
try:
    DB5_ZZZ_UNCOMPRESSED = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 112
try:
    DB5_ZZZ_GNU_GZIP = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 113
try:
    DB5_ZZZ_BURROUGHS_WHEELER = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 117
try:
    DB5_MAJORTYPE_RESERVED = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 118
try:
    DB5_MAJORTYPE_BRLCAD = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 119
try:
    DB5_MAJORTYPE_ATTRIBUTE_ONLY = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 120
try:
    DB5_MAJORTYPE_BINARY_MASK = 24
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 121
try:
    DB5_MAJORTYPE_BINARY_UNIF = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 122
try:
    DB5_MAJORTYPE_BINARY_MIME = 10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 128
try:
    DB5_MINORTYPE_RESERVED = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 129
try:
    DB5_MINORTYPE_BRLCAD_TOR = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 130
try:
    DB5_MINORTYPE_BRLCAD_TGC = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 131
try:
    DB5_MINORTYPE_BRLCAD_ELL = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 132
try:
    DB5_MINORTYPE_BRLCAD_ARB8 = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 133
try:
    DB5_MINORTYPE_BRLCAD_ARS = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 134
try:
    DB5_MINORTYPE_BRLCAD_HALF = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 135
try:
    DB5_MINORTYPE_BRLCAD_REC = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 136
try:
    DB5_MINORTYPE_BRLCAD_POLY = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 137
try:
    DB5_MINORTYPE_BRLCAD_BSPLINE = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 138
try:
    DB5_MINORTYPE_BRLCAD_SPH = 10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 139
try:
    DB5_MINORTYPE_BRLCAD_NMG = 11
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 140
try:
    DB5_MINORTYPE_BRLCAD_EBM = 12
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 141
try:
    DB5_MINORTYPE_BRLCAD_VOL = 13
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 142
try:
    DB5_MINORTYPE_BRLCAD_ARBN = 14
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 143
try:
    DB5_MINORTYPE_BRLCAD_PIPE = 15
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 144
try:
    DB5_MINORTYPE_BRLCAD_PARTICLE = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 145
try:
    DB5_MINORTYPE_BRLCAD_RPC = 17
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 146
try:
    DB5_MINORTYPE_BRLCAD_RHC = 18
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 147
try:
    DB5_MINORTYPE_BRLCAD_EPA = 19
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 148
try:
    DB5_MINORTYPE_BRLCAD_EHY = 20
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 149
try:
    DB5_MINORTYPE_BRLCAD_ETO = 21
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 150
try:
    DB5_MINORTYPE_BRLCAD_GRIP = 22
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 151
try:
    DB5_MINORTYPE_BRLCAD_JOINT = 23
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 152
try:
    DB5_MINORTYPE_BRLCAD_HF = 24
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 153
try:
    DB5_MINORTYPE_BRLCAD_DSP = 25
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 154
try:
    DB5_MINORTYPE_BRLCAD_SKETCH = 26
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 155
try:
    DB5_MINORTYPE_BRLCAD_EXTRUDE = 27
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 156
try:
    DB5_MINORTYPE_BRLCAD_SUBMODEL = 28
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 157
try:
    DB5_MINORTYPE_BRLCAD_CLINE = 29
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 158
try:
    DB5_MINORTYPE_BRLCAD_BOT = 30
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 159
try:
    DB5_MINORTYPE_BRLCAD_COMBINATION = 31
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 163
try:
    DB5_MINORTYPE_BRLCAD_SUPERELL = 35
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 164
try:
    DB5_MINORTYPE_BRLCAD_METABALL = 36
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 165
try:
    DB5_MINORTYPE_BRLCAD_BREP = 37
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 166
try:
    DB5_MINORTYPE_BRLCAD_HYP = 38
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 168
try:
    DB5_MINORTYPE_BRLCAD_CONSTRAINT = 39
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 170
try:
    DB5_MINORTYPE_BRLCAD_REVOLVE = 40
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 171
try:
    DB5_MINORTYPE_BRLCAD_PNTS = 41
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 172
try:
    DB5_MINORTYPE_BRLCAD_ANNOT = 42
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 173
try:
    DB5_MINORTYPE_BRLCAD_HRT = 43
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 174
try:
    DB5_MINORTYPE_BRLCAD_DATUM = 44
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 175
try:
    DB5_MINORTYPE_BRLCAD_SCRIPT = 45
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 178
try:
    DB5_MINORTYPE_BINU_WID_MASK = 48
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 179
try:
    DB5_MINORTYPE_BINU_SGN_MASK = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 180
try:
    DB5_MINORTYPE_BINU_ATM_MASK = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 181
try:
    DB5_MINORTYPE_BINU_FLOAT = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 182
try:
    DB5_MINORTYPE_BINU_DOUBLE = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 183
try:
    DB5_MINORTYPE_BINU_8BITINT_U = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 184
try:
    DB5_MINORTYPE_BINU_16BITINT_U = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 185
try:
    DB5_MINORTYPE_BINU_32BITINT_U = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 186
try:
    DB5_MINORTYPE_BINU_64BITINT_U = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 187
try:
    DB5_MINORTYPE_BINU_8BITINT = 12
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 188
try:
    DB5_MINORTYPE_BINU_16BITINT = 13
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 189
try:
    DB5_MINORTYPE_BINU_32BITINT = 14
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 190
try:
    DB5_MINORTYPE_BINU_64BITINT = 15
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 33
try:
    NMG_DEBUG_PL_ANIM = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 34
try:
    NMG_DEBUG_PL_SLOW = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 35
try:
    NMG_DEBUG_GRAPHCL = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 36
try:
    NMG_DEBUG_PL_LOOP = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 37
try:
    NMG_DEBUG_PLOTEM = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 38
try:
    NMG_DEBUG_POLYSECT = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 39
try:
    NMG_DEBUG_VERIFY = 64
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 40
try:
    NMG_DEBUG_BOOL = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 41
try:
    NMG_DEBUG_CLASSIFY = 256
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 42
try:
    NMG_DEBUG_BOOLEVAL = 512
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 43
try:
    NMG_DEBUG_BASIC = 1024
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 44
try:
    NMG_DEBUG_MESH = 2048
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 45
try:
    NMG_DEBUG_MESH_EU = 4096
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 46
try:
    NMG_DEBUG_POLYTO = 8192
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 47
try:
    NMG_DEBUG_LABEL_PTS = 16384
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 48
try:
    NMG_DEBUG_UNUSED1 = 32768
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 49
try:
    NMG_DEBUG_NMGRT = 65536
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 50
try:
    NMG_DEBUG_FINDEU = 131072
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 51
try:
    NMG_DEBUG_CMFACE = 262144
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 52
try:
    NMG_DEBUG_CUTLOOP = 524288
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 53
try:
    NMG_DEBUG_VU_SORT = 1048576
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 54
try:
    NMG_DEBUG_FCUT = 2097152
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 55
try:
    NMG_DEBUG_RT_SEGS = 4194304
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 56
try:
    NMG_DEBUG_RT_ISECT = 8388608
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 57
try:
    NMG_DEBUG_TRI = 16777216
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 58
try:
    NMG_DEBUG_PNT_FU = 33554432
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 59
try:
    NMG_DEBUG_MANIF = 67108864
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 60
try:
    NMG_DEBUG_UNUSED2 = 134217728
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 61
try:
    NMG_DEBUG_UNUSED3 = 268435456
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 62
try:
    NMG_DEBUG_UNUSED4 = 536870912
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 63
try:
    NMG_DEBUG_UNUSED5 = 1073741824
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 64
try:
    NMG_DEBUG_UNUSED6 = 2147483648
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg/debug.h: 65
try:
    NMG_DEBUG_FORMAT = (((((((((((((((((((((((((((((((('\\020' + '\\040UNUSED6') + '\\037UNUSED5') + '\\036UNUSED4') + '\\035UNUSED3') + '\\034UNUSED2') + '\\033MANIF') + '\\032PT_FU') + '\\031TRI') + '\\030RT_ISECT') + '\\027RT_SEGS') + '\\026FCUT') + '\\025VU_SORT') + '\\024CUTLOOP') + '\\023CMFACE') + '\\022FINDEU') + '\\021NMGRT') + '\\020UNUSED1') + '\\017LABEL_PTS') + '\\016POLYTO') + '\\015MESH_EU') + '\\014MESH') + '\\013BASIC') + '\\012BOOLEVAL') + '\\011CLASSIFY') + '\\010BOOL') + '\\7VERIFY') + '\\6POLYSECT') + '\\5PLOTEM') + '\\4PL_LOOP') + '\\3GRAPHCL') + '\\2PL_SLOW') + '\\1PL_ANIM')
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 103
try:
    NMG_BOOL_SUB = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 104
try:
    NMG_BOOL_ADD = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 105
try:
    NMG_BOOL_ISECT = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 108
try:
    NMG_CLASS_Unknown = (-1)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 109
try:
    NMG_CLASS_AinB = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 110
try:
    NMG_CLASS_AonBshared = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 111
try:
    NMG_CLASS_AonBanti = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 112
try:
    NMG_CLASS_AoutB = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 113
try:
    NMG_CLASS_BinA = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 114
try:
    NMG_CLASS_BonAshared = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 115
try:
    NMG_CLASS_BonAanti = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 116
try:
    NMG_CLASS_BoutA = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 119
try:
    OT_NONE = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 120
try:
    OT_SAME = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 121
try:
    OT_OPPOSITE = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 122
try:
    OT_UNSPEC = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 123
try:
    OT_BOOLPLACE = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 552
def NMG_FREESTRUCT(p, str):
    return (nmg_free (p, 'NMG_FREESTRUCT'))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 619
def NMG_ARE_EUS_ADJACENT(_eu1, _eu2):
    return (((((((_eu1.contents.vu_p).value).contents.v_p).value) == ((((_eu2.contents.vu_p).value).contents.v_p).value)) and (((((((_eu1.contents.eumate_p).value).contents.vu_p).value).contents.v_p).value) == ((((((_eu2.contents.eumate_p).value).contents.vu_p).value).contents.v_p).value))) or ((((((_eu1.contents.vu_p).value).contents.v_p).value) == ((((((_eu2.contents.eumate_p).value).contents.vu_p).value).contents.v_p).value)) and (((((((_eu1.contents.eumate_p).value).contents.vu_p).value).contents.v_p).value) == ((((_eu2.contents.vu_p).value).contents.v_p).value))))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 626
def EDGESADJ(_e1, _e2):
    return (NMG_ARE_EUS_ADJACENT (_e1, _e2))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 629
def PLPRINT(_s, _pl):
    return (bu_log ('%s %gx + %gy + %gz = %g\\n', _s, (_pl [0]), (_pl [1]), (_pl [2]), (_pl [3])))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 634
try:
    NMG_FPI_FIRST = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 637
try:
    NMG_FPI_PERGEOM = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 641
try:
    NMG_FPI_PERUSE = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 658
try:
    PREEXIST = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 659
try:
    NEWEXIST = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 718
def NMG_INDEX_VALUE(_tab, _index):
    return (_tab [_index])

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 719
def NMG_INDEX_TEST(_tab, _p):
    return (_tab [(_p.contents.index)])

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 722
def NMG_INDEX_TEST_AND_SET(_tab, _p):
    return ((_tab [((_p.contents.index).value)]) == 0) and 1 or 0

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 723
def NMG_INDEX_IS_SET(_tab, _p):
    return (NMG_INDEX_TEST (_tab, _p))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 724
def NMG_INDEX_FIRST_TIME(_tab, _p):
    return (NMG_INDEX_TEST_AND_SET (_tab, _p))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 726
def NMG_INDEX_GET(_tab, _p):
    return (_tab [(_p.contents.index)])

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 736
try:
    NMG_0MANIFOLD = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 737
try:
    NMG_1MANIFOLD = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 738
try:
    NMG_2MANIFOLD = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 739
try:
    NMG_DANGLING = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 740
try:
    NMG_3MANIFOLD = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 743
def NMG_MANIFOLDS(_t, _p):
    return (NMG_INDEX_VALUE (_t, (_p.contents.index)))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 749
try:
    NMG_VLIST_STYLE_VECTOR = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 750
try:
    NMG_VLIST_STYLE_POLYGON = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 751
try:
    NMG_VLIST_STYLE_VISUALIZE_NORMALS = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 752
try:
    NMG_VLIST_STYLE_USE_VU_NORMALS = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 753
try:
    NMG_VLIST_STYLE_NO_SURFACES = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 851
try:
    RT_NURB_SPLIT_ROW = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 852
try:
    RT_NURB_SPLIT_COL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 853
try:
    RT_NURB_SPLIT_FLAT = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 870
try:
    RT_NURB_PT_XY = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 871
try:
    RT_NURB_PT_XYZ = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 872
try:
    RT_NURB_PT_UV = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 873
try:
    RT_NURB_PT_DATA = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 874
try:
    RT_NURB_PT_PROJ = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 876
try:
    RT_NURB_PT_RATIONAL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 877
try:
    RT_NURB_PT_NONRAT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 879
def RT_NURB_MAKE_PT_TYPE(n, t, h):
    return (((n << 5) | (t << 1)) | h)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 880
def RT_NURB_EXTRACT_COORDS(pt):
    return (pt >> 5)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 881
def RT_NURB_EXTRACT_PT_TYPE(pt):
    return ((pt >> 1) & 15)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 882
def RT_NURB_IS_PT_RATIONAL(pt):
    return (pt & 1)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 883
def RT_NURB_STRIDE(pt):
    return ((RT_NURB_EXTRACT_COORDS (pt)) * sizeof(fastf_t))

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 885
try:
    DEBUG_NMG_SPLINE = 256
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 964
try:
    NMG_HIT_LIST = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 965
try:
    NMG_MISS_LIST = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 970
def HMG_INBOUND_STATE(_hm):
    return ((((_hm.contents.in_out).value) & 240) >> 4)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 971
def HMG_OUTBOUND_STATE(_hm):
    return (((_hm.contents.in_out).value) & 15)

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 974
try:
    NMG_RAY_STATE_INSIDE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 975
try:
    NMG_RAY_STATE_ON = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 976
try:
    NMG_RAY_STATE_OUTSIDE = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 977
try:
    NMG_RAY_STATE_ANY = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 979
try:
    HMG_HIT_IN_IN = 17
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 980
try:
    HMG_HIT_IN_OUT = 20
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 981
try:
    HMG_HIT_OUT_IN = 65
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 982
try:
    HMG_HIT_OUT_OUT = 68
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 983
try:
    HMG_HIT_IN_ON = 18
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 984
try:
    HMG_HIT_ON_IN = 33
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 985
try:
    HMG_HIT_ON_ON = 34
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 986
try:
    HMG_HIT_OUT_ON = 66
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 987
try:
    HMG_HIT_ON_OUT = 36
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 988
try:
    HMG_HIT_ANY_ANY = 136
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 990
try:
    NMG_VERT_ENTER = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 991
try:
    NMG_VERT_ENTER_LEAVE = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 992
try:
    NMG_VERT_LEAVE = (-1)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 993
try:
    NMG_VERT_UNKNOWN = (-2)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 995
try:
    NMG_HITMISS_SEG_IN = 6909440
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 996
try:
    NMG_HITMISS_SEG_OUT = 1869968384
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1071
try:
    HIT = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1072
try:
    MISS = 0
except:
    pass

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

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 53
try:
    NAMELEN = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 159
try:
    METABALL_METABALL = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 160
try:
    METABALL_ISOPOTENTIAL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 161
try:
    METABALL_BLOB = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 177
try:
    WDB_METABALLPT_TYPE_POINT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 178
try:
    WDB_METABALLPT_TYPE_LINE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 179
try:
    WDB_METABALL_PNT_NULL = cast(0, POINTER(struct_wdb_metaball_pnt))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 290
def RT_NURB_GET_CONTROL_POINT(_s, _u, _v):
    return ((_s.contents.ctl_points) [(((_v * (((_s.contents.s_size).value) [0])) + _u) * (RT_NURB_EXTRACT_COORDS (((_s.contents.pt_type).value))))])

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 305
def RT_BREP_TEST_MAGIC(_p):
    return (_p and ((cast(_p, POINTER(c_uint32))[0]) == (c_uint32 (ord_if_char(RT_BREP_INTERNAL_MAGIC))).value))

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 322
try:
    RT_EBM_NAME_LEN = 256
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 336
try:
    RT_EBM_SRC_FILE = b'f'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 337
try:
    RT_EBM_SRC_OBJ = b'o'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 348
try:
    RT_VOL_NAME_LEN = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 449
try:
    RT_PARTICLE_TYPE_SPHERE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 450
try:
    RT_PARTICLE_TYPE_CYLINDER = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 451
try:
    RT_PARTICLE_TYPE_CONE = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 555
try:
    DSP_NAME_LEN = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 567
try:
    DSP_CUT_DIR_ADAPT = b'a'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 568
try:
    DSP_CUT_DIR_llUR = b'l'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 569
try:
    DSP_CUT_DIR_ULlr = b'L'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 579
try:
    RT_DSP_SRC_V4_FILE = b'4'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 580
try:
    RT_DSP_SRC_FILE = b'f'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 581
try:
    RT_DSP_SRC_OBJ = b'o'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 650
try:
    SKETCH_NAME_LEN = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 835
try:
    RT_BOT_UNORIENTED = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 836
try:
    RT_BOT_CCW = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 837
try:
    RT_BOT_CW = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 840
try:
    RT_BOT_SURFACE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 841
try:
    RT_BOT_SOLID = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 848
try:
    RT_BOT_PLATE = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 854
try:
    RT_BOT_PLATE_NOCOS = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 857
try:
    RT_BOT_HAS_SURFACE_NORMALS = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 858
try:
    RT_BOT_USE_NORMALS = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 859
try:
    RT_BOT_USE_FLOATS = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 860
try:
    RT_BOT_HAS_TEXTURE_UVS = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 861
try:
    RT_BOT_HAS_UNUSED1 = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 862
try:
    RT_BOT_HAS_UNUSED2 = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 863
try:
    RT_BOT_HAS_UNUSED3 = 64
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 864
try:
    RT_BOT_HAS_UNUSED4 = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 991
try:
    RT_TXT_POS_BL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 992
try:
    RT_TXT_POS_BC = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 993
try:
    RT_TXT_POS_BR = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 994
try:
    RT_TXT_POS_ML = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 995
try:
    RT_TXT_POS_MC = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 996
try:
    RT_TXT_POS_MR = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 997
try:
    RT_TXT_POS_TL = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 998
try:
    RT_TXT_POS_TC = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 999
try:
    RT_TXT_POS_TR = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 61
def DB_FULL_PATH_POP(_pp):
    return (((_pp.contents.fp_len).value) > 0) and (((_pp.contents.fp_len).value) - 1) or (_pp.contents.fp_len)

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 63
def DB_FULL_PATH_CUR_DIR(_pp):
    return ((_pp.contents.fp_names) [(((_pp.contents.fp_len).value) - 1)])

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 64
def DB_FULL_PATH_CUR_BOOL(_pp):
    return ((_pp.contents.fp_bool) [(((_pp.contents.fp_len).value) - 1)])

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 65
def DB_FULL_PATH_SET_CUR_BOOL(_pp, _i):
    return _i

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 66
def DB_FULL_PATH_ROOT_DIR(_pp):
    return ((_pp.contents.fp_names) [0])

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 67
def DB_FULL_PATH_GET(_pp, _i):
    return ((_pp.contents.fp_names) [_i])

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 68
def DB_FULL_PATH_GET_BOOL(_pp, _i):
    return ((_pp.contents.fp_bool) [_i])

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 69
def DB_FULL_PATH_SET_BOOL(_pp, _i, _j):
    return _j

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 119
try:
    DB_FP_PRINT_BOOL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 120
try:
    DB_FP_PRINT_TYPE = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 121
try:
    DB_FP_PRINT_MATRIX = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 43
try:
    RT_DEBUG_OFF = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 48
try:
    RT_DEBUG_ALLRAYS = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 49
try:
    RT_DEBUG_ALLHITS = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 50
try:
    RT_DEBUG_SHOOT = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 51
try:
    RT_DEBUG_INSTANCE = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 54
try:
    RT_DEBUG_DB = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 55
try:
    RT_DEBUG_SOLIDS = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 56
try:
    RT_DEBUG_REGIONS = 64
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 57
try:
    RT_DEBUG_ARB8 = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 59
try:
    RT_DEBUG_SPLINE = 256
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 60
try:
    RT_DEBUG_ANIM = 512
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 61
try:
    RT_DEBUG_ANIM_FULL = 1024
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 62
try:
    RT_DEBUG_VOL = 2048
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 65
try:
    RT_DEBUG_ROOTS = 4096
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 66
try:
    RT_DEBUG_PARTITION = 8192
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 67
try:
    RT_DEBUG_CUT = 16384
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 68
try:
    RT_DEBUG_BOXING = 32768
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 70
try:
    RT_DEBUG_UNUSED_0 = 65536
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 71
try:
    RT_DEBUG_UNUSED_1 = 131072
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 72
try:
    RT_DEBUG_FDIFF = 262144
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 73
try:
    RT_DEBUG_PARALLEL = 524288
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 75
try:
    RT_DEBUG_CUTDETAIL = 1048576
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 76
try:
    RT_DEBUG_TREEWALK = 2097152
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 77
try:
    RT_DEBUG_TESTING = 4194304
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 78
try:
    RT_DEBUG_ADVANCE = 8388608
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 80
try:
    RT_DEBUG_MATH = 16777216
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 83
try:
    RT_DEBUG_EBM = 33554432
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 84
try:
    RT_DEBUG_HF = 67108864
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 86
try:
    RT_DEBUG_MESHING = 134217728
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 87
try:
    RT_DEBUG_UNUSED_3 = 268435456
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 88
try:
    RT_DEBUG_UNUSED_4 = 536870912
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 91
try:
    RT_DEBUG_PL_SOLIDS = 1073741824
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 92
try:
    RT_DEBUG_PL_BOX = 2147483648
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 95
try:
    RT_DEBUG_FORMAT = (((((((((((((((((((((((((((((((('\\020' + '\\040PL_BOX') + '\\037PL_SOLIDS') + '\\036UNUSED_4') + '\\035UNUSED_3') + '\\034UNUSED_2') + '\\033HF') + '\\032EBM') + '\\031MATH') + '\\030ADVANCE') + '\\027TESTING') + '\\026TREEWALK') + '\\025CUTDETAIL') + '\\024PARALLEL') + '\\023FDIFF') + '\\022UNUSED_1') + '\\021UNUSED_0') + '\\020BOXING') + '\\017CUT') + '\\016PARTITION') + '\\015ROOTS') + '\\014VOL') + '\\013ANIM_FULL') + '\\012ANIM') + '\\011SPLINE') + '\\010ARB8') + '\\7REGIONS') + '\\6SOLIDS') + '\\5DB') + '\\4INSTANCE') + '\\3SHOOT') + '\\2ALLHITS') + '\\1ALLRAYS')
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/debug.h: 143
try:
    RT_G_DEBUG = rt_debug
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/tol.h: 77
try:
    RT_LEN_TOL = 1e-08
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/tol.h: 78
try:
    RT_DOT_TOL = 0.001
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/tol.h: 79
try:
    RT_PCOEF_TOL = 1e-10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/tol.h: 80
try:
    RT_ROOT_TOL = 1e-05
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 42
try:
    MAP_NULL = cast(0, POINTER(struct_mem_map))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 59
try:
    MATER_NULL = cast(0, POINTER(struct_mater))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 56
try:
    ANM_RSTACK = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 57
try:
    ANM_RARC = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 58
try:
    ANM_LMUL = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 59
try:
    ANM_RMUL = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 60
try:
    ANM_RBOTH = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 67
try:
    RT_ANP_REPLACE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 68
try:
    RT_ANP_APPEND = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 88
try:
    RT_AN_MATRIX = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 89
try:
    RT_AN_MATERIAL = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 90
try:
    RT_AN_COLOR = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 91
try:
    RT_AN_SOLID = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 92
try:
    RT_AN_TEMPERATURE = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 94
try:
    ANIM_NULL = cast(0, POINTER(struct_animate))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 78
try:
    RT_DIR_NULL = cast(0, POINTER(struct_directory))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 85
try:
    RT_DIR_SOLID = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 86
try:
    RT_DIR_COMB = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 87
try:
    RT_DIR_REGION = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 88
try:
    RT_DIR_HIDDEN = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 89
try:
    RT_DIR_NON_GEOM = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 90
try:
    RT_DIR_USED = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 91
try:
    RT_DIR_INMEM = 256
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 94
try:
    LOOKUP_NOISY = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 95
try:
    LOOKUP_QUIET = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h: 90
try:
    DBI_NULL = cast(0, POINTER(struct_db_i))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 60
try:
    REGION_NON_FASTGEN = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 61
try:
    REGION_FASTGEN_PLATE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 62
try:
    REGION_FASTGEN_VOLUME = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 65
try:
    REGION_NULL = cast(0, POINTER(struct_region))
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

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 34
try:
    CORNER_PTS = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 49
try:
    RAY_NULL = cast(0, POINTER(struct_xray))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 71
try:
    HIT_NULL = cast(0, POINTER(struct_hit))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 123
try:
    CURVE_NULL = cast(0, POINTER(struct_curvature))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/seg.h: 65
try:
    RT_SEG_NULL = cast(0, POINTER(struct_seg))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 68
try:
    PT_NULL = cast(0, POINTER(struct_partition))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 78
def RT_PT_MIDDLE_LEN(p):
    return ((String (ord_if_char(pointer(((p.contents.RT_PT_MIDDLE_END).value))))).value - (String (ord_if_char(pointer(((p.contents.RT_PT_MIDDLE_START).value))))).value)

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/application.h: 190
try:
    RT_APPLICATION_NULL = cast(0, POINTER(struct_application))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 128
try:
    NMG_PCA_EDGE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 129
try:
    NMG_PCA_EDGE_VERTEX = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 130
try:
    NMG_PCA_VERTEX = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 98
try:
    TS_SOFAR_MINUS = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 99
try:
    TS_SOFAR_INTER = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 100
try:
    TS_SOFAR_REGION = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 186
try:
    TREE_NULL = cast(0, POINTER(union_tree))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 233
class struct_tree_list(Structure):
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 233
try:
    TREE_LIST_NULL = cast(0, POINTER(struct_tree_list))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 110
try:
    RESOURCE_NULL = cast(0, POINTER(struct_resource))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 67
try:
    CUT_CUTNODE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 68
try:
    CUT_BOXNODE = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 69
try:
    CUT_MAXIMUM = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 78
try:
    CUTTER_NULL = cast(0, POINTER(union_cutter))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 80
try:
    RT_WDB_TYPE_DB_DISK = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 81
try:
    RT_WDB_TYPE_DB_DISK_APPEND_ONLY = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 82
try:
    RT_WDB_TYPE_DB_INMEM = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 83
try:
    RT_WDB_TYPE_DB_INMEM_APPEND_ONLY = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 132
try:
    RTI_NULL = cast(0, POINTER(struct_rt_i))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 36
try:
    RT_MINVIEWSIZE = 0.0001
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 37
try:
    RT_MINVIEWSCALE = 5e-05
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 121
try:
    RT_SORT_UNSORTED = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 122
try:
    RT_SORT_CLOSEST_TO_START = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 145
try:
    RT_SELECTION_NOP = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 146
try:
    RT_SELECTION_TRANSLATION = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 79
def RTFUNCTAB_FUNC_PREP_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), POINTER(struct_rt_db_internal), POINTER(struct_rt_i))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 85
def RTFUNCTAB_FUNC_SHOT_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), POINTER(struct_xray), POINTER(struct_application), POINTER(struct_seg))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 88
def RTFUNCTAB_FUNC_PRINT_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_soltab))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 93
def RTFUNCTAB_FUNC_NORM_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_hit), POINTER(struct_soltab), POINTER(struct_xray))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 101
def RTFUNCTAB_FUNC_PIECE_SHOT_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_piecestate), POINTER(struct_rt_piecelist), c_double, POINTER(struct_xray), POINTER(struct_application), POINTER(struct_seg))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 106
def RTFUNCTAB_FUNC_PIECE_HITSEGS_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_rt_piecestate), POINTER(struct_seg), POINTER(struct_application))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 112
def RTFUNCTAB_FUNC_UV_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_application), POINTER(struct_soltab), POINTER(struct_hit), POINTER(struct_uvcoord))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 117
def RTFUNCTAB_FUNC_CURVE_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_curvature), POINTER(struct_hit), POINTER(struct_soltab))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 120
def RTFUNCTAB_FUNC_CLASS_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), vect_t, vect_t, POINTER(struct_bn_tol))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 123
def RTFUNCTAB_FUNC_FREE_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_soltab))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 130
def RTFUNCTAB_FUNC_PLOT_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_list), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol), POINTER(struct_rt_view_info))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 134
def RTFUNCTAB_FUNC_ADAPTIVE_PLOT_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_rt_view_info))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 141
def RTFUNCTAB_FUNC_VSHOT_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(POINTER(struct_soltab)), POINTER(POINTER(struct_xray)), POINTER(struct_seg), c_int, POINTER(struct_application))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 148
def RTFUNCTAB_FUNC_TESS_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bg_tess_tol), POINTER(struct_bn_tol))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 153
def RTFUNCTAB_FUNC_TNURB_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_nmgregion)), POINTER(struct_model), POINTER(struct_rt_db_internal), POINTER(struct_bn_tol))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 158
def RTFUNCTAB_FUNC_BREP_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(POINTER(ON_Brep)), POINTER(struct_rt_db_internal), POINTER(struct_bn_tol))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 165
def RTFUNCTAB_FUNC_IMPORT5_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_bu_external), mat_t, POINTER(struct_db_i), POINTER(struct_resource))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 172
def RTFUNCTAB_FUNC_EXPORT5_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_external), POINTER(struct_rt_db_internal), c_double, POINTER(struct_db_i), POINTER(struct_resource))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 179
def RTFUNCTAB_FUNC_IMPORT4_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_bu_external), mat_t, POINTER(struct_db_i), POINTER(struct_resource))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 186
def RTFUNCTAB_FUNC_EXPORT4_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_external), POINTER(struct_rt_db_internal), c_double, POINTER(struct_db_i), POINTER(struct_resource))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 189
def RTFUNCTAB_FUNC_IFREE_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_rt_db_internal))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 195
def RTFUNCTAB_FUNC_DESCRIBE_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int, c_double)))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 200
def RTFUNCTAB_FUNC_XFORM_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), mat_t, POINTER(struct_rt_db_internal), c_int, POINTER(struct_db_i))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 207
def RTFUNCTAB_FUNC_GET_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), String)))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 210
def RTFUNCTAB_FUNC_ADJUST_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_db_internal), c_int, POINTER(POINTER(c_char)))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 213
def RTFUNCTAB_FUNC_FORM_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_bu_vls), POINTER(struct_rt_functab))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 216
def RTFUNCTAB_FUNC_MAKE_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_rt_functab), POINTER(struct_rt_db_internal))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 219
def RTFUNCTAB_FUNC_PARAMS_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_pc_pc_set), POINTER(struct_rt_db_internal))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 226
def RTFUNCTAB_FUNC_BBOX_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(point_t), POINTER(point_t), POINTER(struct_bn_tol))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 229
def RTFUNCTAB_FUNC_VOLUME_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(fastf_t), POINTER(struct_rt_db_internal))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 232
def RTFUNCTAB_FUNC_SURF_AREA_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(fastf_t), POINTER(struct_rt_db_internal))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 235
def RTFUNCTAB_FUNC_CENTROID_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(point_t), POINTER(struct_rt_db_internal))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 240
def RTFUNCTAB_FUNC_ORIENTED_BBOX_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_arb_internal), POINTER(struct_rt_db_internal), fastf_t)))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 245
def RTFUNCTAB_FUNC_FIND_SELECTIONS_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(POINTER(struct_rt_selection_set)), POINTER(struct_rt_db_internal), POINTER(struct_rt_selection_query))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 255
def RTFUNCTAB_FUNC_EVALUATE_SELECTION_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(POINTER(struct_rt_selection)), POINTER(struct_rt_db_internal), c_int, POINTER(struct_rt_selection), POINTER(struct_rt_selection))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 262
def RTFUNCTAB_FUNC_PROCESS_SELECTION_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_rt_db_internal), POINTER(struct_db_i), POINTER(struct_rt_selection), POINTER(struct_rt_selection_operation))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 266
def RTFUNCTAB_FUNC_PREP_SERIALIZE_CAST(_func):
    return cast(cast(_func, POINTER(CFUNCTYPE(UNCHECKED(None), ))), POINTER(CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_soltab), POINTER(struct_rt_db_internal), POINTER(struct_bu_external), POINTER(c_size_t))))

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 146
try:
    DB_SEARCH_TREE = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 147
try:
    DB_SEARCH_FLAT = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 148
try:
    DB_SEARCH_HIDDEN = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 149
try:
    DB_SEARCH_RETURN_UNIQ_DP = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 150
try:
    DB_SEARCH_QUIET = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 181
try:
    DB_LS_PRIM = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 182
try:
    DB_LS_COMB = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 183
try:
    DB_LS_REGION = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 184
try:
    DB_LS_HIDDEN = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 185
try:
    DB_LS_NON_GEOM = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 186
try:
    DB_LS_TOPS = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 55
try:
    DB_OPEN_READONLY = 'r'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_io.h: 60
try:
    DB_OPEN_READWRITE = 'rw'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 49
try:
    RT_BREP_OPENNURBS = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 50
try:
    RT_BREP_UV_PARAM = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/brep.h: 51
try:
    RT_BREP_EDGE_CRACK = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 62
try:
    RT_REDUCE_OBJ_PRESERVE_VOLUME = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 228
def ATTR_STD(attr):
    return (db5_standard_attribute ((db5_standardize_attribute (attr))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/solid.h: 68
try:
    SOLID_NULL = cast(0, POINTER(struct_solid))
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/solid.h: 86
def LAST_SOLID(_sp):
    return (DB_FULL_PATH_CUR_DIR (pointer((_sp.contents.s_fullpath))))

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/solid.h: 87
def FIRST_SOLID(_sp):
    return (((_sp.contents.s_fullpath).fp_names) [0])

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 40
try:
    DIFF_EMPTY = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 41
try:
    DIFF_UNCHANGED = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 42
try:
    DIFF_REMOVED = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 43
try:
    DIFF_ADDED = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 44
try:
    DIFF_CHANGED = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 45
try:
    DIFF_CONFLICT = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 52
try:
    TIE_PRECISION = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 55
try:
    TIE_CHECK_DEGENERATE = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 57
try:
    TIE_KDTREE_FAST = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 58
try:
    TIE_KDTREE_OPTIMAL = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 73
try:
    NAMESIZE = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 85
try:
    DB_MINREC = 128
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 92
try:
    ID_NO_UNIT = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 93
try:
    ID_MM_UNIT = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 94
try:
    ID_CM_UNIT = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 95
try:
    ID_M_UNIT = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 96
try:
    ID_IN_UNIT = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 97
try:
    ID_FT_UNIT = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 99
try:
    ID_UM_UNIT = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 100
try:
    ID_KM_UNIT = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 101
try:
    ID_YD_UNIT = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 102
try:
    ID_MI_UNIT = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 104
try:
    ID_VERSION = 'v4'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 108
try:
    ID_BY_UNKNOWN = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 109
try:
    ID_BY_VAX = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 110
try:
    ED_BY_IBM = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 112
try:
    ID_FT_UNKNOWN = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 113
try:
    ID_FT_VAX = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 114
try:
    ID_FT_IBM = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 115
try:
    ID_FT_IEEE = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 116
try:
    ID_FT_CRAY = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 122
try:
    RPP = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 123
try:
    BOX = 2
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 124
try:
    RAW = 3
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 125
try:
    ARB4 = 4
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 126
try:
    ARB5 = 5
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 127
try:
    ARB6 = 6
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 128
try:
    ARB7 = 7
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 129
try:
    ARB8 = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 130
try:
    ELL = 9
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 131
try:
    ELL1 = 10
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 132
try:
    SPH = 11
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 133
try:
    RCC = 12
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 134
try:
    REC = 13
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 135
try:
    TRC = 14
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 136
try:
    TEC = 15
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 137
try:
    TOR = 16
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 138
try:
    TGC = 17
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 139
try:
    GENTGC = 18
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 140
try:
    GENELL = 19
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 141
try:
    GENARB8 = 20
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 142
try:
    ARS = 21
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 143
try:
    ARSCONT = 22
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 144
try:
    ELLG = 23
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 145
try:
    HALFSPACE = 24
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 146
try:
    SPLINE = 25
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 147
try:
    RPC = 26
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 148
try:
    RHC = 27
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 149
try:
    EPA = 28
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 150
try:
    EHY = 29
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 151
try:
    ETO = 30
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 152
try:
    GRP = 31
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 153
try:
    SUPERELL = 32
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 154
try:
    HYP = 33
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 197
try:
    DBV4_NON_REGION = b' '
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 198
try:
    DBV4_NON_REGION_NULL = b'\\0'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 199
try:
    DBV4_REGION = b'R'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 200
try:
    DBV4_REGION_FASTGEN_PLATE = b'P'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 201
try:
    DBV4_REGION_FASTGEN_VOLUME = b'V'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 214
try:
    DB_INH_LOWER = 0
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 215
try:
    DB_INH_HIGHER = 1
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 302
try:
    DB_SS_NGRAN = 8
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 303
try:
    DB_SS_LEN = (((DB_SS_NGRAN * DB_MINREC) - (2 * NAMESIZE)) - 2)
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 424
try:
    ID_IDENT = b'I'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 425
try:
    ID_SOLID = b'S'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 426
try:
    ID_COMB = b'C'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 427
try:
    ID_MEMB = b'M'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 428
try:
    ID_ARS_A = b'A'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 429
try:
    ID_ARS_B = b'B'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 430
try:
    ID_FREE = b'F'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 431
try:
    ID_P_HEAD = b'P'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 432
try:
    ID_P_DATA = b'Q'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 433
try:
    ID_BSOLID = b'b'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 434
try:
    ID_BSURF = b'D'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 435
try:
    ID_MATERIAL = b'm'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 436
try:
    DBID_STRSOL = b's'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 437
try:
    DBID_ARBN = b'n'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 438
try:
    DBID_PIPE = b'w'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 439
try:
    DBID_PARTICLE = b'p'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 440
try:
    DBID_NMG = b'N'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 441
try:
    DBID_SKETCH = b'd'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 442
try:
    DBID_ANNOT = b'a'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 443
try:
    DBID_EXTR = b'e'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 444
try:
    DBID_CLINE = b'c'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 445
try:
    DBID_BOT = b't'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 446
try:
    DBID_SCRIPT = b'T'
except:
    pass

# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 501
try:
    DB_RECORD_NULL = cast(0, POINTER(union_record))
except:
    pass

bn_tol = struct_bn_tol# /usr/brlcad/dev-7.31.0/include/brlcad/bn/tol.h: 72

bn_vlist = struct_bn_vlist# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 67

bn_vlblock = struct_bn_vlblock# /usr/brlcad/dev-7.31.0/include/brlcad/bn/vlist.h: 193

bg_tess_tol = struct_bg_tess_tol# /usr/brlcad/dev-7.31.0/include/brlcad/bg/defines.h: 114

db5_ondisk_header = struct_db5_ondisk_header# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 56

db5_raw_internal = struct_db5_raw_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db5.h: 200

knot_vector = struct_knot_vector# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 188

model = struct_model# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 212

nmgregion_a = struct_nmgregion_a# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 228

nmgregion = struct_nmgregion# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 220

shell_a = struct_shell_a# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 264

vertexuse = struct_vertexuse# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 512

shell = struct_shell# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 252

faceuse = struct_faceuse# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 319

face_g_plane = struct_face_g_plane# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 291

face_g_snurb = struct_face_g_snurb# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 298

face = struct_face# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 275

loopuse = struct_loopuse# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 399

loop_g = struct_loop_g# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 392

loop = struct_loop# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 385

edgeuse = struct_edgeuse# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 471

edge = struct_edge# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 431

edge_g_lseg = struct_edge_g_lseg# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 443

edge_g_cnurb = struct_edge_g_cnurb# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 459

vertex_g = struct_vertex_g# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 506

vertex = struct_vertex# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 499

vertexuse_a_plane = struct_vertexuse_a_plane# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 529

vertexuse_a_cnurb = struct_vertexuse_a_cnurb# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 535

nmg_boolstruct = struct_nmg_boolstruct# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 647

nmg_struct_counts = struct_nmg_struct_counts# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 669

nmg_visit_handlers = struct_nmg_visit_handlers# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 769

nmg_radial = struct_nmg_radial# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 809

nmg_inter_struct = struct_nmg_inter_struct# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 822

nmg_nurb_poly = struct_nmg_nurb_poly# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 910

nmg_nurb_uv_hit = struct_nmg_nurb_uv_hit# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 916

oslo_mat = struct_oslo_mat# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 924

bezier_2d_list = struct_bezier_2d_list# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 933

nmg_ray = struct_nmg_ray# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1075

nmg_hit = struct_nmg_hit# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1083

nmg_seg = struct_nmg_seg# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1094

nmg_hitmiss = struct_nmg_hitmiss# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1101

nmg_ray_data = struct_nmg_ray_data# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 1138

nmg_curvature = struct_nmg_curvature# /usr/brlcad/dev-7.31.0/include/brlcad/nmg.h: 2659

_on_brep_placeholder = struct__on_brep_placeholder# /usr/brlcad/dev-7.31.0/include/brlcad/brep/defines.h: 85

rt_tor_internal = struct_rt_tor_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 60

rt_tgc_internal = struct_rt_tgc_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 79

rt_ell_internal = struct_rt_ell_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 96

rt_superell_internal = struct_rt_superell_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 111

rt_metaball_internal = struct_rt_metaball_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 156

wdb_metaball_pnt = struct_wdb_metaball_pnt# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 169

rt_arb_internal = struct_rt_arb_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 191

rt_ars_internal = struct_rt_ars_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 203

rt_half_internal = struct_rt_half_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 217

rt_grip_internal = struct_rt_grip_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 229

rt_joint_internal = struct_rt_joint_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 244

rt_pg_face_internal = struct_rt_pg_face_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 263

rt_pg_internal = struct_rt_pg_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 268

rt_nurb_internal = struct_rt_nurb_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 281

rt_brep_internal = struct_rt_brep_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 297

rt_db_internal = struct_rt_db_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_internal.h: 46

rt_ebm_internal = struct_rt_ebm_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 323

rt_vol_internal = struct_rt_vol_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 349

rt_hf_internal = struct_rt_hf_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 373

rt_arbn_internal = struct_rt_arbn_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 403

rt_pipe_internal = struct_rt_pipe_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 416

wdb_pipe_pnt = struct_wdb_pipe_pnt# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 423

rt_part_internal = struct_rt_part_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 438

rt_rpc_internal = struct_rt_rpc_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 459

rt_rhc_internal = struct_rt_rhc_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 474

rt_epa_internal = struct_rt_epa_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 490

rt_ehy_internal = struct_rt_ehy_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 506

rt_hyp_internal = struct_rt_hyp_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 523

rt_eto_internal = struct_rt_eto_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 539

rt_dsp_internal = struct_rt_dsp_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 556

rt_curve = struct_rt_curve# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 597

line_seg = struct_line_seg# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 609

carc_seg = struct_carc_seg# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 616

nurb_seg = struct_nurb_seg# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 630

bezier_seg = struct_bezier_seg# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 642

rt_sketch_internal = struct_rt_sketch_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 651

db_i = struct_db_i# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_instance.h: 63

rt_submodel_internal = struct_rt_submodel_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 676

rt_extrude_internal = struct_rt_extrude_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 695

rt_revolve_internal = struct_rt_revolve_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 720

rt_cline_internal = struct_rt_cline_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 744

rt_bot_internal = struct_rt_bot_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 761

rt_bot_list = struct_rt_bot_list# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 828

pnt = struct_pnt# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 901

pnt_color = struct_pnt_color# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 905

pnt_scale = struct_pnt_scale# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 910

pnt_normal = struct_pnt_normal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 915

pnt_color_scale = struct_pnt_color_scale# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 920

pnt_color_normal = struct_pnt_color_normal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 926

pnt_scale_normal = struct_pnt_scale_normal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 932

pnt_color_scale_normal = struct_pnt_color_scale_normal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 938

rt_pnts_internal = struct_rt_pnts_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 947

rt_ant = struct_rt_ant# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 971

txt_seg = struct_txt_seg# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 981

rt_annot_internal = struct_rt_annot_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1010

rt_datum_internal = struct_rt_datum_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1054

rt_hrt_internal = struct_rt_hrt_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1073

rt_script_internal = struct_rt_script_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/geom.h: 1087

resource = struct_resource# /usr/brlcad/dev-7.31.0/include/brlcad/rt/resource.h: 61

directory = struct_directory# /usr/brlcad/dev-7.31.0/include/brlcad/rt/directory.h: 59

db_full_path = struct_db_full_path# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_fullpath.h: 54

mem_map = struct_mem_map# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mem.h: 37

region = struct_region# /usr/brlcad/dev-7.31.0/include/brlcad/rt/region.h: 44

mater_info = struct_mater_info# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 38

mater = struct_mater# /usr/brlcad/dev-7.31.0/include/brlcad/rt/mater.h: 50

anim_mat = struct_anim_mat# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 52

rt_anim_property = struct_rt_anim_property# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 62

rt_anim_color = struct_rt_anim_color# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 71

animate = struct_animate# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 76

animate_specific = union_animate_specific# /usr/brlcad/dev-7.31.0/include/brlcad/rt/anim.h: 81

rt_wdb = struct_rt_wdb# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/wdb.h: 49

tree = union_tree# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 147

bound_rpp = struct_bound_rpp# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 43

rt_functab = struct_rt_functab# /usr/brlcad/dev-7.31.0/include/brlcad/rt/functab.h: 69

rt_i = struct_rt_i# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/rt_instance.h: 61

soltab = struct_soltab# /usr/brlcad/dev-7.31.0/include/brlcad/rt/soltab.h: 56

xray = struct_xray# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 41

xrays = struct_xrays# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 57

pixel_ext = struct_pixel_ext# /usr/brlcad/dev-7.31.0/include/brlcad/rt/xray.h: 74

hit = struct_hit# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 61

curvature = struct_curvature# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 118

uvcoord = struct_uvcoord# /usr/brlcad/dev-7.31.0/include/brlcad/rt/hit.h: 152

seg = struct_seg# /usr/brlcad/dev-7.31.0/include/brlcad/rt/seg.h: 59

partition = struct_partition# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 53

application = struct_application# /usr/brlcad/dev-7.31.0/include/brlcad/rt/application.h: 99

partition_list = struct_partition_list# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 136

partition_bundle = struct_partition_bundle# /usr/brlcad/dev-7.31.0/include/brlcad/rt/ray_partition.h: 149

application_bundle = struct_application_bundle# /usr/brlcad/dev-7.31.0/include/brlcad/rt/application.h: 176

hitmiss = struct_hitmiss# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 43

ray_data = struct_ray_data# /usr/brlcad/dev-7.31.0/include/brlcad/rt/nmg.h: 82

db_tree_state = struct_db_tree_state# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 56

rt_comb_internal = struct_rt_comb_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/nongeom.h: 41

db_traverse = struct_db_traverse# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 115

combined_tree_state = struct_combined_tree_state# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 140

tree_node = struct_tree_node# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 150

tree_leaf = struct_tree_leaf# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 157

tree_cts = struct_tree_cts# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 163

tree_nmgregion = struct_tree_nmgregion# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 169

tree_db_leaf = struct_tree_db_leaf# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 175

rt_tree_array = struct_rt_tree_array# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 227

rt_piecestate = struct_rt_piecestate# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/piece.h: 57

rt_piecelist = struct_rt_piecelist# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/piece.h: 84

cutter = union_cutter# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 70

cutnode = struct_cutnode# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 46

boxnode = struct_boxnode# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 54

bvh_build_node = struct_bvh_build_node# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/space_partition.h: 103

rt_binunif_internal = struct_rt_binunif_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/nongeom.h: 103

rt_constraint_internal = struct_rt_constraint_internal# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/nongeom.h: 127

rt_htbl = struct_rt_htbl# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/piece.h: 41

rt_g = struct_rt_g# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/global.h: 39

rt_view_info = struct_rt_view_info# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 49

rt_selection = struct_rt_selection# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 78

rt_selection_set = struct_rt_selection_set# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 86

rt_object_selections = struct_rt_object_selections# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 104

rt_selection_query = struct_rt_selection_query# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 117

rt_selection_translation = struct_rt_selection_translation# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 132

rt_selection_operation = struct_rt_selection_operation# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/view.h: 144

rt_pnt_node = struct_rt_pnt_node# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/private.h: 42

rt_shootray_status = struct_rt_shootray_status# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/private.h: 51

rt_pattern_data = struct_rt_pattern_data# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/pattern.h: 68

command_tab = struct_command_tab# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/cmd.h: 42

db_search_context = struct_db_search_context# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/search.h: 45

record = union_record# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 421

bot_specific = struct_bot_specific# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/primitives/bot.h: 57

rt_point_labels = struct_rt_point_labels# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/misc.h: 52

rt_reprep_obj_list = struct_rt_reprep_obj_list# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/prep.h: 40

db5_attr_ctype = struct_db5_attr_ctype# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 64

db5_registry = struct_db5_registry# /usr/brlcad/dev-7.31.0/include/brlcad/./rt/db_attr.h: 86

solid = struct_solid# /usr/brlcad/dev-7.31.0/include/brlcad/rt/solid.h: 38

diff_avp = struct_diff_avp# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 51

diff_result = struct_diff_result# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db_diff.h: 60

TIE_3_s = struct_TIE_3_s# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 78

tie_ray_s = struct_tie_ray_s# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 80

tie_id_s = struct_tie_id_s# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 87

tie_tri_s = struct_tie_tri_s# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 95

tie_kdtree_s = struct_tie_kdtree_s# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 107

tie_s = struct_tie_s# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tie.h: 114

ident = struct_ident# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 88

solidrec = struct_solidrec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 119

combination = struct_combination# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 194

member = struct_member# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 218

material_rec = struct_material_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 228

B_solid = struct_B_solid# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 239

b_surf = struct_b_surf# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 247

polyhead = struct_polyhead# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 257

polydata = struct_polydata# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 263

ars_rec = struct_ars_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 270

ars_ext = struct_ars_ext# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 289

strsol = struct_strsol# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 298

arbn_rec = struct_arbn_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 308

exported_pipe_pnt = struct_exported_pipe_pnt# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 317

pipewire_rec = struct_pipewire_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 324

particle_rec = struct_particle_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 333

nmg_rec = struct_nmg_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 343

extr_rec = struct_extr_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 352

sketch_rec = struct_sketch_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 365

annot_rec = struct_annot_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 377

script_rec = struct_script_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 387

cline_rec = struct_cline_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 393

bot_rec = struct_bot_rec# /usr/brlcad/dev-7.31.0/include/brlcad/rt/db4.h: 403

tree_list = struct_tree_list# /usr/brlcad/dev-7.31.0/include/brlcad/rt/tree.h: 233

# No inserted files

# No prefix-stripping

