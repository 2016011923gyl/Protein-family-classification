# -*- coding: utf-8 -*-
"""
	File Name ：    getPDBandFA
	Description :   get PDBid and their family num
	Author :        Gong Yingli
	Time ：         Wed Mar 27 19:12:18 2019
"""


from collections import Counter

class getPDBandFA:
    
     #dKeypdb:key is pdb
     #dKeyfamily:key is family
    def __init__(self):
        
        self.version = ['','-S35','-S60','-S95','-S100'] 
        
    def getCATH(self,n):
        
        file = 'cath-domain-list-S100.txt'
        #file = 'cath-domain-list' + self.version[n] + '.txt'
        f = open(file)
        data_full = f.readlines()
        dKeypdb = {}
        dKeyfamily = {}
        for line in  data_full:
            if line[0] == '#':
                continue
            item = line.split()
            keypdb = item[0][:4]
            if keypdb not in dKeypdb.keys():
                dKeypdb[keypdb] = []
            family = ''
            for i in range(1,9):
                if i == n+5:
                    break
                family += item[i]
                if i != n+4:
                    family += '.'
            dKeypdb[keypdb].append(family)
            keyfamily = family
            if keyfamily not in dKeyfamily.keys():
                dKeyfamily[keyfamily] = []
            dKeyfamily[keyfamily].append(item[0][:4])
        for key in dKeypdb:                 #no repeat
            dKeypdb[key] = list(set(dKeypdb[key]))
        for key in dKeyfamily:
            dKeyfamily[key] = list(set(dKeyfamily[key]))
                        
        f.close()        
        return dKeypdb,dKeyfamily
    
    
    def getSCOPe(self):
        f = open('dir.cla.scope.2.07-stable.txt')
        data_full = f.readlines() 
        dKeypdb = {}
        dKeyfamily = {}
        for line in data_full:
            if line[0] == '#':
                continue
            keypdb = line[1:5]
            if keypdb not in dKeypdb.keys():
                dKeypdb[keypdb] = []
            item = line.split(',')
            for i in item:
                if i[:3] == 'fa=':
                    dKeypdb[keypdb].append(i[3:])
                    keyfamily = i[3:]
                    break
            if keyfamily not in dKeyfamily.keys():
                dKeyfamily[keyfamily] = []
            dKeyfamily[keyfamily].append(item[0][1:5])
        for key in dKeypdb:                 #no repeat
            dKeypdb[key] = list(set(dKeypdb[key]))
        for key in dKeyfamily:
            dKeyfamily[key] = list(set(dKeyfamily[key]))
       
        f.close()
        return dKeypdb,dKeyfamily
    
    def countDict(self,data):       #result:how many keys have the same number of value
        count = []                  #valueNotUniq:a key has more than one value(pdb / family)
        valueNotUniq = {}           
        for key in data:
            if len(data[key])> 1:
                valueNotUniq[key] = data[key]
            count.append(len(data[key]))
        result = dict(Counter(count))
        return result,valueNotUniq    
    
    def outFiles(self,data,str,n):
        if str == 'CATH':
            fileName = 'result_CATH_' + self.version[n] + '.txt'
        else:
            fileName = 'result_SCOPe.txt'
        with open(fileName, 'w') as f_result:
            for k in data.keys():
                st = k + ':'
                for i in data[k]:
                    st += ' '
                    st += i
                f_result.write(st)
                f_result.write('\n')
    
    
if __name__ == '__main__':
    
    temp = getPDBandFA()
# =============================================================================
#     
#     n = [0,1,2,3,4]
#     for v in n:
#         pdbSet,familySet = temp.getCATH(v)
#         pdbCount,pdb = temp.countDict(pdbSet)
#         faCount,fa = temp.countDict(familySet)
#         temp.outFiles(familySet,'CATH',v)        
# =============================================================================
    pdbSet,familySet = temp.getSCOPe()
    temp.outFiles(pdbSet,'SCOPe','')
    
    