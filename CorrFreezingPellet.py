#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:52:29 2019

@author: mirjamheinemans

CONDITIONING columns:
    1.MHbase33,
    2.MHstim33
    3.MHfreeze33
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
'''Part 1: freezing percentages during conditioning:
    DF is called freeze; columns is all animals, rows ['base', 'stim', 'condition']
'''

def ConditionedFreezing(file_names):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'conditioning.csv',usecols=[1,2,3])
        base = dataset.iloc[:,0].diff()[dataset.iloc[:,0].diff() != 0].index.values
        baseline = base[1]
        freeze_base = (sum(dataset.iloc[:baseline,2]))/baseline*100
        
        stim = dataset.iloc[:,1].diff()[dataset.iloc[:,1].diff() != 0].index.values
        end_stim = stim[-1]
        freeze_stim = (sum(dataset.iloc[baseline:end_stim,2]))/(end_stim-baseline)*100
        
        freezing_percent = pd.DataFrame(data =[freeze_base,freeze_stim], index =['base','stim'],columns = [file_names])
       
        return(freezing_percent)


#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'


freeze_t_loom = pd.DataFrame(index =['base','stim'],columns = ['xpos'])

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ConditionedFreezing(file_names)  
    freeze_t_loom = pd.concat([freeze_t_loom, animal], axis=1)
freeze_t_loom = freeze_t_loom.drop(columns = ['xpos'])
freeze_t_loom.loc['condition',:] = 'T_L'
my_list = ['MH043','MH044', 'MH051', 'MH052', 'MH053', 'MH063', 'MH064', 'MH070', 'MH071', 'MH078','MH092','MH096', 'MH101'  ]
freeze_tl_filtered = freeze_t_loom[my_list]

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'

freeze_t_shock = pd.DataFrame(index =['base','stim'],columns = ['xpos'])

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ConditionedFreezing(file_names)  
    freeze_t_shock = pd.concat([freeze_t_shock, animal], axis=1)
freeze_t_shock = freeze_t_shock.drop(columns = ['xpos'])
freeze_t_shock.loc['condition',:] = 'T_S'

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'

freeze_tone = pd.DataFrame(index =['base','stim'],columns = ['xpos'])

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ConditionedFreezing(file_names)  
    freeze_tone = pd.concat([freeze_tone, animal], axis=1)
freeze_tone = freeze_tone.drop(columns = ['xpos'])
freeze_tone.loc['condition',:] = 'T'

#%%

freeze =  pd.concat([freeze_t_loom, freeze_t_shock, freeze_tone], axis =1)
freeze_figure = freeze.T
#%%
'''Part 2: time untill animal grabs pellet'''

path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
def Pellet(file_names):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [4,9])
        stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +40000)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
            
        dataset_stim[file_names+'taken'] = 1
        
        
        if sum(dataset_stim.iloc[:,0]) > 0:
            pellet = (dataset_stim.loc[dataset_stim.iloc[:,0] == 1].index.values.astype(float)[0])/60
                
        else:
            pellet = 40000/60
        
        df_pellet = pd.DataFrame(data =[pellet], index =['pellet'],columns = [file_names])
       
        return(df_pellet)

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
pellet_t_loom = pd.DataFrame(index =['pellet'],columns = ['xpos'])

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Pellet(file_names)  
    pellet_t_loom = pd.concat([pellet_t_loom, animal], axis=1)
pellet_t_loom = pellet_t_loom.drop(columns = ['xpos'])
my_list = ['MH043','MH044', 'MH051', 'MH052', 'MH053', 'MH063', 'MH064', 'MH070', 'MH071', 'MH078','MH092','MH096', 'MH101'  ]
pellet_tl_filtered = pellet_t_loom[my_list]
df_tl = pd.concat([freeze_tl_filtered, pellet_tl_filtered], axis =0)
#df_tl = df_tl.apply(pd.to_numeric, errors='coerce')
df_tl =df_tl.T
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
pellet_t_shock = pd.DataFrame(index =['pellet'],columns = ['xpos'])

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Pellet(file_names)  
    pellet_t_shock = pd.concat([pellet_t_shock, animal], axis=1)

pellet_t_shock = pellet_t_shock.drop(columns = ['xpos'])
df_ts = pd.concat([freeze_t_shock, pellet_t_shock], axis =0)
#df_ts = df_ts.apply(pd.to_numeric, errors='coerce')
df_ts = df_ts.T
#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
pellet_tone = pd.DataFrame(index =['pellet'],columns = ['xpos'])

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = Pellet(file_names)  
    pellet_tone = pd.concat([pellet_tone, animal], axis=1)

pellet_tone = pellet_tone.drop(columns = ['xpos'])
df_tone = pd.concat([freeze_tone, pellet_tone], axis =0)
#df_tone = df_tone.apply(pd.to_numeric, errors='coerce')
df_tone = df_tone.T
#%%

df_all = pd.concat([df_tl, df_ts, df_tone], axis = 0)





ax = sns.scatterplot(x="pellet", y="stim", hue ='condition',
                     data=df_all)
ax.set_title('correlation between amount of freezing during conditioning and time to grab pellet')
ax.set_xlabel('time to take pellet (sec)')
ax.set_ylabel('percent of time freezing during conditioning')
ax.set_ylim([-10, 100])
ax.legend(bbox_to_anchor=(1,1))

#%%

stim = np.array(df_all['stim'])
pellet = np.array(df_all['pellet'])
sns.regplot(x=stim, y=pellet) 
                     
#ax.set_title('correlation between amount of freezing during conditioning and time to grab pellet')
#ax.set_ylabel('time to take pellet (sec)')
#ax.set_xlabel('percent of time freezing during conditioning')
#ax.set_xlim([0, 100])

#%%

ax = sns.lineplot(x=pellet, y=stim)























#%%
