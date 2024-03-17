import time
from datetime import datetime
import os
import sys

# print(datetime.fromtimestamp(time.time()))
# print(os.listdir("."))
# print(datetime.fromtimestamp(os.path.getatime("./retime_subtitle_2.py")))
# print(os.path.isfile("./choose.py"))

# Make a program that given a path to a folder, prints all the files (not directories!)
# in that folder whose last access is more than one month

folder_path = sys.argv[1]
file_list = os.listdir(folder_path)
old_file = []
for item in file_list:
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path) and time.time() - os.path.getatime(item_path) > 2592000:
        old_file.append(item)

print(old_file)