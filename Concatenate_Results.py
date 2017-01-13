import pandas as pd
import numpy
import os
import glob
import datetime
import json

def process_file (path , file):    #This function handles each file
    df = pd.read_json(path+file)
    full_string = file
    nice_string = full_string.replace('.txtoutput.jsontag.json','')
    df["Country"] = nice_string
    return df

source = './tag_to_sentence_1212/'  #This folder contains the individual country files
destination = './output/'           #This folder contains the resulting file
results_filename = destination + 'results_' + str(datetime.datetime.now())
file_filter = '*'                   #This cane be used to limit the files which should be handled e.g. '*.txt'

#This obtains the list of files to process
os.chdir(source)                    #move to source dir
file_list = glob.glob(file_filter)  
os.chdir("..")                      #return to starting dir

#This creates dataframes for each file and concatenates them
frames = []
for i in range(len(file_list)):
    a = process_file(source , file_list[i])
    frames.append(a)
result = pd.concat(frames)

#result.to_csv(results_filename) #Use this line if you wish to save to csv
mydico = result.to_dict(orient='records')

#write the new json file
with open(results_filename, 'w') as f:
    json.dump(mydico,f,sort_keys = True, indent= 4)