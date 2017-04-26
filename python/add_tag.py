#!/usr/bin/env python

import os
import sys

if __name__=='__main__':
    if len(sys.argv) != 4:
        print 'Usage: ./add_tag.py <to_tag_txt_file> <tag> <output_txt_file>'
        exit(1)

    to_tag_fn = sys.argv[1]
    tag = sys.argv[2]
    output_fn = sys.argv[3]

    records = list()
    with open(to_tag_fn) as f:
        records = f.readlines()

    for i in range(0,len(records)):
        records[i] = records[i].strip() + ' ' + tag 
        print records[i]

    with open(output_fn, 'w') as f:
        for record in records:
            f.write('{}\n'.format(record))

    print 'Result saved in {}'.format(output_fn)
