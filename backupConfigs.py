#!/usr/bin/python3

"""
./backupConfigs
---------------

description:
python script that copies all dot files from your home directory into a backup directory

usage:
customize the global variable systems to modify according to your system
```python3
systems = {
    ...,
    "systemName" : ("pathHomeFolder", "pathBackupFolder")
    }
```
dependencies:
1. python3.8 or higher
2. mkdir
3. cp

"""

import os
import subprocess
from sys import argv
from re import match

# add/ modify your systems -> keyword : (homeDirectory, backupDirectory)
systems = {
    "macbookPro": ("/Users/rmn", "/Users/rmn/mainRepo/configs/macbookPro"),
    "matebook": ("/home/rmn", "/home/rmn/github/rmn_main/configs/matebook"),
    "matepad" : ("/data/data/com.termux/files/home", "/data/data/com.termux/files/home/mainRepo/configs/matepad"),
    "xiaomiPoco": ("/data/data/com.termux/files/home", "/data/data/com.termux/files/home/mainRepo/configs/xiaomiPoco")
    # add new system here ...
}

dot_files = []


def checkBackupDir(backupDir: str):
    """Check if backup folder already exists, make one if not"""
    try:
        files = os.listdir(backupDir)
    except PermissionError:     # cron specific permission error occurs here
        print("Permission Error occured!")
        return
    for file in files:
        if match("backupConfigs", file):
            return
    else:
        subprocess.run(["mkdir", f"{backupDir}/backupConfigs"])



def getDotFiles(homeDir: str):
    """collects a list of names for all dot files inside the home directory"""
    global dot_files
    files = os.listdir(homeDir)
    for file in files:
        if match("^[.]+", file):
            if match(".([tT]rash)", file):
                continue  # skip trash & protected files
            absPath = f"{homeDir}/{file}"
            if os.path.isdir(absPath):
                getDotFiles(absPath)
            else:
                dot_files.append(absPath)


def copyDotFiles(backupDir: str) -> None:
    """copy all dot_files to the backup directory"""
    global dot_files
    for file in dot_files:
        subprocess.run(["cp", f"{file}", f"{backupDir}/backupConfigs/"])


def main():

    global systems
    if not 1 < len(argv) < 3:
        print(
            f"Invalid arguments: Provide a single arguments for one of the systems in: {systems.keys()}\n"
        )
        return
    system = argv[1]

    if not system in systems.keys():
        print(f"Invalid arguments: {system} is not a part of {systems.keys()}\n")
        return

    homeDir, backupDir = systems[system]

    checkBackupDir(backupDir)
    getDotFiles(homeDir)
    copyDotFiles(backupDir)


if __name__ == "__main__":
    main()


































