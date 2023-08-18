import os
# from src.features.paths import folder_list, file_list
from functions.file_cleaning_utils import create_directories

DIRECTORIES = 'directories/path/folders'

# skip_list = []
# directories_list = []

directories_list = create_directories(DIRECTORIES)
print(directories_list)





# for folder_path, file_path in zip(folder_list, file_list):
#     directory_path = DIRECTORIES + folder_path
#     os.makedirs(directory_path, exist_ok = True )
    
#     full_path = directory_path+file_path
#     with open(full_path, 'w') as file:
#         pass
#     directories_list.append(directory_path)

# answer = input("Do you really want to proced with the cleaning? [yes/not]: ")


# if answer.lower() in ('y', 'yes'):
#     while True:
#         directories_to_skip = input('Enter the directories to be preserved (press Enter to finish): ')
#         if directories_to_skip == '':
#             break
#         skip_list.append(directories_to_skip)


#     for dir_cleaning in directories_list:
#         if dir_cleaning not in skip_list:
#             for file_cleaning in os.listdir(dir_cleaning):
#                 path_cleaning = os.path.join(dir_cleaning, file_cleaning)
#                 os.remove(path_cleaning)