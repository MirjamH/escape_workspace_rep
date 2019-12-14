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
#df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/MH_training_all_matrix.csv',delimiter=',',index_col =[0], low_memory=False)
xpos = pd.read_csv('/Users/mirjamheinemans/Desktop/escape analysis/all_animals_training.csv',delimiter=',', low_memory=False, index_col=0)        

#%%
'''
Here I use the MH_all LIST created in the other file (matrix_creation_all_animals.py)....
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

export_csv = xpos.to_csv (r'/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos_train.csv', header=True) #Don't forget to add '.csv' at the end of the path

