#!/usr/bin/env python

import os
import sys
import cv2

if __name__=='__main__':
    if len(sys.argv) != 5:
        print './gen_camera_num_list.py is used to select certain number range camera from chongqing data\n'
        print 'Usage: ./gen_camera_num_list.py <image_dir> <begin_camera_num> <end_camera_num> <output_loc>'
        print 'Select range: [<begin_cam_num>, <end_cam_num>)'
        exit(1)

    image_dir = sys.argv[1]
    begin_cam_num = int(sys.argv[2])
    end_cam_num = int(sys.argv[3])
    output_loc = sys.argv[4]

    fns = os.listdir(image_dir)
    output_list = list()

    for fn in fns:
        #print '{}\n'.format(fn) 
        path = os.path.join(image_dir,fn)
        #print '{}\n'.format(path)
        img = cv2.imread(path)
        pos = fn.find('_')
        cur_cam_num = int(fn[0:pos])
        if cur_cam_num>=begin_cam_num and cur_cam_num<end_cam_num:
            #print path
            output_list.append(path)
        #cv2.imshow('test', img)
        #cv2.waitKey(0)

    output = open(output_loc, 'w')
    for record in output_list:
        output.write('{}\n'.format(record))
    output.close()
