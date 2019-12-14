#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:07:30 2019

@author: mirjamheinemans
opening the file with all 0's and 1's for the behavioral events, while also having the frame and x-positition 
per animal.

Now i have to somehow assign a condition or work per animal to get the relevant plots.
Conditions are in conditions variable, connected to animal number
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
xpos = []
for column in df_beh:
    if column.startswith('x-value'):
        col = df_beh[column]
        xpos.append(col)
        
x = pd.DataFrame(xpos)
x = x.T
#%%
x = x.fillna(0)
''' trying to make a heat map with one animal, using dataframe 'x'
'''
#%%

bins = list(range(-1,1250, 5))

binned = x.groupby(pd.cut(x['x-value33'], bins=bins)).size()
binned = pd.DataFrame(binned)
binned.columns = ['x-value33'] # this column is overwritten in the first iteration of next for-loop :)
#%%

''' here everything for the whole time is binned, so not only just after the stimulus etc!!!!!
Next i have to figure out how to do this, and what would be logical timepoints
'''

for column in x:
    if column.startswith('x-value'):
#        next
#    elif column.startswith('binned'):
        binned[column] = x.groupby(pd.cut(x[column], bins=bins)).size()
        #print(binned[column])

#%%
binned_no_shelter = binned.iloc[100:140,:]

#%%

ax = sns.heatmap(binned_no_shelter, vmax =180)
ax.get_ylim()


#%%
df_TL = binned['x-value35'] #MH35 is the first tone-loom animal
df_TL = pd.DataFrame(df_TL)
df_TL.columns = ['x-value35']

for column in binned:
    for animal in TL:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_TL[column]  = bla

#%%
df_L = binned['x-value33'] #MH35 is the first tone-loom animal
df_L = pd.DataFrame(df_L)
df_L.columns = ['x-value33']

for column in binned:
    for animal in L:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_L[column]  = bla

#%%
df_TS = binned['x-value39'] #MH35 is the first tone-loom animal
df_TS = pd.DataFrame(df_TS)
df_TS.columns = ['x-value39']

for column in binned:
    for animal in TS:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_TS[column]  = bla

#%%
df_T = binned['x-value37'] #MH35 is the first tone-loom animal
df_T = pd.DataFrame(df_T)
df_T.columns = ['x-value37']

for column in binned:
    for animal in T:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_T[column]  = bla




#%%

df_L_noshel = df_L.iloc[100:140,:]
ax = sns.heatmap(df_L_noshel, vmax =180)
ax.get_ylim()




