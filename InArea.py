#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:37:21 2019

@author: mirjamheinemans

The amount of time that the animals spend in an area ([-200 200]) around the stimulus.

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
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [1,4,9])
        stimulus = dataset.loc[dataset.iloc[:,2] == 1].index.values.astype(int)[0]  
        
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +3600)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
        
        if file_names[2] == '1':
            number = file_names[2:]
        else:
            number = file_names[3:]
            
        x_value = dataset_stim.iloc[0,0]
        dataset_stim[file_names+ 'crossing_stimulus'] = dataset_stim['x-value'+number]- x_value
        
        dataset_stim[file_names+ 'in_area'] = 0
        for i, row in dataset_stim.iterrows():
        #    if dataset_stim.iloc[i,1] ==  1:
        #        break
            if  -100 < dataset_stim.iloc[i,3] < 200:
                dataset_stim.iloc[i,4] = 1
        in_area = dataset_stim[file_names+'in_area']
        #print(sheltertime)
        return(in_area)
        
#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['shelter_exit']
index = range(1800)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = InArea(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['shelter_exit'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['shelter_exit']
index = range(18000)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = InArea(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['shelter_exit'])
 #%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['shelter_exit']
index = range(18000)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = InArea(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)

shelter_t_shock = shelter_t_shock.drop(columns = ['shelter_exit'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['shelter_exit']
index = range(18000)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = InArea(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)

shelter_tone = shelter_tone.drop(columns = ['shelter_exit'])

#%%
'''only run once: if you run again after adding the condition row, you get only 'nan' in sum row'''
shelter_loom.loc['sum', :] = shelter_loom.sum(axis = 0)
shelter_t_loom.loc['sum', :] = shelter_t_loom.sum(axis = 0)
shelter_t_shock.loc['sum', :] = shelter_t_shock.sum(axis = 0)
shelter_tone.loc['sum', :] = shelter_tone.sum(axis = 0)

#%%
shelter_loom.loc['sec', :] = shelter_loom.loc['sum',:]/60
shelter_t_loom.loc['sec', :] = shelter_t_loom.loc['sum',:]/60
shelter_t_shock.loc['sec', :] = shelter_t_shock.loc['sum',:]/60
shelter_tone.loc['sec', :] = shelter_tone.loc['sum',:]/60

#%%
shelter_loom.loc['condition',:]='L'
shelter_t_loom.loc['condition',:]='T_L'
shelter_t_shock.loc['condition',:]= 'T_S'
shelter_tone.loc['condition',:]='T'

shelter_figure =  pd.concat([shelter_loom, shelter_t_loom, shelter_t_shock, shelter_tone], axis = 1)
shelter = shelter_figure.T
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') 

took_pellet = pd.read_csv('took_pellet.csv')
took_pellet.index = shelter.index
#%%
shelter['took_pellet'] = took_pellet['took_pellet']

#%%
total = list(shelter['sec'])
condition = list(shelter['condition'])
ax = sns.swarmplot(x="condition", y="sec", 
                 data=shelter, hue ="took_pellet", palette =['black','red'])
ax.set_title('All animals: Time in area of stimulus (yes = took pellet; 1 min, -100:200)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
ax.legend(bbox_to_anchor=(1,1))
#%%
#total = list(shelter['sum'])
#condition = list(shelter['condition'])
#
#ax = sns.violinplot(x=condition, y=total, scale = 'count')
#ax.set_ylim([0,18000])     
#
#
#
#%%
shelter_loom_t = shelter_loom.T
shelter_t_loom_t = shelter_t_loom.T
shelter_t_shock_t =shelter_t_shock.T
shelter_tone_t =shelter_tone.T

#%%df = df[df.line_race != 0]
shelter_filtered =shelter[shelter.took_pellet == 'no']


#%%
total = list(shelter_filtered['sec'])
condition = list(shelter_filtered['condition'])
ax = sns.swarmplot(x="condition", y="sec", 
                 data=shelter_filtered,color='black')
ax.set_title('Animals that did not take pellet:Time in area of stimulus (1 min, -100:200)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
ax.legend(bbox_to_anchor=(1,1))
#%%|
T_SvsL = ss.mannwhitneyu(shelter_t_shock_t['sum'],shelter_loom_t['sum'])
T_SvsT = ss.mannwhitneyu(shelter_t_shock_t['sum'],shelter_tone_t['sum'])
T_SvsT_L = ss.mannwhitneyu(shelter_t_shock_t['sum'],shelter_t_loom_t['sum'])
TvsL = ss.mannwhitneyu(shelter_tone_t['sum'],shelter_loom_t['sum'])
TvsT_L = ss.mannwhitneyu(shelter_tone_t['sum'],shelter_t_loom_t['sum'])
LvsdT_L = ss.mannwhitneyu(shelter_loom_t['sum'],shelter_t_loom_t['sum'])
#%%
print('T_SvsT =',T_SvsT)
print('T_SvsL =', T_SvsL)
print('T_SvsT_L =',T_SvsT_L)
print('TvsL =', TvsL)
print('TvsT_L =', TvsT_L)
print('LvsdT_L =', LvsdT_L)



#%%
ss.stats.kruskal(*[group["sum"].values for name, group in shelter.groupby("condition")])


#%%
ss.stats.kruskal(*[group["sum"].values for name, group in shelter_filtered.groupby("condition")])

#%%
t_s_filtered =shelter_filtered[shelter_filtered.condition == 'T_S']
t_filtered =shelter_filtered[shelter_filtered.condition == 'T']
t_l_filtered =shelter_filtered[shelter_filtered.condition == 'T_L']
l_filtered =shelter_filtered[shelter_filtered.condition == 'L']
#%%
T_SvsL = ss.mannwhitneyu(t_s_filtered['sum'],l_filtered['sum'])
T_SvsT = ss.mannwhitneyu(t_s_filtered['sum'],t_filtered['sum'])
T_SvsT_L = ss.mannwhitneyu(t_s_filtered['sum'],t_l_filtered['sum'])
TvsL = ss.mannwhitneyu(t_filtered['sum'],l_filtered['sum'])
TvsT_L = ss.mannwhitneyu(t_filtered['sum'],t_l_filtered['sum'])
LvsdT_L = ss.mannwhitneyu(l_filtered['sum'],t_l_filtered['sum'])

#%%
print('T_SvsT =',T_SvsT)
print('T_SvsL =', T_SvsL)
print('T_SvsT_L =',T_SvsT_L)
print('TvsL =', TvsL)
print('TvsT_L =', TvsT_L)
print('LvsdT_L =', LvsdT_L)












