# -*- coding: utf-8 -*-
"""
	File Name ：    faCode
	Description :   code family id 
	Author :        Gong Yingli
	Time ：         Sat Apr  6 12:56:02 2019
"""
import numpy as np

class faCode(object):
    def __init__(self):
        self.dic = {}
        self.length = 0
        
    def main(self):
        with open('../data/sequ_fa.txt') as f:
            lines = f.readlines()
            count = 0
            num = 0
            for line in lines:
                count += 1
                if count % 2 == 1:
                    continue
                for id in line.split():
                    if id not in self.dic.keys():
                        self.dic[id] = num
                        num += 1        
# =============================================================================
#         with open('../data/dic_fa.txt','w') as fw:
#             for key in self.dic.keys():
#                 fw.write(str(key) + ':' + str(self.dic[key]))
#                 fw.write('\n')
# =============================================================================
        self.length = num
        
    def noSeq_label_creator(self):
        with open('../data/sequ_fa.txt') as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                count += 1
                if count % 2 == 1:
                    continue
                label = np.zeros(self.length,int)
                for id in line.split():
                    label[self.dic[id]] = 1                
                np.savetxt("../data/noSeq_label/" + str(int(count/2)-1) + ".label", label, fmt="%d") 
                        
if __name__ == "__main__": 
    facode = faCode()
    facode.main()
    facode.noSeq_label_creator()