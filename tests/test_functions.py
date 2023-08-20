import os
from pytest import fixture
from src.functions.file_cleaning_utils import create_directories
from src.functions.file_cleaning_utils import create_files
from src.functions.file_cleaning_utils import clean_folders
from src.functions.file_cleaning_utils import delete_folders

@fixture
def test_directory_list(tmpdir):
    directory_test = tmpdir.mkdir('directories')
    directory_list = create_directories(directory_test)
    return directory_list


def test_create_directories(test_directory_list):
    for directory in test_directory_list:
        assert os.path.exists(directory)


def test_create_files(test_directory_list):
    files_list = create_files(test_directory_list)
    for file_path in files_list:
        assert os.path.exists(file_path)


def test_clean_folders(test_directory_list):
    full_path_list = []
    for directory in test_directory_list:
        dir_with_file = os.path.join(directory, 'file_test.txt')
        with open(dir_with_file, 'w') as file:
            pass

    skip_clean_test = [test_directory_list[0], test_directory_list[2]]
    clean_folders(test_directory_list, skip_clean_test)

    for folder in test_directory_list:
        if folder not in skip_clean_test:
            assert len(os.listdir(folder)) == 0
        else:
            assert len(os.listdir(folder)) > 0


def test_delete_folders(test_directory_list):
    skip_clean_test = [test_directory_list[0], test_directory_list[2]]
    delete_folders(test_directory_list, skip_clean_test)

    for folder in test_directory_list:
        if folder not in skip_clean_test:
            assert os.path.exists(folder) == False or len(os.listdir(folder)) == 0
        else:
            assert os.path.exists(folder) == True


def test_delete_folders_no_skip(test_directory_list):
    skip_clean_test = []
    delete_folders(test_directory_list, skip_clean_test)

    for folder in test_directory_list:
        assert os.path.exists(folder) == False or len(os.listdir(folder)) == 0

