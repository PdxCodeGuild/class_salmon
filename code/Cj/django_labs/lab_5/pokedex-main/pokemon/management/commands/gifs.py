import os

file_path = 'C:\\Users\\Cj\\Documents\\PDX_CODE_GUILD_BOOT_CAMP\\class_salmon\\code\\cj\\django_labs\\lab_5\\pokedex-main\\static\\animated'
gif_list = []
# i = 1
for file_name in os.listdir(file_path):
    gif_list.append(file_name)

gif_list= sorted(gif_list, key=len)
# print(gif_list)

i = 0
for x in gif_list:

    print(gif_list[i])

    i+=1



