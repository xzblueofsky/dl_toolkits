#!/usr/bin/env python

import json
import cv2
import shutil
import os
import sys

if __name__=='__main__':
    if len(sys.argv) != 5:
        print 'Usage: ./parse_tag.py <tag_file> <src_img_dir> <tag_name> <result_dir>'
        exit(1)

    tag_file = sys.argv[1] 
    src_img_dir = os.path.abspath(sys.argv[2])
    tag_name = sys.argv[3]
    result_dir = sys.argv[4] 

    tag_file = open(tag_file)

    records = list()
    for line in tag_file:
        tag_data = json.loads(line)
        pos = tag_data['url_image'].rfind('/')
        fn = tag_data['url_image'][pos:]
        loc = src_img_dir + fn
        if not os.path.exists(loc):
            print '{} not exist'.format(loc)
            continue
        try:
            for item in tag_data['result']:
                if item['tagtype'] == tag_name:
                    comment = item['comment']
                    if len(comment)==0:
                        continue
                    try:
                        float(comment)
                    except:
                        continue
                    record = loc + '\t' + comment
                    records.append(record)
        except:
            continue

    result_fn = result_dir + '/' + tag_name + '_result.txt'
    result_file = open(result_fn, 'w')
    for record in records:
        result_file.write('%s\n' % record)
    result_file.close()
