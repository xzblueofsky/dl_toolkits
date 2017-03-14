#!/usr/bin/env python

import sys
import os
import matplotlib.pyplot as plt

def get_statics(records, thresh):
    true_pos = false_pos = true_neg = false_neg = 0.0
    for record in records:
        elems = record.split()
        predict = float(elems[1])
        groundtruth = float(elems[2])
        #print '{},{}'.format(predict, groundtruth)
        if predict<=thresh and groundtruth==0:
            true_neg+=1
        elif predict>=thresh and groundtruth ==1:
            true_pos+=1
        elif predict<thresh and groundtruth ==1:
            false_neg += 1
        elif predict>thresh and groundtruth ==0:
            false_pos += 1
    
    episilon = 1e-6
    accurancy = (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg + episilon);
    precision = true_pos / (true_pos + false_pos + episilon)
    recall = true_pos / (true_pos + false_neg + episilon)
    #"""
    print '---thresh = {}'.format(thresh)
    print 'accurancy = {}'.format(accurancy)
    print 'precision = {}'.format(precision)
    print 'recall = {}'.format(recall)
    sum_num = true_pos + true_neg + false_pos + false_neg
    print 'sum = {}'.format(sum_num)
    #"""
    return (accurancy, precision, recall)

def get_result_list(records):
    threshes = [x *0.001 for x in range(1,1000)]
    accurancy_list = list()
    precision_list = list()
    recall_list = list()

    for thresh in threshes: 
        (accurancy, precision, recall) = get_statics(records, thresh)
        accurancy_list.append(accurancy)
        precision_list.append(precision)
        recall_list.append(recall)

    return (accurancy_list, precision_list, recall_list)

if __name__=='__main__':
    if len(sys.argv)!=2:
        print 'Usage: ./acc_pre_recall.py <path/to/result>'
        exit(1)

    result_loc = sys.argv[1]
    result = open(result_loc)
    records = result.readlines()
    
    (accurancy_list, precision_list, recall_list) = get_result_list(records)
    
    plt.plot(recall_list, precision_list, linewidth=2.0)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.plot(recall_list[50], precision_list[50], 'ro')
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.show()
