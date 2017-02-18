#!/usr/bin/env python

import os
import sys
import acc_pre_recall #my python file
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./compare_result.py <results_dir>'
        exit(1)

    result_dir = os.path.abspath(sys.argv[1])
    fns = os.listdir(result_dir)


    precesion_list = list()
    recall_list = list()
    model_name_list = list()

    for fn in fns:
        result_path = os.path.join(result_dir, fn)

        result = open(result_path)
        records = result.readlines()

        (accurancy, precision, recall) = acc_pre_recall.get_result_list(records)

        precesion_list.append(precision)
        recall_list.append(recall)

        basename_end = fn.rfind('.')
        model_name = fn[:basename_end]
        model_name_list.append(model_name)

    for i in range(len(model_name_list)):
       plt.plot(recall_list[i], precesion_list[i], label=model_name_list[i])
       plt.legend()
    
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.show()
