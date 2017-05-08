#!/usr/bin/env python
# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from PIL import Image
#import pdb
import os
import random
import time
DEBUG=True

def make_nparray(arr):
    if not isinstance(arr,np.ndarray):
        arr=np.array(arr)
    return arr

def fix_nan(arr,value):
    arr[np.where(np.isnan(arr))]=value
    return arr

def show(path,pt=plt):
    img=cv2.imread(path)
    img=img[:,:,::-1]
    pt.imshow(img)
    return img

def _shows(images,showimeddiately=False):
    num=len(images)
    lie=8
    hang=num/lie+(num%lie!=0)
    plt.figure(1,figsize=(lie*2,hang*10))
    #print hang

    for i in range(hang):
        for j in range(lie):
            index=i*lie+j+1
            if index>num:
                break
            image_path=images[index-1]
            
            pt=plt.subplot(hang,lie,index)
            #image = caffe.io.load_image(image_path)
            img=show(image_path,pt)
            print '[%d] %s {%dx%d}' % ((i*lie+j+1),image_path,img.shape[0],img.shape[1])
            pt.set_xticks([])
            pt.set_yticks([])
            

    plt.tight_layout()
    if showimeddiately:
        plt.show()



def _shows_ownfun(images,ofun):
    num=len(images)
    lie=8
    hang=num/lie+(num%lie!=0)
    plt.figure(1,figsize=(lie*2,hang*10))
    #print hang
    for i in range(hang):
        for j in range(lie):
            index=i*lie+j+1
            if index>num:
                break
            image_path=images[index-1]
            print '[%d] %s' % ((i*lie+j+1),image_path)
            pt=plt.subplot(hang,lie,index)
            #image = caffe.io.load_image(image_path)
            ofun(image_path,pt,index)
            pt.set_xticks([])
            pt.set_yticks([])
            
    plt.tight_layout()
    plt.show()


def randsub(oset,num=10):
    clist=np.arange(len(oset),dtype=np.int)
    np.random.shuffle(clist)
    if num>len(oset):
        num=len(oset)
    rs=[]
    for i in range(num):
        rs.append(oset[clist[i]])
    return np.array(rs)

def list_file(dirname,depth=1):
    import Queue
    stack= Queue.Queue()
    stack.put((dirname,0))
    mksfile=[]
    dir_count=0
    dir_contain_pic=0
    while not stack.empty():
        dirname,dep=stack.get()
        if dep>depth:
            break
        files=os.listdir(dirname)
        files=[os.path.join(dirname,x) for x in files]
        add_action=False
        for f in files:
            if os.path.isfile(f) and (f.endswith('.jpg') or f.endswith('.png') or f.endswith('.bmp')):
                mksfile.append(f)
                add_action=True
            elif os.path.isdir(f):
                stack.put((f,dep+1))
                dir_count+=1
        if add_action:
            dir_contain_pic+=1
    print 'sum images:'+str(len(mksfile))
    print 'sum dir_count:'+str(dir_count)
    print 'sum dir_contain_image:'+str(dir_contain_pic)
    return mksfile

def show_folder(dirname,page=-1,itemperpage=24,depth=1):
    if DEBUG:
        timestamp=time.time()
    files=list_file(dirname,depth)
    if len(files)==0:
        print 'No file'
        return
    files=[x for x in files if x.endswith('.jpg') or x.endswith('.png') or x.endswith('.bmp')]
    if page==-1:
        showfiles=randsub(files,itemperpage)
    else:
        begin=itemperpage*page
        end=min((page+1)*itemperpage,len(files))
        if begin>len(files):
            print 'No img to show!'
            return
        showfiles=files[begin:end]
    if DEBUG:
        print 'generate list time:'+str(time.time()-timestamp)
        timestamp=time.time()
    showfiles=[x for x in showfiles]
    _shows(showfiles)
    print "sum images:"+str(len(files))
    if DEBUG:
        print 'show time:'+str(time.time()-timestamp)

def show_listfile(listfile,page=-1,itemperpage=24):
    with open(listfile) as f:
        files=[x.strip().split()[0] for x in f]
        if page==-1:
            showfiles=randsub(files,itemperpage)
        else:
            begin=itemperpage*page
            end=min((page+1)*itemperpage,len(files))
            if begin>len(files):
                print 'No img to show!'
                return
            showfiles=files[begin:end]
        _shows(showfiles)
        print 'sum image num:'+str(len(files))

def shows(toshow,page=-1,itemperpage=24,depth=1,savefig=None):
    if isinstance(toshow,str):
        if os.path.isdir(toshow):
            show_folder(toshow,page=page,itemperpage=itemperpage,depth=depth)
        elif os.path.isfile(toshow):
            show_listfile(toshow,page=page,itemperpage=itemperpage)
        else:
            print 'ERROR,not recognized type'
    elif isinstance(toshow,list) or isinstance(toshow,np.ndarray):
        _shows(toshow)
    if savefig:
        plt.savefig(savefig)
    plt.show()
        
class countmap:
    def __init__(self):
        self._mmap={}
    def add(self,value):
        if self._mmap.has_key(value):
            self._mmap[value]+=1
        else:
            self._mmap[value]=1
    def __str__(self):
        return self._mmap.__str__()
    def getmap(self):
        return self._mmap
    def fromarray(self,mlist):
        for m in mlist:
            self.add(m)
    def printme(self):
        for i in self._mmap.keys():
            try:
                print str(i)+':'+str(self._mmap[i])
            except:
                try:
                    print i+':'+str(self._mmap[i])
                except:
                    print 'error:'
                    print i
                    print self._mmap[i]

class mergemap:
    def __init__(self):
        self._mmap={}
    def add(self,key,value):
        if self._mmap.has_key(key):
            self._mmap[key].append(value)
        else:
            self._mmap[key]=[value]
    def __str__(self):
        return self._mmap.__str__()
    def getmap(self):
        return self._mmap
    def fromarray(self,keylist,valuelist):
        for i,key in enumerate(keylist):
            self.add(key,valuelist[i])
    def printcount(self,order='no'):
        keys=self._mmap.keys()
        if order=='str':
            keys=sorted(keys)
        for i in keys:
            try:
                print str(i)+':'+str(len(self._mmap[i]))
            except:
                try:
                    print i+':'+str(len(self._mmap[i]))
                except:
                    print 'error:'
                    print i
                    print self._mmap[i]

    def printme(self):
        for i in self._mmap.keys():
            try:
                print str(i)+':'+self._mmap[i].__str__()
            except:
                try:
                    print i+':'+self._mmap[i].__str__()
                except:
                    print 'error:'
                    print i
                    print self._mmap[i]

def list_to_map(keys,values,repeated=[]):
    kmap={}
    for i,key in enumerate(keys):
        if kmap.has_key(key):
            print key
            repeated.append((key,values[i]))
        else:
            if values!=None:
                kmap[key]=values[i]
            else:
                kmap[key]=[]
    return kmap  
                    
def read_imagelist(filepath):
    images=[]
    labels=[]
    with open(filepath) as f:
        for line in f:
            items=line.strip().split()
            images.append(items[0])
            labels.append(items[1:])
    return (images,labels)

def read_imagelist_tomap(filepath):
    images,labels=read_imagelist(filepath)
    return list_to_map(images,labels)

def write_imagelist(filepath,images,labels=None):
    with open(filepath,'w') as f:
        for i,image in enumerate(images):
            line=image
            if labels!=None:
                for label in labels[i]:
                    line+=' '+str(label)
            if i!=0:
                f.write('\n')
            f.write(line)
    return True

def write_map(filepath,mmap):
    return write_imagelist(filepath,mmap.keys(),mmap.values())


def write_imagelist_with_order(filepath,images,labels=None,order=None):
    if order is None:
        write_imagelist(filepath,images,labels=labels)
    else:
        kmap=list_to_map(images,labels)
        with open(filepath,'w') as f:
            for oi in order:
                line=oi
                if labels!=None:
                    for label in kmap[oi]:
                        line+=' '+str(label)
                f.write(line+'\n')
    return True

def format_labels_todigits(labels):
    if isinstance(labels,list):
        labels=[map(int,x) for x in labels]
    if isinstance(labels,dict):
        for k in labels:
            labels[k]=map(int,labels[k])
    return labels
