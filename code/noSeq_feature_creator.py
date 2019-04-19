# -*- coding: utf-8 -*-
"""
	File Name ：    noSeq_feature_creator
	Description :   create a feature called noSeq & cut/pad each sequence to 700 residues
	Author :        Gong Yingli (original:Liu Zhe)
	Time ：         Sat Apr  6 11:26:52 2019
"""

import numpy as np

########################################################################
class noSeq_feature_creator(object):
    
    def __init__(self):
        pass
    
    def main(self):
        
        with open("../data/list_legal_file.txt", "r") as legal_list:
            legalfileline = legal_list.readline()
            while legalfileline:
                code = np.loadtxt("../data/residue_one_hot_code/" + legalfileline.strip())
                #print(code)
                length = code.shape[0]
                feature = code.shape[1]
                #print(length)
                #print(feature)
                noSeq = np.zeros([length,1],int)
                code = np.c_[code,noSeq]
            
                if(length <= 700):
                    row = np.zeros([700-length,feature],int)
                    noSeq = np.ones([700-length,1],int)
                    row = np.c_[row,noSeq]
                    code = np.r_[code,row]
                else:
                    code = code[0:700,:]                
                #print(code.shape)
            
                np.savetxt("../data/residue_one_hot_noSeq_code/" + legalfileline.split('.')[0] + ".ncode", code, fmt="%d")                 
                legalfileline = legal_list.readline()
                
    def local(self):
        code = np.loadtxt("../data/residue_one_hot_code/1.code")
        #print(code)
        length = code.shape[0]
        feature = code.shape[1]
        #print(length)
        #print(feature)
        noSeq = np.zeros([length,1],int)
        code = np.c_[code,noSeq]
        #code = np.r_[np.c_[np.zeros([8,20],int),np.ones(8,int)],code]
        length = code.shape[0]

        if(length <= 700):
            row = np.zeros([700-length,feature],int)
            noSeq = np.ones([700-length,1],int)
            row = np.c_[row,noSeq]
            code = np.r_[code,row]
        else:
            code = code[0:700,:]
        #print(code)

        np.savetxt("../data/residue_one_hot_noSeq_code/1.ncode", code, fmt="%d")  

            
########################################################################
if __name__ == "__main__": 
    creator = noSeq_feature_creator()
    #creator.local()
    creator.main()



