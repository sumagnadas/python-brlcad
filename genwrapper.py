#! /usr/bin/env python3
# This file takes one header file(like raytrace.h and passes the header files it contains in #include preprocessor directive to ctypesgen command
from subprocess import call
from sys import argv
from os.path import exists, basename, splitext
from os import environ

script, filename, *options = argv
include_prefix = "/usr/brlcad/dev-7.31.0/include/brlcad/"
path = []
filename = [filename]
i = 0
while i != len(options) - 1:
    if not options[i].startswith('-') and options[i].startswith('/'):
        filename.append(options.pop(i))
        i -= 1
    i+=1
for i in range(0, len(filename) - 1 if not len(filename) - 1 == 0 else 1):
    with open(filename[i]) as e:
        file = e.read().splitlines()
        for j in range(0 ,len(file) - 1):
            if "#include" in file[j]:
                line = file[j].split()
                if not "<" in line[1].strip("\"./"):
                    path.append(include_prefix + line[1].strip("\"./"))
environ['LD_LIBRARY_PATH']="/usr/brlcad/dev-7.31.0/lib/"
file = splitext(basename(filename[0]))[0]
call(['ctypesgen', f'-I{include_prefix}'] + filename + path + ['-o', f'{file}.py'] + options)
