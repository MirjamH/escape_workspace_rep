#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:05:08 2019

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
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +18000)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
            
        dataset_stim.columns = [(file_names), 'stim']
        dataset_stim[file_names+'diff'] = dataset_stim[file_names].diff()
        dataset_stim[file_names+'cum'] = dataset_stim[file_names+'diff'].abs()
        dataset_stim[file_names+'cum']  = dataset_stim[file_names+'cum'].cumsum()
        sheltertime = dataset_stim[file_names+'cum']
        
        #print(sheltertime)
        return(sheltertime)

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['xpos']
index = range(3601)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['xpos'])
shelter_loom = shelter_loom.drop(index = 0)
shelter_loom['frames']=  range(len(shelter_loom))
shelter_loom['sec'] =shelter_loom['frames']/60


#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['xpos']
index = range(3601)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['xpos'])
shelter_t_loom = shelter_t_loom.drop(index = 0)
shelter_t_loom['frames']=  range(len(shelter_loom))
shelter_t_loom['sec'] =shelter_t_loom['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['xpos']
index = range(3601)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)
shelter_t_shock = shelter_t_shock.drop(columns = ['xpos'])
shelter_t_shock = shelter_t_shock.drop(index = 0)
shelter_t_shock['frames']=  range(len(shelter_t_shock))
shelter_t_shock['sec'] =shelter_t_shock['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['xpos']
index = range(3601)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)
shelter_tone = shelter_tone.drop(columns = ['xpos'])
shelter_tone = shelter_tone.drop(index = 0)
shelter_tone['frames']=  range(len(shelter_tone))
shelter_tone['sec'] =shelter_tone['frames']/60

#%%
sns.set_style('darkgrid')
ax = sns.lineplot(x='sec', y='MH033cum', data =shelter_loom, color = 'gray').set_title('Loom')#Loom
ax = sns.lineplot(x='sec', y='MH034cum', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH046cum', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH059cum', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH060cum', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH065cum', data =shelter_loom, color = 'gray')#Loom
ax = sns.lineplot(x='sec', y='MH066cum', data =shelter_loom, color = 'yellowgreen')#Loom, pellet
ax = sns.lineplot(x='sec', y='MH085cum', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='MH086cum', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='MH087cum', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='MH088cum', data =shelter_loom, color = 'black')#Loom



ax.set_ylabel('x-position (a.u)')

#%%
sns.set_style('darkgrid')
#ax = sns.lineplot(x='sec', y='MH035cum', data =shelter_t_loom, color = 'blue').set_title('Tone-Loom')#T-Loom
#ax = sns.lineplot(x='sec', y='MH036cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH043cum', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='MH044cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH051cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH052cum', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='MH053cum', data =shelter_t_loom, color = 'blue')#T-Loom
#ax = sns.lineplot(x='sec', y='MH054cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH063cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH064cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
#ax = sns.lineplot(x='sec', y='MH069cum', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='MH070cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH071cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
#ax = sns.lineplot(x='sec', y='MH072cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
#ax = sns.lineplot(x='sec', y='MH077cum', data =shelter_t_loom, color = 'purple')#T-Loom
ax = sns.lineplot(x='sec', y='MH078cum', data =shelter_t_loom, color = 'purple')#T-Loom
ax = sns.lineplot(x='sec', y='MH092cum', data =shelter_t_loom, color = 'purple')#T-Loom
ax = sns.lineplot(x='sec', y='MH096cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet
ax = sns.lineplot(x='sec', y='MH101cum', data =shelter_t_loom, color = 'yellowgreen')#T-Loom, pellet



ax.set_ylabel('x-position (a.u)')


#%%
sns.set_style('darkgrid')
ax = sns.lineplot(x='sec', y='MH039cum', data =shelter_t_shock, color = 'red').set_title('Tone-Shock')#T-Shock
ax = sns.lineplot(x='sec', y='MH040cum', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH049cum', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH050cum', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH055cum', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH056cum', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH067cum', data =shelter_t_shock, color = 'yellowgreen')#T-Shock, pellet
ax = sns.lineplot(x='sec', y='MH068cum', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='MH073cum', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH074cum', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH079cum', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH080cum', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH084cum', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH089cum', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH090cum', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='MH100cum', data =shelter_t_shock, color = 'orange')#T-Shock

ax.set_ylabel('x-position (a.u)')

#%%
sns.set_style('darkgrid')
ax = sns.lineplot(x='sec', y='MH037cum', data =shelter_tone, color = 'yellowgreen').set_title('Tone')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH038cum', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH042cum', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH047cum', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH048cum', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH057cum', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH058cum', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH061cum', data =shelter_tone, color = 'yellow')#Tone
ax = sns.lineplot(x='sec', y='MH062cum', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH075cum', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH076cum', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH081cum', data =shelter_tone, color = 'yellowgreen')#Tone, pellet
ax = sns.lineplot(x='sec', y='MH082cum', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH093cum', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH097cum', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='MH098cum', data =shelter_tone, color = 'yellowgreen')#Tone, pellet

ax.set_ylabel('x-position (a.u)')

#%%
Loom = shelter_loom.T
Loom['condition'] = 'Loom'
Loom_ = Loom.iloc[:-2, -2:]
Loom_.columns = ['total','condition']

T_Shock = shelter_t_shock.T
T_Shock['condition'] ='T_Shock'
T_Shock_ = T_Shock.iloc[:-2, -2:]
T_Shock_.columns = ['total','condition']

T_Loom = shelter_t_loom.T
T_Loom['condition'] ='T_Loom'
T_Loom_ = T_Loom.iloc[:-2, -2:]
T_Loom_.columns = ['total','condition']

Tone = shelter_tone.T
Tone['condition'] ='Tone'
Tone_ = Tone.iloc[:-2, -2:]
Tone_.columns = ['total','condition']

#%%
my_list = ['MH043cum','MH044cum', 'MH051cum', 'MH052cum', 'MH053cum', 'MH063cum', 'MH064cum', 'MH070cum', 'MH071cum', 'MH078cum','MH092cum','MH096cum', 'MH101cum'  ]
T_Loom_filtered = T_Loom_.loc[my_list]
#%%
df_cumulative = pd.concat([Loom_, T_Loom_, T_Shock_, Tone_])


#%%
condition = list(df_cumulative['condition'])
total = list(df_cumulative['total'])
ax = sns.swarmplot(x="condition", y="total", 
                 data=df_cumulative, color="black")
ax.set_title('Cumulative distance after 10 min')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
ax.set_ylabel('Cumulative distance (a.u.)')








