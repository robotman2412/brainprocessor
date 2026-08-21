#!/usr/bin/env python3

import argparse, sys

parser = argparse.ArgumentParser(description="Converts binary files to hexadecimal files readable by Logisim")

parser.add_argument("input", help="Binary file to convert")
parser.add_argument("output", help="Output logisim hex file; by default, input with the extension changed to .lhf", nargs='?')

args = parser.parse_args()

input: str = args.input
output: str = args.output
if output == None:
    if '.' in input:
        output = input[:input.rindex('.')] + ".lhf"
    else:
        output = input + ".lhf"

try:
    infd = open(input, "rb")
    outfd = open(output, "w")

    outfd.write("v2.0 raw\n")
    outfd.write(' '.join(f"{c:02x}" for c in infd.read()))
    outfd.write("\n")

except IOError as e:
    print(f"I/O Error: {e.strerror}")
    sys.exit(1)
