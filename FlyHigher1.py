#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:21:33 2019

@author: mirjamheinemans
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:54:53 2019

@author: Matheus Farias
"""


import tkinter, tkinter.filedialog
import numpy as np
import glob
import os
import copy

'''DEFINE ANALYSIS PARAMETERS'''

# Size scale
arena_raio_mm = 15

#TIME SCALES
frame_rate = 60
bin_size_sec = 0.5

frame_time_sec = 1 / frame_rate
n_frame_bin = int(bin_size_sec / frame_time_sec)


#EXPERIMENT DURATION (in sec)
baseline  = 300
stimulation = 300

baseline_frames = baseline * frame_rate
stimulation_frames = stimulation * frame_rate

#BEHAVIORAL PARAMETERS

#FREEZING - Minimum time (in sec) of inactivity to be considered freezing
min_freeze_sec = 0.5
min_freeze = min_freeze_sec / frame_time_sec

#GROOMING - Low velocity (mm/s) threshold
groom_velocity = 4

#JUMPING - High velocity (mm/s) threshold
jump_velocity = 75

#Walking velocity is in between groom and jump

'''LOAD DATA'''

def load_path():
    root = tkinter.Tk()
    filename = tkinter.filedialog.askdirectory(parent=root, title='Folder with *tracked files')
    root.destroy()
    return filename


path = load_path()


for filename in glob.glob(os.path.join(path, '*tracked.csv')):
    first, tracked, extention = filename.split('.', 2)
    location, file_name = first.split('\\', 1)
    experimenter, line, protocol, age, fh, date = file_name.split('-' , 5)
    outputname = location+'\\'+line+'-'+protocol+'-'+age+'-'+fh+'-'+date


    raw_data = np.genfromtxt(filename, delimiter=',', dtype=int, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))

    #Align to first loom and crop
    loom = raw_data[:, 0]
    loom_onset = []
    for i in range(len(loom)):
        if loom[i] == 0 and loom[i-1] == 1:
            looms = i
            loom_onset.append(looms)
    first_loom = loom_onset[0]
    
    baseline_start = first_loom - baseline_frames
    stimulation_end = first_loom + stimulation_frames
    data_aligned = raw_data[baseline_start:stimulation_end]
    
    #Load variables
    looming = data_aligned[:, 0]
    redled = data_aligned[:, 1]
    greenled = data_aligned[:, 2]

    fly1_x_position = data_aligned[:, 3]
    fly1_y_position = data_aligned[:, 4]
    fly1_pixelchange = data_aligned[:, 5]
    arena1_x = data_aligned[:, 6]
    arena1_y = data_aligned[:, 7]
    arena1_width = data_aligned[:, 8]
    arena1_heigth = data_aligned[:, 9]

    fly2_x_position = data_aligned[:, 10]
    fly2_y_position = data_aligned[:, 11]
    fly2_pixelchange = data_aligned[:, 12]
    arena2_x = data_aligned[:, 13]
    arena2_y = data_aligned[:, 14]
    arena2_width = data_aligned[:, 15]
    arena2_heigth = data_aligned[:, 16]

    fly3_x_position = data_aligned[:, 17]
    fly3_y_position = data_aligned[:, 18]
    fly3_pixelchange = data_aligned[:, 19]
    arena3_x = data_aligned[:, 20]
    arena3_y = data_aligned[:, 21]
    arena3_width = data_aligned[:, 22]
    arena3_heigth = data_aligned[:, 23]

    fly4_x_position = data_aligned[:, 24]
    fly4_y_position = data_aligned[:, 25]
    fly4_pixelchange = data_aligned[:, 26]
    arena4_x = data_aligned[:, 27]
    arena4_y = data_aligned[:, 28]
    arena4_width = data_aligned[:, 29]
    arena4_heigth = data_aligned[:, 30]

    number_frames = len(looming)
    
    '''    ANALYSIS    '''
    arena1_x_raio = int((round(sum(arena1_width) / number_frames)) / 2)
    arena1_y_raio = int((round(sum(arena1_heigth) / number_frames)) / 2)
    arena1_x_zero = arena1_x - arena1_x_raio
    arena1_y_zero = arena1_y - arena1_y_raio
   
    arena2_x_raio = int((round(sum(arena2_width) / number_frames)) / 2)
    arena2_y_raio = int((round(sum(arena2_heigth) / number_frames)) / 2)
    arena2_x_zero = arena2_x - arena2_x_raio
    arena2_y_zero = arena2_y - arena2_y_raio
    
    arena3_x_raio = int((round(sum(arena3_width) / number_frames)) / 2)
    arena3_y_raio = int((round(sum(arena3_heigth) / number_frames)) / 2)
    arena3_x_zero = arena3_x - arena3_x_raio
    arena3_y_zero = arena3_y - arena3_y_raio
    
    arena4_x_raio = int((round(sum(arena4_width) / number_frames)) / 2)
    arena4_y_raio = int((round(sum(arena4_heigth) / number_frames)) / 2)
    arena4_x_zero = arena4_x - arena4_x_raio
    arena4_y_zero = arena4_y - arena4_y_raio
    
    fly1_x_zero = fly1_x_position - arena1_x_zero
    fly1_y_zero = fly1_y_position - arena1_y_zero
    fly1_x_norm_mm = (fly1_x_zero * (arena_raio_mm)) / arena1_x_raio
    fly1_y_norm_mm = (fly1_y_zero * (arena_raio_mm)) / arena1_y_raio
    
    fly2_x_zero = fly2_x_position - arena2_x_zero
    fly2_y_zero = fly2_y_position - arena2_y_zero
    fly2_x_norm_mm = (fly2_x_zero * (arena_raio_mm)) / arena2_x_raio
    fly2_y_norm_mm = (fly2_y_zero * (arena_raio_mm)) / arena2_y_raio
    
    fly3_x_zero = fly3_x_position - arena3_x_zero
    fly3_y_zero = fly3_y_position - arena3_y_zero
    fly3_x_norm_mm = (fly3_x_zero * (arena_raio_mm)) / arena3_x_raio
    fly3_y_norm_mm = (fly3_y_zero * (arena_raio_mm)) / arena3_y_raio
    
    fly4_x_zero = fly4_x_position - arena4_x_zero
    fly4_y_zero = fly4_y_position - arena4_y_zero
    fly4_x_norm_mm = (fly4_x_zero * (arena_raio_mm)) / arena4_x_raio
    fly4_y_norm_mm = (fly4_y_zero * (arena_raio_mm)) / arena4_y_raio
        
 
    fly1_delta_x = abs(fly1_x_norm_mm[1:] - fly1_x_norm_mm[:-1])
    fly1_delta_y = abs(fly1_y_norm_mm[1:] - fly1_y_norm_mm[:-1])
    fly1_distance_mm = (np.sqrt(fly1_delta_x**2 + fly1_delta_y**2))
    fly1_distance_mm.resize(number_frames)
    
    fly2_delta_x = abs(fly2_x_norm_mm[1:] - fly2_x_norm_mm[:-1])
    fly2_delta_y = abs(fly2_y_norm_mm[1:] - fly2_y_norm_mm[:-1])
    fly2_distance_mm = (np.sqrt(fly2_delta_x**2 + fly2_delta_y**2))
    fly2_distance_mm.resize(number_frames)
    
    fly3_delta_x = abs(fly3_x_norm_mm[1:] - fly3_x_norm_mm[:-1])
    fly3_delta_y = abs(fly3_y_norm_mm[1:] - fly3_y_norm_mm[:-1])
    fly3_distance_mm = (np.sqrt(fly3_delta_x**2 + fly3_delta_y**2))
    fly3_distance_mm.resize(number_frames)
    
    fly4_delta_x = abs(fly4_x_norm_mm[1:] - fly4_x_norm_mm[:-1])
    fly4_delta_y = abs(fly4_y_norm_mm[1:] - fly4_y_norm_mm[:-1])
    fly4_distance_mm = (np.sqrt(fly4_delta_x**2 + fly4_delta_y**2))
    fly4_distance_mm.resize(number_frames)
       
    #Velocity per frame mm/sec
    fly1_velocity = np.array(fly1_distance_mm / frame_time_sec)
    fly2_velocity = np.array(fly2_distance_mm / frame_time_sec)
    fly3_velocity = np.array(fly3_distance_mm / frame_time_sec)
    fly4_velocity = np.array(fly4_distance_mm / frame_time_sec)
     
    #Walking velocity 
    fly1_walk = np.array([1 if fly1_velocity[i] <= jump_velocity and fly1_velocity[i] >= groom_velocity else 0 for i in range(len(fly1_velocity))])
    fly2_walk = np.array([1 if fly2_velocity[i] <= jump_velocity and fly2_velocity[i] >= groom_velocity else 0 for i in range(len(fly2_velocity))])
    fly3_walk = np.array([1 if fly3_velocity[i] <= jump_velocity and fly3_velocity[i] >= groom_velocity else 0 for i in range(len(fly3_velocity))])
    fly4_walk = np.array([1 if fly4_velocity[i] <= jump_velocity and fly4_velocity[i] >= groom_velocity else 0 for i in range(len(fly4_velocity))])

    #Freezing frames
    fly1_freeze = np.array([1 if fly1_pixelchange[i] == 0 else 0 for i in range(number_frames)])
    fly2_freeze = np.array([1 if fly2_pixelchange[i] == 0 else 0 for i in range(number_frames)])
    fly3_freeze = np.array([1 if fly3_pixelchange[i] == 0 else 0 for i in range(number_frames)])
    fly4_freeze = np.array([1 if fly4_pixelchange[i] == 0 else 0 for i in range(number_frames)])
    fly1_freeze.resize(number_frames + 2)
    fly2_freeze.resize(number_frames + 2)
    fly3_freeze.resize(number_frames + 2)
    fly4_freeze.resize(number_frames + 2)    
    
    for i in range(len(fly1_freeze)):
        if fly1_freeze[i] == 0:
            if sum(fly1_freeze[i+1:i+2]) >= 1:
                fly1_freeze[i] = 1

    for i in range(len(fly2_freeze)):
        if fly2_freeze[i] == 0:
            if sum(fly2_freeze[i+1:i+2]) >= 1:
                fly2_freeze[i] = 1

    for i in range(len(fly3_freeze)):
        if fly3_freeze[i] == 0:
            if sum(fly3_freeze[i+1:i+2]) >= 1:
                fly3_freeze[i] = 1

    for i in range(len(fly4_freeze)):
        if fly4_freeze[i] == 0:
            if sum(fly4_freeze[i+1:i+2]) >= 1:
                fly4_freeze[i] = 1
    
    #Jumps 
    fly1_jumps = np.array([1 if fly1_velocity[i] >= jump_velocity else 0 for i in range(number_frames)])
    fly2_jumps = np.array([1 if fly2_velocity[i] >= jump_velocity else 0 for i in range(number_frames)])
    fly3_jumps = np.array([1 if fly3_velocity[i] >= jump_velocity else 0 for i in range(number_frames)])
    fly4_jumps = np.array([1 if fly4_velocity[i] >= jump_velocity else 0 for i in range(number_frames)])
    
    for i in range(len(fly1_jumps)):
        if fly1_jumps[i] == 1:
            fly1_jumps[i+1:i+3] = 0
            fly1_freeze[i+1:i+3] = 0
            fly1_walk[i+1:i+3] = 0
            
    for i in range(len(fly2_jumps)):
        if fly2_jumps[i] == 1:
            fly2_jumps[i+1:i+3] = 0
            fly2_freeze[i+1:i+3] = 0
            fly2_walk[i+1:i+3] = 0        
            
    for i in range(len(fly3_jumps)):
        if fly3_jumps[i] == 1:
            fly3_jumps[i+1:i+3] = 0
            fly3_freeze[i+1:i+3] = 0
            fly3_walk[i+1:i+3] = 0
            
    for i in range(len(fly4_jumps)):
        if fly4_jumps[i] == 1:
            fly4_jumps[i+1:i+3] = 0
            fly4_freeze[i+1:i+3] = 0
            fly4_walk[i+1:i+3] = 0
    
    
    #Minimum freezing duration
    def freeze_threshold(min_atv):
        lol = 0
        onset = []
        offset = []
    
        for i, j in enumerate(min_atv):
            if j == 1 and lol == 0:
                lol = 1
                onset.append(i)
            if j == 0 and lol == 1:
                lol = 0
                offset.append(i)
        if min_atv[-1] == 1:
            offset.append(len(min_atv))
    
        duration = [offset[i] - onset[i] for i in range(len(onset))]
        output = copy.deepcopy(min_atv)
        for i in range(len(duration)):
            if duration[i] < min_freeze:
                output[onset[i]:offset[i]] = 0
            
        return output

    fly1_freeze_bout = freeze_threshold(fly1_freeze)
    fly2_freeze_bout = freeze_threshold(fly2_freeze)
    fly3_freeze_bout = freeze_threshold(fly3_freeze)    
    fly4_freeze_bout = freeze_threshold(fly4_freeze)
    fly1_freeze_bout.resize(number_frames)
    fly2_freeze_bout.resize(number_frames)
    fly3_freeze_bout.resize(number_frames)
    fly4_freeze_bout.resize(number_frames)


    #low velocity behaviors (velocity < 4mm and not freezing)
    fly1_groom = np.array([1 if fly1_velocity[i] <= groom_velocity and fly1_freeze_bout[i] == 0 else 0 for i in range(len(fly1_velocity))])
    fly2_groom = np.array([1 if fly2_velocity[i] <= groom_velocity and fly2_freeze_bout[i] == 0 else 0 for i in range(len(fly2_velocity))])
    fly3_groom = np.array([1 if fly3_velocity[i] <= groom_velocity and fly3_freeze_bout[i] == 0 else 0 for i in range(len(fly3_velocity))])
    fly4_groom = np.array([1 if fly4_velocity[i] <= groom_velocity and fly4_freeze_bout[i] == 0 else 0 for i in range(len(fly4_velocity))])
    
    
    looming_binary = np.array([1 if looming[i] == 0 else 0 for i in range(number_frames)])        

    
    '''SAVE FILES - FREEZE, FRAMES AND BINS'''
    #Frames
    frames_output = np.column_stack((looming_binary, redled, greenled, 
                                     fly1_x_norm_mm, fly1_y_norm_mm, fly1_pixelchange, fly1_velocity, fly1_walk, fly1_freeze_bout, fly1_jumps, fly1_groom,
                                     fly2_x_norm_mm, fly2_y_norm_mm, fly2_pixelchange, fly2_velocity, fly2_walk, fly2_freeze_bout, fly2_jumps, fly2_groom,
                                     fly3_x_norm_mm, fly3_y_norm_mm, fly3_pixelchange, fly3_velocity, fly3_walk, fly3_freeze_bout, fly3_jumps, fly3_groom,
                                     fly4_x_norm_mm, fly4_y_norm_mm, fly4_pixelchange, fly4_velocity, fly4_walk, fly4_freeze_bout, fly4_jumps, fly4_groom))   
    
    fly1_output = np.column_stack((looming_binary, redled, greenled, 
                                     fly1_x_norm_mm, fly1_y_norm_mm, fly1_pixelchange, fly1_velocity, fly1_walk, fly1_freeze_bout, fly1_jumps, fly1_groom))
    fly2_output = np.column_stack((looming_binary, redled, greenled, 
                                     fly2_x_norm_mm, fly2_y_norm_mm, fly2_pixelchange, fly2_velocity, fly2_walk, fly2_freeze_bout, fly2_jumps, fly2_groom))
    fly3_output = np.column_stack((looming_binary, redled, greenled, 
                                     fly3_x_norm_mm, fly3_y_norm_mm, fly3_pixelchange, fly3_velocity, fly3_walk, fly3_freeze_bout, fly3_jumps, fly3_groom))
    fly4_output = np.column_stack((looming_binary, redled, greenled, 
                                     fly4_x_norm_mm, fly4_y_norm_mm, fly4_pixelchange, fly4_velocity, fly4_walk, fly4_freeze_bout, fly4_jumps, fly4_groom))
    
    np.savetxt(str(outputname)+".fly1_scored_frames.csv", fly1_output, delimiter = ",")
    np.savetxt(str(outputname)+".fly2_scored_frames.csv", fly2_output, delimiter = ",")
    np.savetxt(str(outputname)+".fly3_scored_frames.csv", fly3_output, delimiter = ",")
    np.savetxt(str(outputname)+".fly4_scored_frames.csv", fly4_output, delimiter = ",")
    
    
