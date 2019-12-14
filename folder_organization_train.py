#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:08:01 2019

@author: mirjamheinemans
making the folders for analysis
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
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

#%%
df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos_train.csv',delimiter=',', low_memory=False, index_col=0)        

#%%
MH33 = []
for animal in df_beh:
    if '33' in animal:
       MH33.append(df_beh[animal])

test = pd.DataFrame(MH33)
test = test.T
test = test.loc[:(42841-60),:]

export_csv = test.to_csv (path+'/analysis files/MH033/training.csv', header=True)
print(test.head())

#%%

os.chdir(path+'/analysis files/MH033')
metadata = {'name': 'MH33',
            'condition': 'Loom', 
            'batch': 0}
with open('MH33.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH34 = []
for animal in df_beh:
    if '34' in animal:
       MH34.append(df_beh[animal])

test = pd.DataFrame(MH34)
test = test.T
test = test.loc[:(35855-60),:]

export_csv = test.to_csv (path+'/analysis files/MH034/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH034')
metadata = {'name': 'MH34',
             'condition': 'Loom',
             'batch': 0}
with open('MH34.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH35 = []
for animal in df_beh:
    if '35' in animal:
       MH35.append(df_beh[animal])

test = pd.DataFrame(MH35)
test = test.T
test = test.loc[:(39440-60),:]

export_csv = test.to_csv (path+'/analysis files/MH035/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH035')
metadata = {'name': 'MH35',
            'condition': 'T_Loom',
            'batch': 0}
with open('MH35.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH36 = []
for animal in df_beh:
    if '36' in animal:
       MH36.append(df_beh[animal])

test = pd.DataFrame(MH36)
test = test.T
test = test.loc[:(29806-60),:]

export_csv = test.to_csv (path+'/analysis files/MH036/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH036')
metadata = {'name': 'MH36',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH35.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH37 = []
for animal in df_beh:
    if '37' in animal:
       MH37.append(df_beh[animal])

test = pd.DataFrame(MH37)
test = test.T
test = test.loc[:(30455-60),:]

export_csv = test.to_csv (path+'/analysis files/MH037/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH037')
metadata = {'name': 'MH37',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH37.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH38 = []
for animal in df_beh:
    if '38' in animal:
       MH38.append(df_beh[animal])

test = pd.DataFrame(MH38)
test = test.T
test = test.loc[:(18429-60),:]

export_csv = test.to_csv (path+'/analysis files/MH038/training.csv', header=True)

#%%

os.chdir(path+'/analysis files/MH038')
metadata = {'name': 'MH38',
            'condition': 'Tone',
            'batch': 0}
with open('MH38.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH39 = []
for animal in df_beh:
    if '39' in animal:
       MH39.append(df_beh[animal])

test = pd.DataFrame(MH39)
test = test.T
test = test.loc[:(63621-60),:]

export_csv = test.to_csv (path+'/analysis files/MH039/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH039')
metadata = {'name': 'MH39',
            'condition': 'T_Shock',
            'batch': 0}
with open('MH39.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH40 = []
for animal in df_beh:
    if '40' in animal:
       MH40.append(df_beh[animal])

test = pd.DataFrame(MH40)
test = test.T
test = test.loc[:(20411-60),:]

export_csv = test.to_csv (path+'/analysis files/MH040/training.csv', header=True)

#%%

os.chdir(path+'/analysis files/MH040')
metadata = {'name': 'MH40',
            'condition': 'T_Shock',
            'batch': 0}
with open('MH40.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH42 = []
for animal in df_beh:
    if '42' in animal:
       MH42.append(df_beh[animal])

test = pd.DataFrame(MH42)
test = test.T
test = test.loc[:(23836-60),:]

export_csv = test.to_csv (path+'/analysis files/MH042/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH042')
metadata = {'name': 'MH42',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH42.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH43 = []
for animal in df_beh:
    if '43' in animal:
       MH43.append(df_beh[animal])

test = pd.DataFrame(MH43)
test = test.T
test = test.loc[:56263,:]

export_csv = test.to_csv (path+'/analysis files/MH043/training.csv', header=True)

#%%

os.chdir(path+'/analysis files/MH043')
metadata = {'name': 'MH43',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH43.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH44 = []
for animal in df_beh:
    if '44' in animal:
       MH44.append(df_beh[animal])

test = pd.DataFrame(MH44)
test = test.T
test = test.loc[:58538,:]

export_csv = test.to_csv (path+'/analysis files/MH044/training.csv', header=True)

#%%

os.chdir(path+'/analysis files/MH044')
metadata = {'name': 'MH44',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH44.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH46 = []
for animal in df_beh:
    if '46' in animal:
       MH46.append(df_beh[animal])

test = pd.DataFrame(MH46)
test = test.T
test = test.loc[:62795,:]

export_csv = test.to_csv (path+'/analysis files/MH046/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH046')
metadata = {'name': 'MH46',
                        'condition': 'Loom',
                        'batch': 0}
with open('MH46.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH47 = []
for animal in df_beh:
    if '47' in animal:
       MH47.append(df_beh[animal])

test = pd.DataFrame(MH47)
test = test.T
test = test.loc[:174374,:]

export_csv = test.to_csv (path+'/analysis files/MH047/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH047')
metadata = {'name': 'MH47',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH47.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH48 = []
for animal in df_beh:
    if '48' in animal:
       MH48.append(df_beh[animal])

test = pd.DataFrame(MH48)
test = test.T
test = test.loc[:(25325-60),:]

export_csv = test.to_csv (path+'/analysis files/MH048/training.csv', header=True)

#%%

os.chdir(path+'/analysis files/MH048')
metadata = {'name': 'MH48',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH48.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH49 = []
for animal in df_beh:
    if '49' in animal:
       MH49.append(df_beh[animal])

test = pd.DataFrame(MH49)
test = test.T
test = test.loc[:(57426-60),:]

export_csv = test.to_csv (path+'/analysis files/MH049/training.csv', header=True)

#%%

os.chdir(path+'/analysis files/MH049')
metadata = {'name': 'MH49',
                        'condition': 'T_Shock',
                        'batch': 0}
with open('MH49.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH50 = []
for animal in df_beh:
    if '50' in animal:
       MH50.append(df_beh[animal])

test = pd.DataFrame(MH50)
test = test.T
test = test.loc[:(46850-60),:]

export_csv = test.to_csv (path+'/analysis files/MH050/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH050')
metadata = {'name': 'MH50',
                        'condition': 'T_Shock',
                        'batch': 0}
with open('MH50.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH51 = []
for animal in df_beh:
    if '51' in animal:
       MH51.append(df_beh[animal])

test = pd.DataFrame(MH51)
test = test.T
test = test.loc[:(79509-60),:]

export_csv = test.to_csv (path+'/analysis files/MH051/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH051')
metadata = {'name': 'MH51',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH51.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH52 = []
for animal in df_beh:
    if '52' in animal:
       MH52.append(df_beh[animal])

test = pd.DataFrame(MH52)
test = test.T
test = test.loc[:(61320-60),:]

export_csv = test.to_csv (path+'/analysis files/MH052/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH052')
metadata = {'name': 'MH52',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH52.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH53 = []
for animal in df_beh:
    if '53' in animal:
       MH53.append(df_beh[animal])

test = pd.DataFrame(MH53)
test = test.T
test = test.loc[:(169302-60),:]

export_csv = test.to_csv (path+'/analysis files/MH053/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH053')
metadata = {'name': 'MH53',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH53.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH54 = []
for animal in df_beh:
    if '54' in animal:
       MH54.append(df_beh[animal])

test = pd.DataFrame(MH54)
test = test.T
test = test.loc[:(41460-60),:]

export_csv = test.to_csv (path+'/analysis files/MH054/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH054')
metadata = {'name': 'MH54',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH54.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH55 = []
for animal in df_beh:
    if '55' in animal:
       MH55.append(df_beh[animal])

test = pd.DataFrame(MH55)
test = test.T
test = test.loc[:(41098-60),:]

export_csv = test.to_csv (path+'/analysis files/MH055/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH055')
metadata = {'name': 'MH55',
                        'condition': 'T_Shock',
                        'batch': 0}
with open('MH55.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH56 = []
for animal in df_beh:
    if '56' in animal:
       MH56.append(df_beh[animal])

test = pd.DataFrame(MH56)
test = test.T
test = test.loc[:(93002-60),:]

export_csv = test.to_csv (path+'/analysis files/MH056/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH056')
metadata = {'name': 'MH56',
                        'condition': 'T_Shock',
                        'batch': 0}
with open('MH56.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH57 = []
for animal in df_beh:
    if '57' in animal:
       MH57.append(df_beh[animal])

test = pd.DataFrame(MH57)
test = test.T
test = test.loc[:(167531-60),:]

export_csv = test.to_csv (path+'/analysis files/MH057/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH057')
metadata = {'name': 'MH57',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH57.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH58 = []
for animal in df_beh:
    if '58' in animal:
       MH58.append(df_beh[animal])

test = pd.DataFrame(MH58)
test = test.T
test = test.loc[:(38487-60),:]

export_csv = test.to_csv (path+'/analysis files/MH058/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH058')
metadata = {'name': 'MH58',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH58.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH59 = []
for animal in df_beh:
    if '59' in animal:
       MH59.append(df_beh[animal])

test = pd.DataFrame(MH59)
test = test.T
test = test.loc[:(64226-60),:]

export_csv = test.to_csv (path+'/analysis files/MH059/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH059')
metadata = {'name': 'MH59',
                        'condition': 'Loom',
                        'batch': 0}
with open('MH59.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH60 = []
for animal in df_beh:
    if '60' in animal:
       MH60.append(df_beh[animal])

test = pd.DataFrame(MH60)
test = test.T
test = test.loc[:(168545-60),:]

export_csv = test.to_csv (path+'/analysis files/MH060/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH060')
metadata = {'name': 'MH60',
                        'condition': 'Loom',
                        'batch': 0}
with open('MH60.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH61 = []
for animal in df_beh:
    if '61' in animal:
       MH61.append(df_beh[animal])

test = pd.DataFrame(MH61)
test = test.T
test = test.loc[:(168773-60),:]

export_csv = test.to_csv (path+'/analysis files/MH061/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH061')
metadata = {'name': 'MH61',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH61.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH62 = []
for animal in df_beh:
    if '62' in animal:
       MH62.append(df_beh[animal])

test = pd.DataFrame(MH62)
test = test.T
test = test.loc[:(25210-60),:]

export_csv = test.to_csv (path+'/analysis files/MH062/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH062')
metadata = {'name': 'MH62',
                        'condition': 'Tone',
                        'batch': 0}
with open('MH62.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH63 = []
for animal in df_beh:
    if '63' in animal:
       MH63.append(df_beh[animal])

test = pd.DataFrame(MH63)
test = test.T
test = test.loc[:(61031-60),:]

export_csv = test.to_csv (path+'/analysis files/MH063/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH063')
metadata = {'name': 'MH63',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH63.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH64 = []
for animal in df_beh:
    if '64' in animal:
       MH64.append(df_beh[animal])

test = pd.DataFrame(MH64)
test = test.T
test = test.loc[:(21601-60),:]

export_csv = test.to_csv (path+'/analysis files/MH064/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH064')
metadata = {'name': 'MH64',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH64.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH65 = []
for animal in df_beh:
    if '65' in animal:
       MH65.append(df_beh[animal])

test = pd.DataFrame(MH65)
test = test.T
test = test.loc[:(154160-60),:]

export_csv = test.to_csv (path+'/analysis files/MH065/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH065')
metadata = {'name': 'MH65',
                        'condition': 'Loom',
                        'batch': 0}
with open('MH65.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH66 = []
for animal in df_beh:
    if '66' in animal:
       MH66.append(df_beh[animal])

test = pd.DataFrame(MH66)
test = test.T
test = test.loc[:(32860-60),:]

export_csv = test.to_csv (path+'/analysis files/MH066/training.csv', header=True)

#%%

os.chdir(path+'/analysis files/MH066')
metadata = {'name': 'MH66',
                        'condition': 'Loom',
                        'batch': 0}
with open('MH66.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH67 = []
for animal in df_beh:
    if '67' in animal:
       MH67.append(df_beh[animal])

test = pd.DataFrame(MH67)
test = test.T
test = test.loc[:(62047-60),:]

export_csv = test.to_csv (path+'/analysis files/MH067/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH067')
metadata = {'name': 'MH67',
                        'condition': 'T_Shock',
                        'batch': 0}
with open('MH67.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH68 = []
for animal in df_beh:
    if '68' in animal:
       MH68.append(df_beh[animal])

test = pd.DataFrame(MH68)
test = test.T
test = test.loc[:(31181-60),:]

export_csv = test.to_csv (path+'/analysis files/MH068/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH068')
metadata = {'name': 'MH68',
                        'condition': 'T_Shock',
                        'batch': 0}
with open('MH68.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH69 = []
for animal in df_beh:
    if '69' in animal:
       MH69.append(df_beh[animal])

test = pd.DataFrame(MH69)
test = test.T
test = test.loc[:(123127-60),:]

export_csv = test.to_csv (path+'/analysis files/MH069/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH069')
metadata = {'name': 'MH69',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH69.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH70 = []
for animal in df_beh:
    if '70' in animal:
       MH70.append(df_beh[animal])

test = pd.DataFrame(MH70)
test = test.T
test = test.loc[:(31915-60),:]

export_csv = test.to_csv (path+'/analysis files/MH070/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH070')
metadata = {'name': 'MH70',
                        'condition': 'T_Loom',
                        'batch': 0}
with open('MH70.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH71 = []
for animal in df_beh:
    if '71' in animal:
       MH71.append(df_beh[animal])

test = pd.DataFrame(MH71)
test = test.T
test = test.loc[:(38587-60),:]

export_csv = test.to_csv (path+'/analysis files/MH071/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH071')
metadata = {'name': 'MH71',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH71.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH72 = []
for animal in df_beh:
    if '72' in animal:
       MH72.append(df_beh[animal])

test = pd.DataFrame(MH72)
test = test.T
test = test.loc[:(20389-60),:]

export_csv = test.to_csv (path+'/analysis files/MH072/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH072')
metadata = {'name': 'MH72',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH71.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH73 = []
for animal in df_beh:
    if '73' in animal:
       MH73.append(df_beh[animal])

test = pd.DataFrame(MH73)
test = test.T
test = test.loc[:(44707-60),:]

export_csv = test.to_csv (path+'/analysis files/MH073/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH073')
metadata = {'name': 'MH73',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH73.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH74 = []
for animal in df_beh:
    if '74' in animal:
       MH74.append(df_beh[animal])

test = pd.DataFrame(MH74)
test = test.T
test = test.loc[:(54668-60),:]

export_csv = test.to_csv (path+'/analysis files/MH074/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH074')
metadata = {'name': 'MH74',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH74.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH75 = []
for animal in df_beh:
    if '75' in animal:
       MH75.append(df_beh[animal])

test = pd.DataFrame(MH75)
test = test.T
test = test.loc[:(30934-60),:]

export_csv = test.to_csv (path+'/analysis files/MH075/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH075')
metadata = {'name': 'MH75',
                        'condition': 'Tone',
                        'batch': 1}
with open('MH75.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH76 = []
for animal in df_beh:
    if '76' in animal:
       MH76.append(df_beh[animal])

test = pd.DataFrame(MH76)
test = test.T
test = test.loc[:(17284-60),:]

export_csv = test.to_csv (path+'/analysis files/MH076/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH076')
metadata = {'name': 'MH76',
                        'condition': 'Tone',
                        'batch': 1}
with open('MH76.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH77 = []
for animal in df_beh:
    if '77' in animal:
       MH77.append(df_beh[animal])

test = pd.DataFrame(MH77)
test = test.T
test = test.loc[:(20622-60),:]

export_csv = test.to_csv (path+'/analysis files/MH077/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH077')
metadata = {'name': 'MH77',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH77.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH78 = []
for animal in df_beh:
    if '78' in animal:
       MH78.append(df_beh[animal])

test = pd.DataFrame(MH78)
test = test.T
test = test.loc[:(57596-60),:]

export_csv = test.to_csv (path+'/analysis files/MH078/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH078')
metadata = {'name': 'MH78',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH78.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH79 = []
for animal in df_beh:
    if '79' in animal:
       MH79.append(df_beh[animal])

test = pd.DataFrame(MH79)
test = test.T
test = test.loc[:(43771-60),:]

export_csv = test.to_csv (path+'/analysis files/MH079/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH079')
metadata = {'name': 'MH79',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH79.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH80 = []
for animal in df_beh:
    if '80' in animal:
       MH80.append(df_beh[animal])

test = pd.DataFrame(MH80)
test = test.T
test = test.loc[:(63538-60),:]

export_csv = test.to_csv (path+'/analysis files/MH080/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH080')
metadata = {'name': 'MH80',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH80.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH81 = []
for animal in df_beh:
    if '81' in animal:
       MH81.append(df_beh[animal])

test = pd.DataFrame(MH81)
test = test.T
test = test.loc[:(34597-60),:]

export_csv = test.to_csv (path+'/analysis files/MH081/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH081')
metadata = {'name': 'MH81',
                        'condition': 'Tone',
                        'batch': 1}
with open('MH81.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH82 = []
for animal in df_beh:
    if '82' in animal:
       MH82.append(df_beh[animal])

test = pd.DataFrame(MH82)
test = test.T
test = test.loc[:(32166-60),:]

export_csv = test.to_csv (path+'/analysis files/MH082/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH082')
metadata = {'name': 'MH82',
                        'condition': 'Tone',
                        'batch': 1}
with open('MH82.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH83 = []
for animal in df_beh:
    if '83' in animal:
       MH83.append(df_beh[animal])

test = pd.DataFrame(MH83)
test = test.T
test = test.loc[:(108094-60),:]

export_csv = test.to_csv (path+'/analysis files/MH083/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH083')
metadata = {'name': 'MH83',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH83.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH84 = []
for animal in df_beh:
    if '84' in animal:
       MH84.append(df_beh[animal])

test = pd.DataFrame(MH84)
test = test.T
test = test.loc[:(38425-60),:]

export_csv = test.to_csv (path+'/analysis files/MH084/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH084')
metadata = {'name': 'MH84',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH84.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH85 = []
for animal in df_beh:
    if '85' in animal:
       MH85.append(df_beh[animal])

test = pd.DataFrame(MH85)
test = test.T
test = test.loc[:(28571-60),:]

export_csv = test.to_csv (path+'/analysis files/MH085/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH085')
metadata = {'name': 'MH85',
                        'condition': 'Loom',
                        'batch': 1}
with open('MH85.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH86 = []
for animal in df_beh:
    if '86' in animal:
       MH86.append(df_beh[animal])

test = pd.DataFrame(MH86)
test = test.T
test = test.loc[:(34057-60),:]

export_csv = test.to_csv (path+'/analysis files/MH086/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH086')
metadata = {'name': 'MH86',
                        'condition': 'Loom',
                        'batch': 1}
with open('MH86.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH87 = []
for animal in df_beh:
    if '87' in animal:
       MH87.append(df_beh[animal])

test = pd.DataFrame(MH87)
test = test.T
test = test.loc[:(85779-60),:]

export_csv = test.to_csv (path+'/analysis files/MH087/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH087')
metadata = {'name': 'MH87',
                        'condition': 'Loom',
                        'batch': 1}
with open('MH87.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH88 = []
for animal in df_beh:
    if '88' in animal:
       MH88.append(df_beh[animal])

test = pd.DataFrame(MH88)
test = test.T
test = test.loc[:(83318-60),:]

export_csv = test.to_csv (path+'/analysis files/MH088/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH088')
metadata = {'name': 'MH88',
                        'condition': 'Loom',
                        'batch': 1}
with open('MH88.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH89 = []
for animal in df_beh:
    if '89' in animal:
        MH89.append(df_beh[animal])

test = pd.DataFrame(MH89)
test = test.T
test = test.loc[:(110140-60),:]

export_csv = test.to_csv (path+'/analysis files/MH089/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH089')
metadata = {'name': 'MH89',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH89.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH90 = []
for animal in df_beh:
    if '90' in animal:
        MH90.append(df_beh[animal])

test = pd.DataFrame(MH90)
test = test.T
test = test.loc[:(78856-60),:]

export_csv = test.to_csv (path+'/analysis files/MH090/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH090')
metadata = {'name': 'MH90',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH90.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH91 = []
for animal in df_beh:
    if '91' in animal:
        MH91.append(df_beh[animal])

test = pd.DataFrame(MH91)
test = test.T
test = test.loc[:(112580-60),:]

export_csv = test.to_csv (path+'/analysis files/MH091/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH091')
metadata = {'name': 'MH91',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH91.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH92 = []
for animal in df_beh:
    if '92' in animal:
        MH92.append(df_beh[animal])

test = pd.DataFrame(MH92)
test = test.T
test = test.loc[:(15164-60),:]

export_csv = test.to_csv (path+'/analysis files/MH092/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH092')
metadata = {'name': 'MH92',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH92.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)

#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH93 = []
for animal in df_beh:
    if '93' in animal:
        MH93.append(df_beh[animal])

test = pd.DataFrame(MH93)
test = test.T
test = test.loc[:(25646-60),:]

export_csv = test.to_csv (path+'/analysis files/MH093/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH093')
metadata = {'name': 'MH93',
                        'condition': 'Tone',
                        'batch': 1}
with open('MH93.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH96 = []
for animal in df_beh:
    if '96' in animal:
        MH96.append(df_beh[animal])

test = pd.DataFrame(MH96)
test = test.T
test = test.loc[:(31693-60),:]

export_csv = test.to_csv (path+'/analysis files/MH096/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH096')
metadata = {'name': 'MH96',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH96.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH97 = []
for animal in df_beh:
    if '97' in animal:
        MH97.append(df_beh[animal])

test = pd.DataFrame(MH97)
test = test.T
test = test.loc[:(108752-60),:]

export_csv = test.to_csv (path+'/analysis files/MH097/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH097')
metadata = {'name': 'MH97',
                        'condition': 'Tone',
                        'batch': 1}
with open('MH97.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH98 = []
for animal in df_beh:
    if '98' in animal:
        MH98.append(df_beh[animal])

test = pd.DataFrame(MH98)
test = test.T
test = test.loc[:(58740-60),:]

export_csv = test.to_csv (path+'/analysis files/MH098/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH098')
metadata = {'name': 'MH98',
                        'condition': 'Tone',
                        'batch': 1}
with open('MH98.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH100 = []
for animal in df_beh:
    if '100' in animal:
        MH100.append(df_beh[animal])

test = pd.DataFrame(MH100)
test = test.T
test = test.loc[:(109223-60),:]

export_csv = test.to_csv (path+'/analysis files/MH100/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH100')
metadata = {'name': 'MH100',
                        'condition': 'T_Shock',
                        'batch': 1}
with open('MH100.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    
#%%
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout/')
path = os.getcwd() #short for get Current Work Directory

MH101 = []
for animal in df_beh:
    if '101' in animal:
        MH101.append(df_beh[animal])

test = pd.DataFrame(MH101)
test = test.T
test = test.loc[:(57423-60),:]

export_csv = test.to_csv (path+'/analysis files/MH101/training.csv', header=True)

#%%
os.chdir(path+'/analysis files/MH101')
metadata = {'name': 'MH101',
                        'condition': 'T_Loom',
                        'batch': 1}
with open('MH101.metadata.json', 'w') as outfile:
    json.dump(metadata, outfile)
    