#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) <2:
        print 'Usage:./wash.py <tag_file> <useless flags>'
        exit(1)

    tag_file = open(sys.argv[1])
    forbiden_elems = sys.argv[2:]
    records = tag_file.readlines()
    clean_records = list()
    trash_records = list()
    for record in records:
        useful = True
        elems = record.split()
        for forbidden in forbiden_elems:
            if elems[1] == forbidden:
                trash_records.append(record)
                print '{} is useless'.format(record)
                useful = False
                break
        if useful:
            clean_records.append(record)

    clean_fn = 'clean.txt'
    clean_file = open(clean_fn, 'w')
    for record in clean_records:
        clean_file.write('%s' % record)
    clean_file.close()

    useless_fn = 'useless.txt'
    useless_file = open(useless_fn, 'w')
    for record in trash_records:
        useless_file.write('%s' % record)
    useless_file.close()

