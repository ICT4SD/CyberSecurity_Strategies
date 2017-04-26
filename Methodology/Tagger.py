# -*- coding:utf-8 -*-
#_author_ = "Youwei Xiao"

import nltk
import json
import sys
import glob

#load the data and set up the Porter
# porter = nltk.PorterStemmer()
keywords = json.load(open("Dictionary/Dictionary_1.json"))
keywords2 = json.load(open("Dictionary/Dictionary_2.json"))
keywords3 = json.load(open("Dictionary/Dictionary_3.json"))

def tag(sentence):
    label = list()
    word_list = sentence.split()
    sig_label = {"category": [], "subcategory": [], "keywords": []}
    for i in range(len(keywords)):
        for j in range(len(keywords[i]["keywords"])):
            for z in range(len(keywords[i]["keywords"][j])):
                for word in word_list:
                    if keywords[i]['keywords'][j][z] == word:
                        k_1 = keywords[i]["subcategory"][j]
                        k_2 = keywords[i]["keywords"][j][z]
                        k = {k_1 : k_2}
                        sig_label["keywords"].append(k)
                        if not keywords[i]["category"] in sig_label["category"]:
                            sig_label["category"].append(keywords[i]["category"])
                        if not keywords[i]["subcategory"][j] in sig_label["subcategory"]:
                            sig_label["subcategory"].append(keywords[i]["subcategory"][j])

    for i in range(len(keywords2)):
        for j in range(len(keywords2[i]["keywords"])):
            for z in range(len(keywords2[i]["keywords"][j])):
                for h in range(len(word_list)-1):
                    phrase = word_list[h] + " " + word_list[h+1]
                    if keywords2[i]['keywords'][j][z] == phrase:
                        k_1 = keywords2[i]["subcategory"][j]
                        k_2 = keywords2[i]["keywords"][j][z]
                        k = {k_1 : k_2}
                        sig_label["keywords"].append(k)
                        if not keywords[i]["category"] in sig_label["category"]:
                            sig_label["category"].append(keywords[i]["category"])
                        if not keywords[i]["subcategory"][j] in sig_label["subcategory"]:
                            sig_label["subcategory"].append(keywords[i]["subcategory"][j])

    for i in range(len(keywords3)):
        for j in range(len(keywords3[i]["keywords"])):
            for z in range(len(keywords3[i]["keywords"][j])):
                for h in range(len(word_list)-2):
                    phrase3 = word_list[h] + " " + word_list[h+1] + " " + word_list[h+2]
                    if keywords3[i]['keywords'][j][z] == phrase3:
                        k_1 = keywords3[i]["subcategory"][j]
                        k_2 = keywords3[i]["keywords"][j][z]
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


json_files = glob.glob('Materials\*.txtoutput.json')
for name in json_files:
    test_passage = json.load(open(name))
    result = list()
    for line in test_passage:
        sentence_stem = ' '.join(w for w in line['sentence'].lower().split())
        label = tag(sentence_stem)
        if label:
            line['tag'] = label
            result.append(line)

    print json.dumps(result, indent=4)
    # data = json.dumps(result, indent= 4)
    output_name = name + 'tag.json'
    with open(output_name, 'w') as f:
        json.dump(result, f, indent=4)


# #
# # json_files = glob.glob("C:\Users\yxiao\Desktop\Cyber Security\USA\*.txt")
# # for name in json_files:
# test_passage = json.load(open("Materials/US-2.txtoutput.json"))
# #passage = open(name,"r").read()
# result = list()
#
# for line in test_passage:
#     sentence_stem = " ".join(w for w in line["sentence"].lower().split())
#     # print sentence_stem
#     label = tag(sentence_stem)
#     if label:
#         line['tag'] = label
#         result.append(line)
#
#
# print json.dumps(result, indent=4)
# #data = json.dumps(result, indent = 4)
# output_name = "US-2-tag.json"
# with open(output_name, "w") as f:
#     json.dump(result, f, indent= 4)