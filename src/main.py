from functions.file_cleaning_utils import create_directories
from functions.file_cleaning_utils import create_files


DIRECTORIES = 'directories/path/folders'
directories_list = create_directories(DIRECTORIES)
files_list = create_files(directories_list)
# skip_list = []


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