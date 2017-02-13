# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:53:59 2016

@author: williamz
"""
import sys
import json
import re
import string
import nltk
import uuid

try:
    path = sys.argv[1]
    passage = open(path,'r').read()
except:
    print 'Not Valid File Path.\n','Use', sys.argv[0],'<file_path>'
    sys.exit(2)
passage =''.join(filter(lambda x: x in string.printable, passage.replace('\n',' ')))

content_pattern = re.compile("[0-9]+\.$")
sentences = list()
for sen in nltk.sent_tokenize(passage): 
    sen = ' '.join(sen.split())
    if not content_pattern.search(sen) and len(sen)>25: 
        sentences.append(sen)      
        
sentence_id = [(uuid.uuid4().hex[:10],i) for i in sentences]        

sentence_dic = [dict(map(None,['sentence_id,','sentence'],list(sent))) for sent in sentence_id]

print json.dumps(sentence_dic,sort_keys = True, indent= 4)