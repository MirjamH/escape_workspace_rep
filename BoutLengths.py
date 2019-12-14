#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:22:19 2019

@author: mirjamheinemans
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
google:
    find start end index of bouts of consecutive equal values
"""
import scipy.stats as ss
import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
from itertools import groupby

os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files') # to change directory Read csv files with Pandas
#%%



def ShelterTime(file_names):

    if file_names == '.DS_Store':
        next
    else:
       
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [2,4,9])
        stimulus = dataset.loc[dataset.iloc[:,2] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +18000)),:] #18000 is 5 minutes
        
        dataset_stim = dataset_stim.reset_index(drop=True)
            
        dataset_stim[file_names+ 'shelter'] = 0
    
        for i, row in dataset_stim.iterrows():
            if dataset_stim.iloc[i,1] == 1:
                break
            
            elif dataset_stim.iloc[i,0] == 1: 
                dataset_stim.iloc[i,3] = 1   
                
            
        sheltertime = dataset_stim[file_names+'shelter']
        return(sheltertime)



#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['no_pel_in_shel']
index = range(18000)
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
loom = []
for i in shelter_loom.columns:
   
    animal =[ list(group) for key, group in groupby(shelter_loom[i].values.tolist())]
    loom.append(animal)

loom_ones = []
loom_zeros = []

for i in range(len(loom)):
    for j in loom[i]:
        if j[0] == 1:
            ones = len(j)
            loom_ones.append(ones)
           
        elif j[0] == 0:
            zeros = len(j)
            loom_zeros.append(zeros)
        else:
            next
   
#%%
tone_shock = []
for i in shelter_t_shock.columns:
   
    animal =[ list(group) for key, group in groupby(shelter_t_shock[i].values.tolist())]
    tone_shock.append(animal)

tone_shock_ones = []
tone_shock_zeros = []

for i in range(len(tone_shock)):
    for j in tone_shock[i]:
        if j[0] == 1:
            ones = len(j)
            tone_shock_ones.append(ones)
            
        elif j[0] == 0:
            zeros = len(j)
            tone_shock_zeros.append(zeros)
        else:
            next    
    
#%%
tone_loom= []
for i in shelter_t_loom.columns:
   
    animal =[ list(group) for key, group in groupby(shelter_t_loom[i].values.tolist())]
    tone_loom.append(animal)

tone_loom_ones = []
tone_loom_zeros = []

for i in range(len(tone_loom)):
    for j in tone_loom[i]:
        if j[0] == 1:
            ones = len(j)
            tone_loom_ones.append(ones)
            
        elif j[0] == 0:
            zeros = len(j)
            tone_loom_zeros.append(zeros)
        else:
            next
    
            #%%
tone= []
for i in shelter_tone.columns:
   
    animal =[ list(group) for key, group in groupby(shelter_tone[i].values.tolist())]
    tone_loom.append(animal)

tone_ones = []
tone_zeros = []

for i in range(len(tone_loom)):
    for j in tone_loom[i]:
        if j[0] == 1:
            ones = len(j)
            tone_ones.append(ones)
           
        elif j[0] == 0:
            zeros = len(j)
            tone_zeros.append(zeros)
        else:
            next

#%%

#plt.hist(tone_shock_ones, bins=50, color="blue")
#plt.hist(loom_ones, bins=50, color="green")
#plt.hist(tone_ones, bins=50, color="violet")
#plt.hist(tone_loom_ones, bins=50, color="orange")
#plt.title('Bouts in shelter before grabbing pellet')
#plt.ylabel('Number of bouts')
#plt.xlabel('number of frames - divided in 50 bouts')
#plt.xlim(right=10000)  # adjust the right leaving left unchanged
#plt.xlim(left=-10) 

#%%
plt.hist([tone_shock_ones,tone_ones,tone_loom_ones, loom_ones], bins=10,label=['T_Shock', 'Tone', 'T_Loom','Loom'])
plt.legend(loc='upper right')
#plt.xlim(right=4.5) 
plt.ylabel('Number of bouts')
plt.xlabel('number of frames - divided in 10 bouts')
plt.title('Lenghts of bouts in shelter before grabbing pellet')
#%%
T_SvsL = ss.mannwhitneyu(tone_shock_ones,loom_ones)
T_SvsT = ss.mannwhitneyu(tone_shock_ones,tone_ones)
T_SvsT_L = ss.mannwhitneyu(tone_shock_ones,tone_loom_ones)
TvsL = ss.mannwhitneyu(tone_ones,loom_ones)
TvsT_L = ss.mannwhitneyu(tone_ones,tone_loom_ones)
LvsdT_L = ss.mannwhitneyu(loom_ones,tone_loom_ones)
#%%
print('T_SvsT =',T_SvsT)
print('T_SvsL =', T_SvsL)
print('T_SvsT_L =',T_SvsT_L)
print('TvsL =', TvsL)
print('TvsT_L =', TvsT_L)
print('LvsdT_L =', LvsdT_L)

#%%

plt.hist(tone_ones, bins=16, color="violet", alpha =0.5)
plt.hist(tone_shock_ones, bins=16, color="blue", alpha =0.3)
plt.hist(loom_ones, bins=16, color="green", alpha =0.5)
plt.hist(tone_loom_ones, bins=16, color="orange", alpha =0.5)

plt.title('Total number of bouts in shelter')