#this program will read cement bond logs for oil and gas, or geothermal wells
#cement bonding is important for well integrity, aquifer exclusion, and even formation integrity considerations
#pip install lasio#lasio is a python library for reading .las well log files - but this does not work outside of a notebook, I guess
import lasio
import glob #according to example from lasio
import numpy as np #numpy is a mathematics library in python; it looks like numpy actually downloads with lasio anyway
import pandas as pd#pandas is a library that helps you deal with sorting
import matplotlib as plt #matplotlib is what I usually use in notebooks to visualize my data, another option that I like is seaborn, or plotly
#I have downloaded 2 cement bond logs from the North Dakota Industrial Commission reporting system
#Both wells should be owned and operated by WPX Energy, out of McKenzie County - the fracking Bakken
#this is sort of a publicly available resource, but you should pay the subscriber fee ($50)
import os#documents for reading file paths here (https://docs.python.org/3/library/os.html)
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
    if file.endswith('.las'):
        las_files.append(file)
# print(las_files) #prints ['33846-CBL.las', '33847-CBL.las']

# las = lasio.read(r'33846-CBL.las')#this reads a single las file
# curves = las.curves
# print(curves)#prints out the text junk

# for well in bond_logs:
#     well = os.path.splitext(os.path.basename(well))[0]#Leading periods on the basename are ignored; splitext('.cshrc') returns ('.cshrc', '')
#     list_of_wells.append(well)
log_readouts = []
for well in las_files:#dumb lasio keeps trying to read .py file, trying endswith method https://www.w3schools.com/python/ref_string_endswith.asp
    las = lasio.read(well)#reading in the las files to the list
    log_readouts.append(las)#appending the list with the las files
    # print(log_readouts)#printing memory locations of las files

#if I remember correctly the numbers are the NDIC file number and CBL, of course, stands for cement bond logs

#https://lasio.readthedocs.io/en/latest/
print(f"The version information for {las_files[0]}: ")
version_well1 = log_readouts[0].version
print(version_well1)
table_of_well1 = log_readouts[0].curves
print(table_of_well1)
