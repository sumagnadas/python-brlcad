#! /usr/bin/env python3
# This file takes one header file(like raytrace.h and passes the header files it contains in #include preprocessor directive to ctypesgen command
from sys import argv
import optparse
from os.path import exists, basename, splitext, join
from os import environ
from ctypesgen import parser, processor, printer_python
from ctypesgen.options import get_default_options
#from brlcad_version import load_ctypesgen_options
from configparser import ConfigParser

args_parser = optparse.OptionParser()
include_prefix = "/usr/brlcad/dev-7.31.0/include/brlcad/"
path = []

args_parser.add_option("-f","--filename", metavar="FILE",dest="filename")
args_parser.add_option("-l", "--library",dest="library")

(options,args) = args_parser.parse_args()

filename = [options.filename]

def main():
    default_options = get_default_options()

    environ['LD_LIBRARY_PATH']="/usr/brlcad/dev-7.31.0/lib/"

    config = ConfigParser()
    config.read_file(open("python-brlcad.cfg"))
    default_options.headers = []

    for i in ["rt", "bn", "bu", "wdb"]:
        for j in [i for i in config.get("brlcad", f"{i}-lib-headers").split(',')]:
            j = j.strip()
            default_options.headers.append(include_prefix + j)
        if not i == "bu":
            for j in [i for i in config.get("brlcad", f"{i}-dependencies").split(',')]:
                j = "." + j.strip()
                default_options.modules.append(j if not "rt" in j else "raytrace")
        default_options.libraries.extend([f"/usr/brlcad/dev-7.31.0/lib/lib{i}.so"])
        i = i if not i=="rt" else "raytrace"
        default_options.output = "brlcad/bindings/" + i + ".py"
        default_options.include_search_paths.append(include_prefix)

        desc = parser.parse(default_options.headers, default_options)
        processor.process(desc, default_options)
        printer_python.WrapperPrinter(default_options.output, default_options, desc)

if  __name__ == "__main__":
    main()
