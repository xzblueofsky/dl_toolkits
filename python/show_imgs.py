#!/usr/bin/python
# coding=utf-8
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='show_images')
    parser.add_argument('name',type=str)
    parser.add_argument('-p','--page',type=int,default=-1)
    parser.add_argument('-ip','--itemperpage',type=int,default=24)
    parser.add_argument('-d','--depth',type=int,default=1)    
    parser.add_argument('-s','--savefig',type=str,default=None)   
    parser.add_argument('-r','--recursive',action="store_true")   
    args = parser.parse_args()
    import util
    if args.recursive:
        args.depth=10
    util.shows(args.name,args.page,args.itemperpage,args.depth,savefig=args.savefig)
