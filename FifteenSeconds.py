#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:18:23 2019

@author: mirjamheinemans
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


def ShelterTime(file_names):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [1,9])
        stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +900)),:] #900 is 15 seconds
        dataset_stim = dataset_stim.reset_index(drop=True)
            
        dataset_stim.columns = [(file_names), 'stim']
    
        sheltertime = dataset_stim[file_names]
        #print(sheltertime)
        return(sheltertime)

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['xpos']
index = range(18000)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['xpos'])
shelter_loom['frames']=  range(len(shelter_loom))
shelter_loom['sec'] =shelter_loom['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['xpos']
index = range(18000)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['xpos'])
shelter_t_loom['frames']=  range(len(shelter_loom))
shelter_t_loom['sec'] =shelter_t_loom['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['xpos']
index = range(18000)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)
shelter_t_shock = shelter_t_shock.drop(columns = ['xpos'])
shelter_t_shock['frames']=  range(len(shelter_t_shock))
shelter_t_shock['sec'] =shelter_t_shock['frames']/60
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['xpos']
index = range(18000)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)
shelter_tone = shelter_tone.drop(columns = ['xpos'])
shelter_tone['frames']=  range(len(shelter_tone))
shelter_tone['sec'] =shelter_tone['frames']/60
#%%
'''black is batch 2'''
sns.set_style('darkgrid')
ax = sns.lineplot(x='sec', y='MH033', data =shelter_loom, color = 'gray').set_title('Loom')#Loom
ax = sns.lineplot(x='sec', y='MH034', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH046', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH059', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH060', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH065', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH066', data =shelter_loom, color = 'yellowgreen')#Loom, pellet
ax = sns.lineplot(x='sec', y='MH085', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='MH086', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='MH087', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='MH088', data =shelter_loom, color = 'black')#Loom

#ax.set_ylim(0,800)
ax.plot([1 ,1], [0, 1200],color ='orange')
#ax.plot([3 ,3], [0, 1200],color ='orange')
#ax.plot([5 ,5], [0, 1200],color ='orange')
#ax.plot([7 ,7], [0, 1200],color ='orange')
#ax.plot([9 ,9], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u)')
ax.plot([0, 15], [150, 150], color = 'pink')
#%%
'''purple is batch 2'''
sns.set_style('darkgrid')
#ax = sns.lineplot(x='sec', y='MH035', data =shelter_t_loom, dashes=[(2, 2), (2, 2)]).set_title('Tone-Loom')#T-Loom

#%%
sns.set_style('darkgrid')
ax = sns.lineplot(x='sec', y='MH035', data =shelter_t_loom, color = 'blue').set_title('Tone-Loom')#T-Loom
ax = sns.lineplot(x='sec', y='MH036', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH043', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='MH044', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH051', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH052', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='MH053', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='MH054', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH063', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH064', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH069', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='MH070', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH071', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH072', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH077', data =shelter_t_loom, color = 'purple')#T-Loom
ax = sns.lineplot(x='sec', y='MH078', data =shelter_t_loom, color = 'purple')#T-Loom
ax = sns.lineplot(x='sec', y='MH092', data =shelter_t_loom, color = 'purple')#T-Loom
ax = sns.lineplot(x='sec', y='MH096', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH101', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet

#ax.set_ylim(0,800)
ax.plot([1 ,1], [0, 1200],color ='orange')
#ax.plot([3 ,3], [0, 1200],color ='orange')
#ax.plot([5 ,5], [0, 1200],color ='orange')
#ax.plot([7 ,7], [0, 1200],color ='orange')
#ax.plot([9 ,9], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u)')
ax.plot([0, 15], [150, 150], color = 'pink')

#%%
sns.set_style('darkgrid')
ax = sns.lineplot(x='sec', y='MH039', data =shelter_t_shock, color = 'red').set_title('Tone-Shock')#T-Shock
ax = sns.lineplot(x='sec', y='MH040', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH049', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH050', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH055', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH056', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH067', data =shelter_t_shock, color = 'yellowgreen')#T-Shock, pellet
ax = sns.lineplot(x='sec', y='MH068', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH073', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH074', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH079', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH080', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH084', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH089', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH090', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH100', data =shelter_t_shock, color = 'orange')#T-Shock

#ax.set_ylim(0,800)
ax.plot([1 ,1], [0, 1200],color ='orange')
#ax.plot([3 ,3], [0, 1200],color ='orange')
#ax.plot([5 ,5], [0, 1200],color ='orange')
#ax.plot([7 ,7], [0, 1200],color ='orange')
#ax.plot([9 ,9], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u)')
ax.plot([0, 15], [150, 150], color = 'pink')

#%%
sns.set_style('darkgrid')
ax = sns.lineplot(x='sec', y='MH037', data =shelter_tone, color = 'yellowgreen').set_title('Tone')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH038', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH042', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH047', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH048', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH057', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH058', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH061', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH062', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH075', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH076', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH081', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH082', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH093', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH097', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH098', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
#ax.set_ylim(0,800)
ax.plot([1 ,1], [0, 1200],color ='orange')
#ax.plot([3 ,3], [0, 1200],color ='orange')
#ax.plot([5 ,5], [0, 1200],color ='orange')
#ax.plot([7 ,7], [0, 1200],color ='orange')
#ax.plot([9 ,9], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u)')
ax.plot([0, 15], [150, 150], color = 'pink')

#%%
'''not ideal yet because i don't know how to change plot axes after for loop'''
sns.set_style('whitegrid')
for column in shelter_loom:
    if column.startswith('MH'):
        sns.lineplot(x='frames', y=column, data =shelter_loom, color = 'black').set_title('Loom')#Loom

sns.set_style('whitegrid')
for column in shelter_t_loom:
    if column.startswith('MH'):
       sns.lineplot(x='frames', y=column, data =shelter_t_loom, color = 'blue').set_title('T-Loom')#Loom



