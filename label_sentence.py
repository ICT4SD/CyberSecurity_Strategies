# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:57:46 2016

@author: williamz
"""

import nltk
import json
import sys

porter = nltk.PorterStemmer()

try:
    path = sys.argv[1]
    category = json.load(open('category.json'))
    test_passage = json.load(open(path))
    passage = open(path,'r').read()
except:
    print 'Not Valid File Path or json File \n','Use', sys.argv[0],'<file_path>'
    exit(2)

category_stem = list()
for i in category:
    temp = i.copy()
    temp['subcategory'] = [' '.join([porter.stem(w) for w in s.split()]) for s in temp['subcategory']]
    category_stem.append(temp)

def tag(sentence):
    label =list()
    for i in range(len(category_stem)):
        sig_label = {'category':'','subcategory':[]}
        for j in range(len(category_stem[i]['subcategory'])):
            if category_stem[i]['subcategory'][j] in sentence:
                sig_label['category'] = category_stem[i]['category']
                sig_label['subcategory'].append(category[i]['subcategory'][j])
        if sig_label['category']:
            label.append(sig_label)
    return label
    
result = list()    
for line in test_passage:
    sentence_stem = ' '.join(porter.stem(w) for w in line['sentence'].lower().split())
    label = tag(sentence_stem)
    if label:
        line['tag'] = label
        result.append(line)
        
print json.dumps(result, indent= 4)