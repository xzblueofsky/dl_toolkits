#!/usr/bin/env python
# @Author: zhong zhen
# @Date: 2017.03.24
# parse the return tagged json of blur task

import json
import cv2
import shutil
import os
import sys

if __name__=='__main__':
    if len(sys.argv) != 3:
        print 'Usage: ./parse_tag.py <tag_file> <result_dir>'
        exit(1)

    tag_file = sys.argv[1] 
    result_dir = sys.argv[2] 

    src_img_dir1 = "/home/zhongzhen/dataset/raw/blur/libraf_090_blur/"
    src_img_dir2 = "/home/zhongzhen/dataset/raw/blur/libraf_090_clear/"

    tag_file = open(tag_file)

    records = list()
    for line in tag_file:
        tag_data = json.loads(line)
        fn = os.path.basename(tag_data['url_image'])
        loc1 = src_img_dir1 + fn
	loc2 = src_img_dir2 + fn
        if os.path.exists(loc1):
	    loc = loc1
	elif os.path.exists(loc2):
	    loc = loc2
	else:
            print '{} not exist'.format(loc1)
            continue
        try:
            for item in tag_data['result']:
		tag = item['tagtype']

		if tag == "blur":
		    tagNum = 1
		elif tag == "clear":
		    tagNum = 0
		else:
		    tagNum = -1

		record = loc + '\t' + str(tagNum)
                records.append(record)
        except e:
	    print e
            continue

    result_fn = result_dir + '/chongqing_blur_result.txt'
    result_file = open(result_fn, 'w')
    for record in records:
        result_file.write('%s\n' % record)
    result_file.close()
