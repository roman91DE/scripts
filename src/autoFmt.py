#!/usr/bin/python3

"""
./autoFmt
---------

Description:
script to format various types of sourcecode files using language specific formatting utilities on unix-like operating systems

Usage:
autoFmt <myDir>
    -> recursivley iterate all files and subdirectories in myDir, formats all supported files
 
Supported Languages:
1. python   
2. c/c++
3. go

Dependencies:
1. python3
2. black
3. clang-format
4. go fmt
"""


import os
from sys import argv, setrecursionlimit
from re import search
from subprocess import run
from time import time

setrecursionlimit(10000)

logo: str = """
             _        _____          _
  __ _ _   _| |_ ___ |  ___| __ ___ | |_
 / _` | | | | __/ _ \| |_ | '_ ` _ \| __|
| (_| | |_| | || (_) |  _|| | | | | | |_
 \__,_|\__,_|\__\___/|_|  |_| |_| |_|\__|
----------------------------------------- 

written by Roman Hoehn
source code available at:
https://github.com/roman91DE/autoFmt

"""


# count the number of src files
pycount: int = 0
ccount: int = 0
gocount: int = 0
fcount: int = 0


def fmtPy(path: str) -> None:
    """formats a python file by calling the black module as a subprocess"""
    global pycount
    run(args=["black", "-q", path])
    pycount += 1


def fmtC(path: str) -> None:
    """formats a c/cpp/h file by calling the clang-format module as a subprocess"""
    global ccount
    run(args=["clang-format", "-i", "--style=webkit", path])
    ccount += 1


def fmtGo(path: str) -> None:
    """formats a go file by calling the go fmt command as a subprocess"""
    global gocount
    run(args=["go", "fmt", path])
    gocount += 1


def tryFile(path: str) -> None:
    """checks file extension and calls the corresponding format function if recognized"""
    global fcount
    fcount += 1
    if search("\.py$", path):
        fmtPy(path)
    elif search("\.([ch]|cpp)$", path):
        fmtC(path)
    elif search("(\.go$)|(\.go.mod$)", path):
        fmtGo(path)


def recFmt(dir_path: str) -> None:
    """recursive function to iterate through all files and directories"""
    for rel_path in os.listdir(dir_path):
        abs_path: str = os.path.join(dir_path, rel_path)
        if os.path.isdir(abs_path):
            recFmt(abs_path)
        elif os.path.isfile(abs_path):
            tryFile(abs_path)


def main() -> None:
    global logo, pycount, ccount, gocount, fcount
    tstart: float = time()

    print(logo)

    if len(argv) != 2:
        print("Specify a single argument for the parent directory")
        return
    path: str = argv[1]

    print("running autoFmt\n...")
    recFmt(path)
    print("finished autoFmt\n")
    print(
        f"File stats:\n---\ntotal: {fcount}\npython: {pycount}\nc/c++: {ccount}\ngo: {gocount}\n\nelapsed time: {(time()-tstart):.6f} seconds"
    )


if __name__ == "__main__":
    main()
