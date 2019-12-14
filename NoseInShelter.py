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
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [2,3,4,9])
        stimulus = dataset.loc[dataset.iloc[:,3] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +18000)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
            
        dataset_stim[file_names+ 'no_pel_in_door'] = 0
    
        for i, row in dataset_stim.iterrows():
            if dataset_stim.iloc[i,2] == 1:
                break
            elif dataset_stim.iloc[i,1] == 1 and dataset_stim.iloc[i,2] == 0:
                if dataset_stim.iloc[i,0] == 1:
                    next
                else:
                    dataset_stim.iloc[i,4] = 1
        sheltertime = dataset_stim[file_names+'no_pel_in_door']
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
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout')

took_pellet = pd.read_csv('took_pellet.csv')
took_pellet.index = shelter.index
#%%
shelter['took_pellet'] = took_pellet['took_pellet']

#%%
shelter.loc[:,'took_pellet'] = '6 > minutes'

'''manually addig the number of minutes the animals took to get pellet'''

shelter.loc['MH035no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH036no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH037no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH038no_pel_in_door','took_pellet'] = '0 < 1 minute'

shelter.loc['MH040no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH042no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH044no_pel_in_door','took_pellet'] = '0 < 1 minute'

shelter.loc['MH050no_pel_in_door','took_pellet'] ='0 < 1 minute'
shelter.loc['MH051no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH054no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH057no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH058no_pel_in_door','took_pellet'] = '0 < 1 minute'

shelter.loc['MH062no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH063no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH064no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH066no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH067no_pel_in_door','took_pellet'] = '0 < 1 minute'

shelter.loc['MH070no_pel_in_door','took_pellet'] ='0 < 1 minute'
shelter.loc['MH071no_pel_in_door','took_pellet'] ='0 < 1 minute'
shelter.loc['MH072no_pel_in_door','took_pellet'] ='0 < 1 minute'
shelter.loc['MH075no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH076no_pel_in_door','took_pellet'] = '0 < 1 minute'

shelter.loc['MH081no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH082no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH084no_pel_in_door','took_pellet'] = '0 < 1 minute'

shelter.loc['MH092no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH093no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH096no_pel_in_door','took_pellet'] = '0 < 1 minute'
shelter.loc['MH098no_pel_in_door','took_pellet'] = '0 < 1 minute'

shelter.loc['MH101no_pel_in_door','took_pellet'] = '0 < 1 minute'


#%%
shelter.loc['MH048no_pel_in_door','took_pellet'] = '1 < 2 minute'
shelter.loc['MH056no_pel_in_door','took_pellet'] = '1 < 2 minute'
shelter.loc['MH077no_pel_in_door','took_pellet'] = '1 < 2 minute'
shelter.loc['MH085no_pel_in_door','took_pellet'] = '1 < 2 minute'
shelter.loc['MH086no_pel_in_door','took_pellet'] = '1 < 2 minute'
shelter.loc['MH088no_pel_in_door','took_pellet'] = '1 < 2 minute'
shelter.loc['MH090no_pel_in_door','took_pellet'] = '1 < 2 minute'

#%%
shelter.loc['MH043no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH047no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH052no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH055no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH060no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH068no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH069no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH073no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH079no_pel_in_door','took_pellet'] = '2 < 3 minute'
shelter.loc['MH080no_pel_in_door','took_pellet'] = '2 < 3 minute'

#%%
shelter.loc['MH039no_pel_in_door','took_pellet'] = '3 < 6 minute'
shelter.loc['MH049no_pel_in_door','took_pellet'] = '3 < 6 minute'
shelter.loc['MH060no_pel_in_door','took_pellet'] = '3 < 6 minute'

shelter.loc['MH053no_pel_in_door','took_pellet'] = '3 < 6 minute'
shelter.loc['MH078no_pel_in_door','took_pellet'] = '3 < 6 minute'

shelter.loc['MH074no_pel_in_door','took_pellet'] = '3 < 6 minute'
shelter.loc['MH097no_pel_in_door','took_pellet'] = '3 < 6 minute'

shelter.loc[shelter.sec == 0, 'took_pellet'] = '0 - immediately'

#%%
shelter = shelter.sort_values('took_pellet', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

#%%
condition = list(shelter['condition'])
total = list(shelter['sec'])
ax = sns.swarmplot(x="condition", y="sec", 
                 data=shelter, hue = "took_pellet", palette=["red", "purple", "yellow", "orange", "green", "black"])
ax.set_title('Time with nose in doorway without pellet (5 min)')
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
