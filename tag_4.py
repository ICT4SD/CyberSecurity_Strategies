# -*- coding:utf-8 -*-
_author_ = "Youwei Xiao"

import nltk
import json
import sys
import glob

#load the data and set up the Porter
porter = nltk.PorterStemmer()
keywords = json.load(open("keywords-new-1.json"))
print keywords

# Transfer the keywords into stem
keywords_stem = list()
for i in keywords:
    temp = i.copy()
    for k in range(len(temp["keywords"])):
        temp['keywords'][k] = [' '.join([porter.stem(w) for w in s.split()]) for s in temp['keywords'][k]]
    keywords_stem.append(temp)
print keywords_stem
# for t in keywords_stem:
#     print t
keywords = json.load(open("keywords-new-1.json"))
print keywords

# set up the function of tag
def tag(sentence):
    label = list()
    # sig_label = {"category": [], "subcategory": [], "keywords": []}
    sig_label = {"category": [], "subcategory": [], "keywords": []}
    for i in range(len(keywords_stem)):
        for j in range(len(keywords_stem[i]["keywords"])):
            for z in range(len(keywords_stem[i]["keywords"][j])):
                if keywords_stem[i]['keywords'][j][z] in sentence:
                    k_1 = keywords[i]["subcategory"][j]
                    k_2 = keywords[i]["keywords"][j][z]
                    k = {k_1 : k_2}
                    sig_label["keywords"].append(k)
                    if not keywords[i]["category"] in sig_label["category"]:
                        sig_label["category"].append(keywords[i]["category"])
                    if not keywords[i]["subcategory"][j] in sig_label["subcategory"]:
                        sig_label["subcategory"].append(keywords[i]["subcategory"][j])
    if sig_label["keywords"]:
        label.append(sig_label)
    else:
        sig_label2 = {"category": [], "subcategory": [], "keywords": []}
        label.append(sig_label2)
    return label
#
# json_files = glob.glob("C:\Users\yxiao\Desktop\Cyber Security\USA\*.txt")
# for name in json_files:
test_passage = json.load(open("US-1.json"))
#passage = open(name,"r").read()
result = list()

for line in test_passage:
    sentence_stem = " ".join(porter.stem(w)for w in line["sentence"].lower().split())
    # print sentence_stem
    label = tag(sentence_stem)
    if label:
        line['tag'] = label
        result.append(line)


print json.dumps(result, indent=4)
#data = json.dumps(result, indent = 4)
output_name = "US-1-tag.json"
with open(output_name, "w") as f:
    json.dump(result, f, indent= 4)