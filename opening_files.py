#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:57:40 2019

@author: mirjamheinemans
script to get the amount of time animals spend in the shelter without pellet,
after the simulus
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
    x-value33,
    MH33_in_shelter
    MH33_doorway
    MH33_with_pellet
    MH33_eat_pellet
    MH33_freeze
    MH33_reaching
    MH33_scanning
    MH33_new_pellet
"""

#%%

import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files') # to change directory Read csv files with Pandas
#%%
#df.loc[df['column_name'] == some_value]
MH33_dir = '/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files/MH033/MH33.metadata.json'
parent_dir = '/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files'


for root, dirs, files in sorted(os.walk(parent_dir)):

    for file in files:
        if 'metadata' in file:
            #print(parent_dir +'/' + file)
  
            with open(root + '/' +file) as data_file:
                print(data_file['condition'])
   #    print(name.read())
#               
           #
#               print(data[0]['name'])        
#               print(data[0]['condition'])
#           print(f.read())
#           
           #print(root, name)
#      print(os.path.join(root, name))
#   for name in dirs:
#      print(os.path.join(root, name))

#%%

                
#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
data_all = []
MH33_dir = '/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files/MH033/MH33.metadata.json'

#%%
def Metadata(MH33_dir):
    for file in sorted(os.listdir(MH33_dir)):
        #print(file)
        if 'meta' in file:            
            with open(file) as animal:
                data = json.load(animal)
                print(data)
    return(data)
#    if file_names.startswith('MH'):
#        animal = importCsv(file_names)
#        data_all.append(animal)

#%%
Metadata(MH33_dir)
#%%

for file in sorted(os.listdir(MH33_dir)):
    #print(file)
    if 'metd' in file:       
       # print(file)
        with open(file) as animal:
            print(animal.read())
#            data = json.load(animal)
#            print(data)
#    

#%%

MH33_dir = '/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files/MH033/MH33.metadata.json'

with open('/Users/mirjamheinemans/Desktop/Annotator python tryout/analysis files/MH034/MH34.metadata.json') as file:
    data = json.load(file)




     