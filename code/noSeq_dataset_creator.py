# -*- coding:utf-8 -*-
'''
	File Name：     noSeq_dataset_creator
	Description :   create the dataset(training set & testing set) with noSeq feature
	Author :        Gong Yingli (original:Liu Zhe)
	date：          Mon Apr 15 16:55:43 2019
        
'''

import numpy as np

########################################################################
class noSeq_dataset_creator(object):
    
    def __init__(self):
        self.trainList = list(range(1000))
        self.testList = list(range(1000,1500))
    
    def create_x_train_set(self):
        i = self.trainList[0]
        x_train = np.loadtxt("../data/residue_one_hot_noSeq_code/" + str(i) + ".ncode",int)
        x_train = x_train[np.newaxis, :]
        print(x_train.shape)
        for i in self.trainList[1:]:
            matrix = np.loadtxt("../data/residue_one_hot_noSeq_code/" + str(i) + ".ncode",int)
            matrix = matrix[np.newaxis, :]
            #print(matrix.shape)
            x_train = np.vstack((x_train,matrix))
            #print(x_train.shape)
        np.save("../data/train_data/x_train_noSeq.npy", x_train, int)
        #print(x_train)
        print(x_train.shape)
    
    def create_x_test_set(self):
        i = self.testList[0]
        x_test = np.loadtxt("../data/residue_one_hot_noSeq_code/" + str(i) + ".ncode",int)
        x_test = x_test[np.newaxis, :]
        print(x_test.shape)
        for i in self.testList[1:]:
            matrix = np.loadtxt("../data/residue_one_hot_noSeq_code/" + str(i) + ".ncode",int)
            matrix = matrix[np.newaxis, :]
            #print(matrix.shape)
            x_test = np.vstack((x_test,matrix))
            #print(x_test.shape)
        np.save("../data/test_data/x_test_noSeq.npy", x_test, int)
        #print(x_test)
        print(x_test.shape)
        
    def create_y_train_set(self):
        i = self.trainList[0]
        y_train = np.loadtxt("../data/noSeq_label/" + str(i) + ".label",int)
        y_train = y_train[np.newaxis, :]
        print(y_train.shape)
        for i in self.trainList[1:]:
            matrix = np.loadtxt("../data/noSeq_label/" + str(i) + ".label",int)
            matrix = matrix[np.newaxis, :]
            #print(matrix.shape)
            y_train = np.vstack((y_train,matrix))
            #print(y_train.shape)
        np.save("../data/train_data/y_train_noSeq.npy", y_train, int)
        #print(y_train)
        print(y_train.shape)
    
    def create_y_test_set(self):
        i = self.testList[0]
        y_test = np.loadtxt("../data/noSeq_label/" + str(i) + ".label",int)
        y_test = y_test[np.newaxis, :]
        print(y_test.shape)
        for i in self.testList[1:]:
            matrix = np.loadtxt("../data/noSeq_label/" + str(i) + ".label",int)
            matrix = matrix[np.newaxis, :]
            #print(matrix.shape)
            y_test = np.vstack((y_test,matrix))
            #print(y_test.shape)
        np.save("../data/test_data/y_test_noSeq.npy", y_test, int)
        #print(y_test)
        print(y_test.shape)    
            
########################################################################
if __name__ == "__main__": 
    creator = noSeq_dataset_creator()
    creator.create_x_train_set()
    creator.create_x_test_set()
    #show = np.load("train_data/x_train_noSeq.npy")
    #print(show)   
    
    creator.create_y_train_set()
    creator.create_y_test_set()



