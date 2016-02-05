#!/usr/bin/env python
from __future__ import print_function
import os, re, argparse


# Handle command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('dirname', help='Directory containing anime files to prettify', type=str, nargs='?', default='.')
parser.add_argument('-v','--verbose',help='Increase level of verbosity',action="store_true")
args = parser.parse_args()

# Regular expression for filename identification
regex = re.compile(r'\[.*\]\s(.+)\s-\s([0-9]+)\s\[.*\]\.(\w+)')

for f in os.listdir(args.dirname):
    print(f)
    m = regex.match(f)
    if m is not None:
        anime_name = m.group(1)
        anime_num = m.group(2)
        anime_ext = m.group(3)
        new_filename = anime_num + ' - ' + anime_name + '.' + anime_ext
        if args.verbose:
            print('Renaming',f,'to',new_filename)
        os.rename(f,new_filename)

