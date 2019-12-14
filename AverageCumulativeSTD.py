#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:05:54 2019

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
import seaborn as sns; sns.set()
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
#shelter_loom['frames']=  range(len(shelter_loom))
#shelter_loom['sec'] =shelter_loom['frames']/60


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
#shelter_t_loom['frames']=  range(len(shelter_loom))
#shelter_t_loom['sec'] =shelter_t_loom['frames']/60

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
#shelter_t_shock['frames']=  range(len(shelter_t_shock))
#shelter_t_shock['sec'] =shelter_t_shock['frames']/60

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
#shelter_tone['frames']=  range(len(shelter_tone))
#shelter_tone['sec'] =shelter_tone['frames']/60


#%%
Loom = shelter_loom.T
Loom['condition'] = 'Loom'
Loom.loc['average'] = Loom.mean()
Loom.loc['median'] = Loom.median()
Loom.loc['SEM'] = Loom.std()
Loom.loc['frames']=  range(len(Loom.loc['average']))
Loom.loc['sec'] =Loom.loc['frames']/60
Loom_tr = Loom.T
Loom_tr_num = Loom_tr.apply(pd.to_numeric, errors='coerce')
Loom_tr_num['lower_bound'] = Loom_tr_num['average'] - Loom_tr_num['SEM'] 
Loom_tr_num['upper_bound'] = Loom_tr_num['average'] + Loom_tr_num['SEM'] 

#%%
T_Shock = shelter_t_shock.T
T_Shock['condition'] ='T_Shock'
T_Shock.loc['average'] = T_Shock.mean()
T_Shock.loc['median'] = T_Shock.median()
T_Shock.loc['SEM'] = T_Shock.std()
T_Shock.loc['frames']=  range(len(T_Shock.loc['average']))
T_Shock.loc['sec'] =T_Shock.loc['frames']/60
T_Shock_tr = T_Shock.T
T_Shock_tr_num = T_Shock_tr.apply(pd.to_numeric, errors='coerce')
T_Shock_tr_num['lower_bound'] = T_Shock_tr_num['average'] - T_Shock_tr_num['SEM'] 
T_Shock_tr_num['upper_bound'] = T_Shock_tr_num['average'] + T_Shock_tr_num['SEM'] 

#%%
T_Loom = shelter_t_loom.T
T_Loom['condition'] ='T_Loom'
T_Loom.loc['average'] = T_Loom.mean()
T_Loom.loc['median'] = T_Loom.median()
T_Loom.loc['SEM'] = T_Loom.std()
T_Loom.loc['frames']=  range(len(T_Loom.loc['average']))
T_Loom.loc['sec'] =T_Loom.loc['frames']/60
T_Loom_tr = T_Loom.T
T_Loomtr_num = T_Loom_tr.apply(pd.to_numeric, errors='coerce')
T_Loomtr_num['lower_bound'] = T_Loomtr_num['average'] - T_Loomtr_num['SEM'] 
T_Loomtr_num['upper_bound'] = T_Loomtr_num['average'] + T_Loomtr_num['SEM'] 

#%%
Tone = shelter_tone.T
Tone['condition'] ='Tone'
Tone.loc['average'] = Tone.mean()
Tone.loc['median'] = Tone.median()
Tone.loc['SEM'] = Tone.std()
Tone.loc['frames']=  range(len(Tone.loc['average']))
Tone.loc['sec'] =Tone.loc['frames']/60
Tone_tr = Tone.T
Tone_tr_num = Tone_tr.apply(pd.to_numeric, errors='coerce')
Tone_tr_num['lower_bound'] = Tone_tr_num['average'] - Tone_tr_num['SEM'] 
Tone_tr_num['upper_bound'] = Tone_tr_num['average'] + Tone_tr_num['SEM'] 
#%%
my_list = ['MH043cum','MH044cum', 'MH051cum', 'MH052cum', 'MH053cum', 'MH063cum', 'MH064cum', 'MH070cum', 'MH071cum', 'MH078cum','MH092cum','MH096cum', 'MH101cum'  ]
T_Loom_filtered = T_Loom.loc[my_list]
T_Loom_filtered.loc['average'] = T_Loom_filtered.mean()
T_Loom_filtered.loc['median'] = T_Loom_filtered.median()
T_Loom_filtered.loc['SEM'] = T_Loom_filtered.std()

T_Loom_filtered.loc['frames']=  range(len(T_Loom_filtered.loc['average']))
T_Loom_filtered.loc['sec'] =T_Loom_filtered.loc['frames']/60

T_Loom_fil_tr = T_Loom_filtered.T
T_Loom_fil_tr_num = T_Loom_fil_tr.apply(pd.to_numeric, errors='coerce')

T_Loom_fil_tr_num['lower_bound'] = T_Loom_fil_tr_num['average'] - T_Loom_fil_tr_num['SEM'] 
T_Loom_fil_tr_num['upper_bound'] = T_Loom_fil_tr_num['average'] + T_Loom_fil_tr_num['SEM'] 
#%%
T_Loom_trial = T_Loom.loc[my_list]

T_L_tr = T_Loom_trial.T
T_L_tr = T_L_tr.apply(pd.to_numeric, errors='coerce')
#%%

ax = sns.lineplot(x='sec', y='average', data =T_Loom_fil_tr_num, color = 'blue').set_title('Mean cumulative distance +/- St Dev')#T-Shock
ax = plt.fill_between(T_Loom_fil_tr_num['sec'],T_Loom_fil_tr_num['lower_bound'] , T_Loom_fil_tr_num['upper_bound'], color ='blue',alpha=.3)


ax = sns.lineplot(x='sec', y='average', data =T_Shock_tr_num, color = 'red')
ax = plt.fill_between(T_Shock_tr_num['sec'],T_Shock_tr_num['lower_bound'] , T_Shock_tr_num['upper_bound'], color = 'red', alpha=.3)

ax = sns.lineplot(x='sec', y='average', data =Loom_tr_num, color = 'green')
ax = plt.fill_between(Loom_tr_num['sec'],Loom_tr_num['lower_bound'] , Loom_tr_num['upper_bound'], color = 'green',alpha=.3)

ax = sns.lineplot(x='sec', y='average', data =Tone_tr_num, color = 'yellow')
ax = plt.fill_between(Tone_tr_num['sec'],Tone_tr_num['lower_bound'] , Tone_tr_num['upper_bound'], color='yellow',alpha=.3)
ax.legend(bbox_to_anchor=(1,1))
#%%

ax = sns.lineplot(x='frames', y='median', data =T_Loom_fil_tr_num, color = 'blue').set_title('Median cumulative distance')#T-Shock






#%%
ax = sns.lineplot(x='frames', y='median', data =T_Shock_tr_num, color = 'red')
ax = sns.lineplot(x='frames', y='median', data =Loom_tr_num, color = 'black')
ax = sns.lineplot(x='frames', y='median', data =Tone_tr_num, color = 'green')

#%%
ax = T_L_tr.mean(axis =1).plot()

ax = T_L_tr.std(axis =1).plot()


#%%

ax = sns.lineplot(data = T_L_tr, err_style="bars")









