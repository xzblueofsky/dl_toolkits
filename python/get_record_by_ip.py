#!/usr/bin/env python

import os
import sys
import shutil

if __name__=='__main__':
    if len(sys.argv) != 4:
        print ("""
        Usage: ./get_record_by_ip.py <ip_list_file> <src_record_file> <dest_record_file>
        Comment: records containing target ip woulb be cleaned from src_record_file. The results would be save in <src_record_file> '.result' and  <dest_record_file>
        """)
        exit(1)

    ip_list_fn = sys.argv[1]
    src_record_fn = sys.argv[2]
    dest_record_path = sys.argv[3]

    dest_records = list()
    reserved_records = open(src_record_fn).readlines() 

    with open(ip_list_fn) as f:
        ips = f.readlines()
        for ip in ips:
            ip = ip.strip()
            with open(src_record_fn) as record_f:
                records = record_f.readlines()
                for record in records:
                    if ip in record:
                        dest_records.append(record)
                        reserved_records.remove(record)

            

    with open(dest_record_path, 'w') as f:
        for record in dest_records:
            f.write('{}'.format(record))

    with open(src_record_fn + '.result', 'w') as f:
        for record in reserved_records:
            f.write('{}'.format(record))
