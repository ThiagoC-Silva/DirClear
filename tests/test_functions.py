import os
from src.functions.file_cleaning_utils import create_directories
from src.functions.file_cleaning_utils import create_files

def test_create_directories(tmpdir):
    directory_test = tmpdir.mkdir('directories')
    directory_list = create_directories(directory_test)
    for directory in directory_list:
        assert os.path.exists(directory)


def test_create_files(tmpdir):
    directory_test = tmpdir.mkdir('directories')
    directory_list = create_directories(directory_test)
    files_list = create_files(directory_list)
    for file_path in files_list:
        assert os.path.exists(file_path)