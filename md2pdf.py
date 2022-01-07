#!/usr/bin/python3

""" 
simple wrapper script for pandocs markdown to pdf conversion
------------------------------------------------------------
usage:
    ./md2pdf.py <file.md> ...
output:
     <file.pdf> ...
"""

from sys import argv
from re import search
import subprocess


def main():

    if len(argv) < 2:
        print("Error - Invalid number of args! Pass at least a single markdown file")
        return -1

    for arg in argv:

        if not search(r"[.]md$", arg):
            print(f"Warning - Argument {arg} is not a .md file, skipped conversion")
            continue

        pdf_file = arg[:-2] + "pdf"
        subprocess.run(["pandoc", "-o", pdf_file, arg])
        print(f"Created {pdf_file} from {arg}!")

    return 0


if __name__ == "__main__":
    main()

