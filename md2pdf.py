#!/usr/bin/python3

from sys import argv
from re import search
import subprocess



def main():

    if len(argv) != 2:
        print("Error - Invalid args!")
        return -1

    md_file = argv[1]
    if not search(r"[.]md$", md_file):
        print("Error - Pass .md file as arguments")
        return -2

    pdf_file = md_file[:-2] + "pdf"
    subprocess.run(["pandoc", "-o", pdf_file, md_file])
    print(f"Created {pdf_file} from {md_file}!")
    return 0


    

if __name__ == "__main__":
    main()

