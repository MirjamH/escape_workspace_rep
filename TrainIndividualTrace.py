#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:53:27 2019

@author: mirjamheinemans

Individual traces of the animals during the whole test


TRAINING columns:
    0.
    1.MH33,
    2.MH33_in_shelter
    3.MH33_doorway
    4.MH33_with_pellet
    5.MH33_eat_pellet
    6.MH33_freeze
    7.MH33_reaching
    8.MH33_scanning
    9.MH33_new_pellet

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

os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') # to change directory Read csv files with Pandas
#%%

path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'


def Trace(file_names):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'training.csv', usecols = [1,4,9])
        
        
        
        if int(file_names[2:]) >45:
           dataset = dataset.groupby(np.arange(len(dataset.index))//2).mean()
             
        dataset['took_pell'+file_names] = 0
        
        took_pell = dataset.iloc[:,1].diff()[dataset.iloc[:,1].diff() > 0].index.values#[0:4]
        dataset.iloc[took_pell,-1] = dataset.iloc[took_pell,0]
        
        
        #print(sheltertime)
        return(dataset)
        

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['xpos']
index = range(900)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['xpos'])
shelter_loom = shelter_loom.drop(index = 0)
#shelter_loom['frames']=  range(len(shelter_loom))
#shelter_loom['sec'] =shelter_loom['frames']/60


#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['xpos']
index = range(900)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['xpos'])
shelter_t_loom = shelter_t_loom.drop(index = 0)
#shelter_t_loom['frames']=  range(len(shelter_loom))
#shelter_t_loom['sec'] =shelter_t_loom['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['xpos']
index = range(900)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)
shelter_t_shock = shelter_t_shock.drop(columns = ['xpos'])
shelter_t_shock = shelter_t_shock.drop(index = 0)
#shelter_t_shock['frames']=  range(len(shelter_t_shock))
#shelter_t_shock['sec'] =shelter_t_shock['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['xpos']
index = range(900)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Trace(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)
shelter_tone = shelter_tone.drop(columns = ['xpos'])
shelter_tone = shelter_tone.drop(index = 0)
#shelter_tone['frames']=  range(len(shelter_tone))
#shelter_tone['sec'] =shelter_tone['frames']/60
        
        
        

#%%
df = pd.concat([shelter_loom, shelter_t_shock, shelter_t_loom, shelter_tone], axis = 1)
df['frames']=  range(len(df))
df['sec'] =df['frames']/60

#%%
'''Loom'''
#ax = sns.lineplot(x='sec', y='x-value33', data =df, color = 'black', zorder=1).set_title('Loom MH33')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH033', data = df, color = 'c',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value34', data =df, color = 'black', zorder=1).set_title('Loom MH34')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH034', data = df, color = 'c',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value46', data =df, color = 'black', zorder=1).set_title('Loom MH46')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH046', data = df, color = 'c',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value59', data =df, color = 'black', zorder=1).set_title('Loom MH59')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH059', data = df, color = 'c',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value60', data =df, color = 'black', zorder=1).set_title('Loom MH60')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH060', data = df, color = 'c',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value65', data =df, color = 'black', zorder=1).set_title('Loom MH65')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH065', data = df, color = 'c',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value66', data =df, color = 'orange', zorder=1).set_title('Loom MH66')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH066', data = df, color = 'c',s =150,zorder = 2)
#
#
#'''Loom'''
#ax = sns.lineplot(x='sec', y='x-value85', data =df, color = 'gray', zorder = 1).set_title('Loom MH85')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH085', data = df, color = 'g',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value86', data =df, color = 'gray', zorder = 1).set_title('Loom MH86')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH086', data = df, color = 'g',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value87', data =df, color = 'gray', zorder = 1).set_title('Loom MH87')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH087', data = df, color = 'g',s =150,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value88', data =df, color = 'gray', zorder = 1).set_title('Loom MH88')#Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH088', data = df, color = 'g',s =150,zorder = 2)

#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
#ax.plot([10 ,10], [0, 1200],color ='gray')
#ax.plot([1 ,1], [0, 1200],color ='gray')
ax.set_ylabel('x-position (a.u.)')
ax.set_ylim([0, 1200])

#%%
'''Tone-Loom'''

#ax = sns.lineplot(x='sec', y='x-value43', data =df, color = 'blue',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH043', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH43')
#
#
#
#ax = sns.lineplot(x='sec', y='x-value44', data =df, color = 'orange',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH044', data = df, color = 'c',s =100,zorder = 2)#.set_title('Tone-Loom MH44')
#ax.set_xlim([0,350])
#ax.set_title('Tone-Loom MH44')
#
#ax = sns.lineplot(x='sec', y='x-value51', data =df, color = 'orange',zorder = 1)#T-Loom
#ax.set_ylabel('x-position (a.u.)')
#ax.set_ylim([0, 1200])
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH051', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH51')
#
#
#ax = sns.lineplot(x='sec', y='x-value52', data =df, color = 'blue',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH052', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH52')
#
#
#ax = sns.lineplot(x='sec', y='x-value53', data =df, color = 'blue',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH053', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH53')
#
#
#ax = sns.lineplot(x='sec', y='x-value63', data =df, color = 'orange',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH063', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH63')
#
#
#ax = sns.lineplot(x='sec', y='x-value64', data =df, color = 'orange',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH064', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH64')
#
#
#ax = sns.lineplot(x='sec', y='x-value70', data =df, color = 'orange',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH070', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH70')
#
#
#
#ax = sns.lineplot(x='sec', y='x-value71', data =df, color = 'orange',zorder = 1).set_title('Tone-Loom MH71')#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH071', data = df, color = 'c',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value78', data =df, color = 'blue',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH078', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH78')
##
##
#ax = sns.lineplot(x='sec', y='x-value92', data =df, color = 'blue',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH092', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH92')
#
#
#ax = sns.lineplot(x='sec', y='x-value96', data =df, color = 'orange',zorder = 1)#T-Loom
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH096', data = df, color = 'c',s =100,zorder = 2).set_title('Tone-Loom MH96')
#
#
#ax = sns.lineplot(x='sec', y='x-value101',data =df, color = 'orange',zorder = 1).set_title('Tone-Loom MH101')
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH101', data = df, color = 'c',s =100,zorder = 2).set_ylabel('x-position (a.u.)')#T-Loom

#ax = sns.lineplot([10 ,10], [0, 1200],color ='gray')

#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
#ax.set_ylabel('x-position (a.u.)')
#ax.plot([10 ,10], [0, 1200],color ='gray')
#ax.plot([1 ,1], [0, 1200],color ='gray')
ax.set_ylabel('x-position (a.u.)')
ax.set_ylim([0, 1200])

#%%
'''Tone-Shock'''
#ax = sns.lineplot(x='sec', y='x-value39', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH39')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH039', data = df, color = 'b',s =100,zorder = 2)
#
#
ax = sns.lineplot(x='sec', y='x-value40', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH40')#T-Shock
ax = sns.scatterplot(x = 'sec', y = 'took_pellMH040', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value49', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH49')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH049', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value50', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH50')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH050', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value55', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH55')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH055', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value56', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH56')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH056', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value67', data =df, color = 'orange',zorder = 1).set_title('Tone-Shock MH67')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH067', data = df, color = 'b',s =100,zorder = 2)
#
##
#ax = sns.lineplot(x='sec', y='x-value68', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH68')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH068', data = df, color = 'b',s =100,zorder = 2)
#
#
#
#
#'''Tone-Shock'''
#ax = sns.lineplot(x='sec', y='x-value73', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH73')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH073', data = df, color = 'b',s =100,zorder = 2)

#
#ax = sns.lineplot(x='sec', y='x-value74', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH74')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH074', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value79', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH79')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH079', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value80', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH80')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH080', data = df, color = 'b',s =100,zorder = 2)

#
#ax = sns.lineplot(x='sec', y='x-value84', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH84')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH084', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value89', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH89')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH089', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value90', data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH90')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH090', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value100',data =df, color = 'red',zorder = 1).set_title('Tone-Shock MH100')#T-Shock
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH100', data = df, color = 'b',s =100,zorder = 2)


#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
#ax.plot([10 ,10], [0, 1200],color ='gray')
#ax.plot([1 ,1], [0, 1200],color ='gray')
ax.set_ylabel('x-position (a.u.)')
ax.set_ylim([0, 1200])

#%%
'''Tone'''
#ax = sns.lineplot(x='sec', y='x-value37', data =df, color = 'orange', zorder = 1).set_title('Tone MH37')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH037', data = df, color = 'b',s =100,zorder = 2)


#ax = sns.lineplot(x='sec', y='x-value38', data =df, color = 'green', zorder = 1).set_title('Tone MH38')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH038', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value42', data =df, color = 'orange', zorder = 1).set_title('Tone MH42')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH042', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value47', data =df, color = 'green', zorder = 1).set_title('Tone MH47')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH047', data = df, color = 'b',s =100,zorder = 2)
##
#
#ax = sns.lineplot(x='sec', y='x-value48', data =df, color = 'green', zorder = 1).set_title('Tone MH48')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH048', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value57', data =df, color = 'green', zorder = 1).set_title('Tone MH57')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH057', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value58', data =df, color = 'orange', zorder = 1).set_title('Tone MH58')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH058', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value61', data =df, color = 'green', zorder = 1).set_title('Tone MH61')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH061', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value62', data =df, color = 'orange', zorder = 1).set_title('Tone MH62')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH062', data = df, color = 'b',s =100,zorder = 2)
#
#
#
#ax = sns.lineplot(x='sec', y='x-value75', data =df, color = 'green', zorder = 1).set_title('Tone MH75')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH075', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value76', data =df, color = 'orange', zorder = 1).set_title('Tone MH76')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH076', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value81', data =df, color = 'orange', zorder = 1).set_title('Tone MH81')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH081', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value82', data =df, color = 'green', zorder = 1).set_title('Tone MH82')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH082', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value93', data =df, color = 'green', zorder = 1).set_title('Tone MH93')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH093', data = df, color = 'b',s =100,zorder = 2)
#
#
ax = sns.lineplot(x='sec', y='x-value97', data =df, color = 'green', zorder = 1).set_title('Tone MH97')#Tone
ax = sns.scatterplot(x = 'sec', y = 'took_pellMH097', data = df, color = 'b',s =100,zorder = 2)
#
#
#ax = sns.lineplot(x='sec', y='x-value98', data =df, color = 'orange', zorder = 1).set_title('Tone MH98')#Tone
#ax = sns.scatterplot(x = 'sec', y = 'took_pellMH098', data = df, color = 'b',s =100,zorder = 2)


#ax.set_xlim([0, 20])
#ax.set_ylim([0, 800])
#ax.plot([10 ,10], [0, 1200],color ='gray')
#ax.plot([1 ,1], [0, 1200],color ='gray')
ax.set_ylabel('x-position (a.u.)')
ax.set_ylim([0, 1200])



#%%
