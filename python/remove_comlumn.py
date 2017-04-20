#!/usr/bin/env python

import os
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('Usage: ./.remove_comlumn.py <result_file_folder> <column_number_to_remove>')
        exit(1)

    root_dir = os.path.abspath(sys.argv[1])
    fns = os.listdir(root_dir)
    rm_id = int(sys.argv[2])

    for fn in fns:
        fn = os.path.join(root_dir, fn)
        ifs = open(fn, 'r')
        records = list()
        lines = ifs.readlines()
        for line in lines:
            elems = line.split()
            del elems[rm_id]
            record = ''
            for elem in elems:
                record += elem + '\t' 
            #print record
            records.append(record)
        ifs.close()
        ofs = open(fn, 'w')
        for record in records:
            ofs.write('%s\n' % record)
        ofs.close()
