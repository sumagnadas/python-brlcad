#! /usr/bin/env python3
# This file takes one header file(like raytrace.h and passes the header files it contains in #include preprocessor directive to ctypesgen command
import optparse
from os.path import exists, basename, splitext, join
from os import environ
from ctypesgen import parser, processor, printer_python
from ctypesgen.options import get_default_options
import re
import copy
from configparser import ConfigParser

args_parser = optparse.OptionParser()
include_prefix = "/usr/brlcad/dev-7.31.0/include/brlcad/"
path = []


def load_options(config):
    libraries = {}
    default_options = get_default_options()

    environ['LD_LIBRARY_PATH']="/usr/brlcad/dev-7.31.0/lib/"
    options = {}

    default_options.include_symbols = None
    default_options.exclude_symbols = None
    default_options.output_language = "python"
    default_options.header_template = None
    default_options.strip_build_path = None
    default_options.save_preprocessed_headers = None
    default_options.headers = []
    default_options.__dict__.update(config['ctypesgen'])
    default_options.inserted_files = []
    default_options.other_headers = []
    default_options.compile_libdirs = []
    default_options.runtime_libdirs = []

    hasVersionSpecific = len([i for i in config.sections() if re.search(r"brlcad.", i)]) == 0

    for i in config['brlcad']['libraries'].split(','):
        i = i.strip()
        libraries[i] = {}
        libraries[i]['lib-headers'] = config["brlcad"].get(f"{i}-lib-headers", f"{i}.h").split(",")
        libraries[i]['dependencies'] = config["brlcad"].get(f"{i}-dependencies", "").split(",")
        if hasVersionSpecific == True:
            print("version specific information available")
        if " rt" in libraries[i]['dependencies']:
            index = libraries[i]['dependencies'].index(" rt")
            libraries[i]['dependencies'][index] = "raytrace"

        for index, j in enumerate(libraries[i]['dependencies']):
            libraries[i]['dependencies'][index] = "." + j.strip()
        for index, j in enumerate(libraries[i]['lib-headers']):
            libraries[i]['lib-headers'][index] = include_prefix + j.strip()

    for i in libraries.keys():
        i = i.strip()
        options[i] = copy.deepcopy(default_options)
        options[i].headers = libraries[i]['lib-headers']
        #options[i].modules = libraries[i]['dependencies']
        for j in libraries[i]['dependencies']:
            j = j.strip(".")
            j = j if not j == "raytrace" else "rt"
            if j == "":
                continue
            options[i].libraries.extend([f"/usr/brlcad/dev-7.31.0/lib/lib{j}.so"])
        options[i].libraries.extend([f"/usr/brlcad/dev-7.31.0/lib/lib{i}.so"])
        options[i].include_search_paths.append(include_prefix)
        j = i if not i == "rt" else "raytrace"
        options[i].output  = f"brlcad/bindings/{j}.py"
    return options


def main():
    config = ConfigParser()
    config.read_file(open("python-brlcad.cfg"))

    library_options = load_options(config)

    for i in library_options.keys():
        options = library_options[i]
        open("options.txt", "a").write(str(options.modules) + "\n")
        desc = parser.parse(options.headers, options)
        processor.process(desc, options)
        printer_python.WrapperPrinter(options.output, options, desc)

if  __name__ == "__main__":
    main()
