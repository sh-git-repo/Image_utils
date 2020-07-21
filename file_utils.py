'''
NAME:
    file_utils.py

DESCRIPTION:
    Implements an abstract base class for a file handler.

CLASSES:
    FileHandler(from_path="./", to_path="./")
    -------------------------------------------------
    An abstract base class for file handlers.

    CONSTRUCTOR ARGUMENTS
    from_path -- The path where the file is located,
    please include the trailing slashes for the path.

    to_path -- The path where the file must be saved,
    please include the trailing slashes for the path.

    METHODS
    open_file(self)
        An abstract method to open the file.

    save_file(self)
        An abstract method to save the file.
'''
from abc import ABC, abstractmethod

class FileHandler(ABC):
    '''
    FileHandler(from_path, to_path=) --> ABC

    An abstract base class for file handlers.

    CONSTRUCTOR ARGUMENTS
    from_path -- The path where the file is located,
    please include the trailing slashes for the path.

    to_path -- The path where the file must be saved,
    please include the trailing slashes for the path.
    '''
    def __init__(self, from_path: str, to_path: str):
        self.from_path = from_path
        self.to_path = to_path

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def open_file(self):
        ''' An abstract method to open the file. '''
        pass

    @abstractmethod
    def save_file(self):
        ''' An abstract method to save the file. '''
        pass
