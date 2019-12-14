#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:12:50 2019

@author: mirjamheinemans
"""

#%%
import csv 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
import os, glob # Operating System
import pandas as pd
os. chdir("/Users/mirjamheinemans/Desktop/Annotator python tryout")
os.getcwd() #short for get Current Work Directory
#os.listdir(os.getcwd()) # to know which folders you can get with relative path
#os.chdir() # to change directoryRead csv files with Pandas

#%%

path = os.getcwd()
#filename =path+'\all_animals.csv'
df = pd.read_csv(path+'/training_pellet.csv',delimiter=',',index_col =[0], low_memory=False)

df_numeric = df.apply(pd.to_numeric, errors='coerce')
#df_combined = df_numeric.combine_first(df)











#%%
tr1 = df_numeric.groupby('Training1').count()
tr2 = df_numeric.groupby('Training2').count()

tr = pd.concat([tr1,tr2], axis =1)
tr = tr.reset_index()
index = tr.index
tr_T = tr.T
#%%
plt.hist([tr_T[0],tr_T[1],tr_T[2], tr_T[3]], bins=4,label=['1',' 2','3', '4'])

#%%
ax = tr[['Training1', 'Training2']].plot(kind ='bar')
ax.set_title('Number of animals that ate 0, 1, 2, or 3 pellets')