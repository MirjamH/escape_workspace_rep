#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:30:13 2019

@author: mirjamheinemans

With this script I determine how many times the rats cross the ROI that triggered the stimulus (both ways, to shelter and back)
"""

#%%
import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') # to change directory Read csv files with Pandas

#%%
conditions = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/Conditions.csv',delimiter=',', low_memory=False)        
cond = conditions.T

df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos.csv',delimiter=',', low_memory=False, index_col=0)        

#%%
stim_frame = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/stimulus_frame.csv',delimiter=',', index_col =[0])# short version to read CSV into Pandas
pellet = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/pellet.csv',delimiter=',', low_memory=False, index_col =[0])        

#%%
xpos = []
for column in df_beh:
    if column.startswith('x-value'):
        col = df_beh[column]
        xpos.append(col)
        
x = pd.DataFrame(xpos)
x = x.T
x = x.fillna(0)

#%%
i = 0
all_5_min = []
for col in x:
    stim = int(stim_frame.iloc[i]) 
    first_5 = int(stim+(5*60*60))
    x_5_min = x.loc[stim:first_5,col].tolist()
    all_5_min.append(x_5_min)
    i+= 1

#%%
df_5_min = pd.DataFrame(all_5_min)
df_5_min.index = stim_frame.index
df_5_min = df_5_min.T

#%%
'''The next thing is to normalize all numbers, such that the number of the x-position at the moment of stimulus
is 0. So the whole column should be - df_5_min[0,column] 
'''
for column in df_5_min:
    y = df_5_min.loc[0,column]
    corrected = str(column) + 'corr'
    df_5_min[corrected] = (df_5_min[column] - y)

#%%
backwards = []
for column in df_5_min:
    if column.endswith('corr'):
        back = df_5_min[df_5_min[column] < 0].index[0]
        backwards.append(back)

df_back = pd.DataFrame(backwards)
df_back.index = stim_frame.index
df_backwards = df_back.T  
df_conditions = df_back
df_conditions.columns = ['turn']


#%%
conditions = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/Conditions.csv',delimiter=',', low_memory=False)        
cond = conditions.T

TL = []
L = []
TS =[]
T =[]
for animal in cond:
    if cond.iloc[1,animal] == 'T-Loom':
        TL.append(cond.iloc[0,animal])
    elif cond.iloc[1,animal] == 'Loom':
        L.append(cond.iloc[0,animal])
    elif cond.iloc[1,animal] == 'T-Shock':
        TS.append(cond.iloc[0,animal])
    else:
        T.append(cond.iloc[0,animal])
  
#%%
        
df_conditions['condition'] = 'none'
for index in df_conditions.iterrows():
    for animal in TL:
        number = animal
        if number[2:] in index[0]:
            df_conditions.loc[index[0], 'condition'] = 'TL'
    for animal in L:
        number = animal
        if number[2:] in index[0]:
            df_conditions.loc[index[0], 'condition'] = 'L'
    for animal in T:
        number = animal
        if number[2:] in index[0]:
            df_conditions.loc[index[0], 'condition'] = 'T'
    for animal in TS:
        number = animal
        if number[2:] in index[0]:
            df_conditions.loc[index[0], 'condition'] = 'TS'


#%%
'''no differentiation is being made between the animals that take the pellet and the ones that 
    don't'''
            
ax = sns.boxplot(x="condition", y="turn", 
                 data=df_conditions, palette="Set3", showfliers = False)
ax = sns.swarmplot(x="condition", y="turn", 
                 data=df_conditions, color = 'black')
ax.set_ylim(0,2000)

#%%
df_conditions['pellet'] = pellet['test_pellet'] - stim_frame['test_stimulus']
df_conditions['took_pellet'] = df_conditions['pellet'] - df_conditions['turn']
df_conditions['yes_took'] = df_conditions['took_pellet'].map(lambda x: x < 0)

#%%
'''plot of when the animals turn back (i.e. have a negtive x-position for the first time after the stimulus)
with or without pellet: with pellet are orange, rest is blue
'''

ax = sns.boxplot(x="condition", y="turn", 
                 data=df_conditions, palette="Set3", showfliers = False)
ax = sns.swarmplot(x="condition", y="turn", 
                 data=df_conditions, hue = 'yes_took')
#ax.set_ylim(0,2000)



#%%
df_TL = df_back['MH35'] #MH35 is the first tone-loom animal
df_TL = pd.DataFrame(df_TL)
df_TL.columns = ['MH35']

for column in df_back:
    for animal in TL:
        number = animal
        if number[2:] in column:
            bla = df_back[column]
            df_TL[column]  = bla

df_TL = df_TL.apply(pd.to_numeric, errors='coerce')
#%%
df_L = df_back['MH33'] #MH35 is the first tone-loom animal
df_L = pd.DataFrame(df_L)
df_L.columns = ['MH33']

for column in df_back:
    for animal in L:
        number = animal
        if number[2:] in column:
            bla = df_back[column]
            df_L[column]  = bla

df_L = df_L.apply(pd.to_numeric, errors='coerce')
#%%
df_TS = df_back['MH39'] #MH35 is the first tone-loom animal
df_TS = pd.DataFrame(df_TS)
df_TS.columns = ['MH39']

for column in df_back:
    for animal in TS:
        number = animal
        if number[2:] in column:
            bla = df_back[column]
            df_TS[column]  = bla

df_TS =df_TS.apply(pd.to_numeric, errors='coerce')
#%%
df_T = df_back['MH37'] #MH35 is the first tone-loom animal
df_T = pd.DataFrame(df_T)
df_T.columns = ['MH37']

for column in df_back:
    for animal in T:
        number = animal
        if number[2:] in column:
            bla = df_back[column]
            df_T[column]  = bla

df_T = df_T.apply(pd.to_numeric, errors='coerce')
#%%
T_SvsL = ss.mannwhitneyu(df_TS.loc[0],df_L.loc[0])
T_SvsT = ss.mannwhitneyu(df_TS.loc[0],df_T.loc[0])
T_SvsT_L = ss.mannwhitneyu(df_TS.loc[0],df_TL.loc[0])
TvsL = ss.mannwhitneyu(df_T.loc[0],df_L.loc[0])
TvsT_L = ss.mannwhitneyu(df_T.loc[0],df_TL.loc[0])
LvsdT_L = ss.mannwhitneyu(df_L.loc[0],df_TL.loc[0])


'''None of the results significant, except L vs TL, p = 0.015'''

print('L vs T =', TvsL)
print('L vs T_L =', LvsdT_L)
print('L vs T_S =', T_SvsL)

print('T_S vs T =',T_SvsT)
print('T_S vs T_L =',T_SvsT_L)

print('T vs T_L =', TvsT_L)

            
        