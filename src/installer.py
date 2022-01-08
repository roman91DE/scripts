#!/usr/bin/python3

"""
description:
installer script for basic software on linux/macOS

usage:
./installer.py <paketmanager>

supported paketmanagers:
    * homebrew
    * apt
    * snap
    * pkg (for termux)
"""


from sys import argv
import subprocess

paketmanager = {
    "homebrew":     ["brew", "install"],
     "apt":                ["sudo",  "apt", "install"],
     "snap":              ["snap",  "install"],
     "pkg":               ["pkg",  "install"]
}

software = [
    "htop",
    "git",
    "zsh",
    "vim",
    "tree",
    "nnn",
    "tmux",
]

def installer():

    global paketmanager, software
    
    if len(argv) != 2:
        print("Error - Invalid number of arguments")
        return -1

    pm = argv[1].lower()

    if not pm in paketmanager.keys():
        print(f"Error - {pm} is not supported! Choose from {paketmanager.keys()}")
        return  -2

    command = paketmanager[pm] + software
    subprocess.run(command)
    return 0


if __name__ == "__main__":
    installer()