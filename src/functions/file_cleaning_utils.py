import os
import shutil
from .data_paths import folders_list


def create_directories(DIRECTORIES):
    directories_list = []
    for folder in folders_list:
        directories_path = os.path.join(DIRECTORIES, folder)
        os.makedirs(directories_path, exist_ok = True)
        directories_list.append(directories_path)
    return directories_list


def create_files(directories_list):
    files_paths_list = []
    for folder in directories_list:
        file_path = os.path.join(folder, 'file.txt')
        with open(file_path, 'w') as file:
            pass
        files_paths_list.append(file_path)
    return files_paths_list


def clean_folders(directories_list, skip_clean):
    for folder in directories_list:
        if folder not in skip_clean:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                os.remove(file_path)


def delete_folders(directories_list, skip_clean):
    for folder in directories_list:
        if folder not in skip_clean:
            try:
                shutil.rmtree(folder)
            except OSError:
                for file in os.listdir(folder):
                    file_path = os.path.join(folder, file)
                    os.remove(file_path)