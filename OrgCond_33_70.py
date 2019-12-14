#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:15:32 2019

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
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/conditioning33_70')
path = os.getcwd() #short for get Current Work Directory

#%%
df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/conditioning33_70/timeline.csv',delimiter=',', low_memory=False)        
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
data_33 = importCsv('timeline.csv')

#%%

data_33[0] #this calls the first list, i.e. animal 33. 
len(data_33[0]) # this shows the number of lists in the first animal (MH33)


#%%
MH_raw=[]
info = ['freeze_end', 'stim_end', 'base_end','']
volgende = 0
for animal in range(len(data_33)):
#    print(data_33[animal])
    
    if data_33[animal][0] == 'T':
        print(data_33[animal][1])
        
        pre_number = data_33[animal][1]
        number = pre_number[-2:]
        name = ('end'+data_33[animal][1])
        behavior = ['MH'+data_33[animal][1], name]
        MH_raw.append(behavior)
        volgende+=1
    elif data_33[animal][0] == 'P':
        MH_raw.append(data_33[animal][2:4])
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
MH33 = []
for animal in df_cond:
   # print(animal)
    if '33' in animal:
        print(df_cond[animal])
        MH33.append(df_cond[animal])

cond = pd.DataFrame(MH33)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH033/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH34 = []
for animal in df_cond:
    if '34' in animal:
       MH34.append(df_cond[animal])

cond = pd.DataFrame(MH34)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH034/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH35 = []
for animal in df_cond:
    if '35' in animal:
       MH35.append(df_cond[animal])

cond = pd.DataFrame(MH35)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH035/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH36 = []
for animal in df_cond:
    if '36' in animal:
       MH36.append(df_cond[animal])

cond = pd.DataFrame(MH36)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH036/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH37 = []
for animal in df_cond:
    if '37' in animal:
       MH37.append(df_cond[animal])

cond = pd.DataFrame(MH37)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH037/conditioning.csv', header=True)


    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH38 = []
for animal in df_cond:
    if '38' in animal:
       MH38.append(df_cond[animal])

cond = pd.DataFrame(MH38)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH038/conditioning.csv', header=True)


    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH39 = []
for animal in df_cond:
    if '39' in animal:
       MH39.append(df_cond[animal])

cond = pd.DataFrame(MH39)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH039/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH40 = []
for animal in df_cond:
    if '40' in animal:
       MH40.append(df_cond[animal])

cond = pd.DataFrame(MH40)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH040/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH42 = []
for animal in df_cond:
    if '42' in animal:
       MH42.append(df_cond[animal])

cond = pd.DataFrame(MH42)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH042/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH43 = []
for animal in df_cond:
    if '43' in animal:
       MH43.append(df_cond[animal])

cond = pd.DataFrame(MH43)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH043/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH44 = []
for animal in df_cond:
    if '44' in animal:
       MH44.append(df_cond[animal])

cond = pd.DataFrame(MH44)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH044/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH46 = []
for animal in df_cond:
    if '46' in animal:
       MH46.append(df_cond[animal])

cond = pd.DataFrame(MH46)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH046/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH47 = []
for animal in df_cond:
    if '47' in animal:
       MH47.append(df_cond[animal])

cond = pd.DataFrame(MH47)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH047/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH48 = []
for animal in df_cond:
    if '48' in animal:
       MH48.append(df_cond[animal])

cond = pd.DataFrame(MH48)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH048/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH49 = []
for animal in df_cond:
    if '49' in animal:
       MH49.append(df_cond[animal])

cond = pd.DataFrame(MH49)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH049/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH50 = []
for animal in df_cond:
    if '50' in animal:
       MH50.append(df_cond[animal])

cond = pd.DataFrame(MH50)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH050/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH51 = []
for animal in df_cond:
    if '51' in animal:
       MH51.append(df_cond[animal])

cond = pd.DataFrame(MH51)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH051/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH52 = []
for animal in df_cond:
    if '52' in animal:
       MH52.append(df_cond[animal])

cond = pd.DataFrame(MH52)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH052/conditioning.csv', header=True)


    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH53 = []
for animal in df_cond:
    if '53' in animal:
       MH53.append(df_cond[animal])

cond = pd.DataFrame(MH53)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH053/conditioning.csv', header=True)


    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH54 = []
for animal in df_cond:
    if '54' in animal:
       MH54.append(df_cond[animal])

cond = pd.DataFrame(MH54)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH054/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH55 = []
for animal in df_cond:
    if '55' in animal:
       MH55.append(df_cond[animal])

cond = pd.DataFrame(MH55)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH055/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH56 = []
for animal in df_cond:
    if '56' in animal:
       MH56.append(df_cond[animal])

cond = pd.DataFrame(MH56)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH056/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH57 = []
for animal in df_cond:
    if '57' in animal:
       MH57.append(df_cond[animal])

cond = pd.DataFrame(MH57)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH057/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH58 = []
for animal in df_cond:
    if '58' in animal:
       MH58.append(df_cond[animal])

cond = pd.DataFrame(MH58)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH058/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH59 = []
for animal in df_cond:
    if '59' in animal:
       MH59.append(df_cond[animal])

cond = pd.DataFrame(MH59)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH059/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH60 = []
for animal in df_cond:
    if '60' in animal:
       MH60.append(df_cond[animal])

cond = pd.DataFrame(MH60)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH060/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH61 = []
for animal in df_cond:
    if '61' in animal:
       MH61.append(df_cond[animal])

cond = pd.DataFrame(MH61)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH061/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH62 = []
for animal in df_cond:
    if '62' in animal:
       MH62.append(df_cond[animal])

cond = pd.DataFrame(MH62)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH062/conditioning.csv', header=True)


    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH63 = []
for animal in df_cond:
    if '63' in animal:
       MH63.append(df_cond[animal])

cond = pd.DataFrame(MH63)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH063/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH64 = []
for animal in df_cond:
    if '64' in animal:
       MH64.append(df_cond[animal])

cond = pd.DataFrame(MH64)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH064/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH65 = []
for animal in df_cond:
    if '65' in animal:
       MH65.append(df_cond[animal])

cond = pd.DataFrame(MH65)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH065/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH66 = []
for animal in df_cond:
    if '66' in animal:
       MH66.append(df_cond[animal])

cond = pd.DataFrame(MH66)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH066/conditioning.csv', header=True)

    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH67 = []
for animal in df_cond:
    if '67' in animal:
       MH67.append(df_cond[animal])

cond = pd.DataFrame(MH67)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH067/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH68 = []
for animal in df_cond:
    if '68' in animal:
       MH68.append(df_cond[animal])

cond = pd.DataFrame(MH68)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH068/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH69 = []
for animal in df_cond:
    if '69' in animal:
       MH69.append(df_cond[animal])

cond = pd.DataFrame(MH69)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH069/conditioning.csv', header=True)


#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH70 = []
for animal in df_cond:
    if '70' in animal:
       MH70.append(df_cond[animal])

cond = pd.DataFrame(MH70)
cond = cond.T

export_csv = cond.to_csv (path+'/analysis files/MH070/conditioning.csv', header=True)

