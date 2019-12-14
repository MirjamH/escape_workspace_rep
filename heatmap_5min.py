#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:51:35 2019

@author: mirjamheinemans
opening the file with all 0's and 1's for the behavioral events, while also having the frame and x-positition 
per animal.

Before everything for the whole time is binned, so not only just after the stimulus etc!!!!!
Next i have to figure out how to do this, and what would be logical timepoints


Here: first 5 minutes after stimulus. 

First part copy-pasted from 'heatmap_entire_test.py'
"""
#%%

import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') # to change directory Read csv files with Pandas

#%%
conditions = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/Conditions.csv',delimiter=',', low_memory=False)        
cond = conditions.T

df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos.csv',delimiter=',', low_memory=False, index_col=0)        

#%%

stim_frame = pd.read_csv('stimulus_frame.csv',delimiter=',',index_col =[0])# short version to read CSV into Pandas


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
    stim = int(stim_frame.iloc[i])# I cannot change this value, because I depend the relative x on it
    first_5 = int(stim+(0.5*60*60))
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
bins = list(range(-700,850, 20))

binned = df_5_min.groupby(pd.cut(df_5_min['MH33corr'], bins=bins)).size()
binned = pd.DataFrame(binned)
binned.columns = ['MH33corr'] # this column is overwritten in the first iteration of next for-loop :)
#%%

bins = list(range(-700,850, 20))

for column in df_5_min:
    if column.endswith('corr'):
        binned[column] = df_5_min.groupby(pd.cut(df_5_min[column], bins=bins)).size()
        #print(binned[column])

#%%
binned_no_shelter = binned.iloc[:,:]

#%%

ax = sns.heatmap(binned_no_shelter,vmax =3000)
ax.get_ylim()





#%%
''' 
All animals are in a list depending on their condition. Now i can compare the column name to the list and
add the column to a new dataframe? or group them by condition?
''' 
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
df_TL = binned['MH35corr'] #MH35 is the first tone-loom animal
df_TL = pd.DataFrame(df_TL)
df_TL.columns = ['MH35corr']

for column in binned:
    if column.endswith('corr'):
        for animal in TL:
            number = animal
            if number[2:] in column:
                bla = binned[column]
                df_TL[column]  = bla

#%%
df_L = binned['MH33corr'] #MH35 is the first tone-loom animal
df_L = pd.DataFrame(df_L)
df_L.columns = ['MH33corr']

for column in binned:
    for animal in L:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_L[column]  = bla

#%%
df_TS = binned['MH39corr'] #MH35 is the first tone-loom animal
df_TS = pd.DataFrame(df_TS)
df_TS.columns = ['MH39corr']

for column in binned:
    for animal in TS:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_TS[column]  = bla

#%%
df_T = binned['MH37corr'] #MH35 is the first tone-loom animal
df_T = pd.DataFrame(df_T)
df_T.columns = ['MH37corr']

for column in binned:
    for animal in T:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_T[column]  = bla


#%%

df_L_noshel = df_L.iloc[25:45,:]
ax = sns.heatmap(df_L_noshel.T, vmax =1200)
ax.set_title('Loom (end stim + 1 min)')
ax.set(xlabel='x-position (0 = position of stimulus)', ylabel='animal')

#%%

df_TL_noshel = df_TL.iloc[25:45,:]
ax = sns.heatmap(df_TL_noshel.T, vmax =300)
ax.set_title('Tone-Loom (end stim + 1 min)')
ax.set(xlabel='x-position (0 = position of stimulus)', ylabel='animal')

#%%
df_TS_noshel = df_TS.iloc[25:45,:]
ax = sns.heatmap(df_TS_noshel.T, vmax =300)
ax.set_title('Tone-Shock (end stim + 1 min)')
ax.set(xlabel='x-position (0 = position of stimulus)', ylabel='animal')

#%%

df_T_noshel = df_T.iloc[25:45,:]
ax = sns.heatmap(df_T_noshel.T, vmax =300)
ax.set_title('Tone (end stim + 1 min)')
ax.set(xlabel='x-position (0 = position of stimulus)', ylabel='animal')

