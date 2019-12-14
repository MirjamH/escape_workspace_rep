#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:01:22 2019

@author: mirjamheinemans
make a graph with the time spent in the shelter before coming out to get pellet

first open the test file, extract three columns:
    ['MH33_in_shelter'], ['MH33_doorway'], ['MH33_with_pellet'], ['MH33_stim']
    
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

"""
For loom condition
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


def ShelterTime(file):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [3,9])
        stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +18000)),:] #18000 is 5 minutes
        
        dataset_stim = dataset_stim.reset_index(drop=True)
        data_shelter = dataset_stim.iloc[:,0:1]
        
        return(data_shelter)

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['no_pel_in_shel']
index = range(1800)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['no_pel_in_shel'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['no_pel_in_shel']
index = range(18000)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['no_pel_in_shel'])
 #%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['no_pel_in_shel']
index = range(18000)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)

shelter_t_shock = shelter_t_shock.drop(columns = ['no_pel_in_shel'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['no_pel_in_shel']
index = range(18000)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)

shelter_tone = shelter_tone.drop(columns = ['no_pel_in_shel'])


#%%
'''only run once: if you run again after adding the condition row, you get only 'nan' in sum row'''
shelter_loom.loc['sum', :] = shelter_loom.sum(axis = 0)
shelter_t_loom.loc['sum', :] = shelter_t_loom.sum(axis = 0)
shelter_t_shock.loc['sum', :] = shelter_t_shock.sum(axis = 0)
shelter_tone.loc['sum', :] = shelter_tone.sum(axis = 0)

#%%
shelter_loom.loc['condition',:]='L'
shelter_t_loom.loc['condition',:]='T_L'
shelter_t_shock.loc['condition',:]= 'T_S'
shelter_tone.loc['condition',:]='T'

shelter_figure =  pd.concat([shelter_loom, shelter_t_loom, shelter_t_shock, shelter_tone], axis = 1)
#%%

shelter = shelter_figure.T



#%%
total = list(shelter['sum'])
condition = list(shelter['condition'])
ax = sns.swarmplot(x="condition", y="sum", 
                 data=shelter, color ="black")
ax.set_title('Total time in doorway')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)

#%%
#total = list(shelter['sum'])
#condition = list(shelter['condition'])
#
#ax = sns.violinplot(x=condition, y=total, scale = 'count')
#ax.set_ylim([0,18000])     

#%%

shelter_loom = shelter_loom.T
shelter_t_shock = shelter_t_shock.T
shelter_t_loom = shelter_t_loom.T
shelter_tone = shelter_tone.T
#%%
T_SvsL = ss.mannwhitneyu(shelter_t_shock['sum'],shelter_loom['sum'])
T_SvsT = ss.mannwhitneyu(shelter_t_shock['sum'],shelter_tone['sum'])
T_SvsT_L = ss.mannwhitneyu(shelter_t_shock['sum'],shelter_t_loom['sum'])
TvsL = ss.mannwhitneyu(shelter_tone['sum'],shelter_loom['sum'])
TvsT_L = ss.mannwhitneyu(shelter_tone['sum'],shelter_t_loom['sum'])
LvsdT_L = ss.mannwhitneyu(shelter_loom['sum'],shelter_t_loom['sum'])
#%%
print('T_SvsT =',T_SvsT)
print('T_SvsL =', T_SvsL)
print('T_SvsT_L =',T_SvsT_L)
print('TvsL =', TvsL)
print('TvsT_L =', TvsT_L)
print('LvsdT_L =', LvsdT_L)







