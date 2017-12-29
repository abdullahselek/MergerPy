#!/usr/bin/env python

import sys, argparse
from mergerpy import merger

if __name__ == "__main__":

    print("Starting", merger.full_version())

    parser = argparse.ArgumentParser(description='Merge/Concatanate strings.')
    parser.add_argument('--input', metavar='FILE', type=str, help='path of input file that contains texts')
    args = parser.parse_args()

    # Optional bash tab completion support
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    file_created = merger.main(sys.argv[2])

    if file_created:
        print("The file named Merged.txt created on root folder")
        retval = 0
    else:
        retval = 1

    sys.exit(retval)
