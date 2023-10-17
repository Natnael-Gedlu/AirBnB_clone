#!/usr/bin/python3

"""
__init__ magic filestorage method for models directory
"""


from models.engine.file_storage import Filestorage

storage = Filestorage()
storage.reload()
