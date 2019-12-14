#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:20:58 2019

@author: mirjamheinemans
First attempt at making a class Rat that has attributes animal, xpos, pellet, shelter
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
cond = conditions#.T

df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos.csv',delimiter=',', low_memory=False, index_col=0)        

#%%
cond.loc[:,'batch'] = 0
cond.loc[36:,'batch'] = 1
#%%

class Rat():
    def __init__(self, animal, condition, batch):
        self.animal = animal
        self.condition = condition
        self.batch = batch

#%%
      
rats = []
for rat in conditions.iterrows():
    new_rat = Rat(rat[1][0],rat[1][1],rat[1][2])
    rats.append(new_rat)


#%%
class Train(Rat):
       """Represent aspects of a car, specific to electric vehicles."""
       def __init__(self,  animal, condition, batch, xpos):
           """
           Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
           """
           super().__init__( animal, condition, batch)
           self.xpos = xpos
for rat