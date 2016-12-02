from gensim.models.ldamodel import LdaModel
import gensim
import pandas as pd
import glob
import sys
import os

## change dir
os.chdir(os.getcwd()+'\data')

class Go_Ram():

    def get_data(self):
        
        print(sys.version_info) ### Make sure you are using Python3
        
        dict_data = {}
        country_list = []
        content_list = []
        
        for i in glob.glob('*.txt'):
            with open(i,encoding='utf-8',errors = 'ignore') as f:
                country_list += [i.split('.')[0]]
                content = f.readlines()
                content_list += [''.join(list(filter(None, list(map(lambda x:x.strip(), content)))))]
        dict_data['country'] = country_list
        dict_data['content'] = content_list
        df_all = pd.DataFrame(dict_data)

        self.df = df_all
        
        return self.df
    
#################


    def dictionary(self):
    def lda(self):
        
        
#################    