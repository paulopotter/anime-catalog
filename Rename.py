import os

all_dir_names = os.listdir(os.getcwd())

for dir_name in all_dir_names:
    os.rename(dir_name, dir_name.capitalize())
