"""
TODO: 
"""

__author__ = "James Cook"
__copyright__ = "Copyright (C) 2021 James Cook"
__license__ = "GNU General Public License v3"
__version__ = "1.0.0"
__maintainer__ = "James Cook"
__email__ = "contact@cookjames.uk"

from os import listdir
from os.path import isfile, join
import os
import shutil
from pathlib import Path


DOWNLOADS_PATH = str(Path.home() / "Downloads")


def sort_files_in_a_folder(folder=DOWNLOADS_PATH):
    '''
    A function to sort the files in a download folder
    into their respective categories
    '''

    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    file_type_variation_list = []
    filetype_folder_dict = {}

    for file in files:
        filetype = file.split('.')[-1]
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)
            new_folder_name = folder + '/' + filetype
            filetype_folder_dict[str(filetype)] = str(new_folder_name)
            if os.path.isdir(new_folder_name) == True:  # folder exists
                continue
            else:
                os.mkdir(new_folder_name)

    for file in files:
        src_path = folder + '/' + file
        filetype = file.split('.')[-1]
        if filetype in filetype_folder_dict.keys():
            dest_path = filetype_folder_dict[str(filetype)]
            shutil.move(src_path, dest_path)


if __name__ == "__main__":
    sort_files_in_a_folder(DOWNLOADS_PATH)