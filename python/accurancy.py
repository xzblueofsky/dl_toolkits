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

    accurancy = (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg);
    precision = true_pos / (true_pos + false_pos)
    recall = true_pos / (true_pos + false_neg)
    #"""
    print '---thresh = {}'.format(thresh)
    print 'accurancy = {}'.format(accurancy)
    print 'precision = {}'.format(precision)
    print 'recall = {}'.format(recall)
    sum_num = true_pos + true_neg + false_pos + false_neg
    print 'sum = {}'.format(sum_num)
    #"""
    return (accurancy, precision, recall)

if __name__=='__main__':
    if len(sys.argv)!=2:
        print 'Usage: ./accurancy.py <path/to/result>'
        exit(1)

    result_loc = sys.argv[1]
    result = open(result_loc)
    records = result.readlines()

    true_pos = false_pos = true_neg = false_neg = 0.0

    threshes = [x *0.01 for x in range(1,101)]
    accurancy_list = list()
    precision_list = list()
    recall_list = list()

    for thresh in threshes: 
        (accurancy, precision, recall) = get_statics(records, thresh)
        accurancy_list.append(accurancy)
        precision_list.append(precision)
        recall_list.append(recall)
    
    plt.plot(recall_list, precision_list)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.plot(recall_list[50], precision_list[50], 'ro')
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.show()
