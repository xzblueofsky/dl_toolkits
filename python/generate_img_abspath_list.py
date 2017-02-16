#!/usr/bin/env python

import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./generate_img_abspath_list.py <image_dir_root>\n'
        print 'Output: <image_dir_root>/result.txt'
        exit(1)
    
    root = os.path.abspath(sys.argv[1])
    result_path = root + '/result.txt'
    print result_path

    result_file = open(result_path, 'w')
    for (root, subdirs, fns) in os.walk(root):
        for fn in fns:
            if not fn.endswith('jpg'):
                continue
            path = os.path.join(root, fn)
            #print path
            result_file.write('{}\n'.format(path))

    result_file.close()

