#!/usr/bin/env python
import os
import sys
import collections

if __name__ == '__main__':
    print 'main'
    if len(sys.argv) != 2:
        print 'Usage:./print_duplicate_fn.py <tag_file>'
        exit(1)

    tag_fn = sys.argv[1]

    lines = list()
    with open(tag_fn) as f:
        lines = f.readlines()

    base_names = list()
    for line in lines:
        elems = line.split()
        path = elems[0] 
        base_name = os.path.basename(path)
        #print base_name
        base_names.append(base_name)

    #base_names.sort()
    #print base_names

    duplicate_basenames = [item for item, count in collections.Counter(base_names).items() if count > 1]
    print len(duplicate_basenames)
    for item in duplicate_basenames:
        print item

