'''
NAME:
    resize_interfaces.py

DESCRIPTION:
    Interfaces which have the relavent methods
    that allow for easy extension in the future.

CLASSES:
    PILResizeInterface(from_path, to_path) --> FileHandler
    -------------------------------------------------------------------------------------
    Models an interface that can open, resize and save
    a given image using PIL.

    CONSTRUCTOR ARGUMENTS
    see help(image_utils.file_utils.FileHandler)

    METHODS
    open_file(self, file_type="png", files_path="./")
        Yields a single opened image within a given directory
        if it matches the given image type.

        file_type -- It is the type of image file to be opened,
        for supported types please see PIL documentation.

    save_file(self, image, image_name)
        Saves the given image at the given to_path, also
        adds the prefix 'rsz_' to avoid overwriting of the
        original image.

        image -- It is the image that is to be saved,
        it must be a PIL.Image object.

        image_name -- It is the string representation of the
        name of the image file.

    resize(self, image, size, **kwargs)
        Resizes the given image to the given size,
        kwargs are to be provided in case of any extra parameters for PIL.Image.resize(),
        for example, test_obj.resize(image, (200, 200), resample=PIL.Image.NEAREST).
        for the full supported kwargs see the PIL documentation.

        image -- The image to be resized, must
        an object of PIL.Image.

        size -- The size to which the images must
        be resized, it is in the form, (width, height).
    -------------------------------------------------------------------------------------

    CV2ResizeInterface(from_path, to_path) --> FileHandler
    -------------------------------------------------------------------------------------
    Models an interface that can open, resize and save
    a given image using cv2.

    CONSTRUCTOR ARGUMENTS
    see help(image_utils.file_utils.FileHandler)

    METHODS
    open_file(self, file_type="png", files_path="./")
        Yields a single opened image within a given directory
        if it matches the given image type.

        file_type -- It is the type of image file to be opened,
        for supported types please see cv2 documentation.

    save_file(self, image, image_name)
        Saves the given image at the given to_path, also
        adds the prefix 'rsz_' to avoid overwriting of the
        original image.

        image -- It is the image that is to be saved,
        it must be a cv2.imread object.

        image_name -- It is the string representation of the
        name of the image file.

    resize(self, image, size, **kwargs)
        Resizes the given image to the given size,
        kwargs are to be provided in case of any extra parameters for cv2.resize(),
        for example, test_obj.resize(image, (200, 200), interpolation=cv2.INTER_LINEAR).
        for the full supported kwargs see the cv2 documentation.

        image -- The image to be resized, must
        an object of cv2.imread.

        size -- The size to which the images must
        be resized, it is in the form, (width, height).
    -------------------------------------------------------------------------------------
'''
import os
import cv2
from PIL import Image
from .file_utils import FileHandler

class PILResizeInterface(FileHandler):
    '''
    PILResizeInterface(from_path, to_path) --> FileHandler

    Models an interface that can open, resize and save
    a given image using PIL.

    CONSTRUCTOR ARGUMENTS
    see help(image_utils.file_utils.FileHandler)
    '''
    def __repr__(self):
        return f'image_utils.ImageFileHandler({self.from_path}, {self.to_path})'

    def open_file(self, file_type: str = "png"):
        '''
        open_file(self, file_type="png", files_path="./")

        Yields a single opened image within a given directory
        if it matches the given image type.

        file_type -- It is the type of image file to be opened,
        for supported types please see PIL documentation.
        '''
        directory = os.listdir(self.from_path)
        for image_file in directory:
            reverse_index = -len(file_type)
            if image_file[reverse_index:] == file_type:
                image_path = ''.join((self.from_path, image_file))
                yield Image.open(image_path), image_file

    def save_file(self, image, image_name):
        '''
        save_file(self, image, image_name)

        Saves the given image at the given to_path, also
        adds the prefix 'rsz_' to avoid overwriting of the
        original image.

        image -- It is the image that is to be saved,
        it must be a PIL.Image object.

        image_name -- It is the string representation of the
        name of the image file.
        '''
        full_path = ''.join((self.to_path, 'rsz_', image_name))
        image.save(full_path)

    def resize(self, image, size, **kwargs):
        '''
        resize(self, image, size, **kwargs)

        Resizes the given image to the given size,
        kwargs are to be provided in case of any extra parameters for PIL.Image.resize(),
        for example, test_obj.resize(image, (200, 200), resample=PIL.Image.NEAREST).
        for the full supported kwargs see the PIL documentation.

        image -- The image to be resized, must
        an object of PIL.Image.

        size -- The size to which the images must
        be resized, it is in the form, (width, height).
        '''
        return image.resize(size, **kwargs)

class CV2ResizeInterface(FileHandler):
    '''
    CV2ResizeInterface(from_path, to_path) --> FileHandler

    Models an interface that can open, resize and save
    a given image using cv2.

    CONSTRUCTOR ARGUMENTS
    see help(image_utils.file_utils.FileHandler)
    '''
    def __repr__(self):
        return f'image_utils.CV2ResizeInterface({self.from_path}, {self.to_path})'

    def open_file(self, file_type="png"):
        '''
        open_file(self, file_type="png", files_path="./")

        Yields a single opened image within a given directory
        if it matches the given image type.

        file_type -- It is the type of image file to be opened,
        for supported types please see cv2 documentation.
        '''
        directory = os.listdir(self.from_path)
        for image_file in directory:
            reverse_index = -len(file_type)
            if image_file[reverse_index:] == file_type:
                image_path = ''.join((self.from_path, image_file))
                yield cv2.imread(image_path), image_file

    def save_file(self, image, image_name):
        '''
        save_file(self, image, image_name)

        Saves the given image at the given to_path, also
        adds the prefix 'rsz_' to avoid overwriting of the
        original image.

        image -- It is the image that is to be saved,
        it must be a cv2.imread object.

        image_name -- It is the string representation of the
        name of the image file.
        '''
        full_path = ''.join((self.to_path, 'rsz_', image_name))
        cv2.imwrite(full_path, image)

    def resize(self, image, size, **kwargs):
        '''
        resize(self, image, size, **kwargs)

        Resizes the given image to the given size,
        kwargs are to be provided in case of any extra parameters for cv2.resize(),
        for example, test_obj.resize(image, (200, 200), interpolation=cv2.INTER_LINEAR).
        for the full supported kwargs see the cv2 documentation.

        image -- The image to be resized, must
        an object of cv2.imread.

        size -- The size to which the images must
        be resized, it is in the form, (width, height).
        '''
        return cv2.resize(image, size, **kwargs)
