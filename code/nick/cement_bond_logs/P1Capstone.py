#this program will read cement bond logs for oil and gas, or geothermal wells
#cement bonding is important for well integrity, aquifer exclusion, and even formation integrity considerations
#pip install lasio#lasio is a python library for reading .las well log files - but this does not work outside of a notebook, I guess
import lasio #my first time using the lasio library
import glob #according to example from lasio but I am not sure what it needs to be here for
import numpy as np #numpy is a mathematics library in python; it looks like numpy actually downloads with lasio anyway
import pandas as pd#pandas is a library that helps you deal with sorting
import matplotlib.pyplot as plt #matplotlib is what I usually use in notebooks to visualize my data, another option that I like is seaborn, or plotly
from matplotlib.collections import LineCollection #so I can modify the z-order of lines on the plot
#I have downloaded 2 cement bond logs from the North Dakota Industrial Commission reporting system
#Both wells should be owned and operated by WPX Energy, out of McKenzie County - the fracking Bakken
#this is sort of a publicly available resource, but you should pay the subscriber fee ($50)
import os#documents for reading file paths here (https://docs.python.org/3/library/os.html)
#Make the OOP
class Reader_cbl:
    def __init__(self, type, top_line = 0, bottom_line = 0, x_axis):#formation line top and bottom always start at zero feet
        #when you set one of the args for __init__ equal to something this means it is a default (from pete)
        self.top_line = top_line #arg1
        self.bottom_line = bottom_line #arg2
        self.x_axis = x_axis
        self.type = type#this should be a variable density log or a amplitude log
    #casing problem thickness is the method function we want to return something directly from __init__
    def __get_casingproblemthickness(self):
        self.__get_casingproblemthickness = self.bottom_line - self.top_line#private method?
    #x axis value is the second method that is not doing the same thing upon initialization
    # def mneumonic_value(self, x_axis):
    #     #this should print the mneumonic value on the x axis
    #     self.mneumonic_value = x_axis#modify this later 6/6/2021
    #check_withdrawal is the third method that is not doing the same thing upon initialization
    # def type_reading(self, type):#this should be to help the user interpret the log
    #     #we want to return true if the withdrawn amount wont make account negative
    #     if self.type == 'VDL':#check this
    #         #check if thick or thin on x_axis, thick (no return signal) means good cement bond
    #     if self.type == 'AMP3FT':
    #         check if thick or thin on x_axis. Thin (weak signal) means cement present, strong signal means no cement
    def plot_a_log(self, for_that_well):
        plt.figure(figsize=(9,10)) 
        plt.subplot(1,2,1)
        plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
        plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
        plt.xlabel(f"{'TT3FT'} well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)
        plt.gca().invert_yaxis()

        plt.subplot(1,2,2)
        p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
        #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
        plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
        #plt.legend((p1[0], p2[0]), (['Actual amplitude reading', 'average amplitude reading']))
        plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)
        plt.gca().invert_yaxis()

        plt.tight_layout(pad=2.0) # set distance between two plots
        plt.show()
    def plot_a_log_with_hlines(self, for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp):
        plt.figure(figsize=(9,10)) 
        plt.subplot(1,2,1)
        plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
        plt.hlines(top_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
        plt.hlines(bottom_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', zorder = 3)
        plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
        plt.legend()
        plt.xlabel(f"{'TT3FT'} well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)
        plt.gca().invert_yaxis()

        plt.subplot(1,2,2)
        p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
        plt.hlines(top_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
        plt.hlines(bottom_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', zorder = 3)
        #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
        plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
        plt.legend()
        plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)
        plt.gca().invert_yaxis()

        plt.tight_layout(pad=2.0) # set distance between two plots
        plt.show()
        #print(plot_a_log_with_hlines(for_that_well,top_line,bottom_line))
    #printing the log report is the sixth method
    def withdraw(self, amount):
        #we want to decrease the balance by that amount
        self.balance -= amount
        self.transactions.append((f"user withdrew {amount}."))
    # #calc_interest is the fifth function that is not doing the same thing upon initialization
    # def calc_interest(self):
    #     #we want to multiply the balance by the interest rate, not sure what we should do with the earnings
    #     return self.balance * self.interest_rate
    # def print_transactions(self):
    #     print(self.transactions)

#implement initilizer
reader = Reader_cbl() # create an **instance** of our class (also known as instantiating)
#print('reader variable is ' + str(atm))
print('Welcome to the Cement Bond Log Reader')
path = 'C:/Users/Nick/Documents/GitHub/class_salmon/code/nick/cement_bond_logs' #path to files (absolute, will have to fix that)
# status = os.path.isdir(path)#check if path exists 
# print(status)

files = os.listdir(path)
# print(files)#there are two las files ['33846-CBL.las', '33847-CBL.las', 'P1Capstone.py']
las_files = []
for file in files:
    if file.endswith('.las'):#dumb lasio keeps trying to read .py file, trying endswith method https://www.w3schools.com/python/ref_string_endswith.asp
        las_files.append(file)
log_readouts = []
for well in las_files:
    las = lasio.read(well)#reading in the las files to the list
    log_readouts.append(las)#appending the list with the las files
print(f'Here is a list of of the wells in your directory: {las_files} ')
while True:
    pick_a_well = int(input(f'Write the index number of the well you would like explore in this list, starting from 0: {las_files}'))
        #print(pick_a_well)
    for_that_well = log_readouts[pick_a_well]
    command = input('Start by visualizing your well log. \nEnter a command: visualize, annotate, statistics, save figure, log report, help, exit ').lower()
    if command == 'visualize':
        print('command is ' +str(command))
        reader.plot_a_log(for_that_well) # call the bare plot a log method
        well_report_plot = reader.plot_a_log(for_that_well)
        return well_report_plot#return for later saving, if desired
    elif command == 'annotate': 
        # top_line = int(input('What is the top depth, in feet, of your area of concern in the well log? '))
        # bottom_line = int(input('What is the bottom depth, in feet, of your area of concern in the well log? '))
        # annotation = input('Write a sentence that describes your concern for this segment of casing. ')
        top_line = 4000#this should be feet as a test parameter
        bottom_line = 5000 #this should be feet as a test parameter    
        x_min_vdl = min(log_readouts[pick_a_well]['TT3FT'])#time of signal return min x
        x_max_vdl = max(log_readouts[pick_a_well]['TT3FT'])
        x_min_amp = min(log_readouts[pick_a_well]['AMP3FT'])#amplitude of signal return min x
        x_max_amp = max(log_readouts[pick_a_well]['AMP3FT'])
        reader.plot_a_log_with_hlines(for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp) # call the plot_a_log_with_hlines method
        well_report_plot = reader.plot_a_log_with_hlines(for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp)
        #print() #maybe a docx report if I can find another python library to do so
        return well_report_plot#return for later saving, if desired
    elif command == 'statistics':
        #put this stuff in a data frame with pandas
        df = las.df()#built-in lasio method to put data in panda df
        df_selected = df[['AMP3FT', 'TT3FT']]#select only the important columns for exercise
        # print(df_selected)#check those columns, how they appear
        statistics = df_selected.describe()#built in statistics method for pandas
        print(statistics)#check for values that are inconsistent with rock properties
    elif command == 'log report':
        print(f"The version information for {las_files[pick_a_well]}: ")
        version_well = log_readouts[pick_a_well].version#fix this line so it takes user specified index
        print(version_well)
        table_of_well = log_readouts[pick_a_well].curves
        print(table_of_well)
    elif command == 'save figure':
        amount = reader.calc_interest() # call the calc_interest() method
        #reader.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('visulize  - begin by looking at a raw plot of the time of signal return and signal amplitude')
        print('annotate  - draw horizontal lines, marking the area of concern in the cement bond log')
        print('statistics - provide statistics of the .las well logs for amplitude and signal time')
        print('save figure - save a copy of the last figure you had in the visualization pane ')
        print('log report - display the file version, mneumonics, and units of measure in the well log')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
# CURR_DIR = os.path.dirname(os.path.realpath(__file__))
# print(CURR_DIR)
# list_of_wells=  []
path = 'C:/Users/Nick/Documents/GitHub/class_salmon/code/nick/cement_bond_logs' #path to files (absolute, will have to fix that)
# status = os.path.isdir(path)#check if path exists 
# print(status)

files = os.listdir(path)
# print(files)#there are two las files ['33846-CBL.las', '33847-CBL.las', 'P1Capstone.py']
las_files = []
for file in files:
    if file.endswith('.las'):#dumb lasio keeps trying to read .py file, trying endswith method https://www.w3schools.com/python/ref_string_endswith.asp
        las_files.append(file)
# print(las_files) #prints ['33846-CBL.las', '33847-CBL.las']

# las = lasio.read(r'33846-CBL.las')#this reads a single las file
# curves = las.curves
# print(curves)#prints out the text junk

log_readouts = []
for well in las_files:
    las = lasio.read(well)#reading in the las files to the list
    log_readouts.append(las)#appending the list with the las files
#put this stuff in a data frame with pandas
df = las.df()#built-in lasio method to put data in panda df
df_selected = df[['AMP3FT', 'TT3FT']]#select only the important columns for exercise
print(df_selected)#check those columns, how they appear

statistics = df_selected.describe()#built in statistics method for pandas
print(statistics)#check for values that are inconsistent with rock properties

print(f'Here is a list of of the wells in your directory: {las_files} ')#printing memory locations of las files

#if I remember correctly the numbers are the NDIC file number and CBL, of course, stands for cement bond logs

#https://lasio.readthedocs.io/en/latest/
print(f"The version information for {las_files[0]}: ")
version_well1 = log_readouts[0].version
print(version_well1)
table_of_well1 = log_readouts[0].curves
print(table_of_well1)
#mneumonic = input('Look at the Mneumonics column. Pick an attribute to look at and write down the name. ')
pick_a_well = int(input(f'Write the index number of the well you would like to look at in this list, starting from 0: {las_files}'))
#print(pick_a_well)
for_that_well = log_readouts[pick_a_well]
# list_for_that_well = list(log_readouts[pick_a_well])
# print(list_for_that_well)

# def plot_a_log(for_that_well):
#     plt.figure(figsize=(9,10)), 
#     plt.subplot(1,2,1)
#     plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
#     plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
#     plt.xlabel(f"{'TT3FT'} well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
#     plt.grid(True)
#     plt.gca().invert_yaxis()

#     plt.subplot(1,2,2)
#     p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
#     #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
#     plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
#     #plt.legend((p1[0], p2[0]), (['Actual amplitude reading', 'average amplitude reading']))
#     plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
#     plt.grid(True)
#     plt.gca().invert_yaxis()

#     plt.tight_layout(pad=2.0) # set distance between two plots
#     plt.show()
# #reference for a cement bond log https://www.bonnettsenergy.com/images/pdf_files/2018/cement_bond_log_quick_reference.pdf
# plot_a_log(log_readouts[pick_a_well])#has to close out before next function
#now we can plot a log with a top and bottom for the user
top_line = 4000#this should be feet as a test parameter
bottom_line = 5000 #this should be feet as a test parameter
# len_x =len(log_readouts[pick_a_well]['TT3FT'])
# print(len_x)
x_min_vdl = min(log_readouts[pick_a_well]['TT3FT'])
x_max_vdl = max(log_readouts[pick_a_well]['TT3FT'])
x_min_amp = min(log_readouts[pick_a_well]['AMP3FT'])
x_max_amp = max(log_readouts[pick_a_well]['AMP3FT'])
#print(x_min_vdl)
# def plot_a_log_with_hlines(for_that_well, top_line, bottom_line):
#     plt.figure(figsize=(9,10)), 
#     plt.subplot(1,2,1)
#     plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
#     plt.hlines(top_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
#     plt.hlines(bottom_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', zorder = 3)
#     plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
#     plt.legend()
#     plt.xlabel(f"{'TT3FT'} well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
#     plt.grid(True)
#     plt.gca().invert_yaxis()

#     plt.subplot(1,2,2)
#     p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
#     plt.hlines(top_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
#     plt.hlines(bottom_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', zorder = 3)
#     #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
#     plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
#     plt.legend()
#     plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
#     plt.grid(True)
#     plt.gca().invert_yaxis()

#     plt.tight_layout(pad=2.0) # set distance between two plots
#     plt.show()
# print(plot_a_log_with_hlines(for_that_well,top_line,bottom_line))