#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:54:36 2019

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

file_names = 'MH033'

dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [4,9])
stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
#%%
dataset_stim = dataset.iloc[int(stimulus):int((stimulus +180)),:] #18000 is 5 minutes
dataset_stim = dataset_stim.reset_index(drop=True)
#%%
dataset_stim.iloc[-1,0] = 1
#%%
pellet = dataset_stim.loc[dataset_stim.iloc[:,0] == 1].index.values.astype(str)[0]  
        


print(pellet)

#%%