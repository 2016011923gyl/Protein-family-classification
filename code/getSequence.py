# -*- coding: utf-8 -*-
"""
	File Name ：    getSequence
	Description :   get sequence from uniprot with PDBid and union them
	Author :        Gong Yingli
	Time ：         Wed Mar 27 19:16:00 2019
"""

import xml.etree.ElementTree as ET
import re
import getPDBandFA

class getSequence:
    def __init__(self):
        pass
    def getUniprot(self):
        sequSet = {}
        tree = ET.parse('../uniprot/uniprot.xml')
        root = tree.getroot()
        xmlns = '{http://uniprot.org/uniprot}'
        for child in root:
            nodes = child.findall(xmlns+'dbReference')
            if child.find(xmlns+'sequence') is not None:
                sequence = child.find(xmlns+'sequence').text.replace('\n','')
                for node in nodes:
                    if node.attrib['type']=='PDB' or node.attrib['type']=='PDBsum':
                        pdbKey = node.attrib['id'].lower()
                        sequSet[pdbKey] = sequence
        return sequSet
    def getDataSet(self):
        sequSet = self.getUniprot()
# =============================================================================
#         temp = getPDBandFA.getPDBandFA()
#         pdbSet,familySet = temp.getSCOPe()
#         temp.outFiles(pdbSet,'SCOPe','')
# =============================================================================
        with open('result_SCOPe.txt', 'r') as f_name:
            dataSet = {}
            name = f_name.readlines()
            for item in name:
                if item[:4] in sequSet.keys():
                    dtemp = {}
                    dtemp['sequence'] = sequSet[item[:4]]
                    dtemp['class'] = item[4:]
                    dataSet[item[:4]] = dtemp
        return dataSet
        
        
        
        
if __name__ == '__main__':

    temp2 = getSequence()
    dic = temp2.getDataSet()

    with open('pdb_union_uniprot.txt', 'w') as f_result:
        for k in dic.keys():
            f_result.write(k)
            f_result.write(dic[k]['class'])
            f_result.write(dic[k]['sequence'])
            f_result.write('\n')

