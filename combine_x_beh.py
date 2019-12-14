#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:13:07 2019

@author: mirjamheinemans

In this script the matrix with all x-positions for all animals (df_x_pos) will be 
expanded by adding columns of ones and zeros for each behavior scored in the test.

Added columns:


Excluded animals:
MH41 - ate only 1 pellet in total training
MH45 - stimulus did not work
MH94 - got to pellet before start of experiment (opened the door by himself)
MH95 - never came out of shelter during test
MH99 - came out of shelter after >18 minutes during test
MH102 - never came out of shelter during test

"""

#%%

import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') # to change directory Read csv files with Pandas

#%%
df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/MH_all_matrix.csv',delimiter=',',index_col =[0], low_memory=False)
df_33 = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/all_animals33.csv',delimiter=',',index_col =[0], low_memory=False)
df_71 = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/all_animals71.csv',delimiter=',',index_col =[0], low_memory=False)



#%%
df_all = pd.concat([df_33, df_71], axis = 1, sort=False)
df_x_pos = df_all.filter(regex=("x.*"))

df_x_pos= df_x_pos.drop(['ID'])
df_x_pos= df_x_pos.drop(['Condition'])
df_x_pos = df_x_pos.apply(pd.to_numeric, errors='coerce')
df_x_pos = df_x_pos.reset_index(drop = True)
#%%
df_x_pos = df_x_pos.drop(['x-value41'], axis = 1)
df_x_pos = df_x_pos.drop(['x-value45'], axis = 1)
df_x_pos = df_x_pos.drop(['x-value94'], axis = 1)
df_x_pos = df_x_pos.drop(['x-value95'], axis = 1)
df_x_pos = df_x_pos.drop(['x-value99'], axis = 1)
df_x_pos = df_x_pos.drop(['x-value102'], axis = 1)

#%%
xpos = df_x_pos
#%%
'''
Here I use the MH_all list created in the other file (matrix_creation_all_animals.py)
'''


columns = []   
for i in MH_all:
    if i[0].startswith('MH'):
        name = i[0]
        xpos[name] = 0
        #print(i[0])
    else:
        start = int(i[0])
        end = int(i[1])
        xpos.loc[start:end, name] = 1
        
#%%
    ''' 141814 is the maximum number of frames in the test. I don't know why it goes until 180662 in the 
    df33 dataframe, but I am cutting the dataframe here to go until only 141814. '''

xpos = xpos.loc[:141814,:]
   
''' the first two 1's in all 'end_experiment' columns is for the stimulus... Just to keep in mind.
--> so look for the third 1 in these columns?

In principle I could also always do the stimulus + frames to look at the end.
To add stimulus frame, make extra columns again, with zeros, and then only one 1 for the start of stimulus,
from the 'stimulus_frame' file'''

#%%
stimulus = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/stimulus_frame.csv',delimiter=',', low_memory=False)        
stim = stimulus.T

#%% 
for animal in stim:
    name = str(stim.iloc[0,animal])+'_stim'
    xpos[name]=0
    event = stim.iloc[1,animal]
    xpos.loc[event,name] = 1
    
#%%

export_csv = xpos.to_csv (r'/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos.csv', header=True) #Don't forget to add '.csv' at the end of the path

