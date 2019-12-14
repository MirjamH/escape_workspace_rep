#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:37:05 2019

@author: mirjamheinemans
"""

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
Excluded animals:
MH41 - ate only 1 pellet in total training
MH45 - stimulus did not work
MH94 - got to pellet before start of experiment (opened the door by himself)
MH95 - never came out of shelter during test
MH99 - came out of shelter after >18 minutes during test
MH102 - never came out of shelter during test


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
    stim = int(stim_frame.iloc[i]) 
    first_5 = int(stim+(1*60*60))
    x_5_min = x.loc[stim:first_5,col].tolist()
    all_5_min.append(x_5_min)
    i+= 1


#%%
df_5_min = pd.DataFrame(all_5_min)
df_5_min.index = stim_frame.index
df_5_min = df_5_min.T
df_5_min.index.name = None

#%%
'''The next thing is to normalize all numbers, such that the number of the x-position at the moment of stimulus
is 0. So the whole column should be - df_5_min[0,column] 
'''
for column in df_5_min:
    y = df_5_min.loc[0,column]
    corrected = str(column) + 'corr'
    df_5_min[corrected] = (df_5_min[column] - y)

#%%
bins = list(range(-700,850, 200))

binned = df_5_min.groupby(pd.cut(df_5_min['MH33corr'], bins=bins)).size()
binned = pd.DataFrame(binned)
binned.columns = ['MH33corr'] # this column is overwritten in the first iteration of next for-loop :)
#%%

bins = list(range(-700,850, 200))

for column in df_5_min:
    if column.endswith('corr'):
        binned[column] = df_5_min.groupby(pd.cut(df_5_min[column], bins=bins)).size()
        #print(binned[column])

#%%
binned_no_shelter = binned.iloc[:,:]
binned_no_shelter.index.name = None
#%%

ax = sns.heatmap(binned_no_shelter,vmax =3000)
ax.get_ylim()

#%%
'''
Excluded animals:
MH41 - ate only 1 pellet in total training
MH45 - stimulus did not work
MH94 - got to pellet before start of experiment (opened the door by himself)
MH95 - never came out of shelter during test
MH99 - came out of shelter after >18 minutes during test
MH102 - never came out of shelter during test
'''
pellet = ['36','44','51','54','62','64','66','67','70','71','72','76','81','96','98']
no_pellet = ['33','34','35','37','38','39','40','42','43','46','47','48','49','50','52','53','55','56','57','58','59','60','61','63','65','68','69','73','74','75','77','78','79','78','79','80','82','83','84','85','86','87','88','89','90','91','92','93','97','99','100','101']       

    #%%
df_pellet = binned['MH36corr'] #MH35 is the first tone-loom animal
df_pellet = pd.DataFrame(df_pellet)
df_pellet.columns = ['MH36corr']

df_NOpellet = binned['MH33corr'] #MH35 is the first tone-loom animal
df_NOpellet = pd.DataFrame(df_NOpellet)
df_NOpellet.columns = ['MH33corr']


for column in binned:
    for animal in pellet:
        if animal in column:
            bla = binned[column]
            df_pellet[column]  = bla

for column in binned:
    for animal in no_pellet:
        if animal in column:
            bla = binned[column]
            df_NOpellet[column]  = bla
            
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
    for animal in TL:
        number = animal
        if number[2:] in column:
            bla = binned[column]
            df_TL[column]  = bla

        '''No pellet TL: all animals that did not take pellet directly after stimulus all animals that took the pellet after the stimulus'''
df_TL_NO = df_NOpellet['MH35corr'] #MH35 is the first tone-loom animal
df_TL_NO = pd.DataFrame(df_TL_NO)
df_TL_NO.columns = ['MH35corr']

for column in df_NOpellet:
    for animal in TL:
        number = animal
        if number[2:] in column:
            print(column)
            bla = df_NOpellet[column]
            df_TL_NO[column]  = bla


        '''with pellet TL: all animals that took the pellet after the stimulus'''
df_TL_YES = df_pellet['MH36corr'] #MH35 is the first tone-loom animal
df_TL_YES = pd.DataFrame(df_TL_YES)
df_TL_YES.columns = ['MH36corr']

for column in df_pellet:
    for animal in TL:
        number = animal
        if number[2:] in column:
            bla = df_pellet[column]
            df_TL_YES[column]  = bla
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


        '''No pellet L: all animals that did not take pellet directly after stimulus all animals that took the pellet after the stimulus'''
df_L_NO = df_NOpellet['MH33corr'] #MH35 is the first tone-loom animal
df_L_NO = pd.DataFrame(df_L_NO)
df_L_NO.columns = ['MH33corr']

for column in df_NOpellet:
    for animal in L:
        number = animal
        if number[2:] in column:
            print(column)
            bla = df_NOpellet[column]
            df_L_NO[column]  = bla
df_L_NO.index.name = None

'''with pellet L: all animals that took the pellet after the stimulus'''
df_L_YES = df_pellet['MH66corr'] #MH35 is the first tone-loom animal
df_L_YES = pd.DataFrame(df_L_YES)
df_L_YES.columns = ['MH66corr']

for column in df_pellet:
    for animal in L:
        number = animal
        if number[2:] in column:
            bla = df_pellet[column]
            df_L_YES[column]  = bla
df_L_YES.index.name = None

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
            

        '''No pellet TS: all animals that did not take pellet directly after stimulus all animals that took the pellet after the stimulus'''
df_TS_NO = df_NOpellet['MH39corr'] #MH35 is the first tone-loom animal
df_TS_NO = pd.DataFrame(df_TS_NO)
df_TS_NO.columns = ['MH39corr']

for column in df_NOpellet:
    for animal in TS:
        number = animal
        if number[2:] in column:
            bla = df_NOpellet[column]
            df_TS_NO[column]  = bla
df_TS_NO.index.name = None

'''with pellet TS: all animals that took the pellet after the stimulus'''
df_TS_YES = df_pellet['MH67corr'] #MH35 is the first tone-loom animal
df_TS_YES = pd.DataFrame(df_TS_YES)
df_TS_YES.columns = ['MH67corr']

for column in df_pellet:
    for animal in TS:
        number = animal
        if number[2:] in column:
            bla = df_pellet[column]
            df_TS_YES[column]  = bla
df_TS_YES.index.name = None

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


        '''No pellet T: all animals that did not take pellet directly after stimulus all animals that took the pellet after the stimulus'''
df_T_NO = df_NOpellet['MH79corr'] #MH35 is the first tone-loom animal
df_T_NO = pd.DataFrame(df_T_NO)
df_T_NO.columns = ['MH37corr']

for column in df_NOpellet:
    for animal in T:
        number = animal
        if number[2:] in column:
            bla = df_NOpellet[column]
            df_T_NO[column]  = bla
df_T_NO.index.name = None


'''with pellet T: all animals that took the pellet after the stimulus'''
df_T_YES = df_pellet['MH62corr'] #MH35 is the first tone-loom animal
df_T_YES = pd.DataFrame(df_T_YES)
df_T_YES.columns = ['MH62corr']

for column in df_pellet:
    for animal in T:
        number = animal
        if number[2:] in column:
            bla = df_pellet[column]
            df_T_YES[column]  = bla
df_T_YES.index.name = None

#%%
sns.set(font_scale = 1)
f, axes = plt.subplots(4, 2)

df_L_noshel = df_L_YES.iloc[:,:]
ax = sns.heatmap(df_L_noshel, vmax =1000, ax=axes[0,0], cbar=False)
ax.set_title('Loom')
ax.set_xticks([])
ax.set_yticks([])
#ax.set(xlabel='animal - didnot take pellet', ylabel='0 = position of stimulus')


df_L_noshel = df_L_NO.iloc[:,:]
ax = sns.heatmap(df_L_noshel, vmax =1000, ax=axes[0,1], cbar=False)
ax.set_title('Loom')
ax.set_xticks([])
#ax.set_yticks([])
#ax.set(xlabel='animal - took pellet', ylabel='0 = position of stimulus')


df_TL_noshel = df_TL_YES.iloc[:,:]
ax = sns.heatmap(df_TL_noshel, vmax =1000, ax=axes[1,0], cbar=False)
ax.set_title('Tone-Loom')
ax.set_xticks([])
ax.set_yticks([])
#ax.set(xlabel='animal - took pellet', ylabel='0 = position of stimulus')


df_TL_noshel = df_TL_NO.iloc[:,:]
ax = sns.heatmap(df_TL_noshel, vmax =1000, ax=axes[1,1], cbar=False)
ax.set_title('Tone-Loom')
ax.set_xticks([])
##ax.set(xlabel='animal - did not take pellet', ylabel='0 = position of stimulus')


df_TS_noshel = df_TS_YES.iloc[:,:]
ax = sns.heatmap(df_TS_noshel, vmax =1000, ax=axes[2,0], cbar=False)
ax.set_title('Tone-Shock')
ax.set_xticks([])
ax.set_yticks([])
#ax.set(xlabel='animal - took pellet', ylabel='0 = position of stimulus')


df_TS_noshel = df_TS_NO.iloc[:,:]
ax = sns.heatmap(df_TS_noshel, vmax =1000, ax=axes[2,1], cbar=False)
ax.set_title('Tone-Shock')
ax.set_xticks([])
#ax.set_yticks([])
#ax.set(xlabel='animal - did not take pellet', ylabel='0 = position of stimulus')

df_T_noshel = df_T_YES.iloc[:,:]
ax = sns.heatmap(df_T_noshel, vmax =1000, ax=axes[3,0], cbar=False)
ax.set_title('Tone')
ax.set_xticks([])
ax.set_yticks([])
ax.set(xlabel='took pellet')

df_T_noshel = df_T_NO.iloc[:,:]
ax = sns.heatmap(df_T_noshel, vmax =1000, ax=axes[3,1], cbar=False)
ax.set_title('Tone')
ax.set_xticks([])
#ax.set_yticks([])
ax.set(xlabel='did not take pellet')

#f.text(0.5, 0.04, 'common X', ha='center')
f.text(.04, 0.5, '0 = position of stimulus', va='center', rotation='vertical')
f.subplots_adjust(left=None, bottom=0.25, right=None, top=None, wspace=0.5, hspace=0.5)
plt.figure(figsize=(2880,1440))







