import os
from .data_paths import folders_list


def create_directories(DIRECTORIES):
    directories_list = []
    for folder in folders_list:
        directories_path = os.path.join(DIRECTORIES, folder)
        os.makedirs(directories_path, exist_ok = True)
        directories_list.append(directories_path)
    return directories_list