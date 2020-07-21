'''
NAME:
    utilities.py

DESCRIPTION:
    Some extra utility functions.

FUNCTIONS:
    create_folder(folder_path)
    ----------------------------------------
    Creates new folder at the specified path
    if it doesn't exist.
    ----------------------------------------
'''
import os

def create_folder(folder_path):
    '''
    create_folder(foler_path)

    Creates new folder at the specified path
    if it doesn't exist.

    folder_path -- It is the path where the folder
    must be created.
    '''
    if os.path.exists(folder_path) is False:
        os.makedirs(folder_path)
