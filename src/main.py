import os
from paths import folder_list, file_list

DIRECTORYS = 'directorys'

for folder_path, file_path in zip(folder_list, file_list):
    directory_path = DIRECTORYS + folder_path
    os.makedirs(directory_path, exist_ok = True )
    
    with open(directory_path+file_path, 'w') as file:
        pass




