#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:14:08 2019

@author: mirjamheinemans


TRAINING columns:
    0.unnamed column
    1.MH33,
    2.MH33_in_shelter
    3.MH33_doorway
    4.MH33_with_pellet
    5.MH33_eat_pellet
    6.MH33_freeze
    7.MH33_reaching
    8.MH33_scanning
    9.MH33_new_pellet

TEST columns:
    0.unnamed column
    1.x-value33,
    2.MH33_in_shelter
    3.MH33_doorway
    4.MH33_with_pellet
    5.MH33_eat_pellet
    6.MH33_freeze
    7.MH33_reaching
    8.MH33_scanning
    9.MH33_stim
"""
import scipy.stats as ss
import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') # to change directory Read csv files with Pandas
#%%

path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'


def Trace(file_names):

    if file_names == '.DS_Store':
        next
    else:
       
       dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [1,9])
       stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
       dataset_stim = dataset.iloc[int(stimulus):int(stimulus + 600),:] 
       dataset_stim = dataset_stim.reset_index(drop=True)
       
       
       if len(dataset_stim.loc[dataset_stim.iloc[:,0] <300].index.values.astype(int)) != 0:
           halfway = (dataset_stim.loc[dataset_stim.iloc[:,0] <300].index.values.astype(int)[0])/60
       else:
           halfway = 600/60
       pellet = ['066' , '067' , '036' , '044' , '051', '054' , 
                 '063' , '064' , '070' , '071' , '072' , '096' , 
                 '101' , '037' ,'042' ,'058', '062', '076', '081', '098' ]
       if file_names[-3:] in pellet:
           took_pellet = 'yes'
       else:
           took_pellet = 'no'
           
       dataset_train = pd.read_csv(path_name +'/' + file_names +'/' + 'training.csv', usecols = [1,4])
        
       if int(file_names[2:]) >45:
           dataset_train = dataset_train.groupby(np.arange(len(dataset_train.index))//2).mean()
             
       pellet_train = (dataset_train.iloc[:,1].diff()[dataset_train.iloc[:,1].diff() > 0].index.values[0])/60
        
       d = {file_names: [halfway, pellet_train, took_pellet]}
       df = pd.DataFrame(data=d, index = ['halfway', 'training','took_pellet'])
        
       return(df)

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['xpos']
index = range(1)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)
    shelter_loom = pd.concat([shelter_loom, animal], axis=1, sort = True)

shelter_loom = shelter_loom.drop(columns = ['xpos'])
shelter_loom = shelter_loom.drop(index = 0)
df_l = shelter_loom.T
df_l['condition'] = 'Loom'

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['xpos']
index = range(1)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1, sort = True)

shelter_t_loom = shelter_t_loom.drop(columns = ['xpos'])
shelter_t_loom = shelter_t_loom.drop(index = 0)
df_tl = shelter_t_loom.T
df_tl['condition'] = 'T_Loom'

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['xpos']
index = range(1)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1, sort = True)

shelter_t_shock = shelter_t_shock.drop(columns = ['xpos'])
shelter_t_shock = shelter_t_shock.drop(index = 0)
df_ts = shelter_t_shock.T
df_ts['condition'] = 'T_Shock'
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['xpos']
index = range(1)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1, sort = True)

shelter_tone = shelter_tone.drop(columns = ['xpos'])
shelter_tone = shelter_tone.drop(index = 0)
df_tone = shelter_tone.T
df_tone['condition'] = 'Tone'


#%%
df_all = pd.concat([df_l, df_tl, df_ts, df_tone], axis = 0)

#%%
ax = sns.scatterplot(x="training", y='halfway', hue ='took_pellet',
                     data=df_l,palette = ['black', 'orange'], s = 100)
ax.set_title('Loom: correlation between time to grab pellet during training and reaching x = 300')
ax.set_xlabel('training - first pellet')
ax.set_ylabel('time until animal reaches x =300 (sec)')
ax.set_xlim([0, 400])
ax.legend(bbox_to_anchor=(1,1))

#%%
ax = sns.scatterplot(x="training", y='halfway', hue ='took_pellet',
                     data=df_tl, palette = ['blue', 'orange'], s = 100)
ax.set_title('T-Loom: correlation between time to grab pellet during training and reaching x = 300')
ax.set_xlabel('training - first pellet')
ax.set_ylabel('time until animal reaches x =300 (sec)')
ax.set_xlim([0, 400])
ax.legend(bbox_to_anchor=(1,1))

#%%
ax = sns.scatterplot(x="training", y='halfway', hue ='took_pellet',
                     data=df_ts, palette = ['red', 'orange'], s = 100)
ax.set_title('T-Loom: correlation between time to grab pellet during training and reaching x = 300')
ax.set_xlabel('training - first pellet')
ax.set_ylabel('time until animal reaches x =300 (sec)')
ax.set_xlim([0, 400])
ax.legend(bbox_to_anchor=(1,1))

#%%
ax = sns.scatterplot(x="training", y='halfway', hue ='took_pellet',
                     data=df_tone, palette = ['orange', 'green'], s = 100)
ax.set_title('T-Loom: correlation between time to grab pellet during training and reaching x = 300')
ax.set_xlabel('training - first pellet')
ax.set_ylabel('time until animal reaches x =300 (sec)')
ax.set_xlim([0, 700])
ax.legend(bbox_to_anchor=(1,1))

#%%


ax = sns.scatterplot(x="training", y="halfway", hue ='condition',
                     data=df_all, palette = ['black', 'blue', 'red', 'green'], s = 100)
ax.set_title('correlation between time to grab pellet during training and reaching x = 300')
ax.set_xlabel('training - first pellet')
ax.set_ylabel('test')
#ax.set_ylim([-10, 100])
ax.legend(bbox_to_anchor=(1,1))


                             # palette = ['black', 'blue', 'red', 'green']
        

