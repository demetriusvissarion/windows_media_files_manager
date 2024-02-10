import os
import re

def delete_files_with_pattern(folder_path, pattern):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Create a regular expression pattern
    regex_pattern = re.compile(pattern)

    # Iterate through the files and delete those matching the pattern
    for file_name in files:
        if regex_pattern.search(file_name):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

if __name__ == "__main__":
    # Specify the folder path and pattern (e.g., any number inside parentheses)
    folder_path = "E:/04_MEDIA/01_PHOTOS/01_CAMERA"
    pattern = r'\(\d+\)'

    # Call the function to delete files with the specified pattern
    delete_files_with_pattern(folder_path, pattern)

