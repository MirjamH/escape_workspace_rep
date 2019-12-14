#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:26:41 2019

@author: mirjamheinemans
"""
#%%
import json
import csv 
import numpy as np
import matplotlib as plt
import seaborn as sns
import scipy.stats as ss
import os, glob # Operating System
import pandas as pd
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/conditioning71_102')
path = os.getcwd() #short for get Current Work Directory

#%%

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
data_71 = importCsv('/Users/mirjamheinemans/Desktop/Annotator python tryout/conditioning71_102/conditioning_71.csv')

#%%

data_71[0] #this calls the first list, i.e. animal 33. 
len(data_71[0]) # this shows the number of lists in the first animal (MH33)


#%%
MH_raw=[]
info = ['freeze_end', 'stim_end', 'base_end','']
volgende = 0
for animal in range(len(data_71)):
#    print(data_33[animal])
    
    if data_71[animal][0] == 'T':
        print(data_71[animal][1])
        
        pre_number = data_71[animal][1]
        number = pre_number[-2:]
        name = ('end'+data_71[animal][1])
        behavior = ['MH'+data_71[animal][1], name]
        MH_raw.append(behavior)
        volgende+=1
    elif data_71[animal][0] == 'P':
        MH_raw.append(data_71[animal][2:4])
        volgende = 0
    #print(name)
#print(MH_raw)

MH_all = [x for x in MH_raw if x != ['MH','end']]
#%%
df_cond = pd.DataFrame(index = range(60000))


columns = []   
for i in MH_all:
    if i[0].startswith('MH'):
        name = i[0]
        df_cond[name] = 0
        #print(i[0])
    else:
        start = int(i[0])
        end = int(i[1])
        df_cond.loc[start:end, name] = 1



#%%
df_cond = df_cond[df_cond.columns[::-1]]



#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH71 = []
for animal in df_cond:
    if '71' in animal:
       MH71.append(df_cond[animal])

conditioning = pd.DataFrame(MH71)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH071/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH72 = []
for animal in df_cond:
    if '72' in animal:
       MH72.append(df_cond[animal])

conditioning = pd.DataFrame(MH72)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH072/conditioning.csv', header=True)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH73 = []
for animal in df_cond:
    if '73' in animal:
       MH73.append(df_cond[animal])

conditioning = pd.DataFrame(MH73)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH073/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH74 = []
for animal in df_cond:
    if '74' in animal:
       MH74.append(df_cond[animal])

conditioning = pd.DataFrame(MH74)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH074/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH75 = []
for animal in df_cond:
    if '75' in animal:
       MH75.append(df_cond[animal])

conditioning = pd.DataFrame(MH75)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH075/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH76 = []
for animal in df_cond:
    if '76' in animal:
       MH76.append(df_cond[animal])

conditioning = pd.DataFrame(MH76)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH076/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH77 = []
for animal in df_cond:
    if '77' in animal:
       MH77.append(df_cond[animal])

conditioning = pd.DataFrame(MH77)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH077/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH78 = []
for animal in df_cond:
    if '78' in animal:
       MH78.append(df_cond[animal])

conditioning = pd.DataFrame(MH78)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH078/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH79 = []
for animal in df_cond:
    if '79' in animal:
       MH79.append(df_cond[animal])

conditioning = pd.DataFrame(MH79)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH079/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH80 = []
for animal in df_cond:
    if '80' in animal:
       MH80.append(df_cond[animal])

conditioning = pd.DataFrame(MH80)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH080/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH81 = []
for animal in df_cond:
    if '81' in animal:
       MH81.append(df_cond[animal])

conditioning = pd.DataFrame(MH81)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH081/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH82 = []
for animal in df_cond:
    if '82' in animal:
       MH82.append(df_cond[animal])

conditioning = pd.DataFrame(MH82)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH082/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH83 = []
for animal in df_cond:
    if '83' in animal:
       MH83.append(df_cond[animal])

conditioning = pd.DataFrame(MH83)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH083/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH84 = []
for animal in df_cond:
    if '84' in animal:
       MH84.append(df_cond[animal])

conditioning = pd.DataFrame(MH84)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH084/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH85 = []
for animal in df_cond:
    if '85' in animal:
       MH85.append(df_cond[animal])

conditioning = pd.DataFrame(MH85)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH085/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH86 = []
for animal in df_cond:
    if '86' in animal:
       MH86.append(df_cond[animal])

conditioning = pd.DataFrame(MH86)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH086/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH87 = []
for animal in df_cond:
    if '87' in animal:
       MH87.append(df_cond[animal])

conditioning = pd.DataFrame(MH87)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH087/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH88 = []
for animal in df_cond:
    if '88' in animal:
       MH88.append(df_cond[animal])

conditioning = pd.DataFrame(MH88)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH088/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH89 = []
for animal in df_cond:
    if '89' in animal:
        MH89.append(df_cond[animal])

conditioning = pd.DataFrame(MH89)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH089/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH90 = []
for animal in df_cond:
    if '90' in animal:
        MH90.append(df_cond[animal])

conditioning = pd.DataFrame(MH90)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH090/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH91 = []
for animal in df_cond:
    if '91' in animal:
        MH91.append(df_cond[animal])

conditioning = pd.DataFrame(MH91)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH091/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH92 = []
for animal in df_cond:
    if '92' in animal:
        MH92.append(df_cond[animal])

conditioning = pd.DataFrame(MH92)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH092/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH93 = []
for animal in df_cond:
    if '93' in animal:
        MH93.append(df_cond[animal])

conditioning = pd.DataFrame(MH93)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH093/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH96 = []
for animal in df_cond:
    if '96' in animal:
        MH96.append(df_cond[animal])

conditioning = pd.DataFrame(MH96)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH096/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH97 = []
for animal in df_cond:
    if '97' in animal:
        MH97.append(df_cond[animal])

conditioning = pd.DataFrame(MH97)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH097/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH98 = []
for animal in df_cond:
    if '98' in animal:
        MH98.append(df_cond[animal])

conditioning = pd.DataFrame(MH98)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH098/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH100 = []
for animal in df_cond:
    if '100' in animal:
        MH100.append(df_cond[animal])

conditioning = pd.DataFrame(MH100)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH100/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH101 = []
for animal in df_cond:
    if '101' in animal:
        MH101.append(df_cond[animal])

conditioning = pd.DataFrame(MH101)
conditioning = conditioning.T

export_csv = conditioning.to_csv (path+'/analysis files/MH101/conditioning.csv', header=True)