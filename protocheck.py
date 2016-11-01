#!/Users/crhamilt/anaconda/python
"""
This script checks a DICOM file for compliance with a CSV specification file

@author: cahamilton
"""

#
# Version  Date      Notes
#  1.0     20161012  Initial coding
#

import sys
import os
import argparse
import numpy as np
import dicom as dcm
import csv


def protocheck(args):
    # ~~~~~~~~~~~~~~   parse command line   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    parser = argparse.ArgumentParser(
        description="protocheck: check DICOM file with CSV spec file")
    parser.add_argument("image", type=str,
                        help="DICOM image to check.")
    parser.add_argument("specfile", type=str,
                        help="Specification file (CSV).")
    args = parser.parse_args()

    dimg = args.image
    spec_file = args.specfile

    # read the spec_file into the dictionary 'specs' {key,tuple}
    #   the tuple contains (standard, min, max) values

    ifile = open(spec_file, 'rt')
    reader = csv.reader(ifile)
    specs = {}

    rownum = 0
    for line in reader:
        if rownum > 0:
            key = line[0]
            stan = line[1]
            mn = line[2]
            mx = line[3]
            specs[key] = tuple((float(stan), float(mn), float(mx)))
        rownum += 1

    ifile.close()

    # verify the spec_file has ranges that encompass the standard value
    for value in list(specs.values()):
        # value is a tuple (standard,min,max)
        if (value[1] > value[0]) or (value[2] < value[0]):
            print(('bad spec file range:', value))
            sys.exit()

    print('\nspec file looks OK.\n')

    # read the DICOM file and extract the elements in specfile

    ds = dcm.read_file(dimg)

    print('Spec file contains:')
    for key, value in list(specs.items()):
        print((key + '= ', value))

    print('\nImage elements are:')
    for key in list(specs.keys()):
        print((key + '= ', eval('ds.' + key)))

    print('\nResults:\n')
    print(('%18s %8s %8s %8s %8s %12s')
          % ('Element', 'Value', 'Standard', 'Max', 'Min', 'Status'))
    print(('%18s %8s %8s %8s %8s %12s')
          % ('-------', '--------', '--------', '--------', '--------', '------------'))

    for key, value in list(specs.items()):
        imgval = float(eval('ds.' + key))
        if (imgval >= value[1]) and (imgval <= value[2]):
            status = "OK"
        else:
            status = "OutOfRange"

        print(('%18s %8.2f %8.2f %8.2f %8.2f %12s')
              % (key, imgval, value[0], value[1], value[2], status))


if __name__ == "__main__":
    sys.exit(protocheck(sys.argv[1:]))
