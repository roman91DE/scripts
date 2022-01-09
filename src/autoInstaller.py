#!/usr/bin/python3

"""
description:
installer script for basic command line packages on linux/macOS

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
    "homebrew":    [["brew", "update", "&", "brew", "upgrade"], ["brew", "install"]],
    "apt":         [["sudo", "apt" , "update", "&", "sudo", "apt" , "upgrade"], ["sudo",  "apt", "install"]],
    "snap":        [["sudo", "snap", "refresh"], ["sudo", "snap", "install"]],
    "pkg":         [["pkg", "upgrade"], ["pkg", "install"]],
}

software = [
    "htop",
    "git",
    "zsh",
    "vim",
    "tree",
    "nnn",
    "tmux",
    "gcc",
    "make",
    "g++",
    "curl",
    "wget",
    "neofetch"
]

def installer():

    global paketmanager, software

    if len(argv) != 2:
        print("Error - Invalid number of arguments")
        return False

    pm = argv[1].lower()

    if not pm in paketmanager.keys():
        print(f"Error - {pm} is not supported! Choose from {paketmanager.keys()}")
        return  False

    # update repositories
    command = paketmanager[pm][0]
    subprocess.run(command)

    # install packages
    for package in software:
        command = paketmanager[pm][1] + [package]
        subprocess.run(command)

    # set zsh as login shell
    subprocess.run(
        ["chsh", "-s", "$(which zsh)"]
    )

    # set git configuration
    subprocess.run(
        ["git", "config", "--global", "user.email", "rohoehn123@gmail.com", "&",
         "git", "config", "--global", "user.name", "rohoehn"]
    )
    
    return True


if __name__ == "__main__":

    if installer():
        print("Finished installer")

    else:
        print("Something went wrong")
