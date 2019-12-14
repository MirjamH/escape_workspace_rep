#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:37:21 2019

@author: mirjamheinemans

The amount of time that the animals spend in an area ([-200 200]) around the stimulus, 
OR has the pellet

first open the test file, extract three columns:
    ['MH33_in_shelter'], ['MH33_with_pellet'], ['MH33_stim']

TRAINING columns:
    MH33,
    MH33_in_shelter
    MH33_doorway
    MH33_with_pellet
    MH33_eat_pellet
    MH33_freeze
    MH33_reaching
    MH33_scanning
    MH33_new_pellet

TEST columns:
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

os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files') # to change directory Read csv files with Pandas
#%%

path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'


def InArea(file):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [4,9])
        stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
        
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +54000)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
        
        dataset_stim.iloc[-1,0] = 1
        pellet = (int(dataset_stim.loc[dataset_stim.iloc[:,0] == 1].index.values.astype(int)[0])/60)
        

        return(pellet)
  
#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['pellet', 'animal', 'condition']
index = range(0,11)
pellets_loom = pd.DataFrame(index = index, columns = columns)
x = 0

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    if file_names == '.DS_Store':
        next
    else:
        pellet = InArea(file_names)  
        animal = file_names
        pellets_loom.iloc[x,0] = pellet
        pellets_loom.iloc[x,1] = animal
        pellets_loom.iloc[x,2] = 'Loom'
        x +=1
print(pellets_loom)

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'

columns = ['pellet', 'animal', 'condition']
index = range(11,30)
pellets_t_loom = pd.DataFrame(index = index, columns = columns)
x = 0

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    if file_names == '.DS_Store':
        next
    else:
        pellet = InArea(file_names)  
        animal = file_names
        pellets_t_loom.iloc[x,0] = pellet
        pellets_t_loom.iloc[x,1] = animal
        pellets_t_loom.iloc[x,2] = 'T_Loom'
        x +=1
print(pellets_t_loom)

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'

columns = ['pellet', 'animal', 'condition']
index = range(30,46)
pellets_t_shock = pd.DataFrame(index = index, columns = columns)
x = 0

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    if file_names == '.DS_Store':
        next
    else:
        pellet = InArea(file_names)  
        animal = file_names
        pellets_t_shock.iloc[x,0] = pellet
        pellets_t_shock.iloc[x,1] = animal
        pellets_t_shock.iloc[x,2] = 'T_Shock'
        x +=1
print(pellets_t_shock)

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'


columns = ['pellet', 'animal', 'condition']
index = range(46,62)
pellets_tone = pd.DataFrame(index = index, columns = columns)
x = 0

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    if file_names == '.DS_Store':
        next
    else:
        pellet = InArea(file_names)  
        animal = file_names
        pellets_tone.iloc[x,0] = pellet
        pellets_tone.iloc[x,1] = animal
        pellets_tone.iloc[x,2] = 'Tone'
        x +=1
print(pellets_tone)

#%%
df_pellet =  pd.concat([pellets_loom, pellets_t_loom, pellets_t_shock, pellets_tone], axis = 0)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') 

took_pellet = pd.read_csv('took_pellet.csv')
#%%
df_pellet['took_pellet'] = took_pellet['took_pellet']
#%%
condition = list(df_pellet['condition'])
total = list(df_pellet['pellet'])
ax = sns.swarmplot(x="condition", y="pellet", 
                 data=df_pellet, hue = "took_pellet",palette=['black','red'])
ax.set_title('Time after stimulus and before grabbing pellet (15 min maximum)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
ax.set_ylabel('Time to grab pellet in seconds')
#%%
T_SvsL = ss.mannwhitneyu(pellets_t_shock['pellet'],pellets_loom['pellet'])
T_SvsT = ss.mannwhitneyu(pellets_t_shock['pellet'],pellets_tone['pellet'])
T_SvsT_L = ss.mannwhitneyu(pellets_t_shock['pellet'],pellets_t_loom['pellet'])
TvsL = ss.mannwhitneyu(pellets_tone['pellet'],pellets_loom['pellet'])
TvsT_L = ss.mannwhitneyu(pellets_tone['pellet'],pellets_t_loom['pellet'])
LvsdT_L = ss.mannwhitneyu(pellets_loom['pellet'],pellets_t_loom['pellet'])

#%%
print('T_SvsT =',T_SvsT)
print('T_SvsL =', T_SvsL)
print('T_SvsT_L =',T_SvsT_L)
print('TvsL =', TvsL)
print('TvsT_L =', TvsT_L)
print('LvsdT_L =', LvsdT_L)


#%%
condition = list(df_pellet['condition'])
total = list(df_pellet['pellet'])
ax = sns.swarmplot(x="condition", y="pellet", 
                 data=df_pellet, hue = "took_pellet",palette=['black','red'])
ax.set_title('Zoom: Time after stimulus and before grabbing pellet (15 min maximum)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
ax.set_ylim(0, 300)
ax.set_ylabel('Time to grab pellet in seconds')













