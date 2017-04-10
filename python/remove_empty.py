#!/usr/bin/env python

import os
import sys
import cv2
import shutil

if __name__=='__main__':
    if len(sys.argv) != 3:
        print 'Usage:./remove_empty.py <img_dir> <back_up_rm_dir>'
        print 'Comment:<img_dir> containing images, <back_up_rm_dir> save removed empty images'
        exit(1)

    img_dir = sys.argv[1]
    back_up_rm_dir = sys.argv[2]
    fns = os.listdir(img_dir)
    rm_cnt = 0
    for fn in fns:
        path = os.path.join(img_dir, fn)
        img = cv2.imread(path)
        if img is None:
            rm_cnt += 1;
            print 'remove {} image {}'.format(rm_cnt, path) 
            shutil.move(path, back_up_rm_dir) 
