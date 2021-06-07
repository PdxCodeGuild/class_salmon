#this program will read cement bond logs for oil and gas, or geothermal wells
#cement bonding is important for well integrity, aquifer exclusion, and even formation integrity considerations
#pip install lasio#lasio is a python library for reading .las well log files - but this does not work outside of a notebook, I guess
import lasio #my first time using the lasio library
import glob #according to example from lasio but I am not sure what it needs to be here for
import numpy as np #numpy is a mathematics library in python; it looks like numpy actually downloads with lasio anyway
import pandas as pd#pandas is a library that helps you deal with sorting
import matplotlib.pyplot as plt #matplotlib is what I usually use in notebooks to visualize my data, another option that I like is seaborn, or plotly
#I have downloaded 2 cement bond logs from the North Dakota Industrial Commission reporting system
#Both wells should be owned and operated by WPX Energy, out of McKenzie County - the fracking Bakken
#this is sort of a publicly available resource, but you should pay the subscriber fee ($50)
import os#documents for reading file paths here (https://docs.python.org/3/library/os.html)
#Make the OOP
class Reader:
    def __init__(self, top_line = 0, bottom_line = 0, x_axis):#formation line top and bottom always start at zero feet
        #when you set one of the args for __init__ equal to something this means it is a default (from pete)
        self.top_line = top_line #arg1
        self.bottom_line = bottom_line #arg2
        self.x_axis = x_axis
    #formation thickness is the first function we want to return something directly from __init__
    def get_formationthickness(self):
        self.get_formationthickness = self.bottom_line - self.top_line
    #x axis value is the second function that is not doing the same thing upon initialization
    def mneumonic_value(self, x_axis):
        #this should print the mneumonic value on the x axis
        self.mneumonic_value = x_axis#modify this later 6/6/2021
        self.transactions.append((f"user deposited {amount}."))
    #check_withdrawal is the third function that is not doing the same thing upon initialization
    def check_withdrawal(self, amount):
        #we want to return true if the withdrawn amount wont make account negative
        if self.balance >= amount:
            return True
    #withdraw is the fourth function that is not doing the same thing upon initialization
    def withdraw(self, amount):
        #we want to decrease the balance by that amount
        self.balance -= amount
        self.transactions.append((f"user withdrew {amount}."))
    #calc_interest is the fifth function that is not doing the same thing upon initialization
    def calc_interest(self):
        #we want to multiply the balance by the interest rate, not sure what we should do with the earnings
        return self.balance * self.interest_rate
    def print_transactions(self):
        print(self.transactions)

    
    '''balance(self, account):
        balance = ATM(account, balance=self)
        self.balance.append(balance)#I feel like I do not know what this means.
    def interest_rate(self, account):
        interest_rate = ATM(account, interest_rate=self)
        self.interest_rate.append(interest_rate)
    def '''
#implement initilizer
atm = ATM() # create an **instance** of our class (also known as instantiating)
print('atm variable is ' + str(atm))
print('Welcome to the ATM')
while True:
    command = input('Enter a command: balance, deposit, withdraw, interest, previous transactions, help, exit ')
    if command == 'balance':
        print('command is ' +str(command))
        #print('balance is ' + str(balance))#the variable balance has not been defined yet, here
        #print(atm.balance())
        balance = atm.get_balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        #atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    #Previous transactions is for Version 2
    elif command == 'previous transactions':
        history = atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
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


print(f'Here is a list of of the wells in your directory: {las_files} ')#printing memory locations of las files

#if I remember correctly the numbers are the NDIC file number and CBL, of course, stands for cement bond logs

#https://lasio.readthedocs.io/en/latest/
print(f"The version information for {las_files[0]}: ")
version_well1 = log_readouts[0].version
print(version_well1)
table_of_well1 = log_readouts[0].curves
print(table_of_well1)
mneumonic = input('Look at the Mneumonics column. Pick an attribute to look at and write down the name. ')
pick_a_well = int(input(f'Write the index number of the well you would like to look at in this list, starting from 0: {las_files}'))
print(pick_a_well)

plt.figure(figsize=(9,10))
plt.subplot(1,2,1)
plt.plot((log_readouts[pick_a_well][mneumonic]), (log_readouts[pick_a_well]['DEPT']), '.', color='blue')
plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
plt.xlabel(f"{mneumonic} well log reading"); plt.ylabel("Depth (ft)")
plt.grid(True)
plt.gca().invert_yaxis()

plt.subplot(1,2,2)
plt.plot(log_readouts[pick_a_well]['AMP3FT'], (log_readouts[pick_a_well]['DEPT']), '.', color='red')
plt.title(f"This is the Cement Bond Log of {las_files[pick_a_well]}", pad=20, size=11)
plt.xlabel(f"'AMP3FT' well log reading from {las_files[pick_a_well]}"); plt.ylabel("Depth (ft)")
plt.grid(True)
plt.gca().invert_yaxis()

plt.tight_layout(pad=2.0) # set distance between two plots
plt.show()
#reference for a cement bond log https://www.bonnettsenergy.com/images/pdf_files/2018/cement_bond_log_quick_reference.pdf
