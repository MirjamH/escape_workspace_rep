#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:35:29 2019

@author: mirjamheinemans
"""

"""
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
sns.set_style("whitegrid", {'axes.grid' : False})

os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files') # to change directory Read csv files with Pandas
#%%

path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'


def ShelterTime(file_names):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [1,4,9])
        stimulus = dataset.loc[dataset.iloc[:,2] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int((stimulus -900)):int((stimulus +900)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
                    
        dataset_stim['pellet'+ file_names] = 0
        if sum(dataset_stim.iloc[:,1]) > 0:
            pellet = dataset_stim.loc[dataset_stim.iloc[:,1] == 1].index.values.astype(int)[0]
            dataset_stim.iloc[pellet, -1] = dataset_stim.iloc[pellet, 0]
        
        x_value = dataset_stim.iloc[:,0]
        pellet_frame = dataset_stim.iloc[:,3]
        trace = pd.concat([x_value, pellet_frame], axis = 1)
        
        return(trace)
        

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['xpos']
index = range(300)
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
index = range(300)
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
index = range(300)
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
index = range(300)
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
df = pd.concat([shelter_loom, shelter_t_shock, shelter_t_loom, shelter_tone], axis = 1)
df['frames']=  range(len(df))
df['sec'] =(df['frames']/60) - 15

#%%
'''Loom'''
ax = sns.lineplot(x='sec', y='x-value33', data =df, color = 'black', zorder=1).set_title('Loom MH33')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH033', data = df, color = 'c',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value34', data =df, color = 'black', zorder=1).set_title('Loom MH34')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH034', data = df, color = 'c',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value46', data =df, color = 'black', zorder=1).set_title('Loom MH46')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH046', data = df, color = 'c',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value59', data =df, color = 'black', zorder=1).set_title('Loom MH59')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH059', data = df, color = 'c',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value60', data =df, color = 'black', zorder=1).set_title('Loom MH60')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH060', data = df, color = 'c',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value65', data =df, color = 'black', zorder=1).set_title('Loom MH65')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH065', data = df, color = 'c',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value66', data =df, color = 'orange', zorder=1).set_title('Loom MH66')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH066', data = df, color = 'c',s =150,zorder = 2)


'''Loom'''
ax = sns.lineplot(x='sec', y='x-value85', data =df, color = 'gray', zorder = 1).set_title('Loom MH85')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH085', data = df, color = 'g',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value86', data =df, color = 'gray', zorder = 1).set_title('Loom MH86')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH086', data = df, color = 'g',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value87', data =df, color = 'gray', zorder = 1).set_title('Loom MH87')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH087', data = df, color = 'g',s =150,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value88', data =df, color = 'gray', zorder = 1).set_title('Loom MH88')#Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH088', data = df, color = 'g',s =150,zorder = 2)

#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
ax.plot([9 ,9], [0, 1200],color ='gray')
ax.plot([0 ,0], [0, 1200],color ='gray')
ax.set_ylabel('x-position (a.u.)')

#%%
'''Tone-Loom'''

ax = sns.lineplot(x='sec', y='x-value43', data =df, color = 'blue',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH043', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH43')



ax = sns.lineplot(x='sec', y='x-value44', data =df, color = 'orange',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH044', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH44')


ax = sns.lineplot(x='sec', y='x-value51', data =df, color = 'orange',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH051', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH51')


ax = sns.lineplot(x='sec', y='x-value52', data =df, color = 'blue',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH052', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH52')


ax = sns.lineplot(x='sec', y='x-value53', data =df, color = 'blue',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH053', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH53')


ax = sns.lineplot(x='sec', y='x-value63', data =df, color = 'orange',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH063', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH63')


ax = sns.lineplot(x='sec', y='x-value64', data =df, color = 'orange',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH064', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH64')


ax = sns.lineplot(x='sec', y='x-value70', data =df, color = 'orange',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH070', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH70')



ax = sns.lineplot(x='sec', y='x-value71', data =df, color = 'orange',zorder = 1).set_title('Tone-Loom MH71')#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH071', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value78', data =df, color = 'blue',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH078', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH78')


ax = sns.lineplot(x='sec', y='x-value92', data =df, color = 'blue',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH092', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH92')


ax = sns.lineplot(x='sec', y='x-value96', data =df, color = 'orange',zorder = 1)#T-Loom
ax = sns.scatterplot(x = 'sec', y = 'pelletMH096', data = df, color = 'b',s =100,zorder = 2).set_title('Tone-Loom MH96')


ax = sns.lineplot(x='sec', y='x-value101',data =df, color = 'orange',zorder = 1).set_title('Tone-Loom MH101')
ax = sns.scatterplot(x = 'sec', y = 'pelletMH101', data = df, color = 'b',s =100,zorder = 2).set_ylabel('x-position (a.u.)')#T-Loom


ax = sns.lineplot([9 ,9], [0, 1200],color ='black', linewidth =10)
ax = sns.lineplot([0 ,0], [0, 1200],color ='black')

#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
#ax.set_ylabel('x-position (a.u.)')
#ax.plot([10 ,10], [0, 1200],color ='gray')
#ax.plot([1 ,1], [0, 1200],color ='gray')


#%%
'''Tone-Shock'''
ax = sns.lineplot(x='sec', y='x-value39', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH39')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH039', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value40', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH40')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH040', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value49', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH49')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH049', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value50', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH50')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH050', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value55', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH55')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH055', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value56', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH56')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH056', data = df, color = 'b',s =100,zorder = 2)
##
#
ax = sns.lineplot(x='sec', y='x-value67', data =df, color = 'orange',zorder = 1).set_title('Tone-Shock MH67')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH067', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value68', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH68')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH068', data = df, color = 'b',s =100,zorder = 2)




'''Tone-Shock'''
ax = sns.lineplot(x='sec', y='x-value73', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH73')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH073', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value74', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH74')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH074', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value79', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH79')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH079', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value80', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH80')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH080', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value84', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH84')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH084', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value89', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH89')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH089', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value90', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH90')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH090', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value100',data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH100')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'pelletMH100', data = df, color = 'b',s =100,zorder = 2)


#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
ax.plot([9 ,9], [0, 1200],color ='gray')
ax.plot([0 ,0], [0, 1200],color ='gray')
ax.set_ylabel('x-position (a.u.)')

#%%
'''Tone'''
ax = sns.lineplot(x='sec', y='x-value37', data =df, color = 'orange').set_title('Tone MH37')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH037', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value38', data =df, color = 'green').set_title('Tone MH38')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH038', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value42', data =df, color = 'orange').set_title('Tone MH42')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH042', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value47', data =df, color = 'green').set_title('Tone MH47')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH047', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value48', data =df, color = 'green').set_title('Tone MH48')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH048', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value57', data =df, color = 'green').set_title('Tone MH57')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH057', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value58', data =df, color = 'orange').set_title('Tone MH58')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH058', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value61', data =df, color = 'green').set_title('Tone MH61')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH061', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value62', data =df, color = 'orange').set_title('Tone MH62')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH062', data = df, color = 'b',s =100,zorder = 2)



ax = sns.lineplot(x='sec', y='x-value75', data =df, color = 'green').set_title('Tone MH75')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH075', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value76', data =df, color = 'orange').set_title('Tone MH76')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH076', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value81', data =df, color = 'orange').set_title('Tone MH81')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH081', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value82', data =df, color = 'green').set_title('Tone MH82')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH082', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value93', data =df, color = 'green').set_title('Tone MH93')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH093', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value97', data =df, color = 'green').set_title('Tone MH97')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH097', data = df, color = 'b',s =100,zorder = 2)


ax = sns.lineplot(x='sec', y='x-value98', data =df, color = 'orange').set_title('Tone MH98')#Tone
ax = sns.scatterplot(x = 'sec', y = 'pelletMH098', data = df, color = 'b',s =100,zorder = 2)


#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
ax.plot([10 ,10], [0, 1200],color ='gray')
ax.plot([1 ,1], [0, 1200],color ='gray')
ax.set_ylabel('x-position (a.u.)')




#%%



