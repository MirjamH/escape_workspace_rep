#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:20:05 2019

@author: mirjamheinemans

this script is to see how much time each animal spends in the shelter without eating the pellet

"""
#%%
import csv 
import numpy as np
import os, glob # Operating System
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
os.chdir('/Users/mirjamheinemans/Desktop/Annotator python tryout') # to change directory Read csv files with Pandas

#%%
df_beh = pd.read_csv('/Users/mirjamheinemans/Desktop/Annotator python tryout/beh_and_xpos.csv',delimiter=',', low_memory=False, index_col=0)        

#%%
for column in df_beh:
    if '33' in column:
        df_beh.loc['ID',column] = 'MH33'
    elif '34' in column:
        df_beh.loc['ID',column] = 'MH34'
    elif '35' in column:
        df_beh.loc['ID',column] = 'MH35'
    elif '36' in column:
        df_beh.loc['ID',column] = 'MH36'
    elif '37' in column:
        df_beh.loc['ID',column] = 'MH37'
    elif '38' in column:
        df_beh.loc['ID',column] = 'MH38'
    elif '39' in column:
        df_beh.loc['ID',column] = 'MH39'
    elif '40' in column:
        df_beh.loc['ID',column] = 'MH40'
    elif '41' in column:
        df_beh.loc['ID',column] = 'MH41'
    elif '42' in column:
        df_beh.loc['ID',column] = 'MH42'
    elif '43' in column:
        df_beh.loc['ID',column] = 'MH43'
    elif '44' in column:
        df_beh.loc['ID',column] = 'MH44'
    elif '45' in column:
        df_beh.loc['ID',column] = 'MH45'
    elif '46' in column:
        df_beh.loc['ID',column] = 'MH46'
    elif '47' in column:
        df_beh.loc['ID',column] = 'MH47'
    elif '48' in column:
        df_beh.loc['ID',column] = 'MH48'
    elif '49' in column:
        df_beh.loc['ID',column] = 'MH49'
    elif '50' in column:
        df_beh.loc['ID',column] = 'MH50'
    elif '51' in column:
        df_beh.loc['ID',column] = 'MH51'
    elif '52' in column:
        df_beh.loc['ID',column] = 'MH52'
    elif '53' in column:
        df_beh.loc['ID',column] = 'MH53'
    elif '54' in column:
        df_beh.loc['ID',column] = 'MH54'
    elif '55' in column:
        df_beh.loc['ID',column] = 'MH55'
    elif '56' in column:
        df_beh.loc['ID',column] = 'MH56'
    elif '57' in column:
        df_beh.loc['ID',column] = 'MH57'
    elif '58' in column:
        df_beh.loc['ID',column] = 'MH58'
    elif '59' in column:
        df_beh.loc['ID',column] = 'MH59'
    elif '60' in column:
        df_beh.loc['ID',column] = 'MH60'
    elif '61' in column:
        df_beh.loc['ID',column] = 'MH61'
    elif '62' in column:
        df_beh.loc['ID',column] = 'MH62'
    elif '63' in column:
        df_beh.loc['ID',column] = 'MH63'
    elif '64' in column:
        df_beh.loc['ID',column] = 'MH64'
    elif '65' in column:
        df_beh.loc['ID',column] = 'MH65'
    elif '66' in column:
        df_beh.loc['ID',column] = 'MH66'
    elif '67' in column:
        df_beh.loc['ID',column] = 'MH67'
    elif '68' in column:
        df_beh.loc['ID',column] = 'MH68'
    elif '69' in column:
        df_beh.loc['ID',column] = 'MH69'
    elif '70' in column:
        df_beh.loc['ID',column] = 'MH70'
    elif '71' in column:
        df_beh.loc['ID',column] = 'MH71'
    elif '72' in column:
        df_beh.loc['ID',column] = 'MH72'
    elif '73' in column:
        df_beh.loc['ID',column] = 'MH73'
    elif '74' in column:
        df_beh.loc['ID',column] = 'MH74'
    elif '75' in column:
        df_beh.loc['ID',column] = 'MH75'
    elif '76' in column:
        df_beh.loc['ID',column] = 'MH76'
    elif '77' in column:
        df_beh.loc['ID',column] = 'MH77'
    elif '78' in column:
        df_beh.loc['ID',column] = 'MH78'
    elif '79' in column:
        df_beh.loc['ID',column] = 'MH79'
    elif '80' in column:
        df_beh.loc['ID',column] = 'MH80'
    elif '81' in column:
        df_beh.loc['ID',column] = 'MH81'
    elif '82' in column:
        df_beh.loc['ID',column] = 'MH82'
    elif '83' in column:
        df_beh.loc['ID',column] = 'MH83'
    elif '84' in column:
        df_beh.loc['ID',column] = 'MH84'
    elif '85' in column:
        df_beh.loc['ID',column] = 'MH85'
    elif '86' in column:
        df_beh.loc['ID',column] = 'MH86'
    elif '87' in column:
        df_beh.loc['ID',column] = 'MH87'
    elif '88' in column:
        df_beh.loc['ID',column] = 'MH88'
    elif '89' in column:
        df_beh.loc['ID',column] = 'MH89'
    elif '90' in column:
        df_beh.loc['ID',column] = 'MH90'
    elif '91' in column:
        df_beh.loc['ID',column] = 'MH91'
    elif '92' in column:
        df_beh.loc['ID',column] = 'MH92'
    elif '93' in column:
        df_beh.loc['ID',column] = 'MH93'
    elif '94' in column:
        df_beh.loc['ID',column] = 'MH94'
    elif '95' in column:
        df_beh.loc['ID',column] = 'MH95'
    elif '96' in column:
        df_beh.loc['ID',column] = 'MH96'
    elif '97' in column:
        df_beh.loc['ID',column] = 'MH97'
    elif '98' in column:
        df_beh.loc['ID',column] = 'MH98'
    elif '99' in column:
        df_beh.loc['ID',column] = 'MH99'
    elif '100' in column:
        df_beh.loc['ID',column] = 'MH100'
    elif '101' in column:
        df_beh.loc['ID',column] = 'MH101'