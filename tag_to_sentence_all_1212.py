# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:34:01 2016

@author: Liyi Li
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:57:46 2016

@author: williamz
"""

import nltk
import json
import sys
import glob

porter = nltk.PorterStemmer()
#label list: keep original category, but stem subcategory 
category = json.load(open('category.json'))
category_stem = list()  
for i in category:
    temp = i.copy()
    temp['subcategory'] = [' '.join([porter.stem(w) for w in s.split()]) for s in temp['subcategory']]
    category_stem.append(temp)  

def tag(sentence):
    label =list()
    for i in range(len(category_stem)):  #go through all the categories
        sig_label = {'category':'','subcategory':[]}
        for j in range(len(category_stem[i]['subcategory'])):
            if category_stem[i]['subcategory'][j] in sentence:
                sig_label['category'] = category_stem[i]['category']
                sig_label['subcategory'].append(category[i]['subcategory'][j])
        if sig_label['category']:
            label.append(sig_label)
    return label
    
json_files = glob.glob('D:\lly\UN_CYBER SECURITY\CyberSecurity_Strategies-Fordham_Designlab\CyberSecurity_Strategies-Fordham_Designlab\passage_to_sentence_json_1212\*.txtoutput.json')
for name in json_files:
    test_passage = json.load(open(name))
    #passage = open(name,'r').read()
    result = list()    
    for line in test_passage:
        sentence_stem = ' '.join(porter.stem(w) for w in line['sentence'].lower().split())
        label = tag(sentence_stem)
        if label:
            line['tag'] = label
            result.append(line)
        
    print json.dumps(result, indent= 4)
    #data = json.dumps(result, indent= 4)
    output_name = name + 'tag.json'
    with open(output_name, 'w') as f:
        json.dump(result, f, indent= 4)
    