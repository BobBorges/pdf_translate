#!/usr/bin/env python3
from tika import parser
import sys, os

def main():
    inpdf = sys.argv[1]
    filebase = os.path.splitext(inpdf)[0]

    pdf_content = parser.from_file(inpdf)
    outstring = pdf_content['content']

    with open(f'{filebase}.txt', 'w+') as outfile:
        outfile.write(outstring)

if __name__ == '__main__':
	main()
