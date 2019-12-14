#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:02:16 2019

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
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [2,3,4,9])
        stimulus = dataset.loc[dataset.iloc[:,3] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +18001)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
            
        dataset_stim[file_names+ 'no_pel_in_shel'] = 0
        
        pellet = 0
        for i, row in dataset_stim.iterrows():
            if dataset_stim.iloc[i,0] == 1:
                break
            elif dataset_stim.iloc[i,2] == 1:
                pellet = 1
        

        return(pellet)


#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'

pellet_frame_loom =[]
files = []

for file_names in sorted(os.listdir(path_name)): 
    if file_names == '.DS_Store':
        next
    else:
        print(file_names)
        animal = ShelterTime(file_names)  
        files.append(file_names)
        pellet_frame_loom.append(animal)
 
    #%%
pellet_loom = pd.DataFrame(pellet_frame_loom, index =files, columns =['took_pellet'])           
pellet_loom ['condition'] = 'L'
loom_fract = (pellet_loom.groupby('took_pellet').count())/len(pellet_loom)
loom = loom_fract.iloc[1,0]

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'

pellet_frame_t_loom =[]
files = []

for file_names in sorted(os.listdir(path_name)): 
        if file_names == '.DS_Store':
            next
        else:
            print(file_names)
            animal = ShelterTime(file_names)  
            files.append(file_names)
            pellet_frame_t_loom.append(animal)

#%%
pellet_t_loom = pd.DataFrame(pellet_frame_t_loom, index =files, columns =['took_pellet'])           
pellet_t_loom ['condition'] = 'TL'
t_loom_fract = (pellet_t_loom.groupby('took_pellet').count())/len(pellet_t_loom)
t_loom = t_loom_fract.iloc[1,0]
 #%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
pellet_frame_t_shock =[]
files = []

for file_names in sorted(os.listdir(path_name)): 
        if file_names == '.DS_Store':
            next
        else:
            print(file_names)
            animal = ShelterTime(file_names)  
            files.append(file_names)
            pellet_frame_t_shock.append(animal)
#%%
pellet_t_shock = pd.DataFrame(pellet_frame_t_shock, index =files, columns =['took_pellet'])           
pellet_t_shock ['condition'] = 'TS'
t_shock_fract = (pellet_t_shock.groupby('took_pellet').count())/len(pellet_t_shock)
t_shock = t_shock_fract.iloc[1,0]
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'

pellet_frame_tone =[]
files = []

for file_names in sorted(os.listdir(path_name)): 
        if file_names == '.DS_Store':
            next
        else:
            print(file_names)
            animal = ShelterTime(file_names)  
            files.append(file_names)
            pellet_frame_tone.append(animal)
#%%
pellet_tone = pd.DataFrame(pellet_frame_tone, index =files, columns =['took_pellet'])           
pellet_tone ['condition'] = 'T'
tone_fract = (pellet_tone.groupby('took_pellet').count())/len(pellet_tone)
tone = tone_fract.iloc[1,0]
#%%
shelter_figure =  pd.concat([pellet_loom, pellet_t_loom, pellet_t_shock, pellet_tone])
#%%
pel = pd.DataFrame([loom, t_loom, t_shock, tone], columns = ['fraction'])
pel['condition'] = ['loom', 't_loom', 't_shock', 'tone']
#%%
#total = list(shelter_figure['took_pellet'])
#condition = list(shelter_figure['condition'])
ax = sns.swarmplot(x="condition", y="took_pellet", 
                 data=shelter_figure)
ax = sns.swarmplot(x="condition", y="fraction", 
                 data=pel, s=10, color = 'black')
ax.set_title('Fraction of animals taking the pellet before going into shelter')
#ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)


#%%
''' calculating the p-value for differences in pellet grabbing between conditions
Tone = 7 yes, 9 no
T-Loom = 11 yes, 8 no
T-Shock = 1 yes, 15 no
Loom = 1 yes, 10 no'''
oddsratio, pvalue = ss.fisher_exact([[11, 8], [7, 9]])


#%%
plt.hist([pellet_t_shock['took_pellet'],pellet_tone['took_pellet'],pellet_t_loom['took_pellet'], pellet_loom['took_pellet']], bins=9,label=['T_Shock', 'Tone', 'T_Loom','Loom'])
plt.legend(loc='upper center')
plt.xlim(right=1) 
plt.title('number of animals taking (1) or not taking (0) pellet')

#%%
pel = pd.DataFrame([loom, t_loom, t_shock, tone], columns = ['fraction'])
pel['condition'] = ['loom', 't_loom', 't_shock', 'tone']
#%%
tones = [9,7]
labels = ['no pellet (n = 9)', 'took pellet (n = 7)']
colors = ['skyblue', 'lightcoral']
plt.pie(tones,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title ('tone')

#%%
tone_looms = [6,8]# for all animals included: no pellet = 8 , took pellet = 11
labels = ['no pellet (n = 6)', 'took pellet (n = 8)']
colors = ['skyblue', 'lightcoral']
plt.title ('tone_loom')
plt.pie(tone_looms,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)


#%%
tone_shock = [15,1]
labels = ['no pellet (n = 15)', 'took pellet (n = 1)']
colors = ['skyblue', 'lightcoral']
plt.pie(tone_shock,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title ('tone_shock')


#%%

loom = [10,1]
labels = ['no pellet (n = 10)', 'took pellet (n = 1)']
colors = ['skyblue', 'lightcoral']
plt.pie(loom,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title ('loom')




#%%
#plt.rcParams['axes.facecolor'] = 'black'
total = [42, 20]
labels = ['no pellet (n = 42)', 'took pellet (n = 20)']
colors = ['skyblue', 'lightcoral']
plt.pie(total,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title ('total')

#%%
total = [26,12]
labels = ['no pellet (n = 26)', 'took pellet (n = 12)']
colors = ['skyblue', 'lightcoral']
plt.pie(total,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title ('batch 1')

#%%
total = [24,8]
labels = ['no pellet (n = 24)', 'took pellet (n = 8)']
colors = ['skyblue', 'lightcoral']
plt.pie(total,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title ('batch 2')