import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
with open('c:\\Users\\achen\\OneDrive\\Documents\\pdx_code\\class_salmon\\code\\austin\\lab10\\contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)