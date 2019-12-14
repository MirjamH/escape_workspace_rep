#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:15:18 2019

@author: mirjamheinemans

This file makes a DataFrame with all the bouts of different behaviors per animal (in total 64 animals).


Excluded animals:
MH41 - ate only 1 pellet in total training
MH45 - stimulus did not work
MH94 - got to pellet before start of experiment (opened the door by himself)
MH95 - never came out of shelter during test
MH99 - came out of shelter after >18 minutes during test
MH102 - never came out of shelter during test

The structure is like this: 
    

"""

#%%
import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/training2') # to change directory Read csv files with Pandas
path_name = os.getcwd() # this is a string
file_names = sorted(os.listdir(path_name)) # this is a list

def importCsv(file):
    dataset = []
    x = 0
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in data:
            if row:
                dataset.append(row)
                x += 1
    return(dataset)



#%%
df_x = pd.read_csv('/Users/mirjamheinemans/Desktop/escape analysis/all_animals_training.csv',delimiter=',', low_memory=False, index_col=0)        

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
data_all = []

for file_names in sorted(os.listdir(path_name)):
    if file_names.startswith('MH'):
        animal = importCsv(file_names)
        data_all.append(animal)
#%%

data_all[0] #this calls the first list, i.e. animal 33. 
len(data_all[0]) # this shows the number of lists in the first animal (MH33)
#%%
MH_raw=[]
info = ['shelter_end', 'doorway_end', 'with_pellet_end', 'eat_pellet_end', 'freeze_end', 'reaching_end', 'scanning_end', 'new_pellet_end','', '']
volgende = 0
for animal in range(len(data_all)):
    for i in range(len(data_all[animal])):
        #print(data_all[animal][i])
        #print(i)
        if data_all[animal][i][0] == 'T':
            pre_number = data_all[animal][i][1]
            number = pre_number[2:5]
            name = (info[volgende] + number)
            behavior = [data_all[animal][i][1], name]
            MH_raw.append(behavior)
            volgende+=1
        elif data_all[animal][i][0] == 'P':
            MH_raw.append(data_all[animal][i][2:4])
    volgende = 0
#print(MH_raw)

MH_all = [x for x in MH_raw if x != ['','']]

#%%
df_all =pd.DataFrame(MH_all)
MH_all_matrix = pd.DataFrame(np.full([70,1021],np.nan))


column = 0
row = 1
for i in range(len(df_all)):
    
    if df_all.loc[i,0].startswith("MH"):
        MH_all_matrix.loc[0,column]= df_all.loc[i,0]
        MH_all_matrix.loc[0,(column+1)]= df_all.loc[i,1]
        column +=2
        row = 1
    else:
        MH_all_matrix.loc[row,column-2]= df_all.loc[i,0]
        MH_all_matrix.loc[row,(column-1)]= df_all.loc[i,1]
        row +=1
        #print(MH33_matrix.loc[row,column])

MH_all_matrix.columns = MH_all_matrix.iloc[0]
MH_all_matrix= MH_all_matrix.drop([0])
MH_all_matrix = MH_all_matrix.apply(pd.to_numeric, errors='coerce')
MH_all_matrix = MH_all_matrix.reset_index(drop='True')
#%%

export_csv = MH_all_matrix.to_csv (r'/Users/mirjamheinemans/Desktop/Annotator python tryout/MH_training_all_matrix.csv', header=True) #Don't forget to add '.csv' at the end of the path
