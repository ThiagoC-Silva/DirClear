import os
from functions.file_cleaning_utils import create_directories
from functions.file_cleaning_utils import create_files
from functions.file_cleaning_utils import clean_folders
from functions.file_cleaning_utils import delete_folders


DIRECTORIES = 'directories/path/folders'
directories_list = create_directories(DIRECTORIES)
files_list = create_files(directories_list)
skip_clean = []


answer = input("Do you really want to proced with the cleaning? [yes/not]: ")

if answer.lower() in ('y', 'yes'):
    while True:
        folder_skip = input('Enter the directories to be preserved (press Enter to finish): ')
        if folder_skip == '':
            break

        full_path_skip = os.path.join(DIRECTORIES, folder_skip)
        skip_clean.append(full_path_skip)
    
    while True:
        clear = input('1 - [Delete folders] / 2 - [Clean folders]: ')
        if clear in ('1', '2'):
            break
    
    if clear == '1':
        delete_folders(directories_list, skip_clean)
    else:
        clean_folders(directories_list, skip_clean)

else:
    print('Cleaning process canceled.')

