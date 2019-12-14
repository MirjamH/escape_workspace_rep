"""
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
    1.x-value33,
    2.MH33_in_shelter
    3.MH33_doorway
    4.MH33_with_pellet
    5.MH33_eat_pellet
    6.MH33_freeze
    7.MH33_reaching
    8.MH33_scanning
    9.MH33_stim
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

path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'


def ShelterTime(file_names):

    if file_names == '.DS_Store':
        next
    else:
        dataset = pd.read_csv(path_name +'/' + file_names +'/' + 'test.csv', usecols = [1,9])
        stimulus = dataset.loc[dataset.iloc[:,1] == 1].index.values.astype(int)[0]  
        dataset_stim = dataset.iloc[int(stimulus):int((stimulus +900)),:] #18000 is 5 minutes
        dataset_stim = dataset_stim.reset_index(drop=True)
            
       
        sheltertime = dataset_stim.iloc[:,0]
        
        #print(sheltertime)
        return(sheltertime)
        

#%%
'''in this for-loop i create a list of lists of lists with each animal on one line.'''
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Loom'
columns = ['xpos']
index = range(900)
shelter_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_loom = pd.concat([shelter_loom, animal], axis=1)
shelter_loom = shelter_loom.drop(columns = ['xpos'])
shelter_loom = shelter_loom.drop(index = 0)
shelter_loom['frames']=  range(len(shelter_loom))
shelter_loom['sec'] =shelter_loom['frames']/60


#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Loom'
columns = ['xpos']
index = range(900)
shelter_t_loom = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_loom = pd.concat([shelter_t_loom, animal], axis=1)
shelter_t_loom = shelter_t_loom.drop(columns = ['xpos'])
shelter_t_loom = shelter_t_loom.drop(index = 0)
shelter_t_loom['frames']=  range(len(shelter_loom))
shelter_t_loom['sec'] =shelter_t_loom['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_T_Shock'
columns = ['xpos']
index = range(900)
shelter_t_shock = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_t_shock = pd.concat([shelter_t_shock, animal], axis=1)
shelter_t_shock = shelter_t_shock.drop(columns = ['xpos'])
shelter_t_shock = shelter_t_shock.drop(index = 0)
shelter_t_shock['frames']=  range(len(shelter_t_shock))
shelter_t_shock['sec'] =shelter_t_shock['frames']/60

#%%
path_name = '/Users/mirjamheinemans/Desktop/Annotator python tryout/_Tone'
columns = ['xpos']
index = range(900)
shelter_tone = pd.DataFrame(index = index, columns = columns)

for file_names in sorted(os.listdir(path_name)): 
    print(file_names)
    animal = ShelterTime(file_names)  
    shelter_tone = pd.concat([shelter_tone, animal], axis=1)
shelter_tone = shelter_tone.drop(columns = ['xpos'])
shelter_tone = shelter_tone.drop(index = 0)
shelter_tone['frames']=  range(len(shelter_tone))
shelter_tone['sec'] =shelter_tone['frames']/60
        
        
        

#%%
df = pd.concat([shelter_loom, shelter_t_shock, shelter_t_loom, shelter_tone], axis = 1)
df['frames']=  range(len(df))
df['sec'] =df['frames']/60
#%%

'''Loom'''
ax = sns.lineplot(x='sec', y='x-value33', data =shelter_loom, color = 'black').set_title('Loom batch 1')#Loom
ax = sns.lineplot(x='sec', y='x-value34', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='x-value46', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='x-value59', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='x-value60', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='x-value65', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='x-value66', data =shelter_loom, color = 'orange')#Loom
ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')
#%%
'''Loom'''
ax = sns.lineplot(x='sec', y='x-value85', data =shelter_loom, color = 'black').set_title('Loom batch 2')#Loom
ax = sns.lineplot(x='sec', y='x-value86', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='x-value87', data =shelter_loom, color = 'black')#Loom
ax = sns.lineplot(x='sec', y='x-value88', data =shelter_loom, color = 'black')#Loom
ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')

#%%
'''Tone-Loom'''
ax = sns.lineplot(x='sec', y='x-value35', data =shelter_t_loom, color = 'blue').set_title('Tone-Loom batch 1')#T-Loom
ax = sns.lineplot(x='sec', y='x-value36', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value43', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='x-value44', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value51', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value52', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='x-value53', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='x-value54', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value63', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value64', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value69', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='x-value70', data =shelter_t_loom, color = 'orange')#T-Loom
ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')

#%%
'''Tone-Loom'''
ax = sns.lineplot(x='sec', y='x-value71', data =shelter_t_loom, color = 'orange').set_title('Tone-Loom batch 2')#T-Loom
ax = sns.lineplot(x='sec', y='x-value72', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value77', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='x-value78', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='x-value92', data =shelter_t_loom, color = 'blue')#T-Loom
ax = sns.lineplot(x='sec', y='x-value96', data =shelter_t_loom, color = 'orange')#T-Loom
ax = sns.lineplot(x='sec', y='x-value101',data =shelter_t_loom, color = 'orange')#T-Loom
ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')


#%%
'''Tone-Shock'''
ax = sns.lineplot(x='sec', y='x-value39', data =shelter_t_shock, color = 'red').set_title('Tone-Shock batch 1')#T-Shock
ax = sns.lineplot(x='sec', y='x-value40', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value49', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value50', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value55', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value56', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value67', data =shelter_t_shock, color = 'orange')#T-Shock
ax = sns.lineplot(x='sec', y='x-value68', data =shelter_t_shock, color = 'red')#T-Shock
ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')


#%%
'''Tone-Shock'''
ax = sns.lineplot(x='sec', y='x-value73', data =shelter_t_shock, color = 'red').set_title('Tone-Shock batch 2')#T-Shock
ax = sns.lineplot(x='sec', y='x-value74', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value79', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value80', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value84', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value89', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value90', data =shelter_t_shock, color = 'red')#T-Shock
ax = sns.lineplot(x='sec', y='x-value100',data =shelter_t_shock, color = 'red')#T-Shock

ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')
#%%
'''Tone'''
ax = sns.lineplot(x='sec', y='x-value37', data =shelter_tone, color = 'orange').set_title('Tone batch 1')#Tone
ax = sns.lineplot(x='sec', y='x-value38', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value42', data =shelter_tone, color = 'orange')#Tone
ax = sns.lineplot(x='sec', y='x-value47', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value48', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value57', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value58', data =shelter_tone, color = 'orange')#Tone
ax = sns.lineplot(x='sec', y='x-value61', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value62', data =shelter_tone, color = 'orange')#Tone
ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')

#%%
ax = sns.lineplot(x='sec', y='x-value75', data =shelter_tone, color = 'green').set_title('Tone batch 2')#Tone
ax = sns.lineplot(x='sec', y='x-value76', data =shelter_tone, color = 'orange')#Tone
ax = sns.lineplot(x='sec', y='x-value81', data =shelter_tone, color = 'orange')#Tone
ax = sns.lineplot(x='sec', y='x-value82', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value93', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value97', data =shelter_tone, color = 'green')#Tone
ax = sns.lineplot(x='sec', y='x-value98', data =shelter_tone, color = 'orange')#Tone
ax.plot([10 ,10], [0, 1200],color ='orange')
ax.plot([1 ,1], [0, 1200],color ='orange')
ax.set_ylabel('x-position (a.u.)')

#%%
ax = sns.lineplot(x='frames', y='x-value67', data =df, color = 'red')#T-Shock
ax.plot([600 ,600], [0, 1200],color ='orange')


#%%



