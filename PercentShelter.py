#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:16:56 2019

@author: mirjamheinemans


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
    
        for i, row in dataset_stim.iterrows():
            if dataset_stim.iloc[i,2] == 1:
                dataset_stim.iloc[i,4] = 2
                break
            elif dataset_stim.iloc[i,0] == 1 and dataset_stim.iloc[i,2] == 0:
                dataset_stim.iloc[i,4] = 1
        dataset_stim.iloc[-2,4] = 2    
        sheltertime = dataset_stim[file_names+'no_pel_in_shel']
        #print(sheltertime)
        return(sheltertime)

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['no_pel_in_shel']
index = range(18001)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['no_pel_in_shel'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['no_pel_in_shel']
index = range(18001)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['no_pel_in_shel'])
 #%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['no_pel_in_shel']
index = range(18001)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)

shelter_t_shock = shelter_t_shock.drop(columns = ['no_pel_in_shel'])
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['no_pel_in_shel']
index = range(18001)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)

shelter_tone = shelter_tone.drop(columns = ['no_pel_in_shel'])

#%%
'''only run once: if you run again after adding the condition row, you get only 'nan' in sum row'''
pellet_frame_loom =[]
shelter = 0
for column in shelter_loom: 
    pellet = shelter_loom.loc[shelter_loom.loc[:,column] == 2].index.values.astype(int)[0]



    for row in shelter_loom[column]:
       if row == 2:
           break
       elif row == 1:
           shelter +=1
           
    percent = shelter / pellet *100
    pellet_frame_loom.append(percent)
    shelter = 0
#           pellet = row
#           pellet_frame_loom.append(pellet)
#           break
#          
pellet_loom = pd.DataFrame(pellet_frame_loom, index =shelter_loom.columns, columns =['percent'])           
pellet_loom ['condition'] = 'L'


#%%
pellet_frame_TL =[]
shelter = 0
for column in shelter_t_loom: 
    pellet = shelter_t_loom.loc[shelter_t_loom.loc[:,column] == 2].index.values.astype(int)[0]



    for row in shelter_t_loom[column]:
       if row == 2:
           break
       elif row == 1:
           shelter +=1
           
    percent = shelter / pellet *100
    pellet_frame_TL.append(percent)
    shelter = 0
#           pellet = row
#           pellet_frame_loom.append(pellet)
#           break
#          
pellet_t_loom = pd.DataFrame(pellet_frame_TL, index =shelter_t_loom.columns, columns =['percent'])           
pellet_t_loom ['condition'] = 'TL'

#%%
pellet_frame_TS =[]
shelter = 0
for column in shelter_t_shock: 
    pellet = shelter_t_shock.loc[shelter_t_shock.loc[:,column] == 2].index.values.astype(int)[0]



    for row in shelter_t_shock[column]:
       if row == 2:
           break
       elif row == 1:
           shelter +=1
           
    percent = shelter / pellet *100
    pellet_frame_TS.append(percent)
    shelter = 0
#           pellet = row
#           pellet_frame_loom.append(pellet)
#           break
#          
pellet_t_shock = pd.DataFrame(pellet_frame_TS, index =shelter_t_shock.columns, columns =['percent'])           
pellet_t_shock ['condition'] = 'TS'

#%%
pellet_frame_T =[]
shelter = 0
for column in shelter_tone: 
    pellet = shelter_tone.loc[shelter_tone.loc[:,column] == 2].index.values.astype(int)[0]



    for row in shelter_tone[column]:
       if row == 2:
           break
       elif row == 1:
           shelter +=1
           
    percent = shelter / pellet *100
    pellet_frame_T.append(percent)
    shelter = 0
#           pellet = row
#           pellet_frame_loom.append(pellet)
#           break
#          
pellet_tone = pd.DataFrame(pellet_frame_T, index =shelter_tone.columns, columns =['percent'])           
pellet_tone ['condition'] = 'T'

#%%


shelter_figure =  pd.concat([pellet_loom, pellet_t_loom, pellet_t_shock, pellet_tone])
#shelter = shelter_figure.T

#%%
shelter_figure.loc[:,'took_pellet'] = '6 > minutes'

'''manually addig the number of minutes the animals took to get pellet'''

shelter_figure.loc['MH035no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH036no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH037no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH038no_pel_in_shel','took_pellet'] = '0 < 1 minute'

shelter_figure.loc['MH040no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH042no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH044no_pel_in_shel','took_pellet'] = '0 < 1 minute'

shelter_figure.loc['MH050no_pel_in_shel','took_pellet'] ='0 < 1 minute'
shelter_figure.loc['MH051no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH054no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH057no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH058no_pel_in_shel','took_pellet'] = '0 < 1 minute'

shelter_figure.loc['MH062no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH063no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH064no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH066no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH067no_pel_in_shel','took_pellet'] = '0 < 1 minute'

shelter_figure.loc['MH070no_pel_in_shel','took_pellet'] ='0 < 1 minute'
shelter_figure.loc['MH071no_pel_in_shel','took_pellet'] ='0 < 1 minute'
shelter_figure.loc['MH072no_pel_in_shel','took_pellet'] ='0 < 1 minute'
shelter_figure.loc['MH075no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH076no_pel_in_shel','took_pellet'] = '0 < 1 minute'

shelter_figure.loc['MH081no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH082no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH084no_pel_in_shel','took_pellet'] = '0 < 1 minute'

shelter_figure.loc['MH092no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH093no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH096no_pel_in_shel','took_pellet'] = '0 < 1 minute'
shelter_figure.loc['MH098no_pel_in_shel','took_pellet'] = '0 < 1 minute'

shelter_figure.loc['MH101no_pel_in_shel','took_pellet'] = '0 < 1 minute'


#%%
shelter_figure.loc['MH048no_pel_in_shel','took_pellet'] = '1 < 2 minute'
shelter_figure.loc['MH056no_pel_in_shel','took_pellet'] = '1 < 2 minute'
shelter_figure.loc['MH077no_pel_in_shel','took_pellet'] = '1 < 2 minute'
shelter_figure.loc['MH085no_pel_in_shel','took_pellet'] = '1 < 2 minute'
shelter_figure.loc['MH086no_pel_in_shel','took_pellet'] = '1 < 2 minute'
shelter_figure.loc['MH088no_pel_in_shel','took_pellet'] = '1 < 2 minute'
shelter_figure.loc['MH090no_pel_in_shel','took_pellet'] = '1 < 2 minute'

#%%
shelter_figure.loc['MH043no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH047no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH052no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH055no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH060no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH068no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH069no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH073no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH079no_pel_in_shel','took_pellet'] = '2 < 3 minute'
shelter_figure.loc['MH080no_pel_in_shel','took_pellet'] = '2 < 3 minute'

#%%
shelter_figure.loc['MH039no_pel_in_shel','took_pellet'] = '3 < 6 minute'
shelter_figure.loc['MH049no_pel_in_shel','took_pellet'] = '3 < 6 minute'
shelter_figure.loc['MH060no_pel_in_shel','took_pellet'] = '3 < 6 minute'

shelter_figure.loc['MH053no_pel_in_shel','took_pellet'] = '3 < 6 minute'
shelter_figure.loc['MH078no_pel_in_shel','took_pellet'] = '3 < 6 minute'

shelter_figure.loc['MH074no_pel_in_shel','took_pellet'] = '3 < 6 minute'
shelter_figure.loc['MH097no_pel_in_shel','took_pellet'] = '3 < 6 minute'

shelter_figure.loc[shelter_figure.percent == 0, 'took_pellet'] = '0 - immediately'

#%%
shelter_figure = shelter_figure.sort_values('took_pellet', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

#%%
total = list(shelter_figure['percent'])
condition = list(shelter_figure['condition'])
ax = sns.swarmplot(x="condition", y="percent", 
                 data=shelter_figure, hue = "took_pellet", palette=["red", "purple", "yellow", "orange", "green", "black"])
ax.set_title('Percent time in shelter before pellet (5 min)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
ax.legend(bbox_to_anchor=(1,1))
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
T_SvsL = ss.mannwhitneyu(pellet_t_shock['percent'],pellet_loom['percent'])
T_SvsT = ss.mannwhitneyu(pellet_t_shock['percent'],pellet_tone['percent'])
T_SvsT_L = ss.mannwhitneyu(pellet_t_shock['percent'],pellet_t_loom['percent'])
TvsL = ss.mannwhitneyu(pellet_tone['percent'],pellet_loom['percent'])
TvsT_L = ss.mannwhitneyu(pellet_tone['percent'],pellet_t_loom['percent'])
LvsdT_L = ss.mannwhitneyu(pellet_loom['percent'],pellet_t_loom['percent'])
#%%
print('T_SvsT =',T_SvsT)
print('T_SvsL =', T_SvsL)
print('T_SvsT_L =',T_SvsT_L)
print('TvsL =', TvsL)
print('TvsT_L =', TvsT_L)
print('LvsdT_L =', LvsdT_L)

#%%
#os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files')
#export_csv = shelter_figure.to_csv ('took_pellet.csv', header=True)
#
#
