#!/usr/bin/env python

import os
import sys
import shutil

if __name__=='__main__':
    if len(sys.argv) !=3:
        print 'Usage:./.add_prefix.py <folder> <prefix_to_add>\n'
        exit(1)
    
    folder = sys.argv[1]
    prefix = sys.argv[2]

    root = os.path.abspath(folder)
    for (root, subdirs, fns) in os.walk(root):
        for fn in fns:
            path = os.path.join(root, fn)
            new_path = os.path.join(root, prefix + fn)
            shutil.move(path, new_path)

