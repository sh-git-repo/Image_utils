# Simple yet handy utilities for images.

-- read __requirements.txt__ for dependencies --

#### 1. image_utils package
Package contains Resizer, Cropper* and Filter*

###### Resizer
A Resizer class that can be used to resize all pictures of same the type from
a given directory and can be saved in the same or a different directory.

see help(Resizer) for more info

'''
    >>> from image_utils import Resizer
    
    >>> test_obj = Resizer(from_path, to_path)
    
    >>> test_obj.resize("png")
    
    >>> Successfully resized 3 png image/images.
'''

Update* - To be released soon in later commits.
