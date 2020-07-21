'''
NAME:
    image_utils.py

DESCRIPTION:
    Some useful and simple utilities for dealing with
    lots of images.

CLASSES:
    Resizer(from_path, to_path)
    --------------------------------------------------------
    Models a resizer for all images of a specified type.

    CONSTRUCTOR ARGUMENTS
    from_path -- The path where the images are located, must
    keep the trailing slashes, for example, "some_path//".

    to_path -- The path where the images must be saved, must
    keep the trailing slashes, for example, "other_path//"
    --------------------------------------------------------
'''
from .utilities import create_folder
from .resize_interfaces import PILResizeInterface

class Resizer():
    '''
    Resizer(from_path, to_path)
    Models a resizer for all images of a specified type.

    CONSTRUCTOR ARGUMENTS
    from_path -- The path where the images are located, must
    keep the trailing slashes, for example, "some_path//".

    to_path -- The path where the images must be saved, must
    keep the trailing slashes, for example, "other_path//"
    '''
    def __init__(self, from_path, to_path):
        self.from_path = from_path
        self.to_path = to_path

    def resize_all(
            self,
            image_type: str = 'png',
            size: tuple = (256, 256),
            image_interface=PILResizeInterface,
            **kwargs
        ):
        ''' Resizes all images of the given image file type. '''
        create_folder(self.to_path)
        image_tool = image_interface(self.from_path, self.to_path)
        image_count = 0
        for image, image_name in image_tool.open_file(image_type):
            image_count += 1
            rsz_image = image_tool.resize(image, size, **kwargs)
            image_tool.save_file(rsz_image, image_name)
        print(
            " Successfully resized %s %s image/images." \
            %(image_count, image_type)
        )
