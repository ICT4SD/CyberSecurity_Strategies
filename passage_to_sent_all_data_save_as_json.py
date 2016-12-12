# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:02:11 2016
save passage to senten results as json files
@author: Liyi Li
"""



import json
import re
import string
import nltk
import uuid
import glob

files = glob.glob('D:/lly/UN_CYBER SECURITY/CyberSecurity_Strategies-Fordham_Designlab/CyberSecurity_Strategies-Fordham_Designlab/data_raw/*.txt')

for name in files:
    passage = open(name,'r').read()
    passage =''.join(filter(lambda x: x in string.printable, passage.replace('\n',' ')))

    content_pattern = re.compile("[0-9]+\.$")
    sentences = list()
    for sen in nltk.sent_tokenize(passage): 
        sen = ' '.join(sen.split())
        if not content_pattern.search(sen) and len(sen)>25: 
            sentences.append(sen)      
        
    sentence_id = [(uuid.uuid4().hex[:10],i) for i in sentences]        

    sentence_dic = [dict(map(None,['sentence_id,','sentence'],list(sent))) for sent in sentence_id]


    output_name = name + 'output.json'
    with open(output_name, 'w') as f:
        json.dump(sentence_dic,f,sort_keys = True, indent= 4)