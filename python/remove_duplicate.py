#!/usr/bin/env python

import os
import re
import hashlib
import sys
import errno
from time import time

picDic = {}
regular = re.compile(r'^(.*)\.(jpg|jpeg|bmp|gif|png|JPG|JPEG|BMP|GIF|PNG)$')

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def RemoverRePic(dirPath, backupPath):
    quantity = 0
    for childPath in os.listdir(dirPath):
        childPath = dirPath + '/'  + childPath
        if os.path.isdir(childPath):
            quantity =+ RemoverRePic(childPath)
        else:
            if regular.match(childPath):
                pic = open(childPath, 'rb')
                picMd5 = hashlib.md5(pic.read()).hexdigest()
                pic.close()
                if picDic.has_key(picMd5):
                    #newPath = backupPath + '/'  + hashlib.md5(childPath)\
                    #.hexdigest() + childPath[childPath.find('.'):]
                    newPathDir = backupPath + '/'  + hashlib.md5(picMd5).hexdigest(); 
                    mkdir_p(newPathDir)
                    newPath = os.path.join(newPathDir, os.path.basename(childPath))
                    os.rename(childPath, newPath)
                    quantity =+ 1
                else:
                    picDic[picMd5] = childPath
    return quantity

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: ./remove_duplicate.py <img_dir> <backup_img_dir>'
        print 'Comment: remove duplicate images in img_dir folder. Save removed images in back_up_dir, subdir name using hash sum'
        exit(1)

    src_path = sys.argv[1]
    dest_path = sys.argv[2]
    t = time()
    print 'start:'
    print t
    print RemoverRePic(src_path, dest_path)
    print 'end:'
    print time() - t
