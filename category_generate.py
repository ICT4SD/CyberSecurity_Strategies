# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:53:29 2016

@author: williamz
"""
import json

test = open('category.txt','r')

lines = [line.strip() for line in test]

def clean(line):
    return ' '.join(line.lower().split())[1:-1]

lines = [clean(line) for line in lines]
result = list()
for row in lines:
    row = row.split('|')
    dic = dict()
    dic['category'] = row[0].strip()
    dic['subcategory'] = [text.strip() for text in row[1].split(',')]
    result.append(dic)

with open('category.json','w') as f:
    f.write(json.dumps(result,indent=4))
    f.close()