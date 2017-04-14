#!/usr/bin/env python
# @Author: zhen zhong
# @Date: March 22 2017
# Draw the loss curve by parsing the log generated by caffe

import sys
import os
import matplotlib.pyplot as plt

batchSize = 128
trainFileNum = 74109 
iterPerEpoch = float(trainFileNum) / batchSize
maxDisplayEpoch = 30

def parseLogFile(logfn, lossNum = 0):
	logFile = open(logfn)
	lines = logFile.readlines()
	epochList = {"Train":[],"Test":[]}
	lossList = {"Train":[],"Test":[]}
	for line in lines:
		lexArr = line.split()
		if len(lexArr) < 5:
			continue
		if lexArr[4] == "Iteration":
			if lexArr[5][-1] == ",":
				iterNum = int(lexArr[5][:-1])
			else:
				iterNum = int(lexArr[5])
		if len(lexArr) < 11:
			continue
		if (lexArr[4] == "Test" or lexArr[4] == "Train") and lexArr[5] == "net" and int(lexArr[7][1:-1]) == lossNum:
			loss = float(lexArr[10])
			epoch = iterNum / iterPerEpoch
			epochList[lexArr[4]].append(epoch)
			lossList[lexArr[4]].append(loss)

			if epoch > maxDisplayEpoch:
				break

	return (epochList, lossList)	

if __name__=='__main__':
	if len(sys.argv) != 2:
        	print 'Usage:./log_loss.py <caffe_train_log_dir>'
        	exit(1)
	colorArr = ['b','c','g','k','m','r','w','y']
	colorInd = 0
	
	logDir = os.path.abspath(sys.argv[1])
	logFileArr = os.listdir(logDir)
	for logFileName in logFileArr:
		lossNum = 0
		fnLexArr = logFileName.split("_")
		modelName = logFileName.split(".")[0]
		if len(fnLexArr) > 2 and fnLexArr[2] == "3loss":
			lossNum = 2
		epochList, lossList = parseLogFile(logDir + "/" + logFileName, lossNum)	
		plt.plot(epochList["Train"],lossList["Train"],colorArr[colorInd] + "--", label=modelName+"-train", )
		plt.plot(epochList["Test"],lossList["Test"],colorArr[colorInd],label=modelName+"-test",)
		colorInd += 1
		plt.legend()
	
	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.show()





			

    