#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:08:01 2019

@author: mirjamheinemans
making the folders for analysis, test files
"""

#%%
import csv 
import numpy as np
import matplotlib as plt
import seaborn as sns
import scipy.stats as ss
import os, glob # Operating System
import pandas as pd

os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') # to change directory Read csv files with Pandas

path = os.getcwd() #short for get Current Work Directory

#%%
df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos.csv',delimiter=',', low_memory=False, index_col=0)        

#%%
MH33 = []
for animal in df_beh:
    if '33' in animal:
       MH33.append(df_beh[animal])

test = pd.DataFrame(MH33)
test = test.T
test = test.loc[:63553,:]
test = test.drop(columns=['MH33_end_experiment'])

export_csv = test.to_csv (path+'/analysis files/MH33/test.csv', header=True)
print(test.head())
#%%
MH34 = []
for animal in df_beh:
    if '34' in animal:
       MH34.append(df_beh[animal])

test = pd.DataFrame(MH34)
test = test.T
test = test.loc[:61787,:]
test = test.drop(columns=['MH34_end_experiment'])
export_csv = test.to_csv (path+'/analysis files/MH34/test.csv', header=True)

#%%
MH35 = []
for animal in df_beh:
    if '35' in animal:
       MH35.append(df_beh[animal])

test = pd.DataFrame(MH35)
test = test.T
test = test.loc[:61452,:]
test = test.drop(columns=['MH35_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH35/test.csv', header=True)

#%%
MH36 = []
for animal in df_beh:
    if '36' in animal:
       MH36.append(df_beh[animal])

test = pd.DataFrame(MH36)
test = test.T
test = test.loc[:59546,:]
test = test.drop(columns=['MH36_new_pellet'])


export_csv = test.to_csv (path+'/analysis files/MH36/test.csv', header=True)

#%%
MH37 = []
for animal in df_beh:
    if '37' in animal:
       MH37.append(df_beh[animal])

test = pd.DataFrame(MH37)
test = test.T
test = test.loc[:97692,:]
test = test.drop(columns=['MH37_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH37/test.csv', header=True)

#%%
MH38 = []
for animal in df_beh:
    if '38' in animal:
       MH38.append(df_beh[animal])

test = pd.DataFrame(MH38)
test = test.T
test = test.loc[:59427,:]
test = test.drop(columns=['MH38_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH38/test.csv', header=True)

#%%
MH39 = []
for animal in df_beh:
    if '39' in animal:
       MH39.append(df_beh[animal])

test = pd.DataFrame(MH39)
test = test.T
test = test.loc[:71158,:]
test = test.drop(columns=['MH39_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH39/test.csv', header=True)

#%%
MH40 = []
for animal in df_beh:
    if '40' in animal:
       MH40.append(df_beh[animal])

test = pd.DataFrame(MH40)
test = test.T
test = test.loc[:55627,:]
test = test.drop(columns=['MH40_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH40/test.csv', header=True)


#%%
MH42 = []
for animal in df_beh:
    if '42' in animal:
       MH42.append(df_beh[animal])

test = pd.DataFrame(MH42)
test = test.T
test = test.loc[:55699,:]
test = test.drop(columns=['MH42_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH42/test.csv', header=True)


#%%
MH43 = []
for animal in df_beh:
    if '43' in animal:
       MH43.append(df_beh[animal])

test = pd.DataFrame(MH43)
test = test.T
test = test.loc[:56263,:]
test = test.drop(columns=['MH43_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH43/test.csv', header=True)


#%%
MH44 = []
for animal in df_beh:
    if '44' in animal:
       MH44.append(df_beh[animal])

test = pd.DataFrame(MH44)
test = test.T
test = test.loc[:58538,:]
test = test.drop(columns=['MH44_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH44/test.csv', header=True)


#%%
MH46 = []
for animal in df_beh:
    if '46' in animal:
       MH46.append(df_beh[animal])

test = pd.DataFrame(MH46)
test = test.T
test = test.loc[:62795,:]
test = test.drop(columns=['MH46_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH46/test.csv', header=True)



#%%
MH47 = []
for animal in df_beh:
    if '47' in animal:
       MH47.append(df_beh[animal])

test = pd.DataFrame(MH47)
test = test.T
test = test.loc[:74374,:]
test = test.drop(columns=['MH47_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH47/test.csv', header=True)


#%%
MH48 = []
for animal in df_beh:
    if '48' in animal:
       MH48.append(df_beh[animal])

test = pd.DataFrame(MH48)
test = test.T
test = test.loc[:55855,:]
test = test.drop(columns=['MH48_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH48/test.csv', header=True)



#%%
MH49 = []
for animal in df_beh:
    if '49' in animal:
       MH49.append(df_beh[animal])

test = pd.DataFrame(MH49)
test = test.T
test = test.loc[:54679,:]
test = test.drop(columns=['MH49_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH49/test.csv', header=True)




#%%
MH50 = []
for animal in df_beh:
    if '50' in animal:
       MH50.append(df_beh[animal])

test = pd.DataFrame(MH50)
test = test.T
test = test.loc[:57842,:]
test = test.drop(columns=['MH50_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH50/test.csv', header=True)


#%%
MH51 = []
for animal in df_beh:
    if '51' in animal:
       MH51.append(df_beh[animal])

test = pd.DataFrame(MH51)
test = test.T
test = test.loc[:71037,:]
test = test.drop(columns=['MH51_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH51/test.csv', header=True)



#%%
MH52 = []
for animal in df_beh:
    if '52' in animal:
       MH52.append(df_beh[animal])

test = pd.DataFrame(MH52)
test = test.T
test = test.loc[:67897,:]
test = test.drop(columns=['MH52_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH52/test.csv', header=True)




#%%
MH53 = []
for animal in df_beh:
    if '53' in animal:
       MH53.append(df_beh[animal])

test = pd.DataFrame(MH53)
test = test.T
test = test.loc[:78400,:]
test = test.drop(columns=['MH53_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH53/test.csv', header=True)



#%%
MH54 = []
for animal in df_beh:
    if '54' in animal:
       MH54.append(df_beh[animal])

test = pd.DataFrame(MH54)
test = test.T
test = test.loc[:56801,:]
test = test.drop(columns=['MH54_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH54/test.csv', header=True)




#%%
MH55 = []
for animal in df_beh:
    if '55' in animal:
       MH55.append(df_beh[animal])

test = pd.DataFrame(MH55)
test = test.T
test = test.loc[:56171,:]
test = test.drop(columns=['MH55_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH55/test.csv', header=True)




#%%
MH56 = []
for animal in df_beh:
    if '56' in animal:
       MH56.append(df_beh[animal])

test = pd.DataFrame(MH56)
test = test.T
test = test.loc[:56335,:]
test = test.drop(columns=['MH56_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH56/test.csv', header=True)




#%%
MH57 = []
for animal in df_beh:
    if '57' in animal:
       MH57.append(df_beh[animal])

test = pd.DataFrame(MH57)
test = test.T
test = test.loc[:62221,:]
test = test.drop(columns=['MH57_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH57/test.csv', header=True)



#%%
MH58 = []
for animal in df_beh:
    if '58' in animal:
       MH58.append(df_beh[animal])

test = pd.DataFrame(MH58)
test = test.T
test = test.loc[:56974,:]
test = test.drop(columns=['MH58_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH58/test.csv', header=True)



#%%
MH59 = []
for animal in df_beh:
    if '59' in animal:
       MH59.append(df_beh[animal])

test = pd.DataFrame(MH59)
test = test.T
test = test.loc[:58535,:]
test = test.drop(columns=['MH59_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH59/test.csv', header=True)




#%%
MH60 = []
for animal in df_beh:
    if '60' in animal:
       MH60.append(df_beh[animal])

test = pd.DataFrame(MH60)
test = test.T
test = test.loc[:58952,:]
test = test.drop(columns=['MH60_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH60/test.csv', header=True)




#%%
MH61 = []
for animal in df_beh:
    if '61' in animal:
       MH61.append(df_beh[animal])

test = pd.DataFrame(MH61)
test = test.T
test = test.loc[:111296,:]
test = test.drop(columns=['MH61_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH61/test.csv', header=True)




#%%
MH62 = []
for animal in df_beh:
    if '62' in animal:
       MH62.append(df_beh[animal])

test = pd.DataFrame(MH62)
test = test.T
test = test.loc[:55336,:]
test = test.drop(columns=['MH62_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH62/test.csv', header=True)




#%%
MH63 = []
for animal in df_beh:
    if '63' in animal:
       MH63.append(df_beh[animal])

test = pd.DataFrame(MH63)
test = test.T
test = test.loc[:55489,:]
test = test.drop(columns=['MH63_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH63/test.csv', header=True)




#%%
MH64 = []
for animal in df_beh:
    if '64' in animal:
       MH64.append(df_beh[animal])

test = pd.DataFrame(MH64)
test = test.T
test = test.loc[:55218,:]
test = test.drop(columns=['MH64_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH64/test.csv', header=True)




#%%
MH65 = []
for animal in df_beh:
    if '65' in animal:
       MH65.append(df_beh[animal])

test = pd.DataFrame(MH65)
test = test.T
test = test.loc[:62921,:]
test = test.drop(columns=['MH65_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH65/test.csv', header=True)




#%%
MH66 = []
for animal in df_beh:
    if '66' in animal:
       MH66.append(df_beh[animal])

test = pd.DataFrame(MH66)
test = test.T
test = test.loc[:55799,:]
test = test.drop(columns=['MH66_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH66/test.csv', header=True)




#%%
MH67 = []
for animal in df_beh:
    if '67' in animal:
       MH67.append(df_beh[animal])

test = pd.DataFrame(MH67)
test = test.T
test = test.loc[:58196,:]
test = test.drop(columns=['MH67_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH67/test.csv', header=True)




#%%
MH68 = []
for animal in df_beh:
    if '68' in animal:
       MH68.append(df_beh[animal])

test = pd.DataFrame(MH68)
test = test.T
test = test.loc[:55824,:]
test = test.drop(columns=['MH68_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH68/test.csv', header=True)




#%%
MH69 = []
for animal in df_beh:
    if '69' in animal:
       MH69.append(df_beh[animal])

test = pd.DataFrame(MH69)
test = test.T
test = test.loc[:60769,:]
test = test.drop(columns=['MH69_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH69/test.csv', header=True)




#%%
MH70 = []
for animal in df_beh:
    if '70' in animal:
       MH70.append(df_beh[animal])

test = pd.DataFrame(MH70)
test = test.T
test = test.loc[:58394,:]
test = test.drop(columns=['MH70_new_pellet'])

export_csv = test.to_csv (path+'/analysis files/MH70/test.csv', header=True)




#%%
MH71 = []
for animal in df_beh:
    if '71' in animal:
       MH71.append(df_beh[animal])

test = pd.DataFrame(MH71)
test = test.T
test = test.loc[:58474,:]
test = test.drop(columns=['MH71_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH71/test.csv', header=True)




#%%
MH72 = []
for animal in df_beh:
    if '72' in animal:
       MH72.append(df_beh[animal])

test = pd.DataFrame(MH72)
test = test.T
test = test.loc[:55518,:]
test = test.drop(columns=['MH72_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH72/test.csv', header=True)





#%%
MH73 = []
for animal in df_beh:
    if '73' in animal:
       MH73.append(df_beh[animal])

test = pd.DataFrame(MH73)
test = test.T
test = test.loc[:55906,:]
test = test.drop(columns=['MH73_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH73/test.csv', header=True)





#%%
MH74 = []
for animal in df_beh:
    if '74' in animal:
       MH74.append(df_beh[animal])

test = pd.DataFrame(MH74)
test = test.T
test = test.loc[:56050,:]
test = test.drop(columns=['MH74_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH74/test.csv', header=True)





#%%
MH75 = []
for animal in df_beh:
    if '75' in animal:
       MH75.append(df_beh[animal])

test = pd.DataFrame(MH75)
test = test.T
test = test.loc[:56772,:]
test = test.drop(columns=['MH75_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH75/test.csv', header=True)




#%%
MH76 = []
for animal in df_beh:
    if '76' in animal:
       MH76.append(df_beh[animal])

test = pd.DataFrame(MH76)
test = test.T
test = test.loc[:55096,:]
test = test.drop(columns=['MH76_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH76/test.csv', header=True)




#%%
MH77 = []
for animal in df_beh:
    if '77' in animal:
       MH77.append(df_beh[animal])

test = pd.DataFrame(MH77)
test = test.T
test = test.loc[:58359,:]
test = test.drop(columns=['MH77_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH77/test.csv', header=True)




#%%
MH78 = []
for animal in df_beh:
    if '78' in animal:
       MH78.append(df_beh[animal])

test = pd.DataFrame(MH78)
test = test.T
test = test.loc[:57590,:]
test = test.drop(columns=['MH78_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH78/test.csv', header=True)




#%%
MH79 = []
for animal in df_beh:
    if '79' in animal:
       MH79.append(df_beh[animal])

test = pd.DataFrame(MH79)
test = test.T
test = test.loc[:55621,:]
test = test.drop(columns=['MH79_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH79/test.csv', header=True)




#%%
MH80 = []
for animal in df_beh:
    if '80' in animal:
       MH80.append(df_beh[animal])

test = pd.DataFrame(MH80)
test = test.T
test = test.loc[:61873,:]
test = test.drop(columns=['MH80_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH80/test.csv', header=True)




#%%
MH81 = []
for animal in df_beh:
    if '81' in animal:
       MH81.append(df_beh[animal])

test = pd.DataFrame(MH81)
test = test.T
test = test.loc[:63511,:]
test = test.drop(columns=['MH81_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH81/test.csv', header=True)

#%%
MH82 = []
for animal in df_beh:
    if '82' in animal:
       MH82.append(df_beh[animal])

test = pd.DataFrame(MH82)
test = test.T
test = test.loc[:56260,:]
test = test.drop(columns=['MH82_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH82/test.csv', header=True)


#%%
MH83 = []
for animal in df_beh:
    if '83' in animal:
       MH83.append(df_beh[animal])

test = pd.DataFrame(MH83)
test = test.T
test = test.loc[:73371,:]
test = test.drop(columns=['MH83_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH83/test.csv', header=True)


#%%
MH84 = []
for animal in df_beh:
    if '84' in animal:
       MH84.append(df_beh[animal])

test = pd.DataFrame(MH84)
test = test.T
test = test.loc[:59069,:]
test = test.drop(columns=['MH84_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH84/test.csv', header=True)


#%%
MH85 = []
for animal in df_beh:
    if '85' in animal:
       MH85.append(df_beh[animal])

test = pd.DataFrame(MH85)
test = test.T
test = test.loc[:54946,:]
test = test.drop(columns=['MH85_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH85/test.csv', header=True)


#%%
MH86 = []
for animal in df_beh:
    if '86' in animal:
       MH86.append(df_beh[animal])

test = pd.DataFrame(MH86)
test = test.T
test = test.loc[:54774,:]
test = test.drop(columns=['MH86_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH86/test.csv', header=True)


#%%
MH87 = []
for animal in df_beh:
    if '87' in animal:
       MH87.append(df_beh[animal])

test = pd.DataFrame(MH87)
test = test.T
test = test.loc[:63079,:]
test = test.drop(columns=['MH87_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH87/test.csv', header=True)


#%%
MH88 = []
for animal in df_beh:
    if '88' in animal:
       MH88.append(df_beh[animal])

test = pd.DataFrame(MH88)
test = test.T
test = test.loc[:54648,:]
test = test.drop(columns=['MH88_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH88/test.csv', header=True)



#%%
MH89 = []
for animal in df_beh:
    if '89' in animal:
        MH89.append(df_beh[animal])

test = pd.DataFrame(MH89)
test = test.T
test = test.loc[:55430,:]
test = test.drop(columns=['MH89_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH89/test.csv', header=True)


#%%
MH90 = []
for animal in df_beh:
    if '90' in animal:
        MH90.append(df_beh[animal])

test = pd.DataFrame(MH90)
test = test.T
test = test.loc[:54614,:]
test = test.drop(columns=['MH90_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH90/test.csv', header=True)


#%%
MH91 = []
for animal in df_beh:
    if '91' in animal:
        MH91.append(df_beh[animal])

test = pd.DataFrame(MH91)
test = test.T
test = test.loc[:71306,:]
test = test.drop(columns=['MH91_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH91/test.csv', header=True)


#%%
MH92 = []
for animal in df_beh:
    if '92' in animal:
        MH92.append(df_beh[animal])

test = pd.DataFrame(MH92)
test = test.T
test = test.loc[:54696,:]
test = test.drop(columns=['MH92_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH92/test.csv', header=True)


#%%
MH93 = []
for animal in df_beh:
    if '93' in animal:
        MH93.append(df_beh[animal])

test = pd.DataFrame(MH93)
test = test.T
test = test.loc[:54995,:]
test = test.drop(columns=['MH93_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH93/test.csv', header=True)

#%%
MH96 = []
for animal in df_beh:
    if '96' in animal:
        MH96.append(df_beh[animal])

test = pd.DataFrame(MH96)
test = test.T
test = test.loc[:55460,:]
test = test.drop(columns=['MH96_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH96/test.csv', header=True)



#%%
MH97 = []
for animal in df_beh:
    if '97' in animal:
        MH97.append(df_beh[animal])

test = pd.DataFrame(MH97)
test = test.T
test = test.loc[:59255,:]
test = test.drop(columns=['MH97_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH97/test.csv', header=True)



#%%
MH98 = []
for animal in df_beh:
    if '98' in animal:
        MH98.append(df_beh[animal])

test = pd.DataFrame(MH98)
test = test.T
test = test.loc[:54580,:]
test = test.drop(columns=['MH98_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH98/test.csv', header=True)



#%%
MH100 = []
for animal in df_beh:
    if '100' in animal:
        MH100.append(df_beh[animal])

test = pd.DataFrame(MH100)
test = test.T
test = test.loc[:65245,:]
test = test.drop(columns=['MH100_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH100/test.csv', header=True)




#%%
MH101 = []
for animal in df_beh:
    if '101' in animal:
        MH101.append(df_beh[animal])

test = pd.DataFrame(MH101)
test = test.T
test = test.loc[:55903,:]
test = test.drop(columns=['MH101_end_test'])

export_csv = test.to_csv (path+'/analysis files/MH101/test.csv', header=True)



