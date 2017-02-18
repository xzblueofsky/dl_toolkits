#!/usr/bin/env python

import sys
import os
import accurancy #my python file
import subprocess

def get_model_path_list(model_dir):
    fns = os.listdir(model_dir) 
    model_paths = list()
    for fn in fns:
        if not fn.endswith('caffemodel'):
            continue
        path = os.path.join(model_dir, fn)
        model_paths.append(path)
    return model_paths

def generate_evaluate_files(deploy_path, model_paths, ground_truth_loc):
    for path in model_paths:
        #cmd = '../cpp/build/evaluate_main ' + deploy_path + ' ' + path + ' ' + './result' 
        cmd = list()
        cmd.append('../cpp/build/evaluate_main')
        cmd.append(deploy_path)
        cmd.append(path)
        cmd.append(ground_truth_loc)

        base_begin = path.rfind('/') + 1
        base_end = path.rfind('.')
        tmp_result_name = path[base_begin:base_end] + '.txt'
        #print tmp_result_name
        cmd.append(tmp_result_name)
        #print cmd
        subprocess.call(cmd) 

if __name__=='__main__':
    if len(sys.argv) != 4:
        print 'Usage:./compare_models.py <deploy_path> <caffe_model_dir> <ground_truth_loc>'
        exit(1)

    deploy_path = os.path.abspath(sys.argv[1])
    model_dir = os.path.abspath(sys.argv[2])
    ground_truth_loc = os.path.abspath(sys.argv[3])

    # get modle_paths list
    model_paths = get_model_path_list(model_dir)
    generate_evaluate_files(deploy_path, model_paths, ground_truth_loc)
    
