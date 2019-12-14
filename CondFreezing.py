#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:22:42 2019

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

total = list(freeze_figure['stim'])
condition = list(freeze_figure['condition'])
ax = sns.swarmplot(x="condition", y="stim", 
                 data=freeze_figure, color = 'black')
ax.set_title('Percent freezing during stimulus (all animals included)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)
#ax.legend(bbox_to_anchor=(1,1))



#%%

freeze_t_shock = freeze_t_shock.T
freeze_t_loom = freeze_t_loom.T
freeze_tl_filtered = freeze_tl_filtered.T
freeze_tone = freeze_tone.T
#%%

T_SvsT = ss.mannwhitneyu(freeze_t_shock['stim'],freeze_tone['stim'])
T_SvsT_L = ss.mannwhitneyu(freeze_t_shock['stim'],freeze_t_loom['stim'])

TvsT_L = ss.mannwhitneyu(freeze_tone['stim'],freeze_t_loom['stim'])

#%%
print('T_SvsT =',T_SvsT)
print('T_SvsT_L =',T_SvsT_L)
print('TvsT_L =', TvsT_L)



#%%

freeze_figure_fil =  pd.concat([freeze_tl_filtered, freeze_t_shock, freeze_tone], axis =0)

freeze_figure_fil['increase'] = freeze_figure_fil['stim'] - freeze_figure_fil['base'] 
#%%
'''freezing during stimulus'''
total = list(freeze_figure_fil['stim'])
condition = list(freeze_figure_fil['condition'])
ax = sns.swarmplot(x="condition", y="stim", 
                 data=freeze_figure_fil, color = 'black')
ax.set_title('freezing during stimulus (T_L only >15% freezing included)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)


#%%
'''Figure with increase of freezing from baseline to stimulus'''
total = list(freeze_figure_fil['increase'])
condition = list(freeze_figure_fil['condition'])
ax = sns.swarmplot(x="condition", y="increase", 
                 data=freeze_figure_fil, color = 'black')
ax.set_title('increase of freezing(T_L only >15% freezing included)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)

#%%
'''freezing during baseline'''
total = list(freeze_figure_fil['base'])
condition = list(freeze_figure_fil['condition'])
ax = sns.swarmplot(x="condition", y="base", 
                 data=freeze_figure_fil, color = 'black')
ax.set_title('freezing during baseline(T_L only >15% freezing included)')
ax = sns.boxplot(x=condition, y=total, palette="Set2", showfliers = False)

#%%

T_SvsT = ss.mannwhitneyu(freeze_t_shock['stim'],freeze_tone['stim'])
T_SvsT_L = ss.mannwhitneyu(freeze_t_shock['stim'],freeze_tl_filtered['stim'])

TvsT_L = ss.mannwhitneyu(freeze_tone['stim'],freeze_tl_filtered['stim'])

#%%
'''somehow wrong values from mann whitney U test: prism values are T_LvsT and T_SvsT<0.0001; T_SvsT_L = 0.14)'''
print('T_SvsT =',T_SvsT)
print('T_SvsT_L =',T_SvsT_L)
print('TvsT_L =', TvsT_L)






