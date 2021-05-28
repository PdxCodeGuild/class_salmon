import os

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(file)
# with open('contacts.csv', 'r') as file:
#     firstline = True
#     a = []
#     for line in file:
#         if firstline:
#             mykeys = "".join(line.split()).split(',')
#             firstline = False
#         else:
#             values = "".join(line.split()).split(',')
#             a.append({mykeys[n]:values[n] for n in range(0,len(mykeys))})
# print(a)