#!/usr/bin/python3
"""this impoort ABD Initializes the package"""

from models.engine.file_storage import FileStorage
storage = FileStorage()

#calling and using the reload function
storage.reload()
