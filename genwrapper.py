#! /usr/bin/env python3
# This file takes one header file(like raytrace.h and passes the header files it contains in #include preprocessor directive to ctypesgen command
from sys import argv
import optparse
from os.path import exists, basename, splitext, join
from os import environ
from ctypesgen import parser, processor, printer_python
from ctypesgen.options import get_default_options

args_parser = optparse.OptionParser()
include_prefix = "/usr/brlcad/dev-7.31.0/include/brlcad/"
path = []

args_parser.add_option("-f","--filename", metavar="FILE",dest="filename")
args_parser.add_option("-l", "--library",dest="library")

(options,args) = args_parser.parse_args()

filename = [options.filename]

def main(filename, library):
    default_options = get_default_options()
    default_options.libraries.extend(library)
    for i in range(0, len(filename) - 1 if not len(filename) - 1 == 0 else 1):
        with open(filename[i]) as e:
            file = e.read().splitlines()
            for j in range(0 ,len(file) - 1):
                if "#include" in file[j]:
                    line = file[j].split()
                    if not "<" in line[1].strip("\"./"):
                        path.append(include_prefix + line[1].strip("\"./"))

    default_options.headers = filename

    environ['LD_LIBRARY_PATH']="/usr/brlcad/dev-7.31.0/lib/"
    file = splitext(basename(filename[0]))[0]

    default_options.output = "brlcad/bindings/" + file + ".py"
    default_options.include_search_paths.append(include_prefix)

    desc = parser.parse(filename, default_options)
    processor.process(desc, default_options)
    printer_python.WrapperPrinter(default_options.output, default_options, desc)

if  __name__ == "__main__":
    main(filename, [options.library])
