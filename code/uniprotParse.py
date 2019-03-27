# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:20:26 2019
parse uniport and write in a .txt file
format -> pdbid sequence
@author: neneee
"""

import xml.etree.ElementTree as ET
sequSet = {}
tree = ET.parse('../uniprot/uniprot1.xml')
root = tree.getroot()
xmlns = '{http://uniprot.org/uniprot}'
for child in root:
    nodes = child.findall(xmlns+'dbReference')
    if child.find(xmlns+'sequence') is not None:
        sequence = child.find(xmlns+'sequence').text.replace('\n','')
        for node in nodes:
            if node.attrib['type']=='PDB' or node.attrib['type']=='PDBsum':
                if node.attrib['id'] in sequSet.keys() and sequSet[node.attrib['id']] != sequence:
                    print(node.attrib['id'])
                sequSet[node.attrib['id']] = sequence
with open('uniprot_out.txt', 'w') as f_result:
    for k in sequSet.keys():
        f_result.write(k)
        f_result.write(' ')
        f_result.write(sequSet[k])
        f_result.write('\n')