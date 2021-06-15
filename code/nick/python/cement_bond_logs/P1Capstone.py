#this program will read cement bond logs for oil and gas, or geothermal wells
#cement bonding is important for well integrity, aquifer exclusion, and even formation integrity considerations
#pip install lasio#lasio is a python library for reading .las well log files - but this does not work outside of a notebook or terminal, I guess
import time
from datetime import date#goes in the pdf output file
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
from fpdf import FPDF #another library I found to generate a formatted PDF report http://www.fpdf.org/ this creates a class according to docs
#Make the OOP
class Reader_cbl:
    def __init__(self, for_that_well):#formation line top and bottom always start at zero feet
        # #when you set one of the args for __init__ equal to something this means it is a default (from pete)
        self.self = self
        self.for_that_well = for_that_well
    def plot_a_log(self, for_that_well):
        plt.figure(figsize=(9,10)) 
        plt.subplot(1,2,1)
        plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
        plt.title(f"This is the time of return for the transmission \non {las_files[pick_a_well]}", pad=20, size=11)
        plt.xlabel(f"{'TT3FT'} well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)#Define the line properties of the grid
        plt.gca().invert_yaxis()

        plt.subplot(1,2,2)
        p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
        #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
        plt.title(f"This is the sound wave amplitude \nof {las_files[pick_a_well]}", pad=20, size=11)
        #plt.legend((p1[0], p2[0]), (['Actual amplitude reading', 'average amplitude reading']))
        plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)
        plt.gca().invert_yaxis()#get the current axes (gca), then invert the y-axis

        plt.tight_layout(pad=2.8) # set distance between two plots
        # plt.savefig('well_report_plot.png', dpi = 400)
        plt.show()
    def save_plot_a_log(self, for_that_well, dpi_user = 300):
        plt.figure(figsize=(9,10)) 
        plt.subplot(1,2,1)
        plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
        plt.title(f"This is the time of return for the transmission \non {las_files[pick_a_well]}", pad=20, size=11)
        plt.xlabel(f"{'TT3FT'} well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)
        plt.gca().invert_yaxis()
        #another subplot, adjacent on the x-axis. The subplot function considers this the next column.
        plt.subplot(1,2,2)
        p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
        #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
        plt.title(f"This is the sound wave amplitude \nof {las_files[pick_a_well]}", pad=20, size=11)
        #plt.legend((p1[0], p2[0]), (['Actual amplitude reading', 'average amplitude reading']))
        plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)
        plt.gca().invert_yaxis()

        plt.tight_layout(pad=2.8) # set distance between two plots
        plt.savefig('well_report_plot.jpeg', dpi = dpi_user, bbox_inches = "tight")#added bbox_inches to stop the save fig from cutting off text
        plt.show()
        print('Your visualization of the well logs has been saved as well_report_plot.jpeg')

    def plot_a_log_with_hlines(self, for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp):
        plt.figure(figsize=(9,10)) 
        plt.subplot(1,2,1)
        plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
        plt.hlines(top_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
        plt.hlines(bottom_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', zorder = 3)
        plt.title(f"This is the time of return for the transmission \non {las_files[pick_a_well]}", pad=20, size=11)
        plt.legend()
        plt.xlabel(f"{'TT3FT'} well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)#Define the line properties of the grid
        plt.gca().invert_yaxis()

        plt.subplot(1,2,2)
        p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
        plt.hlines(top_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
        plt.hlines(bottom_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', zorder = 3)
        #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
        plt.title(f"This is the sound wave amplitude \nof {las_files[pick_a_well]}", pad=20, size=11)
        plt.legend()
        plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)#Define the line properties of the grid
        plt.gca().invert_yaxis()

        plt.tight_layout(pad=2.8) # set distance between two plots
        # plt.savefig('well_report_plot.png', dpi = 400)
        plt.show()
        #print(plot_a_log_with_hlines(for_that_well,top_line,bottom_line))

    def save_plot_a_log_with_hlines(self, for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp, dpi_user = 300):
        plt.figure(figsize=(9,10)) 
        plt.subplot(1,2,1)
        plt.plot((log_readouts[pick_a_well]['TT3FT']), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
        plt.hlines(top_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
        plt.hlines(bottom_line, x_min_vdl, x_max_vdl, color = 'black', linestyles= 'dashdot', zorder = 3)#I think specifying the zorder above 2 makes it display on top
        plt.title(f"This is the time of return for the transmission \non {las_files[pick_a_well]}", pad=20, size=11)
        plt.legend()
        plt.xlabel("'TT3FT' well log reading of the time wave on \na Variable Density Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)#Define the line properties of the grid
        plt.gca().invert_yaxis()

        plt.subplot(1,2,2)
        p1 = plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
        plt.hlines(top_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', label='Area of Concern Specified by User', zorder = 3)
        plt.hlines(bottom_line, x_min_amp, x_max_amp, color = 'black', linestyles= 'dashdot', zorder = 3)
        #p2 = plt.plot((log_readouts[pick_a_well]['DEPT']), log_readouts[pick_a_well]['AMPAVG'])
        plt.title(f"This is the sound wave amplitude \nof {las_files[pick_a_well]}", pad=20, size=11)
        plt.legend()
        plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]} of the amplitude\nof the sound wave in the Cement Bond Log"); plt.ylabel("Depth (ft)")
        plt.grid(True)#Define the line properties of the grid
        plt.gca().invert_yaxis()

        plt.tight_layout(pad=2.8) # set distance between two plots
        plt.savefig('well_report_plot.jpeg', dpi = dpi_user, bbox_inches = "tight")#added bbox_inches to stop the save fig from cutting off text
        plt.show()
        print('Your annotation of the well logs has been saved as well_report_plot.jpeg')
    
#following fpdf documentation, I will create a separate class for the document generation http://www.fpdf.org/
class PDF(FPDF):
    def lines(self):
        self.rect(.2, .2, 8.0,10.5)#this is the rectangle outside
    def header(self):
        self.set_font('Arial', 'B', 18)# Arial bold 18         
        self.cell(w=7.7, h=1.5, align='C', txt=f"Cement Bond Log Report for {well}", border=0)# Title. The w adjusts the size of the box the text floats in. Show the border if you want to find out where it is.
        self.set_text_color(220, 50, 50)#text color       
    def plots(self):
        self.image('well_report_plot.jpeg', 1.5, 1.3, 5.1, 7)

    def notes_body(self, top_line = 100, bottom_line = 100, annotation = 'No notes provided by user. This may indicate an incomplete/incorrect report. ', avg_amp_selected = 0, avg_time_selected = 0, avg_amp_all = 0, avg_time_all = 0, std_amp_selected = 0, std_time_selected = 0):
        statistics_notes = ''#an empty string as a default, if the user says no to adding statistics
        if avg_amp_selected != 0 or avg_time_selected != 0:
            statistics_notes = f'For the area of concern specified, the average time in usec is {avg_time_selected} with a standard deviation of {std_time_selected}.\nIn contrast, the average time of return for the entire length of the well log is {avg_time_all}.\nFor the area of concern specified, the average amplitude in mV is {avg_amp_selected} with a standard deviation of {std_amp_selected}.\nIn contrast, the average amplitude for the entire well log is {avg_amp_all}. '
        #     self.notes_body(top_line=top_line, bottom_line=bottom_line, annotation=annotation)
        # else:
        #     self.notes_body()
        today = date.today()
        self.set_font('Times', '', 7)
        self.set_xy(.3, 8.4)#previously set to 8.1 for y
        self.multi_cell(0, .12, txt = f'Well Logger Notes from {today}:\n{annotation}\nThe area of concern for casing inspection ranges from {top_line} - {bottom_line} feet.\n{statistics_notes} \n\nKey:\nHigh amplitudes indicate poor bonding or an absence of cement behind the casing. The opposite indicates the presence of cement.\nLonger return travel times indicate a signal coming from the formation wall, indicating good cement bonding. The opposite means there is likely poor bonding or no cement present. ', border=1, align='J')# Output justified text
        # self.ln(1)# Line break
        self.set_font('', 'I')# Mention in italics
        # self.cell(0, 5, 'some text')#fix this
    def footer(self):
        self.set_xy(5, 0.5)# Position at 1.5 cm from bottom
        self.set_font('Arial', 'I', 8)# Arial italic 8
        self.cell(0, 0, 'Page ' + str(self.page_no()) + ' of {nb}', 0, 0, 'C')# Page number

print('Welcome to the Cement Bond Log Reader')
path = '../cement_bond_logs' #path to files ../ represents the parent directory
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
#print(f'Here is a list of of the wells in your directory: {las_files} ')
las_files_dict = dict(enumerate(las_files, start=1))#bumps the starting number up to 1 for ease of use 6/9/2021
# print(las_files_dict)
print ("This is the catalog of wells in your directory: \n*******************\nSelection Number     Well File Number")#column head print
for key, value in las_files_dict.items():
    selection_number, well_file = key, value
    print (f"{key}                     {value}")#.format(selection_number, well_file))
pick_a_well = int(input(f'Write the index number of the well you would like explore in this list, starting from 1: '))-1#subtracting 1 to readjust to the index number in list las_files
while pick_a_well < 0:
    print('Please re-enter a valid selection number before continuing. ')
    pick_a_well = int(input(f'Write the index number of the well you would like explore in this list, starting from 1: '))-1
# print(pick_a_well)
for_that_well = log_readouts[pick_a_well]
top_line = 0#default starting value for REPL
bottom_line = 0#default starting value for REPL
annotation = ''#default starting string for REPL
avg_amp_selected = 0
avg_time_selected = 0
avg_amp_all = 0
avg_time_all = 0
std_time_selected = 0
std_amp_selected = 0
#implement initilizer
reader = Reader_cbl(for_that_well) # create an **instance** of our class (also known as instantiating)
while True:
    # pick_a_well = int(input(f'Write the index number of the well you would like explore in this list, starting from 0: {las_files}'))
    #     #print(pick_a_well)
    # for_that_well = log_readouts[pick_a_well]
    command = input('\n*************\nStart by visualizing your well log. \nNext annotate the plots as you wish.\nSave your figure.\nAfter saving your annotated plots, generate a PDF report if you wish.\n\nEnter a command: visualize, annotate, statistics, save figure, log report, annotation report, help, exit \n*************\n').lower()
    if command == 'visualize':
        well_report_plot = 'visualize'
        print('command is ' +str(command))
        # reader.plot_a_log(for_that_well) # call the bare plot a log method
        reader.plot_a_log(for_that_well)
        # return well_report_plot#return for later saving, if desired
    elif command == 'annotate': 
        well_report_plot = 'annotate'
        top_line = int(input('What is the top depth, in feet, of your area of concern in the well log? '))
        bottom_line = int(input('What is the bottom depth, in feet, of your area of concern in the well log? '))
        annotation = input('Write a sentence that describes your concern for this segment of casing. ')
        # annotation = 'this is a bad spot in the cement'#this text is here for test purposes
        # top_line = 4000#this should be feet as a test parameter
        # bottom_line = 5000 #this should be feet as a test parameter    
        x_min_vdl = min(log_readouts[pick_a_well]['TT3FT'])#time of signal return min x
        x_max_vdl = max(log_readouts[pick_a_well]['TT3FT'])
        x_min_amp = min(log_readouts[pick_a_well]['AMP3FT'])#amplitude of signal return min x
        x_max_amp = max(log_readouts[pick_a_well]['AMP3FT'])
        include_stats = input('Would you like to include statistics for amplitude and time of return across the area of concern? Yes or No ').lower()
        if include_stats == 'yes':
            df = las.df()#built-in lasio method to put data in panda df
            df_selected_amp = df['AMP3FT']#select only the amplitude columns
            df_selected_amp_rows = df_selected_amp[bottom_line:top_line]#select the length of casing along the area of concern https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
            # print(df_selected_amp_rows)
            df_selected_time= df['TT3FT']#select only the amplitude columns
            df_selected_time_rows = df_selected_time[bottom_line:top_line]    
            avg_amp_selected = np.around(np.average(df_selected_amp_rows))#average amplitude value of selected depths
            avg_time_selected = np.around(np.average(df_selected_time_rows))#average time of return value of selected depths
            std_amp_selected = np.around(np.std(df_selected_amp_rows))#standard deviation
            std_time_selected = np.around(np.std(df_selected_time_rows))
            avg_amp_all = np.around(np.average(df_selected_amp))
            avg_time_all = np.around(np.average(df_selected_time))
        # average_amplitude = np.average()
        # reader.plot_a_log_with_hlines(for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp) # call the plot_a_log_with_hlines method
        reader.plot_a_log_with_hlines(for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp)
        #print() #maybe a docx report if I can find another python library to do so
        # return well_report_plot#return for later saving, if desired
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
    elif command == 'annotation report':
        # Instantiation of inherited class for each iteration of the loop
        pdf = PDF(orientation='P', unit='in', format='Letter')#orientation is portrait, units are inches (formatting on x,y coord), format is letter
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.lines()
        pdf.plots()#freezing the file writing
        pdf.set_font('Times', '', 12)
        if top_line != 0 or bottom_line != 0 or annotation != '':
            pdf.notes_body(top_line, bottom_line, annotation, avg_amp_selected, avg_time_selected, avg_amp_all, avg_time_all, std_amp_selected, std_time_selected)
        else:
            pdf.notes_body()
        # pdf.notes_body(top_line, bottom_line, annotation)
        pdf.footer()
        if os.path.exists('output_report.pdf'):
            os.remove('output_report.pdf')#this is to remove any old pdf by the same name in the directory
        pdf.output('output_report.pdf', 'F')
        # pdf.close()
        print('\n*************\nThe annotated plot with your notes has been saved as "output_report.pdf" in the same directory as this program. \nThis report will be overwritten if you generate another annotated report.\nSave the file elsewhere if you wish to keep it.\n*************\n')
    elif command == 'save figure':
        resolution = float(input('What is the resolution of the image you want saved? 300-600 dpi '))
        if well_report_plot == 'visualize':
            reader.save_plot_a_log(for_that_well, resolution)
        elif well_report_plot == 'annotate':
            reader.save_plot_a_log_with_hlines(for_that_well, top_line, bottom_line, x_min_vdl, x_max_vdl, x_min_amp, x_max_amp, resolution)
        else:
            print('///////////////////////////////////////////////////////////\nBefore saving the last figure, please visualize or annotate the well logs. \n///////////////////////////////////////////////////////////')
    elif command == 'help':
        print('Available commands:')
        print('visualize  - begin by looking at a raw plot of the time of signal return and signal amplitude')
        print('annotate  - draw horizontal lines, marking the area of concern in the cement bond log')
        print('statistics - provide statistics of the .las well logs for amplitude and signal time')
        print('save figure - save a copy of the last figure you had in the visualization pane ')
        print('log report - display the file version, mneumonics, and units of measure in the well log')
        print('annotation report - generates and saves a PDF of the annotated plot with your notes ')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
# CURR_DIR = os.path.dirname(os.path.realpath(__file__))
# print(CURR_DIR)
# list_of_wells=  []
# path = 'C:/Users/Nick/Documents/GitHub/class_salmon/code/nick/cement_bond_logs' #path to files (absolute, will have to fix that)
# # status = os.path.isdir(path)#check if path exists 
# # print(status)

# files = os.listdir(path)
# # print(files)#there are two las files ['33846-CBL.las', '33847-CBL.las', 'P1Capstone.py']
# las_files = []
# for file in files:
#     if file.endswith('.las'):#dumb lasio keeps trying to read .py file, trying endswith method https://www.w3schools.com/python/ref_string_endswith.asp
#         las_files.append(file)
# # print(las_files) #prints ['33846-CBL.las', '33847-CBL.las']

# # las = lasio.read(r'33846-CBL.las')#this reads a single las file
# # curves = las.curves
# # print(curves)#prints out the text junk

# log_readouts = []
# for well in las_files:
#     las = lasio.read(well)#reading in the las files to the list
#     log_readouts.append(las)#appending the list with the las files
# #put this stuff in a data frame with pandas
# df = las.df()#built-in lasio method to put data in panda df
# df_selected = df[['AMP3FT', 'TT3FT']]#select only the important columns for exercise
# print(df_selected)#check those columns, how they appear

# statistics = df_selected.describe()#built in statistics method for pandas
# print(statistics)#check for values that are inconsistent with rock properties

# print(f'Here is a list of of the wells in your directory: {las_files} ')#printing memory locations of las files

# #if I remember correctly the numbers are the NDIC file number and CBL, of course, stands for cement bond logs

# #https://lasio.readthedocs.io/en/latest/
# print(f"The version information for {las_files[0]}: ")
# version_well1 = log_readouts[0].version
# print(version_well1)
# table_of_well1 = log_readouts[0].curves
# print(table_of_well1)
# #mneumonic = input('Look at the Mneumonics column. Pick an attribute to look at and write down the name. ')
# pick_a_well = int(input(f'Write the index number of the well you would like to look at in this list, starting from 0: {las_files}'))
# #print(pick_a_well)
# for_that_well = log_readouts[pick_a_well]
# # list_for_that_well = list(log_readouts[pick_a_well])
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
# top_line = 4000#this should be feet as a test parameter
# bottom_line = 5000 #this should be feet as a test parameter
# # len_x =len(log_readouts[pick_a_well]['TT3FT'])
# # print(len_x)
# x_min_vdl = min(log_readouts[pick_a_well]['TT3FT'])
# x_max_vdl = max(log_readouts[pick_a_well]['TT3FT'])
# x_min_time= min(log_readouts[pick_a_well]['AMP3FT'])
# x_max_amp = max(log_readouts[pick_a_well]['AMP3FT'])
# #print(x_min_vdl)
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