# -*- coding: utf-8 -*-
"""
	File Name ：    dicTransform
	Description :   sequence and family id;capture sequence with abnormal character
	Author :        Gong Yingli
	Time ：         Fri Apr  5 20:44:31 2019
"""

class dicTransform(object):
    def __init__(self):
        self.dict = {'C':1, 'D':2, 'S':3, 'Q':4, 'K':5,
                'I':6, 'P':7, 'T':8, 'F':9, 'N':10,
                'G':11, 'H':12, 'L':13, 'R':14, 'W':15,
                'A':16, 'V':17, 'E':18, 'Y':19, 'M':20}
    def main(self):
        count = 0
        dic = {}
        with open('../data/pdb_union_uniprot.txt') as f:
            with open('../data/abnormal_squence.txt','w') as fw:
                lines = f.readlines()
                for line in lines:
                    if count % 2 == 0:
                        value = line.split(':')[1].split()
                    else:
                        flag = 1
                        for i in line:
                            if i != '\n' and i not in self.dict.keys():
                                fw.write(line)
                                fw.write('\n')
                                flag = 0
                                break
                        if flag:
                            if line not in dic.keys():
                                dic[line] = value
                            else:
                                for i in value:
                                   dic[line].append(i) 
                    count += 1
        for key in dic:
            dic[key] = list(set(dic[key]))        
        return dic
                
if __name__ == "__main__": 
    dicTf = dicTransform()
    dic = dicTf.main()
    with open('../data/squ_fa.txt', 'w') as f_result:
        for k in dic.keys():
            f_result.write(k)
            for i in dic[k]:
                f_result.write(' ')
                f_result.write(i)
            f_result.write('\n')

