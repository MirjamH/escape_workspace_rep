#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:33:58 2019

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
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [7,9])
        stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +18000)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
            

        sheltertime = dataset_stim.iloc[:,0]
        #print(sheltertime)
        return(sheltertime)

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['no_pel_in_door']
index = range(18000)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['no_pel_in_door'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['no_pel_in_door']
index = range(18000)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['no_pel_in_door'])
 #%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['no_pel_in_door']
index = range(18000)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)

shelter_t_shock = shelter_t_shock.drop(columns = ['no_pel_in_door'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['no_pel_in_door']
index = range(18000)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)

shelter_tone = shelter_tone.drop(columns = ['no_pel_in_door'])

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

#%%
shelter_loom.loc['sec', :] = shelter_loom.loc['sum',:]/60
shelter_t_loom.loc['sec', :] = shelter_t_loom.loc['sum',:]/60
shelter_t_shock.loc['sec', :] = shelter_t_shock.loc['sum',:]/60
shelter_tone.loc['sec', :] = shelter_tone.loc['sum',:]/60

shelter_figure =  pd.concat([shelter_loom, shelter_t_loom, shelter_t_shock, shelter_tone], axis = 1)
shelter = shelter_figure.T

#%%
shelter.loc[:,'took_pellet'] = '6 > minutes'

'''manually addig the number of minutes the animals took to get pellet'''

shelter.loc['MH35_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH36_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH37_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH38_reaching','took_pellet'] = '0 < 1 minute'

shelter.loc['MH40_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH42_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH44_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH50_reaching','took_pellet'] ='0 < 1 minute'
shelter.loc['MH51_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH54_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH57_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH58_reaching','took_pellet'] = '0 < 1 minute'

shelter.loc['MH62_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH63_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH64_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH66_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH67_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH70_reaching','took_pellet'] ='0 < 1 minute'
shelter.loc['MH71_reaching','took_pellet'] ='0 < 1 minute'
shelter.loc['MH72_reaching','took_pellet'] ='0 < 1 minute'
shelter.loc['MH75_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH76_reaching','took_pellet'] = '0 < 1 minute'

shelter.loc['MH81_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH82_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH84_reaching','took_pellet'] = '0 < 1 minute'

shelter.loc['MH92_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH93_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH96_reaching','took_pellet'] = '0 < 1 minute'
shelter.loc['MH98_reaching','took_pellet'] = '0 < 1 minute'

shelter.loc['MH101_reaching','took_pellet'] = '0 < 1 minute'


#%%
shelter.loc['MH48_reaching','took_pellet'] = '1 < 2 minute'
shelter.loc['MH56_reaching','took_pellet'] = '1 < 2 minute'
shelter.loc['MH77_reaching','took_pellet'] = '1 < 2 minute'
shelter.loc['MH85_reaching','took_pellet'] = '1 < 2 minute'
shelter.loc['MH86_reaching','took_pellet'] = '1 < 2 minute'
shelter.loc['MH88_reaching','took_pellet'] = '1 < 2 minute'
shelter.loc['MH90_reaching','took_pellet'] = '1 < 2 minute'

#%%
shelter.loc['MH43_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH47_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH52_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH55_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH60_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH68_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH69_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH73_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH79_reaching','took_pellet'] = '2 < 3 minute'
shelter.loc['MH80_reaching','took_pellet'] = '2 < 3 minute'
#%%
shelter.loc['MH39_reaching','took_pellet'] = '3 < 6 minute'
shelter.loc['MH49_reaching','took_pellet'] = '3 < 6 minute'
shelter.loc['MH60_reaching','took_pellet'] = '3 < 6 minute'

shelter.loc['MH53_reaching','took_pellet'] = '3 < 6 minute'
shelter.loc['MH78_reaching','took_pellet'] = '3 < 6 minute'

shelter.loc['MH74_reaching','took_pellet'] = '3 < 6 minute'
shelter.loc['MH97_reaching','took_pellet'] = '3 < 6 minute'

#shelter.loc[shelter.sec == 0, 'took_pellet'] = '0 - immediately'

#%%
shelter = shelter.sort_values('took_pellet', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

#%%
condition = list(shelter['condition'])
total = list(shelter['sec'])
ax = sns.swarmplot(x="condition", y="sec", 
                 data=shelter, hue = "took_pellet", palette=["red", "purple", "yellow", "orange", "green", "black"])
ax.set_title('Time spent reaching (5 min)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
ax.legend(bbox_to_anchor=(1,1))
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



#%%
