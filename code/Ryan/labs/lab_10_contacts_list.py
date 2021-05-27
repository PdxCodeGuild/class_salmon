import sys, os, io, math

contacts = open("contacts.csv", "w+")
#contacts.write("a,b,c\na1,b1,c1\na2,b2,c2")
contacts
contacts.close()

with open('contacts.csv', 'r') as file:
   lines = file.read().split('\n') 

print(lines)

headers = []
row2 = []
row3 = []

for l in lines[0].split(","):
    headers.append(l)

for l in lines[1].split(","):
    row2.append(l)

for l in lines[2].split(","):
    row3.append(l)

print(headers)
print(row2)
print(row3)

# Ask user for choice
menu = int(input(f"\n(1) Create \n(2) Retrieve \n(3) Update \n(4) Delete \nPick: "))

# Create a record
if menu == 1:

    new_header = headers.append(input("Enter new header: "))        
    new_row2 = row2.append(input("Enter new column in row 2: "))
    new_row3 = row3.append(input("Enter new column in row 3: "))
    print(headers)
    print(row2)
    print(row3)

# Retrieve a record
if menu == 2:
    find_header = input(f"Select a header {headers}: ")

# # Create a record
# create_name = input()

# f = open("contacts.csv", "r")
# #lines = file.read().split('\n') 
# # lines = file.read().split(",")

# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n') 


#ari_scale = {
#     1: {"name": "", "favorite fruit": "", "favorite color": ""},
#}



"""
with f as file:
    lines = file.read().split('\n') 
    lines = lines.split(",")
    print(lines)
    lines = [lines]
    for i in lines:
        print(i, lines[i])
"""

