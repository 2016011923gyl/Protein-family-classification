# -*- coding: utf-8 -*-
'''
	File Name：     residue_coder
	Description :   use one-hot code to build the residue feature matrix
	Author :        Gong Yingli (original:Liu Zhe)
	date：          Fri Apr  6 23:26:52 2019
'''

import os
import numpy as np
from keras.utils import to_categorical

########################################################################
class residue_coder(object):
    '''
    d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
         'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
         'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
         'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    '''
    def __init__(self):
        pass
    
    def main(self):
        dict = {'C':0, 'D':1, 'S':2, 'Q':3, 'K':4,
                'I':5, 'P':6, 'T':7, 'F':8, 'N':9,
                'G':10, 'H':11, 'L':12, 'R':13, 'W':14,
                'A':15, 'V':16, 'E':17, 'Y':18, 'M':19}
        with open('../data/sequ_fa.txt') as f:
            count = 0
            lines = f.readlines()
            with open('../data/list_legal_file.txt','w') as list_legal_file:
                for line in lines:
                    count += 1
                    if count % 2 == 0:
                        continue
                    codelist = []
                    for stri in line:
                        if stri == '\n':
                            continue
                        code = dict[stri.upper()]
                        codelist.append(code)
                
                    data = np.array(codelist)
                    #print('Shape of data (BEFORE encode): %s' % str(data.shape))
                    encoded = to_categorical(data)
                    if(encoded.shape[1] <20):
                        column = np.zeros([encoded.shape[0],20-encoded.shape[1]],int)
                        encoded = np.c_[encoded,column]
                    #print('Shape of data (AFTER  encode): %s\n' % str(encoded.shape))
                    #print(encoded.shape)
                    
                    np.savetxt("../data/residue_one_hot_code/" + str(int(count/2)) + ".code", encoded, fmt="%d") 
                    
                    list_legal_file.write(str(int(count/2)) + ".code" + '\n')
                    
                    
            
########################################################################
if __name__ == "__main__": 
    coder = residue_coder()
    coder.main()

