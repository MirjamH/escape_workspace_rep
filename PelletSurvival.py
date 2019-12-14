#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:45:57 2019

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
    0. ''
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
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
def Pellet(file_names):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [4,9])
        stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +40000)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
            
        dataset_stim[file_names+'taken'] = 1
        
        
        if sum(dataset_stim.iloc[:,0]) > 0:
            pellet = dataset_stim.loc[dataset_stim.iloc[:,0] == 1].index.values.astype(int)[0]
                
        else:
            pellet = 40000
        
        dataset_stim.iloc[int(pellet):,2] = 0
        
        survival = dataset_stim.iloc[:,2]
        return(survival)

##%%
#path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
#dataset = pd.read_csv(path_name +'/MH053/test.csv', usecols = [4,9])
#stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
#print(stimulus)
#dataset_stim = dataset.iloc[int(stimulus):int((stimulus +18000)),:] #18000 is 5 minutes
#dataset_stim = dataset_stim.reset_index(drop=True)
        
 #%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['xpos']
index = range(3601)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Pellet(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['xpos'])
shelter_loom = shelter_loom.drop(index = 0)
shelter_loom = shelter_loom.apply(pd.to_numeric, errors='coerce')
#shelter_loom['frames']=  range(len(shelter_loom))
#shelter_loom['sec'] =shelter_loom['frames']/60


#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['xpos']
index = range(3601)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Pellet(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['xpos'])
shelter_t_loom = shelter_t_loom.drop(index = 0)
#shelter_t_loom['frames']=  range(len(shelter_loom))
#shelter_t_loom['sec'] =shelter_t_loom['frames']/60
my_list = ['MH043taken','MH044taken', 'MH051taken', 'MH052taken', 'MH053taken', 'MH063taken', 'MH064taken', 'MH070taken', 'MH071taken', 'MH078taken','MH092taken','MH096taken', 'MH101taken'  ]
shelter_t_loom_fil = shelter_t_loom[my_list]
shelter_t_loom_fil = shelter_t_loom_fil.apply(pd.to_numeric, errors='coerce')

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['xpos']
index = range(3601)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Pellet(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)
shelter_t_shock = shelter_t_shock.drop(columns = ['xpos'])
shelter_t_shock = shelter_t_shock.drop(index = 0)
#shelter_t_shock['frames']=  range(len(shelter_t_shock))
#shelter_t_shock['sec'] =shelter_t_shock['frames']/60
shelter_t_shock = shelter_t_shock.apply(pd.to_numeric, errors='coerce')

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['xpos']
index = range(3601)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Pellet(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)
shelter_tone = shelter_tone.drop(columns = ['xpos'])
shelter_tone = shelter_tone.drop(index = 0)
#shelter_tone['frames']=  range(len(shelter_tone))
#shelter_tone['sec'] =shelter_tone['frames']/60
shelter_tone = shelter_tone.apply(pd.to_numeric, errors='coerce')
   
#%%
loom_survival = []
for i in shelter_loom.iterrows():
    survived = sum(i[1]) / len(i[1])
    loom_survival.append(survived)
survival_loom = pd.DataFrame(loom_survival, columns = ['Loom'])   

#%%
t_l_survival = []
for i in shelter_t_loom_fil.iterrows():
    survived = sum(i[1]) / len(i[1])
    t_l_survival.append(survived)
survival_t_l = pd.DataFrame(t_l_survival, columns = ['T_Loom'])  
    
#%%
t_s_survival = []
for i in shelter_t_shock.iterrows():
    survived = sum(i[1]) / len(i[1])
    t_s_survival.append(survived)
survival_t_s = pd.DataFrame(t_s_survival, columns = ['T_Shock'])    
    
#%%
tone_survival = []
for i in shelter_tone.iterrows():
    survived = sum(i[1]) / len(i[1])
    tone_survival.append(survived)
survival_tone = pd.DataFrame(tone_survival, columns = ['Tone'])    
        
#%%
survival = pd.concat([survival_loom,survival_t_l,survival_t_s, survival_tone], axis =1)
survival['frames'] = survival.index
survival['second'] = survival['frames']/60
#%%
ax = sns.lineplot(x ='second', y='Loom', data =survival, color = 'green')
ax = sns.lineplot(x ='second', y='T_Loom', data =survival, color = 'blue')
ax = sns.lineplot(x ='second', y='T_Shock', data =survival, color = 'red').set_title('Survival of pellet')#T-Shock
ax = sns.lineplot(x ='second', y='Tone', data =survival, color = 'yellow').set_ylabel('fraction of animals without pellet')#T-Shock

#%%
    
    
    
    
    
    