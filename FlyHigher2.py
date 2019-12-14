#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:20:57 2019

@author: mirjamheinemans
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:54:30 2019

@author: Matheus Farias
"""


import tkinter, tkinter.filedialog
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
import seaborn as sns
import os

'''
EXPERIMENT NAME = FILE NAME START
'''

#Change the name here
experiment_name = 'Empty_X_DL_10xKir_FHcompare' #for figs names
experiment0 = 'Empty_X_DL_10xKir-20Loom-FH0'
experiment1 = 'Empty_X_DL_10xKir-20Loom-FH1'


'''
DEFINE ANALYSIS PARAMETERS
'''

#TIME SCALES
frame_rate = 60
bin_size_sec = 0.5
bin_zoom_size = 3 #frames

frame_time_sec = 1 / frame_rate
n_frame_bin = int(bin_size_sec / frame_time_sec)


#EXPERIMENT DURATION (in sec)
baseline  = 300
stimulation = 300

baseline_frames = baseline * frame_rate
stimulation_frames = stimulation * frame_rate

zoom_before_loom_onset = 60
zoom_after_loom_onset = 90
zoom_after_loom_offset = 60

#BEHAVIORAL PARAMETERS

#FREEZING - Minimum time (in sec) of inativity to be considered freezing
min_freeze_sec = 0.5
min_freeze = min_freeze_sec / frame_time_sec

#GROOMING - Low velocity (mm/s) threshold
groom_velocity = 4

#JUMPING - High velocity (mm/s) threshold
jump_velocity = 75

#Walking velocity is in between groom and jump

#Time of looms bins - to plot vertical lines in raster
looming_x = [600, 634, 662, 700, 736, 772, 802, 826, 860, 888, 918, 946, 974, 996, 1020, 1056, 1084, 1112, 1146, 1172]
looming_x_zoom = [20, 30]
looming_x_frames = [i * n_frame_bin for i in looming_x]


'''
Choosing where to load and save files
'''

def load_path():
    root = tkinter.Tk()
    filename = tkinter.filedialog.askdirectory(parent=root, title='Choose a folder to load files')
    root.destroy()
    return filename


path = load_path()


#FUNCTION TO DETECT OUTLIERS
def is_outlier(points, thresh=3.5):
    '''
    Returns a boolean array with True if points are outliers and False 
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor. 
    '''
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh

'''
Loading experiment files
'''

''' FRAMES '''
exp0_header = []
exp0_looming = []
exp0_redled = []
exp0_greenled = []
exp0_x_position = []
exp0_y_position = []
exp0_pxchange = []
exp0_velocity = []
exp0_vel_2d = []
exp0_walk_vel = []
exp0_walking = []
exp0_freezing = []
exp0_jumping = []
exp0_bin_jumping = []
exp0_grooming = []

''' ZOOM '''
exp0_zoom_looming = []
exp0_zoom_redled = []
exp0_zoom_greenled = []
exp0_zoom_x_position = []
exp0_zoom_y_position = []
exp0_zoom_pxchange = []
exp0_zoom_velocity = []
exp0_zoom_vel_2d = []
exp0_zoom_walk_vel = []
exp0_zoom_walking = []
exp0_zoom_freezing = []
exp0_zoom_jumping = []
exp0_zoom_grooming = []

'''CONDITIONAL ZOOM'''
exp0_zoom_pxchange_freezer_before_after = []
exp0_zoom_velocity_freezer_before_after = []
exp0_zoom_vel_2d_freezer_before_after = []
exp0_zoom_walk_vel_freezer_before_after = []
exp0_zoom_walking_freezer_before_after = []
exp0_zoom_freezing_freezer_before_after = []
exp0_zoom_jumping_freezer_before_after = []
exp0_zoom_grooming_freezer_before_after = []

exp0_zoom_pxchange_runner_before_after = []
exp0_zoom_velocity_runner_before_after = []
exp0_zoom_vel_2d_runner_before_after = []
exp0_zoom_walk_vel_runner_before_after = []
exp0_zoom_walking_runner_before_after = []
exp0_zoom_freezing_runner_before_after = []
exp0_zoom_jumping_runner_before_after = []
exp0_zoom_grooming_runner_before_after = []


for filename in glob.glob(os.path.join(path , (str(experiment0)+'*scored_frames.csv'))):
     first, scored, extention = filename.split('.', 2)
     location, exp0_file_name = first.split('\\', 1)
     exp0_line, exp0_protocol, exp0_date = exp0_file_name.split('-' , 2)
     exp0_outputname = location+'\\'+exp0_line+'-'+exp0_protocol+'-'+exp0_date
     
     raw = pd.read_csv(filename,',', header = None)
     number_frames = len(raw)
     
     '''HEADER'''
     exp0_fly = exp0_file_name
     exp0_header.append(exp0_fly)
     
     
     '''LOOMING'''
     #FRAMES
     exp0_looming_data = pd.DataFrame({'loom':raw[0]})
     exp0_loom1 = exp0_looming_data['loom'].tolist()
     exp0_looming.append(exp0_loom1)
     
     
     '''RED LED'''
     #FRAMES
     exp0_redled_data = pd.DataFrame({'redled':raw[1]})
     exp0_red1 = exp0_redled_data['redled'].tolist()
     exp0_redled.append(exp0_red1)

     
     '''GREEN LED'''
     #FRAMES
     exp0_greenled_data = pd.DataFrame({'greenled':raw[2]})
     exp0_green1 = exp0_greenled_data['greenled'].tolist()
     exp0_greenled.append(exp0_green1)
  
     
     '''X POSITION'''
     exp0_x_position_data = pd.DataFrame({'xpos1':raw[3]})
     exp0_xpos1 = exp0_x_position_data['xpos1'].tolist()
     exp0_x_position.append(exp0_xpos1)

    
     '''Y POSITION'''
     exp0_y_position_data = pd.DataFrame({'ypos1':raw[4]})
     exp0_ypos1 = exp0_y_position_data['ypos1'].tolist()
     exp0_y_position.append(exp0_ypos1)


     '''PIXEL CHANGE'''
     exp0_pxchange_data = pd.DataFrame({'px1':raw[5]})
     exp0_px1 = exp0_pxchange_data['px1'].tolist()
     exp0_pxchange.append(exp0_px1)
     
     
     '''VELOCITY'''
     #FRAMES
     exp0_velocity_data = pd.DataFrame({'vel1':raw[6]})
     exp0_vel1 = exp0_velocity_data['vel1'].tolist()
     exp0_velocity.append(exp0_vel1)
     
     
     '''Velocity 2d'''
     exp0_vel2d1 = [exp0_vel1[i] if exp0_vel1[i] <= jump_velocity else 0 for i in range(number_frames)]     
     exp0_vel_2d.append(exp0_vel2d1)
     
     
     '''WALKING VELOCITY'''
     #FRAMES
     exp0_walking_data = pd.DataFrame({'walk1':raw[7]})
     exp0_walk1 = exp0_walking_data['walk1'].tolist()
     exp0_walking_to_vel1 = np.array([exp0_vel1[i] if exp0_walk1[i] == 1 else 0 for i in range(number_frames)])       
     
     exp0_walking.append(exp0_walk1)
     exp0_walk_vel.append(exp0_walking_to_vel1)
      
     
     '''FREEZING'''
     #FRAMES
     exp0_freezing_data = pd.DataFrame({'fre1':raw[8]})
     exp0_fre1 = exp0_freezing_data['fre1'].tolist()
     exp0_freezing.append(exp0_fre1)


     '''JUMPING'''
     #FRAMES     
     exp0_jumping_data = pd.DataFrame({'jum1':raw[9]})
     exp0_jum1 = exp0_jumping_data['jum1'].tolist()
     exp0_jumping.append(exp0_jum1)
     
     #BINS - SUM OF JUMPS
     exp0_fly1_jump_bins = np.array([sum(exp0_jum1[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)])
     exp0_bin_jumping.append(exp0_fly1_jump_bins)

    
     '''GROOMING'''
     #FRAMES
     exp0_grooming_data = pd.DataFrame({'gro1':raw[10]})
     exp0_gro1 = exp0_grooming_data['gro1'].tolist()
     exp0_grooming.append(exp0_gro1)

     
     '''ZOOMS'''
     for i in range(len(exp0_loom1)):
         if exp0_loom1[i] == 1 and exp0_loom1[i-1] == 0:
             exp0_loom_loom_onset1 = i

             exp0_zoom_loom1 = exp0_loom1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_looming.append(exp0_zoom_loom1)   
             number_frames_zoom = len(exp0_zoom_loom1)

             exp0_zoom_red1 = exp0_red1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_redled.append(exp0_zoom_red1)

             exp0_zoom_green1 = exp0_green1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_greenled.append(exp0_zoom_green1)

             exp0_zoom_xpos1 = exp0_xpos1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_x_position.append(exp0_zoom_xpos1)
             
             exp0_zoom_ypos1 = exp0_ypos1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_y_position.append(exp0_zoom_ypos1)
             
             exp0_zoom_px1 = exp0_px1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_pxchange.append(exp0_zoom_px1)
             
             exp0_zoom_vel1 = exp0_vel1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_velocity.append(exp0_zoom_vel1)
             
             exp0_zoom_vel2d1 = exp0_vel2d1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_vel_2d.append(exp0_zoom_vel2d1)

             exp0_zoom_walking1 = exp0_walk1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_walking.append(exp0_zoom_walking1)
             
             exp0_zoom_walk_vel1 = exp0_walking_to_vel1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_walk_vel.append(exp0_zoom_walk_vel1)

             exp0_zoom_freezing1 = exp0_fre1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_freezing.append(exp0_zoom_freezing1)

             exp0_zoom_jumping1 = exp0_jum1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_jumping.append(exp0_zoom_jumping1)

             exp0_zoom_grooming1 = exp0_gro1[(exp0_loom_loom_onset1-zoom_before_loom_onset):(exp0_loom_loom_onset1+zoom_after_loom_onset)]
             exp0_zoom_grooming.append(exp0_zoom_grooming1)
             
             '''Selecting freezers'''
             for i in range(len(exp0_zoom_freezing1)):
                 exp0_fly1_freezing_zoom = np.array(np.array([sum(exp0_zoom_freezing1[current : current + n_frame_bin]) for current in range(0, len(exp0_zoom_freezing1), n_frame_bin)]) / n_frame_bin)
                 exp0_fly1_freezing_zoom_before = sum(exp0_fly1_freezing_zoom[:2])
                 exp0_fly1_freezing_zoom_after = sum(exp0_fly1_freezing_zoom[3:])
                 if exp0_fly1_freezing_zoom_before > 1 and exp0_fly1_freezing_zoom_after > 1:
                     exp0_zoom_pxchange_freezer_before_after.append(exp0_zoom_px1)
                     exp0_zoom_velocity_freezer_before_after.append(exp0_zoom_vel1)
                     exp0_zoom_vel_2d_freezer_before_after.append(exp0_zoom_vel2d1)
                     exp0_zoom_walking_freezer_before_after.append(exp0_zoom_walking1)
                     exp0_zoom_walk_vel_freezer_before_after.append(exp0_zoom_walk_vel1)
                     exp0_zoom_freezing_freezer_before_after.append(exp0_zoom_freezing1)
                     exp0_zoom_jumping_freezer_before_after.append(exp0_zoom_jumping1)
                     exp0_zoom_grooming_freezer_before_after.append(exp0_zoom_grooming1)
                       
             '''Selecting runners'''
             for i in range(len(exp0_zoom_walking1)):
                 exp0_fly1_walking_zoom = np.array(np.array([sum(exp0_zoom_walking1[current : current + n_frame_bin]) for current in range(0, len(exp0_zoom_walking1), n_frame_bin)]) / n_frame_bin)
                 exp0_fly1_walking_zoom_before = sum(exp0_fly1_walking_zoom[:2])
                 exp0_fly1_walking_zoom_after = sum(exp0_fly1_walking_zoom[3:])
                 if exp0_fly1_walking_zoom_before > 1 and exp0_fly1_walking_zoom_after > 1:
                     exp0_zoom_pxchange_runner_before_after.append(exp0_zoom_px1)
                     exp0_zoom_velocity_runner_before_after.append(exp0_zoom_vel1)
                     exp0_zoom_vel_2d_runner_before_after.append(exp0_zoom_vel2d1)
                     exp0_zoom_walking_runner_before_after.append(exp0_zoom_walking1)
                     exp0_zoom_walk_vel_runner_before_after.append(exp0_zoom_walk_vel1)
                     exp0_zoom_freezing_runner_before_after.append(exp0_zoom_freezing1)
                     exp0_zoom_jumping_runner_before_after.append(exp0_zoom_jumping1)
                     exp0_zoom_grooming_runner_before_after.append(exp0_zoom_grooming1)

exp0_header_name = str(exp0_header)


'''
RASTER PLOTS VARIABLES
'''

exp0_x_position_array = np.squeeze((np.asarray([exp0_x_position])), axis = 0)
exp0_x_position_output = np.transpose(exp0_x_position_array)

exp0_y_position_array = np.squeeze((np.asarray([exp0_y_position])), axis = 0)
exp0_y_position_output = np.transpose(exp0_y_position_array)

exp0_pxchange_array = np.squeeze((np.asarray([exp0_pxchange])), axis = 0)
exp0_pxchange_output = np.transpose(exp0_pxchange_array)


exp0_velocity_array = np.squeeze((np.asarray([exp0_velocity])), axis = 0)
exp0_velocity_output = np.transpose(exp0_velocity_array)
exp0_velocity_average = np.array(np.array([sum(exp0_velocity_array[i] for i in range(len(exp0_velocity_array)))]) / [len(exp0_velocity_array)])
exp0_velocity_avgraster = np.squeeze(np.transpose(exp0_velocity_average))
exp0_velocity_bined = np.array(np.array([sum(exp0_velocity_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp0_vel_2d_array = np.squeeze((np.asarray([exp0_vel_2d])), axis = 0)
exp0_vel_2d_output = np.transpose(exp0_vel_2d_array)

exp0_walk_vel_array = np.squeeze((np.asarray([exp0_walk_vel])), axis = 0)
exp0_walk_vel_output = np.transpose(exp0_walk_vel_array)
exp0_walk_vel_numberflys = np.sum(np.array(exp0_walk_vel_array) > 0, axis=0)
exp0_walk_vel_average = np.array([sum(exp0_walk_vel_array[i] for i in range(len(exp0_walk_vel_array)))] / (exp0_walk_vel_numberflys))
exp0_walk_vel_avgraster = np.squeeze(np.transpose(exp0_walk_vel_average))
exp0_walk_vel_bined = np.array(np.array([sum(exp0_walk_vel_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp0_walking_array = np.squeeze((np.asarray([exp0_walking])), axis=0)
exp0_walking_output = np.transpose(exp0_walking_array)
exp0_walking_average = np.array(np.array([sum(exp0_walking_array[i] for i in range(len(exp0_walking_array)))]) / [len(exp0_walking_array)])
exp0_walking_avgraster = np.squeeze(np.transpose(exp0_walking_average))
exp0_walking_bined = np.array(np.array([sum(exp0_walking_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp0_freezing_array = np.squeeze((np.asarray([exp0_freezing])), axis=0)
exp0_freezing_output = np.transpose(exp0_freezing_array)
exp0_freezing_average = np.array(np.array([sum(exp0_freezing_array[i] for i in range(len(exp0_freezing_array)))]) / [len(exp0_freezing_array)])
exp0_freezing_avgraster = np.squeeze(np.transpose(exp0_freezing_average))
exp0_freezing_bined = np.array(np.array([sum(exp0_freezing_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp0_jumping_array = np.squeeze((np.asarray([exp0_jumping])), axis=0)
exp0_jumping_output = np.transpose(exp0_jumping_array)
exp0_jumping_average = np.array(np.array([sum(exp0_jumping_array[i] for i in range(len(exp0_jumping_array)))]))
exp0_jumping_avgraster = np.squeeze(np.transpose(exp0_jumping_average))
exp0_jumping_bined = np.array(np.array([sum(exp0_jumping_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / (int(len(exp0_jumping_array))))


exp0_bin_jumping_array = np.squeeze((np.asarray([exp0_bin_jumping])), axis=0)
exp0_bin_jumping_output = np.transpose(exp0_bin_jumping_array)
exp0_bin_jumping_average = np.array(np.array([sum(exp0_bin_jumping_array[i] for i in range(len(exp0_bin_jumping_array)))])/ [len(exp0_bin_jumping_array)])
exp0_bin_jumping_avgraster = np.squeeze(np.transpose(exp0_bin_jumping_average))

exp0_grooming_array = np.squeeze((np.asarray([exp0_grooming])), axis=0)
exp0_grooming_output = np.transpose(exp0_grooming_array)
exp0_grooming_average = np.array(np.array([sum(exp0_grooming_array[i] for i in range(len(exp0_grooming_array)))]) / [len(exp0_grooming_array)])
exp0_grooming_avgraster = np.squeeze(np.transpose(exp0_grooming_average))
exp0_grooming_bined = np.array(np.array([sum(exp0_grooming_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)


exp0_zoom_x_position_array = np.squeeze((np.asarray([exp0_zoom_x_position])), axis=0)
exp0_zoom_x_position_output = np.transpose(exp0_zoom_x_position_array)

exp0_zoom_y_position_array = np.squeeze((np.asarray([exp0_zoom_y_position])), axis=0)
exp0_zoom_y_position_output = np.transpose(exp0_zoom_y_position_array)

exp0_zoom_pxchange_array = np.squeeze((np.asarray([exp0_zoom_pxchange])), axis=0)
exp0_zoom_pxchange_output = np.transpose(exp0_zoom_pxchange_array)
exp0_zoom_pxchange_average = np.array(np.array([sum(exp0_zoom_pxchange_array[i] for i in range(len(exp0_zoom_pxchange_array)))]) / [len(exp0_zoom_pxchange_array)])
exp0_zoom_pxchange_avgraster = np.squeeze(np.transpose(exp0_zoom_pxchange_average))
exp0_zoom_pxchange_bined = np.array(np.array([sum(exp0_zoom_pxchange_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


exp0_zoom_velocity_array = np.squeeze((np.asarray([exp0_zoom_velocity])), axis=0)
exp0_zoom_velocity_output = np.transpose(exp0_zoom_velocity_array)
exp0_zoom_velocity_average = np.array(np.array([sum(exp0_zoom_velocity_array[i] for i in range(len(exp0_zoom_velocity_array)))]) / [len(exp0_zoom_velocity_array)])
exp0_zoom_velocity_avgraster = np.squeeze(np.transpose(exp0_zoom_velocity_average))
exp0_zoom_velocity_bined = np.array(np.array([sum(exp0_zoom_pxchange_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_vel_2d_array = np.squeeze((np.asarray([exp0_zoom_vel_2d])), axis=0)
exp0_zoom_vel_2d_output = np.transpose(exp0_zoom_vel_2d_array)
exp0_zoom_vel_2d_numberflys = np.sum(np.array(exp0_zoom_vel_2d_array) > 0, axis=0)
exp0_zoom_vel_2d_average = np.array([sum(exp0_zoom_vel_2d_array[i] for i in range(len(exp0_zoom_vel_2d_array)))] / (exp0_zoom_vel_2d_numberflys))
exp0_zoom_vel_2d_avgraster = np.squeeze(np.transpose(exp0_zoom_vel_2d_average))
exp0_zoom_vel_2d_bined = np.array(np.array([sum(exp0_zoom_vel_2d_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_walk_vel_array = np.squeeze((np.asarray([exp0_zoom_walk_vel])), axis=0)
exp0_zoom_walk_vel_output = np.transpose(exp0_zoom_walk_vel_array)
exp0_zoom_walk_vel_numberflys = np.sum(np.array(exp0_zoom_walk_vel_array) > 0, axis=0)
exp0_zoom_walk_vel_average = np.array([sum(exp0_zoom_walk_vel_array[i] for i in range(len(exp0_zoom_walk_vel_array)))] / (exp0_zoom_walk_vel_numberflys))
exp0_zoom_walk_vel_avgraster = np.squeeze(np.transpose(exp0_zoom_walk_vel_average))
exp0_zoom_walk_vel_bined = np.array(np.array([sum(exp0_zoom_walk_vel_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_walking_array = np.squeeze((np.asarray([exp0_zoom_walking])), axis=0)
exp0_zoom_walking_output = np.transpose(exp0_zoom_walking_array)
exp0_zoom_walking_average = np.array(np.array([sum(exp0_zoom_walking_array[i] for i in range(len(exp0_zoom_walking_array)))]) / [len(exp0_zoom_walking_array)])
exp0_zoom_walking_avgraster = np.squeeze(np.transpose(exp0_zoom_walking_average))
exp0_zoom_walking_bined = np.array(np.array([sum(exp0_zoom_walking_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


exp0_zoom_freezing_array = np.squeeze((np.asarray([exp0_zoom_freezing])), axis=0)
exp0_zoom_freezing_output = np.transpose(exp0_zoom_freezing_array)
exp0_zoom_freezing_average = np.array(np.array([sum(exp0_zoom_freezing_array[i] for i in range(len(exp0_zoom_freezing_array)))]) / [len(exp0_zoom_freezing_array)])
exp0_zoom_freezing_avgraster = np.squeeze(np.transpose(exp0_zoom_freezing_average))
exp0_zoom_freezing_bined = np.array(np.array([sum(exp0_zoom_freezing_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_jumping_array = np.squeeze((np.asarray([exp0_zoom_jumping])), axis=0)
exp0_zoom_jumping_output = np.transpose(exp0_zoom_jumping_array)
exp0_zoom_jumping_average = np.array(np.array([sum(exp0_zoom_jumping_array[i] for i in range(len(exp0_zoom_jumping_array)))])/ [len(exp0_zoom_freezing_array)])
exp0_zoom_jumping_avgraster = np.squeeze(np.transpose(exp0_zoom_jumping_average))
exp0_zoom_jumping_bined = np.array(np.array([sum(exp0_zoom_jumping_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


exp0_zoom_grooming_array = np.squeeze((np.asarray([exp0_zoom_grooming])), axis=0)
exp0_zoom_grooming_output = np.transpose(exp0_zoom_grooming_array)
exp0_zoom_grooming_average = np.array(np.array([sum(exp0_zoom_grooming_array[i] for i in range(len(exp0_zoom_grooming_array)))]) / [len(exp0_zoom_grooming_array)])
exp0_zoom_grooming_avgraster = np.squeeze(np.transpose(exp0_zoom_grooming_average))
exp0_zoom_grooming_bined = np.array(np.array([sum(exp0_zoom_grooming_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_pxchange_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_pxchange_freezer_before_after])), axis=0)
exp0_zoom_pxchange_freezer_before_after_output = np.transpose(exp0_zoom_pxchange_freezer_before_after_array)
exp0_zoom_pxchange_freezer_before_after_average = np.array(np.array([sum(exp0_zoom_pxchange_freezer_before_after_array[i] for i in range(len(exp0_zoom_pxchange_freezer_before_after_array)))]) / [len(exp0_zoom_pxchange_freezer_before_after_array)])
exp0_zoom_pxchange_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_pxchange_freezer_before_after_average))
exp0_zoom_pxchange_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_pxchange_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_velocity_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_velocity_freezer_before_after])), axis=0)
exp0_zoom_velocity_freezer_before_after_output = np.transpose(exp0_zoom_velocity_freezer_before_after_array)
exp0_zoom_velocity_freezer_before_after_average = np.array(np.array([sum(exp0_zoom_velocity_freezer_before_after_array[i] for i in range(len(exp0_zoom_velocity_freezer_before_after_array)))]) / [len(exp0_zoom_velocity_freezer_before_after_array)])
exp0_zoom_velocity_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_velocity_freezer_before_after_average))
exp0_zoom_velocity_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_velocity_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_vel_2d_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_vel_2d_freezer_before_after])), axis=0)
exp0_zoom_vel_2d_freezer_before_after_output = np.transpose(exp0_zoom_vel_2d_freezer_before_after_array)
exp0_zoom_vel_2d_freezer_before_after_numberflys = np.sum(np.array(exp0_zoom_vel_2d_freezer_before_after_array) > 0, axis=0)
exp0_zoom_vel_2d_freezer_before_after_average = np.array([sum(exp0_zoom_vel_2d_freezer_before_after_array[i] for i in range(len(exp0_zoom_vel_2d_freezer_before_after_array)))] / (exp0_zoom_vel_2d_freezer_before_after_numberflys))
exp0_zoom_vel_2d_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_vel_2d_freezer_before_after_average))
exp0_zoom_vel_2d_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_vel_2d_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_walk_vel_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_walk_vel_freezer_before_after])), axis=0)
exp0_zoom_walk_vel_freezer_before_after_output = np.transpose(exp0_zoom_walk_vel_freezer_before_after_array)
exp0_zoom_walk_vel_freezer_before_after_numberflys = np.sum(np.array(exp0_zoom_walk_vel_freezer_before_after_array) > 0, axis=0)
exp0_zoom_walk_vel_freezer_before_after_average = np.array([sum(exp0_zoom_walk_vel_freezer_before_after_array[i] for i in range(len(exp0_zoom_walk_vel_freezer_before_after_array)))] / (exp0_zoom_walk_vel_freezer_before_after_numberflys))
exp0_zoom_walk_vel_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_walk_vel_freezer_before_after_average))
exp0_zoom_walk_vel_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_walk_vel_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_walking_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_walking_freezer_before_after])), axis=0)
exp0_zoom_walking_freezer_before_after_output = np.transpose(exp0_zoom_walking_freezer_before_after_array)
exp0_zoom_walking_freezer_before_after_average = np.array(np.array([sum(exp0_zoom_walking_freezer_before_after_array[i] for i in range(len(exp0_zoom_walking_freezer_before_after_array)))]) / [len(exp0_zoom_walking_freezer_before_after_array)])
exp0_zoom_walking_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_walking_freezer_before_after_average))
exp0_zoom_walking_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_walking_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_freezing_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_freezing_freezer_before_after])), axis=0)
exp0_zoom_freezing_freezer_before_after_output = np.transpose(exp0_zoom_freezing_freezer_before_after_array)
exp0_zoom_freezing_freezer_before_after_average = np.array(np.array([sum(exp0_zoom_freezing_freezer_before_after_array[i] for i in range(len(exp0_zoom_freezing_freezer_before_after_array)))]) / [len(exp0_zoom_freezing_freezer_before_after_array)])
exp0_zoom_freezing_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_freezing_freezer_before_after_average))
exp0_zoom_freezing_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_freezing_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_jumping_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_jumping_freezer_before_after])), axis=0)
exp0_zoom_jumping_freezer_before_after_output = np.transpose(exp0_zoom_jumping_freezer_before_after_array)
exp0_zoom_jumping_freezer_before_after_average = np.array(np.array([sum(exp0_zoom_jumping_freezer_before_after_array[i] for i in range(len(exp0_zoom_jumping_freezer_before_after_array)))]))
exp0_zoom_jumping_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_jumping_freezer_before_after_average))
exp0_zoom_jumping_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_jumping_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)])/ (len(exp0_zoom_jumping_freezer_before_after_array)))

exp0_zoom_grooming_freezer_before_after_array = np.squeeze((np.asarray([exp0_zoom_grooming_freezer_before_after])), axis=0)
exp0_zoom_grooming_freezer_before_after_output = np.transpose(exp0_zoom_grooming_freezer_before_after_array)
exp0_zoom_grooming_freezer_before_after_average = np.array(np.array([sum(exp0_zoom_grooming_freezer_before_after_array[i] for i in range(len(exp0_zoom_grooming_freezer_before_after_array)))]) / [len(exp0_zoom_grooming_freezer_before_after_array)])
exp0_zoom_grooming_freezer_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_grooming_freezer_before_after_average))
exp0_zoom_grooming_freezer_before_after_bined = np.array(np.array([sum(exp0_zoom_grooming_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_pxchange_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_pxchange_runner_before_after])), axis=0)
exp0_zoom_pxchange_runner_before_after_output = np.transpose(exp0_zoom_pxchange_runner_before_after_array)
exp0_zoom_pxchange_runner_before_after_average = np.array(np.array([sum(exp0_zoom_pxchange_runner_before_after_array[i] for i in range(len(exp0_zoom_pxchange_runner_before_after_array)))]) / [len(exp0_zoom_pxchange_runner_before_after_array)])
exp0_zoom_pxchange_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_pxchange_runner_before_after_average))
exp0_zoom_pxchange_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_pxchange_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_velocity_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_velocity_runner_before_after])), axis=0)
exp0_zoom_velocity_runner_before_after_output = np.transpose(exp0_zoom_velocity_runner_before_after_array)
exp0_zoom_velocity_runner_before_after_average = np.array(np.array([sum(exp0_zoom_velocity_runner_before_after_array[i] for i in range(len(exp0_zoom_velocity_runner_before_after_array)))]) / [len(exp0_zoom_velocity_runner_before_after_array)])
exp0_zoom_velocity_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_velocity_runner_before_after_average))
exp0_zoom_velocity_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_velocity_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_vel_2d_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_vel_2d_runner_before_after])), axis=0)
exp0_zoom_vel_2d_runner_before_after_output = np.transpose(exp0_zoom_vel_2d_runner_before_after_array)
exp0_zoom_vel_2d_runner_before_after_numberflys = np.sum(np.array(exp0_zoom_vel_2d_runner_before_after_array) > 0, axis=0)
exp0_zoom_vel_2d_runner_before_after_average = np.array([sum(exp0_zoom_vel_2d_runner_before_after_array[i] for i in range(len(exp0_zoom_vel_2d_runner_before_after_array)))] / (exp0_zoom_vel_2d_runner_before_after_numberflys))
exp0_zoom_vel_2d_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_vel_2d_runner_before_after_average))
exp0_zoom_vel_2d_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_vel_2d_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_walk_vel_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_walk_vel_runner_before_after])), axis=0)
exp0_zoom_walk_vel_runner_before_after_output = np.transpose(exp0_zoom_walk_vel_runner_before_after_array)
exp0_zoom_walk_vel_runner_before_after_numberflys = np.sum(np.array(exp0_zoom_walk_vel_runner_before_after_array) > 0, axis=0)
exp0_zoom_walk_vel_runner_before_after_average = np.array([sum(exp0_zoom_walk_vel_runner_before_after_array[i] for i in range(len(exp0_zoom_walk_vel_runner_before_after_array)))] / (exp0_zoom_walk_vel_runner_before_after_numberflys))
exp0_zoom_walk_vel_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_walk_vel_runner_before_after_average))
exp0_zoom_walk_vel_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_walk_vel_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_walking_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_walking_runner_before_after])), axis=0)
exp0_zoom_walking_runner_before_after_output = np.transpose(exp0_zoom_walking_runner_before_after_array)
exp0_zoom_walking_runner_before_after_average = np.array(np.array([sum(exp0_zoom_walking_runner_before_after_array[i] for i in range(len(exp0_zoom_walking_runner_before_after_array)))]) / [len(exp0_zoom_walking_runner_before_after_array)])
exp0_zoom_walking_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_walking_runner_before_after_average))
exp0_zoom_walking_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_walking_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_freezing_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_freezing_runner_before_after])), axis=0)
exp0_zoom_freezing_runner_before_after_output = np.transpose(exp0_zoom_freezing_runner_before_after_array)
exp0_zoom_freezing_runner_before_after_average = np.array(np.array([sum(exp0_zoom_freezing_runner_before_after_array[i] for i in range(len(exp0_zoom_freezing_runner_before_after_array)))]) / [len(exp0_zoom_freezing_runner_before_after_array)])
exp0_zoom_freezing_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_freezing_runner_before_after_average))
exp0_zoom_freezing_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_freezing_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp0_zoom_jumping_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_jumping_runner_before_after])), axis=0)
exp0_zoom_jumping_runner_before_after_output = np.transpose(exp0_zoom_jumping_runner_before_after_array)
exp0_zoom_jumping_runner_before_after_average = np.array(np.array([sum(exp0_zoom_jumping_runner_before_after_array[i] for i in range(len(exp0_zoom_jumping_runner_before_after_array)))]))
exp0_zoom_jumping_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_jumping_runner_before_after_average))
exp0_zoom_jumping_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_jumping_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / (len(exp0_zoom_jumping_runner_before_after_array)))

exp0_zoom_grooming_runner_before_after_array = np.squeeze((np.asarray([exp0_zoom_grooming_runner_before_after])), axis=0)
exp0_zoom_grooming_runner_before_after_output = np.transpose(exp0_zoom_grooming_runner_before_after_array)
exp0_zoom_grooming_runner_before_after_average = np.array(np.array([sum(exp0_zoom_grooming_runner_before_after_array[i] for i in range(len(exp0_zoom_grooming_runner_before_after_array)))]) / [len(exp0_zoom_grooming_runner_before_after_array)])
exp0_zoom_grooming_runner_before_after_avgraster = np.squeeze(np.transpose(exp0_zoom_grooming_runner_before_after_average))
exp0_zoom_grooming_runner_before_after_bined = np.array(np.array([sum(exp0_zoom_grooming_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


'''
VIOLIN PLOTS VARIABLES
'''

exp0_base_walk_vel = exp0_walk_vel_output[:baseline_frames]
exp0_base_walk_vel_exclude = np.count_nonzero(exp0_base_walk_vel, axis = 0)
exp0_base_walk_vel_all = np.array(sum(exp0_base_walk_vel[i] for i in range(len(exp0_base_walk_vel))))
exp0_base_walk_vel_nan = np.array(exp0_base_walk_vel_all / exp0_base_walk_vel_exclude)
exp0_base_walk_vel_exclude_nan = exp0_base_walk_vel_nan[~np.isnan(exp0_base_walk_vel_nan)]
exp0_base_walk_vel_outliers = exp0_base_walk_vel_exclude_nan[~is_outlier(exp0_base_walk_vel_exclude_nan)]
exp0_base_walk_vel_df2 = pd.DataFrame(exp0_base_walk_vel_outliers)
exp0_base_walk_vel_df2.columns = [str(experiment0)]

exp0_stim_walk_vel = exp0_walk_vel_output[baseline_frames:]
exp0_stim_walk_vel_exclude = np.count_nonzero(exp0_stim_walk_vel, axis = 0)
exp0_stim_walk_vel_all = np.array(sum(exp0_stim_walk_vel[i] for i in range(len(exp0_stim_walk_vel))))
exp0_stim_walk_vel_nan = np.array(exp0_stim_walk_vel_all / exp0_stim_walk_vel_exclude)
exp0_stim_walk_vel_exclude_nan = exp0_stim_walk_vel_nan[~np.isnan(exp0_stim_walk_vel_nan)]
exp0_stim_walk_vel_outliers = exp0_stim_walk_vel_exclude_nan[~is_outlier(exp0_stim_walk_vel_exclude_nan)]
exp0_stim_walk_vel_df2 = pd.DataFrame(exp0_stim_walk_vel_outliers)
exp0_stim_walk_vel_df2.columns = [str(experiment0)]

exp0_base_walking = exp0_walking_output[:baseline_frames]
exp0_base_walking_all = np.array(sum(exp0_base_walking[i] for i in range(len(exp0_base_walking))))
exp0_base_walking_nan = np.array(exp0_base_walking_all / (len(exp0_base_walking)))
exp0_base_walking_outliers = exp0_base_walking_nan[~is_outlier(exp0_base_walking_nan)]
exp0_base_walking_df2 = pd.DataFrame(exp0_base_walking_outliers * 100)
exp0_base_walking_df2.columns = [str(experiment0)]

exp0_stim_walking = exp0_walking_output[baseline_frames:]
exp0_stim_walking_all = np.array(sum(exp0_stim_walking[i] for i in range(len(exp0_stim_walking))))
exp0_stim_walking_nan = np.array(exp0_stim_walking_all / (len(exp0_stim_walking)))
exp0_stim_walking_outliers = exp0_stim_walking_nan[~is_outlier(exp0_stim_walking_nan)]
exp0_stim_walking_df2 = pd.DataFrame(exp0_stim_walking_outliers * 100)
exp0_stim_walking_df2.columns = [str(experiment0)]


exp0_base_freezing = exp0_freezing_output[:baseline_frames]
exp0_base_freezing_all = np.array(sum(exp0_base_freezing[i] for i in range(len(exp0_base_freezing))))
exp0_base_freezing_nan = np.array(exp0_base_freezing_all / (len(exp0_base_freezing)))
exp0_base_freezing_outliers = exp0_base_freezing_nan[~is_outlier(exp0_base_freezing_nan)]
exp0_base_freezing_df2 = pd.DataFrame(exp0_base_freezing_outliers * 100)
exp0_base_freezing_df2.columns = [str(experiment0)]

exp0_stim_freezing = exp0_freezing_output[baseline_frames:]
exp0_stim_freezing_all = np.array(sum(exp0_stim_freezing[i] for i in range(len(exp0_stim_freezing))))
exp0_stim_freezing_nan = np.array(exp0_stim_freezing_all / (len(exp0_stim_freezing)))
exp0_stim_freezing_outliers = exp0_stim_freezing_nan[~is_outlier(exp0_stim_freezing_nan)]
exp0_stim_freezing_df2 = pd.DataFrame(exp0_stim_freezing_outliers * 100)
exp0_stim_freezing_df2.columns = [str(experiment0)]


exp0_base_grooming = exp0_grooming_output[:baseline_frames]
exp0_base_grooming_all = np.array(sum(exp0_base_grooming[i] for i in range(len(exp0_base_grooming))))
exp0_base_grooming_nan = np.array(exp0_base_grooming_all / (len(exp0_base_grooming)))
exp0_base_grooming_outliers = exp0_base_grooming_nan[~is_outlier(exp0_base_grooming_nan)]
exp0_base_grooming_df2 = pd.DataFrame(exp0_base_grooming_outliers * 100)
exp0_base_grooming_df2.columns = [str(experiment0)]

exp0_stim_grooming = exp0_grooming_output[baseline_frames:]
exp0_stim_grooming_all = np.array(sum(exp0_stim_grooming[i] for i in range(len(exp0_stim_grooming))))
exp0_stim_grooming_nan = np.array(exp0_stim_grooming_all / (len(exp0_stim_grooming)))
exp0_stim_grooming_outliers = exp0_stim_grooming_nan[~is_outlier(exp0_stim_grooming_nan)]
exp0_stim_grooming_df2 = pd.DataFrame(exp0_stim_grooming_outliers * 100)
exp0_stim_grooming_df2.columns = [str(experiment0)]




''' FRAMES '''
exp1_header = []
exp1_looming = []
exp1_redled = []
exp1_greenled = []
exp1_x_position = []
exp1_y_position = []
exp1_pxchange = []
exp1_velocity = []
exp1_vel_2d = []
exp1_walk_vel = []
exp1_walking = []
exp1_freezing = []
exp1_jumping = []
exp1_bin_jumping = []
exp1_grooming = []

''' ZOOM '''
exp1_zoom_looming = []
exp1_zoom_redled = []
exp1_zoom_greenled = []
exp1_zoom_x_position = []
exp1_zoom_y_position = []
exp1_zoom_pxchange = []
exp1_zoom_velocity = []
exp1_zoom_vel_2d = []
exp1_zoom_walk_vel = []
exp1_zoom_walking = []
exp1_zoom_freezing = []
exp1_zoom_jumping = []
exp1_zoom_grooming = []

'''CONDITIONAL ZOOM'''
exp1_zoom_pxchange_freezer_before_after = []
exp1_zoom_velocity_freezer_before_after = []
exp1_zoom_vel_2d_freezer_before_after = []
exp1_zoom_walk_vel_freezer_before_after = []
exp1_zoom_walking_freezer_before_after = []
exp1_zoom_freezing_freezer_before_after = []
exp1_zoom_jumping_freezer_before_after = []
exp1_zoom_grooming_freezer_before_after = []

exp1_zoom_pxchange_runner_before_after = []
exp1_zoom_velocity_runner_before_after = []
exp1_zoom_vel_2d_runner_before_after = []
exp1_zoom_walk_vel_runner_before_after = []
exp1_zoom_walking_runner_before_after = []
exp1_zoom_freezing_runner_before_after = []
exp1_zoom_jumping_runner_before_after = []
exp1_zoom_grooming_runner_before_after = []


for filename in glob.glob(os.path.join(path , (str(experiment1)+'*scored_frames.csv'))):
     first, scored, extention = filename.split('.', 2)
     location, exp1_file_name = first.split('\\', 1)
     exp1_line, exp1_protocol, exp1_date = exp1_file_name.split('-' , 2)
     exp1_outputname = location+'\\'+exp1_line+'-'+exp1_protocol+'-'+exp1_date
     
     raw = pd.read_csv(filename,',', header = None)
     number_frames = len(raw)
     
     '''HEADER'''
     exp1_fly = exp1_file_name
     exp1_header.append(exp1_fly)
     
     
     '''LOOMING'''
     #FRAMES
     exp1_looming_data = pd.DataFrame({'loom':raw[0]})
     exp1_loom1 = exp1_looming_data['loom'].tolist()
     exp1_looming.append(exp1_loom1)
     
     
     '''RED LED'''
     #FRAMES
     exp1_redled_data = pd.DataFrame({'redled':raw[1]})
     exp1_red1 = exp1_redled_data['redled'].tolist()
     exp1_redled.append(exp1_red1)

     
     '''GREEN LED'''
     #FRAMES
     exp1_greenled_data = pd.DataFrame({'greenled':raw[2]})
     exp1_green1 = exp1_greenled_data['greenled'].tolist()
     exp1_greenled.append(exp1_green1)
  
     
     '''X POSITION'''
     exp1_x_position_data = pd.DataFrame({'xpos1':raw[3]})
     exp1_xpos1 = exp1_x_position_data['xpos1'].tolist()
     exp1_x_position.append(exp1_xpos1)

    
     '''Y POSITION'''
     exp1_y_position_data = pd.DataFrame({'ypos1':raw[4]})
     exp1_ypos1 = exp1_y_position_data['ypos1'].tolist()
     exp1_y_position.append(exp1_ypos1)


     '''PIXEL CHANGE'''
     exp1_pxchange_data = pd.DataFrame({'px1':raw[5]})
     exp1_px1 = exp1_pxchange_data['px1'].tolist()
     exp1_pxchange.append(exp1_px1)
     
     
     '''VELOCITY'''
     #FRAMES
     exp1_velocity_data = pd.DataFrame({'vel1':raw[6]})
     exp1_vel1 = exp1_velocity_data['vel1'].tolist()
     exp1_velocity.append(exp1_vel1)
     
     
     '''Velocity 2d'''
     exp1_vel2d1 = [exp1_vel1[i] if exp1_vel1[i] <= jump_velocity else 0 for i in range(number_frames)]     
     exp1_vel_2d.append(exp1_vel2d1)
     
     
     '''WALKING VELOCITY'''
     #FRAMES
     exp1_walking_data = pd.DataFrame({'walk1':raw[7]})
     exp1_walk1 = exp1_walking_data['walk1'].tolist()
     exp1_walking_to_vel1 = np.array([exp1_vel1[i] if exp1_walk1[i] == 1 else 0 for i in range(number_frames)])       
     
     exp1_walking.append(exp1_walk1)
     exp1_walk_vel.append(exp1_walking_to_vel1)
      
     
     '''FREEZING'''
     #FRAMES
     exp1_freezing_data = pd.DataFrame({'fre1':raw[8]})
     exp1_fre1 = exp1_freezing_data['fre1'].tolist()
     exp1_freezing.append(exp1_fre1)


     '''JUMPING'''
     #FRAMES     
     exp1_jumping_data = pd.DataFrame({'jum1':raw[9]})
     exp1_jum1 = exp1_jumping_data['jum1'].tolist()
     exp1_jumping.append(exp1_jum1)
     
     #BINS - SUM OF JUMPS
     exp1_fly1_jump_bins = np.array([sum(exp1_jum1[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)])
     exp1_bin_jumping.append(exp1_fly1_jump_bins)

    
     '''GROOMING'''
     #FRAMES
     exp1_grooming_data = pd.DataFrame({'gro1':raw[10]})
     exp1_gro1 = exp1_grooming_data['gro1'].tolist()
     exp1_grooming.append(exp1_gro1)

     
     '''ZOOMS'''
     for i in range(len(exp1_loom1)):
         if exp1_loom1[i] == 1 and exp1_loom1[i-1] == 0:
             exp1_loom_loom_onset1 = i

             exp1_zoom_loom1 = exp1_loom1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_looming.append(exp1_zoom_loom1)   
             number_frames_zoom = len(exp1_zoom_loom1)

             exp1_zoom_red1 = exp1_red1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_redled.append(exp1_zoom_red1)

             exp1_zoom_green1 = exp1_green1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_greenled.append(exp1_zoom_green1)

             exp1_zoom_xpos1 = exp1_xpos1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_x_position.append(exp1_zoom_xpos1)
             
             exp1_zoom_ypos1 = exp1_ypos1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_y_position.append(exp1_zoom_ypos1)
             
             exp1_zoom_px1 = exp1_px1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_pxchange.append(exp1_zoom_px1)
             
             exp1_zoom_vel1 = exp1_vel1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_velocity.append(exp1_zoom_vel1)
             
             exp1_zoom_vel2d1 = exp1_vel2d1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_vel_2d.append(exp1_zoom_vel2d1)

             exp1_zoom_walking1 = exp1_walk1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_walking.append(exp1_zoom_walking1)
             
             exp1_zoom_walk_vel1 = exp1_walking_to_vel1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_walk_vel.append(exp1_zoom_walk_vel1)

             exp1_zoom_freezing1 = exp1_fre1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_freezing.append(exp1_zoom_freezing1)

             exp1_zoom_jumping1 = exp1_jum1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_jumping.append(exp1_zoom_jumping1)

             exp1_zoom_grooming1 = exp1_gro1[(exp1_loom_loom_onset1-zoom_before_loom_onset):(exp1_loom_loom_onset1+zoom_after_loom_onset)]
             exp1_zoom_grooming.append(exp1_zoom_grooming1)
             
             '''Selecting freezers'''
             for i in range(len(exp1_zoom_freezing1)):
                 exp1_fly1_freezing_zoom = np.array(np.array([sum(exp1_zoom_freezing1[current : current + n_frame_bin]) for current in range(0, len(exp1_zoom_freezing1), n_frame_bin)]) / n_frame_bin)
                 exp1_fly1_freezing_zoom_before = sum(exp1_fly1_freezing_zoom[:2])
                 exp1_fly1_freezing_zoom_after = sum(exp1_fly1_freezing_zoom[3:])
                 if exp1_fly1_freezing_zoom_before > 1 and exp1_fly1_freezing_zoom_after > 1:
                     exp1_zoom_pxchange_freezer_before_after.append(exp1_zoom_px1)
                     exp1_zoom_velocity_freezer_before_after.append(exp1_zoom_vel1)
                     exp1_zoom_vel_2d_freezer_before_after.append(exp1_zoom_vel2d1)
                     exp1_zoom_walking_freezer_before_after.append(exp1_zoom_walking1)
                     exp1_zoom_walk_vel_freezer_before_after.append(exp1_zoom_walk_vel1)
                     exp1_zoom_freezing_freezer_before_after.append(exp1_zoom_freezing1)
                     exp1_zoom_jumping_freezer_before_after.append(exp1_zoom_jumping1)
                     exp1_zoom_grooming_freezer_before_after.append(exp1_zoom_grooming1)
                       
             '''Selecting runners'''
             for i in range(len(exp1_zoom_walking1)):
                 exp1_fly1_walking_zoom = np.array(np.array([sum(exp1_zoom_walking1[current : current + n_frame_bin]) for current in range(0, len(exp1_zoom_walking1), n_frame_bin)]) / n_frame_bin)
                 exp1_fly1_walking_zoom_before = sum(exp1_fly1_walking_zoom[:2])
                 exp1_fly1_walking_zoom_after = sum(exp1_fly1_walking_zoom[3:])
                 if exp1_fly1_walking_zoom_before > 1 and exp1_fly1_walking_zoom_after > 1:
                     exp1_zoom_pxchange_runner_before_after.append(exp1_zoom_px1)
                     exp1_zoom_velocity_runner_before_after.append(exp1_zoom_vel1)
                     exp1_zoom_vel_2d_runner_before_after.append(exp1_zoom_vel2d1)
                     exp1_zoom_walking_runner_before_after.append(exp1_zoom_walking1)
                     exp1_zoom_walk_vel_runner_before_after.append(exp1_zoom_walk_vel1)
                     exp1_zoom_freezing_runner_before_after.append(exp1_zoom_freezing1)
                     exp1_zoom_jumping_runner_before_after.append(exp1_zoom_jumping1)
                     exp1_zoom_grooming_runner_before_after.append(exp1_zoom_grooming1)

exp1_header_name = str(exp1_header)


'''
RASTER PLOTS VARIABLES
'''

exp1_x_position_array = np.squeeze((np.asarray([exp1_x_position])), axis = 0)
exp1_x_position_output = np.transpose(exp1_x_position_array)

exp1_y_position_array = np.squeeze((np.asarray([exp1_y_position])), axis = 0)
exp1_y_position_output = np.transpose(exp1_y_position_array)

exp1_pxchange_array = np.squeeze((np.asarray([exp1_pxchange])), axis = 0)
exp1_pxchange_output = np.transpose(exp1_pxchange_array)


exp1_velocity_array = np.squeeze((np.asarray([exp1_velocity])), axis = 0)
exp1_velocity_output = np.transpose(exp1_velocity_array)
exp1_velocity_average = np.array(np.array([sum(exp1_velocity_array[i] for i in range(len(exp1_velocity_array)))]) / [len(exp1_velocity_array)])
exp1_velocity_avgraster = np.squeeze(np.transpose(exp1_velocity_average))
exp1_velocity_bined = np.array(np.array([sum(exp1_velocity_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp1_vel_2d_array = np.squeeze((np.asarray([exp1_vel_2d])), axis = 0)
exp1_vel_2d_output = np.transpose(exp1_vel_2d_array)

exp1_walk_vel_array = np.squeeze((np.asarray([exp1_walk_vel])), axis = 0)
exp1_walk_vel_output = np.transpose(exp1_walk_vel_array)
exp1_walk_vel_numberflys = np.sum(np.array(exp1_walk_vel_array) > 0, axis=0)
exp1_walk_vel_average = np.array([sum(exp1_walk_vel_array[i] for i in range(len(exp1_walk_vel_array)))] / (exp1_walk_vel_numberflys))
exp1_walk_vel_avgraster = np.squeeze(np.transpose(exp1_walk_vel_average))
exp1_walk_vel_bined = np.array(np.array([sum(exp1_walk_vel_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp1_walking_array = np.squeeze((np.asarray([exp1_walking])), axis=0)
exp1_walking_output = np.transpose(exp1_walking_array)
exp1_walking_average = np.array(np.array([sum(exp1_walking_array[i] for i in range(len(exp1_walking_array)))]) / [len(exp1_walking_array)])
exp1_walking_avgraster = np.squeeze(np.transpose(exp1_walking_average))
exp1_walking_bined = np.array(np.array([sum(exp1_walking_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp1_freezing_array = np.squeeze((np.asarray([exp1_freezing])), axis=0)
exp1_freezing_output = np.transpose(exp1_freezing_array)
exp1_freezing_average = np.array(np.array([sum(exp1_freezing_array[i] for i in range(len(exp1_freezing_array)))]) / [len(exp1_freezing_array)])
exp1_freezing_avgraster = np.squeeze(np.transpose(exp1_freezing_average))
exp1_freezing_bined = np.array(np.array([sum(exp1_freezing_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)

exp1_jumping_array = np.squeeze((np.asarray([exp1_jumping])), axis=0)
exp1_jumping_output = np.transpose(exp1_jumping_array)
exp1_jumping_average = np.array(np.array([sum(exp1_jumping_array[i] for i in range(len(exp1_jumping_array)))]))
exp1_jumping_avgraster = np.squeeze(np.transpose(exp1_jumping_average))
exp1_jumping_bined = np.array(np.array([sum(exp1_jumping_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / (int(len(exp1_jumping_array))))


exp1_bin_jumping_array = np.squeeze((np.asarray([exp1_bin_jumping])), axis=0)
exp1_bin_jumping_output = np.transpose(exp1_bin_jumping_array)
exp1_bin_jumping_average = np.array(np.array([sum(exp1_bin_jumping_array[i] for i in range(len(exp1_bin_jumping_array)))])/ [len(exp1_bin_jumping_array)])
exp1_bin_jumping_avgraster = np.squeeze(np.transpose(exp1_bin_jumping_average))

exp1_grooming_array = np.squeeze((np.asarray([exp1_grooming])), axis=0)
exp1_grooming_output = np.transpose(exp1_grooming_array)
exp1_grooming_average = np.array(np.array([sum(exp1_grooming_array[i] for i in range(len(exp1_grooming_array)))]) / [len(exp1_grooming_array)])
exp1_grooming_avgraster = np.squeeze(np.transpose(exp1_grooming_average))
exp1_grooming_bined = np.array(np.array([sum(exp1_grooming_avgraster[current : current + n_frame_bin]) for current in range(0, number_frames, n_frame_bin)]) / n_frame_bin)


exp1_zoom_x_position_array = np.squeeze((np.asarray([exp1_zoom_x_position])), axis=0)
exp1_zoom_x_position_output = np.transpose(exp1_zoom_x_position_array)

exp1_zoom_y_position_array = np.squeeze((np.asarray([exp1_zoom_y_position])), axis=0)
exp1_zoom_y_position_output = np.transpose(exp1_zoom_y_position_array)

exp1_zoom_pxchange_array = np.squeeze((np.asarray([exp1_zoom_pxchange])), axis=0)
exp1_zoom_pxchange_output = np.transpose(exp1_zoom_pxchange_array)
exp1_zoom_pxchange_average = np.array(np.array([sum(exp1_zoom_pxchange_array[i] for i in range(len(exp1_zoom_pxchange_array)))]) / [len(exp1_zoom_pxchange_array)])
exp1_zoom_pxchange_avgraster = np.squeeze(np.transpose(exp1_zoom_pxchange_average))
exp1_zoom_pxchange_bined = np.array(np.array([sum(exp1_zoom_pxchange_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


exp1_zoom_velocity_array = np.squeeze((np.asarray([exp1_zoom_velocity])), axis=0)
exp1_zoom_velocity_output = np.transpose(exp1_zoom_velocity_array)
exp1_zoom_velocity_average = np.array(np.array([sum(exp1_zoom_velocity_array[i] for i in range(len(exp1_zoom_velocity_array)))]) / [len(exp1_zoom_velocity_array)])
exp1_zoom_velocity_avgraster = np.squeeze(np.transpose(exp1_zoom_velocity_average))
exp1_zoom_velocity_bined = np.array(np.array([sum(exp1_zoom_pxchange_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_vel_2d_array = np.squeeze((np.asarray([exp1_zoom_vel_2d])), axis=0)
exp1_zoom_vel_2d_output = np.transpose(exp1_zoom_vel_2d_array)
exp1_zoom_vel_2d_numberflys = np.sum(np.array(exp1_zoom_vel_2d_array) > 0, axis=0)
exp1_zoom_vel_2d_average = np.array([sum(exp1_zoom_vel_2d_array[i] for i in range(len(exp1_zoom_vel_2d_array)))] / (exp1_zoom_vel_2d_numberflys))
exp1_zoom_vel_2d_avgraster = np.squeeze(np.transpose(exp1_zoom_vel_2d_average))
exp1_zoom_vel_2d_bined = np.array(np.array([sum(exp1_zoom_vel_2d_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_walk_vel_array = np.squeeze((np.asarray([exp1_zoom_walk_vel])), axis=0)
exp1_zoom_walk_vel_output = np.transpose(exp1_zoom_walk_vel_array)
exp1_zoom_walk_vel_numberflys = np.sum(np.array(exp1_zoom_walk_vel_array) > 0, axis=0)
exp1_zoom_walk_vel_average = np.array([sum(exp1_zoom_walk_vel_array[i] for i in range(len(exp1_zoom_walk_vel_array)))] / (exp1_zoom_walk_vel_numberflys))
exp1_zoom_walk_vel_avgraster = np.squeeze(np.transpose(exp1_zoom_walk_vel_average))
exp1_zoom_walk_vel_bined = np.array(np.array([sum(exp1_zoom_walk_vel_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_walking_array = np.squeeze((np.asarray([exp1_zoom_walking])), axis=0)
exp1_zoom_walking_output = np.transpose(exp1_zoom_walking_array)
exp1_zoom_walking_average = np.array(np.array([sum(exp1_zoom_walking_array[i] for i in range(len(exp1_zoom_walking_array)))]) / [len(exp1_zoom_walking_array)])
exp1_zoom_walking_avgraster = np.squeeze(np.transpose(exp1_zoom_walking_average))
exp1_zoom_walking_bined = np.array(np.array([sum(exp1_zoom_walking_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


exp1_zoom_freezing_array = np.squeeze((np.asarray([exp1_zoom_freezing])), axis=0)
exp1_zoom_freezing_output = np.transpose(exp1_zoom_freezing_array)
exp1_zoom_freezing_average = np.array(np.array([sum(exp1_zoom_freezing_array[i] for i in range(len(exp1_zoom_freezing_array)))]) / [len(exp1_zoom_freezing_array)])
exp1_zoom_freezing_avgraster = np.squeeze(np.transpose(exp1_zoom_freezing_average))
exp1_zoom_freezing_bined = np.array(np.array([sum(exp1_zoom_freezing_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_jumping_array = np.squeeze((np.asarray([exp1_zoom_jumping])), axis=0)
exp1_zoom_jumping_output = np.transpose(exp1_zoom_jumping_array)
exp1_zoom_jumping_average = np.array(np.array([sum(exp1_zoom_jumping_array[i] for i in range(len(exp1_zoom_jumping_array)))])/ [len(exp1_zoom_freezing_array)])
exp1_zoom_jumping_avgraster = np.squeeze(np.transpose(exp1_zoom_jumping_average))
exp1_zoom_jumping_bined = np.array(np.array([sum(exp1_zoom_jumping_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


exp1_zoom_grooming_array = np.squeeze((np.asarray([exp1_zoom_grooming])), axis=0)
exp1_zoom_grooming_output = np.transpose(exp1_zoom_grooming_array)
exp1_zoom_grooming_average = np.array(np.array([sum(exp1_zoom_grooming_array[i] for i in range(len(exp1_zoom_grooming_array)))]) / [len(exp1_zoom_grooming_array)])
exp1_zoom_grooming_avgraster = np.squeeze(np.transpose(exp1_zoom_grooming_average))
exp1_zoom_grooming_bined = np.array(np.array([sum(exp1_zoom_grooming_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_pxchange_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_pxchange_freezer_before_after])), axis=0)
exp1_zoom_pxchange_freezer_before_after_output = np.transpose(exp1_zoom_pxchange_freezer_before_after_array)
exp1_zoom_pxchange_freezer_before_after_average = np.array(np.array([sum(exp1_zoom_pxchange_freezer_before_after_array[i] for i in range(len(exp1_zoom_pxchange_freezer_before_after_array)))]) / [len(exp1_zoom_pxchange_freezer_before_after_array)])
exp1_zoom_pxchange_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_pxchange_freezer_before_after_average))
exp1_zoom_pxchange_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_pxchange_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_velocity_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_velocity_freezer_before_after])), axis=0)
exp1_zoom_velocity_freezer_before_after_output = np.transpose(exp1_zoom_velocity_freezer_before_after_array)
exp1_zoom_velocity_freezer_before_after_average = np.array(np.array([sum(exp1_zoom_velocity_freezer_before_after_array[i] for i in range(len(exp1_zoom_velocity_freezer_before_after_array)))]) / [len(exp1_zoom_velocity_freezer_before_after_array)])
exp1_zoom_velocity_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_velocity_freezer_before_after_average))
exp1_zoom_velocity_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_velocity_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_vel_2d_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_vel_2d_freezer_before_after])), axis=0)
exp1_zoom_vel_2d_freezer_before_after_output = np.transpose(exp1_zoom_vel_2d_freezer_before_after_array)
exp1_zoom_vel_2d_freezer_before_after_numberflys = np.sum(np.array(exp1_zoom_vel_2d_freezer_before_after_array) > 0, axis=0)
exp1_zoom_vel_2d_freezer_before_after_average = np.array([sum(exp1_zoom_vel_2d_freezer_before_after_array[i] for i in range(len(exp1_zoom_vel_2d_freezer_before_after_array)))] / (exp1_zoom_vel_2d_freezer_before_after_numberflys))
exp1_zoom_vel_2d_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_vel_2d_freezer_before_after_average))
exp1_zoom_vel_2d_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_vel_2d_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_walk_vel_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_walk_vel_freezer_before_after])), axis=0)
exp1_zoom_walk_vel_freezer_before_after_output = np.transpose(exp1_zoom_walk_vel_freezer_before_after_array)
exp1_zoom_walk_vel_freezer_before_after_numberflys = np.sum(np.array(exp1_zoom_walk_vel_freezer_before_after_array) > 0, axis=0)
exp1_zoom_walk_vel_freezer_before_after_average = np.array([sum(exp1_zoom_walk_vel_freezer_before_after_array[i] for i in range(len(exp1_zoom_walk_vel_freezer_before_after_array)))] / (exp1_zoom_walk_vel_freezer_before_after_numberflys))
exp1_zoom_walk_vel_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_walk_vel_freezer_before_after_average))
exp1_zoom_walk_vel_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_walk_vel_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_walking_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_walking_freezer_before_after])), axis=0)
exp1_zoom_walking_freezer_before_after_output = np.transpose(exp1_zoom_walking_freezer_before_after_array)
exp1_zoom_walking_freezer_before_after_average = np.array(np.array([sum(exp1_zoom_walking_freezer_before_after_array[i] for i in range(len(exp1_zoom_walking_freezer_before_after_array)))]) / [len(exp1_zoom_walking_freezer_before_after_array)])
exp1_zoom_walking_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_walking_freezer_before_after_average))
exp1_zoom_walking_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_walking_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_freezing_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_freezing_freezer_before_after])), axis=0)
exp1_zoom_freezing_freezer_before_after_output = np.transpose(exp1_zoom_freezing_freezer_before_after_array)
exp1_zoom_freezing_freezer_before_after_average = np.array(np.array([sum(exp1_zoom_freezing_freezer_before_after_array[i] for i in range(len(exp1_zoom_freezing_freezer_before_after_array)))]) / [len(exp1_zoom_freezing_freezer_before_after_array)])
exp1_zoom_freezing_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_freezing_freezer_before_after_average))
exp1_zoom_freezing_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_freezing_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_jumping_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_jumping_freezer_before_after])), axis=0)
exp1_zoom_jumping_freezer_before_after_output = np.transpose(exp1_zoom_jumping_freezer_before_after_array)
exp1_zoom_jumping_freezer_before_after_average = np.array(np.array([sum(exp1_zoom_jumping_freezer_before_after_array[i] for i in range(len(exp1_zoom_jumping_freezer_before_after_array)))]))
exp1_zoom_jumping_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_jumping_freezer_before_after_average))
exp1_zoom_jumping_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_jumping_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)])/ bin_zoom_size)

exp1_zoom_grooming_freezer_before_after_array = np.squeeze((np.asarray([exp1_zoom_grooming_freezer_before_after])), axis=0)
exp1_zoom_grooming_freezer_before_after_output = np.transpose(exp1_zoom_grooming_freezer_before_after_array)
exp1_zoom_grooming_freezer_before_after_average = np.array(np.array([sum(exp1_zoom_grooming_freezer_before_after_array[i] for i in range(len(exp1_zoom_grooming_freezer_before_after_array)))]) / [len(exp1_zoom_grooming_freezer_before_after_array)])
exp1_zoom_grooming_freezer_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_grooming_freezer_before_after_average))
exp1_zoom_grooming_freezer_before_after_bined = np.array(np.array([sum(exp1_zoom_grooming_freezer_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_pxchange_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_pxchange_runner_before_after])), axis=0)
exp1_zoom_pxchange_runner_before_after_output = np.transpose(exp1_zoom_pxchange_runner_before_after_array)
exp1_zoom_pxchange_runner_before_after_average = np.array(np.array([sum(exp1_zoom_pxchange_runner_before_after_array[i] for i in range(len(exp1_zoom_pxchange_runner_before_after_array)))]) / [len(exp1_zoom_pxchange_runner_before_after_array)])
exp1_zoom_pxchange_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_pxchange_runner_before_after_average))
exp1_zoom_pxchange_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_pxchange_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_velocity_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_velocity_runner_before_after])), axis=0)
exp1_zoom_velocity_runner_before_after_output = np.transpose(exp1_zoom_velocity_runner_before_after_array)
exp1_zoom_velocity_runner_before_after_average = np.array(np.array([sum(exp1_zoom_velocity_runner_before_after_array[i] for i in range(len(exp1_zoom_velocity_runner_before_after_array)))]) / [len(exp1_zoom_velocity_runner_before_after_array)])
exp1_zoom_velocity_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_velocity_runner_before_after_average))
exp1_zoom_velocity_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_velocity_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_vel_2d_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_vel_2d_runner_before_after])), axis=0)
exp1_zoom_vel_2d_runner_before_after_output = np.transpose(exp1_zoom_vel_2d_runner_before_after_array)
exp1_zoom_vel_2d_runner_before_after_numberflys = np.sum(np.array(exp1_zoom_vel_2d_runner_before_after_array) > 0, axis=0)
exp1_zoom_vel_2d_runner_before_after_average = np.array([sum(exp1_zoom_vel_2d_runner_before_after_array[i] for i in range(len(exp1_zoom_vel_2d_runner_before_after_array)))] / (exp1_zoom_vel_2d_runner_before_after_numberflys))
exp1_zoom_vel_2d_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_vel_2d_runner_before_after_average))
exp1_zoom_vel_2d_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_vel_2d_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_walk_vel_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_walk_vel_runner_before_after])), axis=0)
exp1_zoom_walk_vel_runner_before_after_output = np.transpose(exp1_zoom_walk_vel_runner_before_after_array)
exp1_zoom_walk_vel_runner_before_after_numberflys = np.sum(np.array(exp1_zoom_walk_vel_runner_before_after_array) > 0, axis=0)
exp1_zoom_walk_vel_runner_before_after_average = np.array([sum(exp1_zoom_walk_vel_runner_before_after_array[i] for i in range(len(exp1_zoom_walk_vel_runner_before_after_array)))] / (exp1_zoom_walk_vel_runner_before_after_numberflys))
exp1_zoom_walk_vel_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_walk_vel_runner_before_after_average))
exp1_zoom_walk_vel_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_walk_vel_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_walking_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_walking_runner_before_after])), axis=0)
exp1_zoom_walking_runner_before_after_output = np.transpose(exp1_zoom_walking_runner_before_after_array)
exp1_zoom_walking_runner_before_after_average = np.array(np.array([sum(exp1_zoom_walking_runner_before_after_array[i] for i in range(len(exp1_zoom_walking_runner_before_after_array)))]) / [len(exp1_zoom_walking_runner_before_after_array)])
exp1_zoom_walking_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_walking_runner_before_after_average))
exp1_zoom_walking_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_walking_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_freezing_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_freezing_runner_before_after])), axis=0)
exp1_zoom_freezing_runner_before_after_output = np.transpose(exp1_zoom_freezing_runner_before_after_array)
exp1_zoom_freezing_runner_before_after_average = np.array(np.array([sum(exp1_zoom_freezing_runner_before_after_array[i] for i in range(len(exp1_zoom_freezing_runner_before_after_array)))]) / [len(exp1_zoom_freezing_runner_before_after_array)])
exp1_zoom_freezing_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_freezing_runner_before_after_average))
exp1_zoom_freezing_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_freezing_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)

exp1_zoom_jumping_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_jumping_runner_before_after])), axis=0)
exp1_zoom_jumping_runner_before_after_output = np.transpose(exp1_zoom_jumping_runner_before_after_array)
exp1_zoom_jumping_runner_before_after_average = np.array(np.array([sum(exp1_zoom_jumping_runner_before_after_array[i] for i in range(len(exp1_zoom_jumping_runner_before_after_array)))]))
exp1_zoom_jumping_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_jumping_runner_before_after_average))
exp1_zoom_jumping_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_jumping_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) /bin_zoom_size)
exp1_zoom_grooming_runner_before_after_array = np.squeeze((np.asarray([exp1_zoom_grooming_runner_before_after])), axis=0)
exp1_zoom_grooming_runner_before_after_output = np.transpose(exp1_zoom_grooming_runner_before_after_array)
exp1_zoom_grooming_runner_before_after_average = np.array(np.array([sum(exp1_zoom_grooming_runner_before_after_array[i] for i in range(len(exp1_zoom_grooming_runner_before_after_array)))]) / [len(exp1_zoom_grooming_runner_before_after_array)])
exp1_zoom_grooming_runner_before_after_avgraster = np.squeeze(np.transpose(exp1_zoom_grooming_runner_before_after_average))
exp1_zoom_grooming_runner_before_after_bined = np.array(np.array([sum(exp1_zoom_grooming_runner_before_after_avgraster[current : current + bin_zoom_size]) for current in range(0, number_frames_zoom, bin_zoom_size)]) / bin_zoom_size)


'''
VIOLIN PLOTS VARIABLES
'''

exp1_base_walk_vel = exp1_walk_vel_output[:baseline_frames]
exp1_base_walk_vel_exclude = np.count_nonzero(exp1_base_walk_vel, axis = 0)
exp1_base_walk_vel_all = np.array(sum(exp1_base_walk_vel[i] for i in range(len(exp1_base_walk_vel))))
exp1_base_walk_vel_nan = np.array(exp1_base_walk_vel_all / exp1_base_walk_vel_exclude)
exp1_base_walk_vel_exclude_nan = exp1_base_walk_vel_nan[~np.isnan(exp1_base_walk_vel_nan)]
exp1_base_walk_vel_outliers = exp1_base_walk_vel_exclude_nan[~is_outlier(exp1_base_walk_vel_exclude_nan)]
exp1_base_walk_vel_df2 = pd.DataFrame(exp1_base_walk_vel_outliers)
exp1_base_walk_vel_df2.columns = [str(experiment1)]

exp1_stim_walk_vel = exp1_walk_vel_output[baseline_frames:]
exp1_stim_walk_vel_exclude = np.count_nonzero(exp1_stim_walk_vel, axis = 0)
exp1_stim_walk_vel_all = np.array(sum(exp1_stim_walk_vel[i] for i in range(len(exp1_stim_walk_vel))))
exp1_stim_walk_vel_nan = np.array(exp1_stim_walk_vel_all / exp1_stim_walk_vel_exclude)
exp1_stim_walk_vel_exclude_nan = exp1_stim_walk_vel_nan[~np.isnan(exp1_stim_walk_vel_nan)]
exp1_stim_walk_vel_outliers = exp1_stim_walk_vel_exclude_nan[~is_outlier(exp1_stim_walk_vel_exclude_nan)]
exp1_stim_walk_vel_df2 = pd.DataFrame(exp1_stim_walk_vel_outliers)
exp1_stim_walk_vel_df2.columns = [str(experiment1)]

exp1_base_walking = exp1_walking_output[:baseline_frames]
exp1_base_walking_all = np.array(sum(exp1_base_walking[i] for i in range(len(exp1_base_walking))))
exp1_base_walking_nan = np.array(exp1_base_walking_all / (len(exp1_base_walking)))
exp1_base_walking_outliers = exp1_base_walking_nan[~is_outlier(exp1_base_walking_nan)]
exp1_base_walking_df2 = pd.DataFrame(exp1_base_walking_outliers * 100)
exp1_base_walking_df2.columns = [str(experiment1)]

exp1_stim_walking = exp1_walking_output[baseline_frames:]
exp1_stim_walking_all = np.array(sum(exp1_stim_walking[i] for i in range(len(exp1_stim_walking))))
exp1_stim_walking_nan = np.array(exp1_stim_walking_all / (len(exp1_stim_walking)))
exp1_stim_walking_outliers = exp1_stim_walking_nan[~is_outlier(exp1_stim_walking_nan)]
exp1_stim_walking_df2 = pd.DataFrame(exp1_stim_walking_outliers * 100)
exp1_stim_walking_df2.columns = [str(experiment1)]


exp1_base_freezing = exp1_freezing_output[:baseline_frames]
exp1_base_freezing_all = np.array(sum(exp1_base_freezing[i] for i in range(len(exp1_base_freezing))))
exp1_base_freezing_nan = np.array(exp1_base_freezing_all / (len(exp1_base_freezing)))
exp1_base_freezing_outliers = exp1_base_freezing_nan[~is_outlier(exp1_base_freezing_nan)]
exp1_base_freezing_df2 = pd.DataFrame(exp1_base_freezing_outliers * 100)
exp1_base_freezing_df2.columns = [str(experiment1)]

exp1_stim_freezing = exp1_freezing_output[baseline_frames:]
exp1_stim_freezing_all = np.array(sum(exp1_stim_freezing[i] for i in range(len(exp1_stim_freezing))))
exp1_stim_freezing_nan = np.array(exp1_stim_freezing_all / (len(exp1_stim_freezing)))
exp1_stim_freezing_outliers = exp1_stim_freezing_nan[~is_outlier(exp1_stim_freezing_nan)]
exp1_stim_freezing_df2 = pd.DataFrame(exp1_stim_freezing_outliers * 100)
exp1_stim_freezing_df2.columns = [str(experiment1)]


exp1_base_grooming = exp1_grooming_output[:baseline_frames]
exp1_base_grooming_all = np.array(sum(exp1_base_grooming[i] for i in range(len(exp1_base_grooming))))
exp1_base_grooming_nan = np.array(exp1_base_grooming_all / (len(exp1_base_grooming)))
exp1_base_grooming_outliers = exp1_base_grooming_nan[~is_outlier(exp1_base_grooming_nan)]
exp1_base_grooming_df2 = pd.DataFrame(exp1_base_grooming_outliers * 100)
exp1_base_grooming_df2.columns = [str(experiment1)]

exp1_stim_grooming = exp1_grooming_output[baseline_frames:]
exp1_stim_grooming_all = np.array(sum(exp1_stim_grooming[i] for i in range(len(exp1_stim_grooming))))
exp1_stim_grooming_nan = np.array(exp1_stim_grooming_all / (len(exp1_stim_grooming)))
exp1_stim_grooming_outliers = exp1_stim_grooming_nan[~is_outlier(exp1_stim_grooming_nan)]
exp1_stim_grooming_df2 = pd.DataFrame(exp1_stim_grooming_outliers * 100)
exp1_stim_grooming_df2.columns = [str(experiment1)]



#JUMPING STATS

#Jumping - spliting stimulation and baseline
exp1_bin_stim_jumping = exp1_bin_jumping_output[600:1200]
exp1_bin_stim_jumping_all = np.array(sum(exp1_bin_stim_jumping[i] for i in range(len(exp1_bin_stim_jumping))))
exp1_bin_stim_jumping_nan = np.array(exp1_bin_stim_jumping_all / (len(exp1_bin_stim_jumping)))

exp1_bin_base_jumping = exp1_bin_jumping_output[0:600]
exp1_bin_base_jumping_all = np.array(sum(exp1_bin_base_jumping[i] for i in range(len(exp1_bin_base_jumping))))
exp1_bin_base_jumping_nan = np.array(exp1_bin_base_jumping_all / (len(exp1_bin_base_jumping)))

exp0_bin_stim_jumping = exp0_bin_jumping_output[600:1200]
exp0_bin_stim_jumping_all = np.array(sum(exp0_bin_stim_jumping[i] for i in range(len(exp0_bin_stim_jumping))))
exp0_bin_stim_jumping_nan = np.array(exp0_bin_stim_jumping_all / (len(exp0_bin_stim_jumping)))

exp0_bin_base_jumping = exp0_bin_jumping_output[0:600]
exp0_bin_base_jumping_all = np.array(sum(exp0_bin_base_jumping[i] for i in range(len(exp0_bin_base_jumping))))
exp0_bin_base_jumping_nan = np.array(exp0_bin_base_jumping_all / (len(exp0_bin_base_jumping)))


#Jumping - removing outliers
exp1_bin_stim_jumping_outliers = exp1_bin_stim_jumping_nan[~is_outlier(exp1_bin_stim_jumping_nan)]
exp1_bin_base_jumping_outliers = exp1_bin_base_jumping_nan[~is_outlier(exp1_bin_base_jumping_nan)]
exp0_bin_stim_jumping_outliers = exp0_bin_stim_jumping_nan[~is_outlier(exp0_bin_stim_jumping_nan)]
exp0_bin_base_jumping_outliers = exp0_bin_base_jumping_nan[~is_outlier(exp0_bin_base_jumping_nan)]

exp0_bin_stim_jumping_df1 = pd.DataFrame(exp0_bin_stim_jumping_outliers * 100)
exp0_bin_stim_jumping_df1.columns = [str(experiment0)]
exp1_bin_stim_jumping_df2 = pd.DataFrame(exp1_bin_stim_jumping_outliers * 100)
exp1_bin_stim_jumping_df2.columns = [str(experiment1)]

exp0_bin_base_jumping_df1 = pd.DataFrame(exp0_bin_base_jumping_outliers * 100)
exp0_bin_base_jumping_df1.columns = [str(experiment0)]
exp1_bin_base_jumping_df2 = pd.DataFrame(exp1_bin_base_jumping_outliers * 100)
exp1_bin_base_jumping_df2.columns = [str(experiment1)]

max_jumping_stimulation_df1 = (max(exp0_bin_stim_jumping_outliers) * 100)
max_jumping_stimulation_df2 = (max(exp1_bin_stim_jumping_outliers) * 100)
max_jumping_baseline_df1 = (max(exp0_bin_base_jumping_outliers) * 100)
max_jumping_baseline_df2 = (max(exp1_bin_base_jumping_outliers) * 100)
max_jump = [max_jumping_stimulation_df1, max_jumping_stimulation_df2, max_jumping_baseline_df1, max_jumping_baseline_df2]




#RASTER PLOTS 10min

'''WALKING SPEED'''

x_coordinate = [ i for i in range(len(exp0_walk_vel_bined)) ]

fig, axs = plt.subplots(1, 2, figsize= (15, 5), gridspec_kw={'width_ratios': [3, 1.5]}, sharey = True)
#fig.suptitle(str(experiment), y=0.98, fontsize = 20)
fig.subplots_adjust(wspace = 0.07)
axs[1].set_facecolor('white')
axs[1].axes.xaxis.set_visible(False)
axs[1].set_title('Baseline               Stimulation', y=-0.09, fontsize = 14)
axs[1].set_yticks([5, 10, 15, 20, 25])
axs[1].set_yticklabels([5, 10, 15, 20, 25])
axs[1].yaxis.grid(which='both', linestyle='--', color='grey')
dashed = [1.5]
axs[1].vlines(dashed, 0, 30, linestyles='-', lw= 0.5)
axs[1].set_axisbelow(True)
sns.despine(left=True, bottom=True, right=True)
my_pal = {0: "grey", 1: "#781c6d", 2:"grey", 3:"#781c6d"}
axs[1] = sns.violinplot(data=(exp0_base_walk_vel_df2, exp1_base_walk_vel_df2, exp0_stim_walk_vel_df2, exp1_stim_walk_vel_df2), bw =0.2, linewidth=1.3, width= 0.75, scale='count', inner=('box'), palette=my_pal, cut=0)


axs[0].set_facecolor('white')
axs[0].set_ylabel('Walking speed (mm/sec)', fontsize = 14)
axs[0].set_ylim(4, 26)
axs[0].set_xlim(0, 1200)
axs[0].vlines(looming_x, 0, 30, linestyles='-', lw= 0.5)
axs[0].set_xlabel('Time (min)', fontsize = 14)
axs[0].set_yticks([5, 10, 15, 20, 25])
axs[0].set_xticks([0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200])
axs[0].set_xticklabels([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axs[0].spines['left'].set_visible(True)
axs[0].spines['bottom'].set_visible(True)
axs[0].spines['right'].set_visible(False)
axs[0].spines['top'].set_visible(False)
axs[0].spines['left'].set_position(('outward', 5))
axs[0].spines['bottom'].set_position(('outward', 5))
axs[0].spines['left'].set_color('dimgrey')
axs[0].spines['bottom'].set_color('dimgrey')
axs[0].tick_params(axis='x', colors = 'k')
axs[0].tick_params(axis='y', colors = 'k')
axs[0].xaxis.label.set_color('k')
axs[0].yaxis.label.set_color('k')
axs[0].plot(x_coordinate, exp0_walk_vel_bined, label = (str(experiment0) + ' (' + str(len(exp0_walk_vel)) + ')'), color='grey')
axs[0].plot(x_coordinate, exp1_walk_vel_bined, label = (str(experiment1) + ' (' + str(len(exp1_walk_vel)) + ')'), color='#781c6d', alpha = 0.85)
axs[0].legend(loc="upper left", frameon = False, fontsize = 13)
fig.savefig((str(path)+"/"+str(experiment_name)+"_walkingspeed.png"), format='png') 


'''FREEZING'''
x_coordinate = [ i for i in range(len(exp0_freezing_bined)) ]

fig, axs = plt.subplots(1, 2, figsize= (15, 5), gridspec_kw={'width_ratios': [3, 1.5]}, sharey = True)
#fig.suptitle(str(experiment), y=0.98, fontsize = 20)
fig.subplots_adjust(wspace = 0.07)
axs[1].set_facecolor('white')
axs[1].axes.xaxis.set_visible(False)
axs[1].set_title('Baseline               Stimulation', y=-0.09, fontsize = 14)
axs[1].set_xlabel('t')
axs[1].yaxis.set_label_position("right")
axs[1].set_yticks([20, 40, 60, 80])
axs[1].yaxis.grid(which='both', linestyle='--', color='grey')
dashed = [1.5]
axs[1].vlines(dashed, 0, 100, linestyles='-', lw= 0.5)
axs[1].set_axisbelow(True)
sns.despine(left=True, bottom=True, right=True)
my_pal = {0: "grey", 1: "#781c6d", 2:"grey", 3:"#781c6d"}
axs[1] = sns.violinplot(data=(exp0_base_freezing_df2, exp1_base_freezing_df2, exp0_stim_freezing_df2, exp1_stim_freezing_df2), bw =0.2, linewidth=1.3, width= 0.75, scale='count', inner=('box'), palette=my_pal, cut=0)


axs[0].set_facecolor('white')
axs[0].set_ylabel('Freezing %', fontsize = 14)
axs[0].set_ylim(0, 100)
axs[0].set_xlim(0, 1200)
axs[0].vlines(looming_x, 0, 100, linestyles='-', lw= 0.5)
axs[0].set_xlabel('Time (min)', fontsize = 14)
axs[0].set_yticks([20, 40, 60, 80])
axs[0].set_xticks([0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200])
axs[0].set_xticklabels([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axs[0].spines['left'].set_visible(True)
axs[0].spines['bottom'].set_visible(True)
axs[0].spines['right'].set_visible(False)
axs[0].spines['top'].set_visible(False)
axs[0].spines['left'].set_position(('outward', 5))
axs[0].spines['bottom'].set_position(('outward', 5))
axs[0].spines['left'].set_color('dimgrey')
axs[0].spines['bottom'].set_color('dimgrey')
axs[0].tick_params(axis='x', colors = 'k')
axs[0].tick_params(axis='y', colors = 'k')
axs[0].xaxis.label.set_color('k')
axs[0].yaxis.label.set_color('k')
axs[0].plot(x_coordinate, (exp0_freezing_bined*100), label = (str(experiment0) + ' (' + str(len(exp0_freezing)) + ')'), color='grey')
axs[0].plot(x_coordinate, (exp1_freezing_bined*100), label = (str(experiment1) + ' (' + str(len(exp1_freezing)) + ')'), color='#781c6d', alpha = 0.85)
axs[0].legend(loc="upper left", frameon = False, fontsize = 13)
fig.savefig((str(path)+"/"+str(experiment_name)+"_freezing.png"), format='png') 


'''jumping'''
x_coordinate = [ i for i in range(len(exp0_jumping_bined)) ]

fig, axs = plt.subplots(1, 2, figsize= (15, 5), gridspec_kw={'width_ratios': [3, 1.5]}, sharey = False)
#fig.suptitle(str(experiment), y=0.98, fontsize = 20)
fig.subplots_adjust(wspace = 0.1)
axs[1].set_facecolor('white')
axs[1].axes.xaxis.set_visible(False)
axs[1].set_title('Baseline               Stimulation', y=-0.09, fontsize = 14)
axs[1].set_ylabel('Jumps per fly', fontsize = 14)
axs[1].set_ylim(-0.2, (max(max_jump)+.5))
axs[1].yaxis.grid(which='both', linestyle='--', color='grey')
dashed = [1.5]
axs[1].vlines(dashed, 0, 100, linestyles='-', lw= 0.5)
axs[1].set_axisbelow(True)
sns.despine(left=True, bottom=True, right=True)
my_pal = {0: "grey", 1: "#781c6d", 2:"grey", 3:"#781c6d"}
axs[1] = sns.violinplot(data=(exp0_bin_base_jumping_df1, exp1_bin_base_jumping_df2, exp0_bin_stim_jumping_df1, exp1_bin_stim_jumping_df2), bw =0.2, linewidth=1.3, width= 0.75, scale='count', inner=('box'), palette=my_pal, cut=0)


axs[0].set_facecolor('white')
axs[0].set_ylabel('Jumping %', fontsize = 14)
axs[0].set_ylim(0, 100)
axs[0].set_xlim(0, 1200)
axs[0].vlines(looming_x, 0, 100, linestyles='-', lw= 0.5)
axs[0].set_xlabel('Time (min)', fontsize = 14)
axs[0].set_yticks([20, 40, 60, 80])
axs[0].set_xticks([0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200])
axs[0].set_xticklabels([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axs[0].spines['left'].set_visible(True)
axs[0].spines['bottom'].set_visible(True)
axs[0].spines['right'].set_visible(False)
axs[0].spines['top'].set_visible(False)
axs[0].spines['left'].set_position(('outward', 5))
axs[0].spines['bottom'].set_position(('outward', 5))
axs[0].spines['left'].set_color('dimgrey')
axs[0].spines['bottom'].set_color('dimgrey')
axs[0].tick_params(axis='x', colors = 'k')
axs[0].tick_params(axis='y', colors = 'k')
axs[0].xaxis.label.set_color('k')
axs[0].yaxis.label.set_color('k')
axs[0].plot(x_coordinate, (exp0_jumping_bined*100), label = (str(experiment0) + ' (' + str(len(exp0_jumping)) + ')'), color='grey')
axs[0].plot(x_coordinate, (exp1_jumping_bined*100), label = (str(experiment1) + ' (' + str(len(exp1_jumping)) + ')'), color='#781c6d', alpha = 0.85)
axs[0].legend(loc="upper left", frameon = False, fontsize = 13)
fig.savefig((str(path)+"/"+str(experiment_name)+"_jumping.png"), format='png') 

'''grooming'''
x_coordinate = [ i for i in range(len(exp0_grooming_bined)) ]

fig, axs = plt.subplots(1, 2, figsize= (15, 5), gridspec_kw={'width_ratios': [3, 1.5]}, sharey = True)
#fig.suptitle(str(experiment), y=0.98, fontsize = 20)
fig.subplots_adjust(wspace = 0.07)
axs[1].set_facecolor('white')
axs[1].axes.xaxis.set_visible(False)
axs[1].set_title('Baseline               Stimulation', y=-0.09, fontsize = 14)
axs[1].set_xlabel('t')
axs[1].yaxis.set_label_position("right")
axs[1].set_yticks([20, 40, 60, 80])
axs[1].yaxis.grid(which='both', linestyle='--', color='grey')
dashed = [1.5]
axs[1].vlines(dashed, 0, 100, linestyles='-', lw= 0.5)
axs[1].set_axisbelow(True)
sns.despine(left=True, bottom=True, right=True)
my_pal = {0: "grey", 1: "#781c6d", 2:"grey", 3:"#781c6d"}
axs[1] = sns.violinplot(data=(exp0_base_grooming_df2, exp1_base_grooming_df2, exp0_stim_grooming_df2, exp1_stim_grooming_df2), bw =0.2, linewidth=1.3, width= 0.75, scale='count', inner=('box'), palette=my_pal, cut=0)


axs[0].set_facecolor('white')
axs[0].set_ylabel('Grooming %', fontsize = 14)
axs[0].set_ylim(0, 100)
axs[0].set_xlim(0, 1200)
axs[0].vlines(looming_x, 0, 100, linestyles='-', lw= 0.5)
axs[0].set_xlabel('Time (min)', fontsize = 14)
axs[0].set_yticks([20, 40, 60, 80])
axs[0].set_xticks([0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200])
axs[0].set_xticklabels([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axs[0].spines['left'].set_visible(True)
axs[0].spines['bottom'].set_visible(True)
axs[0].spines['right'].set_visible(False)
axs[0].spines['top'].set_visible(False)
axs[0].spines['left'].set_position(('outward', 5))
axs[0].spines['bottom'].set_position(('outward', 5))
axs[0].spines['left'].set_color('dimgrey')
axs[0].spines['bottom'].set_color('dimgrey')
axs[0].tick_params(axis='x', colors = 'k')
axs[0].tick_params(axis='y', colors = 'k')
axs[0].xaxis.label.set_color('k')
axs[0].yaxis.label.set_color('k')
axs[0].plot(x_coordinate, (exp0_grooming_bined*100), label = (str(experiment0) + ' (' + str(len(exp0_grooming)) + ')'), color='grey')
axs[0].plot(x_coordinate, (exp1_grooming_bined*100), label = (str(experiment1) + ' (' + str(len(exp1_grooming)) + ')'), color='#781c6d', alpha = 0.85)
axs[0].legend(loc="upper left", frameon = False, fontsize = 13)
fig.savefig((str(path)+"/"+str(experiment_name)+"_grooming.png"), format='png') 



'''#RASTER PLOTS ZOOM'''

x_coordinate = [ i for i in range(len(exp0_zoom_velocity_runner_before_after_bined)) ]

fig, axs = plt.subplots(2, 2, figsize= (12, 10), sharex = True)
fig.subplots_adjust(hspace = 0.1)
axs[0, 0].set_facecolor('white')
axs[0, 0].set_ylabel('Speed 2D (mm/sec)', fontsize = 14)
axs[0, 0].set_ylim(0, 25)
axs[0, 0].set_xlim(0, 50)
axs[0, 0].vlines(looming_x_zoom, 0, 150, linestyles='dashed', lw= 0.5)
axs[0, 0].set_yticks([5, 10, 15, 20])
axs[0, 0].set_xticks([])
axs[0, 0].spines['left'].set_visible(False)
axs[0, 0].spines['bottom'].set_visible(False)
axs[0, 0].spines['right'].set_visible(False)
axs[0, 0].spines['top'].set_visible(False)
axs[0, 0].spines['left'].set_position(('outward', 5))
axs[0, 0].spines['bottom'].set_position(('outward', 5))
axs[0, 0].spines['left'].set_color('dimgrey')
axs[0, 0].spines['bottom'].set_color('dimgrey')
axs[0, 0].tick_params(axis='y', colors = 'k')
axs[0, 0].yaxis.label.set_color('k')
axs[0, 0].plot(x_coordinate, exp0_zoom_vel_2d_runner_before_after_bined, label = (str(experiment0) + ' (' + str(len(exp0_zoom_velocity)) + ')'), color='grey', linewidth=3)
axs[0, 0].plot(x_coordinate, exp1_zoom_vel_2d_runner_before_after_bined, label = (str(experiment1) + ' (' + str(len(exp1_zoom_velocity)) + ')'), color='#781c6d', alpha = 0.85, linewidth=3)

axs[0, 1].set_facecolor('white')
axs[0, 1].set_ylabel('Freezing %', fontsize = 14)
axs[0, 1].set_ylim(0, 100)
axs[0, 1].set_xlim(0, 50)
axs[0, 1].vlines(looming_x_zoom, 0, 150, linestyles='dashed', lw= 0.5)
axs[0, 1].set_yticks([20, 40, 60, 80])
axs[0, 1].set_xticks([])
axs[0, 1].spines['left'].set_visible(False)
axs[0, 1].spines['bottom'].set_visible(False)
axs[0, 1].spines['right'].set_visible(False)
axs[0, 1].spines['top'].set_visible(False)
axs[0, 1].spines['left'].set_position(('outward', 5))
axs[0, 1].spines['bottom'].set_position(('outward', 5))
axs[0, 1].spines['left'].set_color('dimgrey')
axs[0, 1].spines['bottom'].set_color('dimgrey')
axs[0, 1].tick_params(axis='y', colors = 'k')
axs[0, 1].yaxis.label.set_color('k')
axs[0, 1].plot(x_coordinate, exp0_zoom_freezing_bined*100, label = (str(experiment0) + ' (' + str(len(exp0_zoom_freezing_array)) + ')'), color='grey', linewidth=3)
axs[0, 1].plot(x_coordinate, exp1_zoom_freezing_bined*100, label = (str(experiment1) + ' (' + str(len(exp1_zoom_freezing_array)) + ')'), color='#781c6d', alpha = 0.85, linewidth=3)
axs[0, 1].legend(loc="upper right", frameon = False, fontsize = 13)

axs[1, 1].set_facecolor('white')
axs[1, 1].set_ylabel('Pixel change', fontsize = 14)
axs[1, 1].set_ylim(0, 150)
axs[1, 1].set_yticks([])
axs[1, 1].set_xlim(0, 50)
axs[1, 1].vlines(looming_x_zoom, 0, 150, linestyles='dashed', lw= 0.5)
axs[1, 1].set_xlabel('Time (sec)', fontsize = 14)
axs[1, 1].set_xticks([0, 10, 20, 30, 40, 50])
axs[1, 1].set_xticklabels([-1, -0.5, 0, 0.5, 1, 1.5])
axs[1, 1].spines['left'].set_visible(False)
axs[1, 1].spines['bottom'].set_visible(True)
axs[1, 1].spines['right'].set_visible(False)
axs[1, 1].spines['top'].set_visible(False)
axs[1, 1].spines['left'].set_position(('outward', 5))
axs[1, 1].spines['bottom'].set_position(('outward', 5))
axs[1, 1].spines['left'].set_color('dimgrey')
axs[1, 1].spines['bottom'].set_color('dimgrey')
axs[1, 1].tick_params(axis='x', colors = 'k')
axs[1, 1].xaxis.label.set_color('k')
axs[1, 1].yaxis.label.set_color('k')
axs[1, 1].plot(x_coordinate, exp0_zoom_pxchange_freezer_before_after_bined, label = (str(experiment0) + ' (' + str(len(exp0_zoom_pxchange_array)) + ')'), color='grey', linewidth=3)
axs[1, 1].plot(x_coordinate, exp1_zoom_pxchange_freezer_before_after_bined, label = (str(experiment1) + ' (' + str(len(exp1_zoom_pxchange_array)) + ')'), color='#781c6d', alpha = 0.85, linewidth=3)

axs[1, 0].set_facecolor('white')
axs[1, 0].set_ylabel('Jumping', fontsize = 14)
axs[1, 0].set_ylim(0, 0.8)
axs[1, 0].set_yticks([])
axs[1, 0].set_xlim(0, 50)
axs[1, 0].vlines(looming_x_zoom, 0, 150, linestyles='dashed', lw= 0.5)
axs[1, 0].set_xlabel('Time (sec)', fontsize = 14)
axs[1, 0].set_xticks([0, 10, 20, 30, 40, 50])
axs[1, 0].set_xticklabels([-1, -0.5, 0, 0.5, 1, 1.5])
axs[1, 0].spines['left'].set_visible(False)
axs[1, 0].spines['bottom'].set_visible(True)
axs[1, 0].spines['right'].set_visible(False)
axs[1, 0].spines['top'].set_visible(False)
axs[1, 0].spines['left'].set_position(('outward', 5))
axs[1, 0].spines['bottom'].set_position(('outward', 5))
axs[1, 0].spines['left'].set_color('dimgrey')
axs[1, 0].spines['bottom'].set_color('dimgrey')
axs[1, 0].tick_params(axis='x', colors = 'k')
axs[1, 0].xaxis.label.set_color('k')
axs[1, 0].yaxis.label.set_color('k')
axs[1, 0].plot(x_coordinate, exp0_zoom_jumping_bined*10, label = (str(experiment0) + ' (' + str(len(exp0_zoom_jumping_array)) + ')'), color='grey', linewidth=3)
axs[1, 0].plot(x_coordinate, exp1_zoom_jumping_bined*10, label = (str(experiment1) + ' (' + str(len(exp1_zoom_jumping_array)) + ')'), color='#781c6d', alpha = 0.85, linewidth=3)
fig.savefig((str(path)+"/"+str(experiment_name)+"_zoom.png"), format='png') 


#SORTED HEATMAPS
#Control sorted
exp0_bin_sort_velocity = exp0_velocity_array[(np.transpose(exp0_stim_freezing) == 0).sum(axis=1).argsort()]
exp0_bin_sort_velocity_pops = np.ma.masked_greater(exp0_bin_sort_velocity, 0)

exp0_bin_sort_freezing = exp0_freezing_array[(np.transpose(exp0_stim_freezing) == 0).sum(axis=1).argsort()]
exp0_bin_sort_freezing_pops = np.ma.masked_equal(exp0_bin_sort_freezing, 1)

exp1_bin_sort_velocity = exp1_velocity_array[(np.transpose(exp1_stim_freezing) == 0).sum(axis=1).argsort()]
exp1_bin_sort_velocity_pops = np.ma.masked_greater(exp1_bin_sort_velocity, 0)

exp1_bin_sort_freezing = exp1_freezing_array[(np.transpose(exp1_stim_freezing) == 0).sum(axis=1).argsort()]
exp1_bin_sort_freezing_pops = np.ma.masked_equal(exp1_bin_sort_freezing, 1)

fig, axs = plt.subplots(1, 2, figsize=(20, 10))
fig.subplots_adjust(wspace = 0.02)

axs[0].xaxis.set_visible(False)
axs[0].yaxis.set_visible(False)
axs[0].set_title(str(experiment0))
axs[0].vlines(looming_x_frames, -6, 110, linestyles='-', lw= 0.5, color='white')
sns.heatmap(exp0_bin_sort_freezing, cmap="Greys" , cbar=False, alpha = 0.35, linewidths=0, ax=axs[0])
sns.heatmap(exp0_bin_sort_velocity, mask=exp0_bin_sort_freezing_pops, cmap='viridis', vmin=0, vmax=20, cbar=False, linewidths=0, ax=axs[0])

axs[1].xaxis.set_visible(False)
axs[1].yaxis.set_visible(False)
axs[1].set_title(str(experiment1))
axs[1].vlines(looming_x_frames, -6, 110, linestyles='-', lw= 0.5, color='white')
axs[1] = sns.heatmap(exp1_bin_sort_freezing, cmap="Greys" , cbar=False, alpha = 0.35, linewidths=0)
axs[1] = sns.heatmap(exp1_bin_sort_velocity, mask=exp1_bin_sort_freezing_pops, cmap='viridis', vmin=0, vmax=20, cbar=False, cbar_kws={"shrink": .25}, linewidths=0)
fig.savefig((str(path)+"/"+str(experiment_name)+"_heatmaps.png"), format='png') 
