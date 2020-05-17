#! /usr/bin/env python3
# This file takes one header file(like raytrace.h and passes the header files it contains in #include preprocessor directive to ctypesgen command
from subprocess import call
from sys import argv
from os.path import exists, basename, splitext
from os import environ

script, filename, *options = argv
include_prefix = "/usr/brlcad/dev-7.31.0/include/brlcad/"
path = []

with open(filename) as e:
    file = e.read().splitlines()
    for i in range(0 ,len(file) - 1):
        if "#include" in file[i]:
            line = file[i].split()
            if not "<" in line[1].strip("\"./"):
                path.append(include_prefix + line[1].strip("\"./"))
environ['LD_LIBRARY_PATH']="/usr/brlcad/dev-7.31.0/lib/"
file = splitext(basename(filename))[0]
call(['ctypesgen', f'-I{include_prefix}', filename] + path + ['-o', f'{file}.py'] + options)
