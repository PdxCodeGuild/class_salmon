import os

folder_path = 'C:\\Users\\Cj\\Documents\\PDX_CODE_GUILD_BOOT_CAMP\\class_salmon\\code\\cj\\django_labs\\lab_5\\pokedex-main\\static\\animated'

for file_name in os.listdir(folder_path):
    print(file_name)