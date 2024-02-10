import os
import re

def remove_pattern_from_filenames(folder_path, pattern):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    files = os.listdir(folder_path)

    regex_pattern = re.compile(pattern)

    for file_name in files:
        if regex_pattern.search(file_name):
            new_file_name = regex_pattern.sub('', file_name)
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)

            os.rename(old_file_path, new_file_path)
            print(f"Renamed file: {old_file_path} to {new_file_path}")

if __name__ == "__main__":
    folder_path = "E:/04_MEDIA/01_PHOTOS/01_CAMERA"
    # pattern = r'\(\d+\)'
    # pattern = r'^DOC-'
    # pattern = r'^IMG_'
    pattern = r'^P_'

    remove_pattern_from_filenames(folder_path, pattern)
