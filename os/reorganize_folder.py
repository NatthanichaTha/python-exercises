import shutil
import os
import sys

#shutil.move("phonebook.txt", "..")
folder_path = sys.argv[1]
file_list = os.listdir(folder_path)
image_file = ("jpg", "png", "gif")
video_file = ("mp4", "mkv", "avi") 
document_file = ("docx", "xlsx", "txt", "pdf")

image_folder_path = os.path.join(folder_path, "Image")
video_folder_path = os.path.join(folder_path, "Video")
document_folder_path = os.path.join(folder_path, "Documents")
other_folder_path = os.path.join(folder_path, "Others")

os.makedirs(image_folder_path, exist_ok=True)
os.makedirs(video_folder_path, exist_ok=True)
os.makedirs(document_folder_path, exist_ok=True)
os.makedirs(other_folder_path, exist_ok=True)
            
for item in file_list:
    item_path = os.path.join(folder_path, item)
    item_name_split = item.split(".")
    if len(item_name_split) == 1:
        item_extension = ""
    else:
        item_extension = item_name_split[-1]
    if item_extension in image_file:
        shutil.move(item_path, image_folder_path)
    elif item_extension in video_file:
        shutil.move(item_path, video_folder_path)
    elif item_extension in document_file:
        shutil.move(item_path, document_folder_path)
    else:
        shutil.move(item_path, other_folder_path)