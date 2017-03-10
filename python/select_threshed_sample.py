#!/usr/bin/env python

import os
import sys
import shutil

if __name__=='__main__':
    if len(sys.argv) != 4:
        print 'Usage: ./selece_threshed_sample.py <result_file_loc> <pos_thresh> <output_dir>'
        exit(1)

    result_file_loc = sys.argv[1]
    pos_thresh = float(sys.argv[2])
    output_dir = sys.argv[3]

    result_file = open(result_file_loc)

    false_pos_paths = list()
    false_neg_paths = list()

    records = result_file.readlines()
    for record in records:
        elems = record.split()
        path = elems[0]
        predict = float(elems[1])

        if predict>pos_thresh:
            false_pos_paths.append(path)

        if predict<pos_thresh:
            false_neg_paths.append(path)

    false_pos_dir = output_dir + '/false_pos' 
    false_neg_dir = output_dir + '/false_neg' 
    os.mkdir(false_pos_dir, 0755)
    os.mkdir(false_neg_dir, 0755)

    for path in false_pos_paths:
        shutil.copy(path, false_pos_dir)

    for path in false_neg_paths:
        shutil.copy(path, false_neg_dir)

