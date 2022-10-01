import logging
import hashlib
import time
import random
import os
from contextlib import contextmanager

from PyPDF2 import PdfReader

import PARAMS


def random_string(num):
    """ 
    Generate a random string of certain length.
    ref: https://www.educative.io/answers/how-to-generate-a-random-string-in-python
     """
    return ''.join(random.choice(PARAMS.RANDOM_STRING_OPTIONS) for _ in range(num))


@contextmanager
def my_temp_file(num):
    """ 
    Create a temporary file in the current working directory.
    Use as a context manager.
     """
    # Generate random file name and ensure it doesn't exist.
    filename = None
    while filename is None:
        temp_filename = random_string(num)
        if not os.path.exists(temp_filename):
            filename = temp_filename
    try:
        with open(filename, mode='xb') as f:
            yield f
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def hash_file(file_path:str, buffer_size=PARAMS.DEF_BUFFER_SIZE) -> str:
    """ 
    Convert a file via binary mode to a hash. 
    buffer_size breaks-up file size to help not use-up too much RAM.
    NB: Cannot compare hashes with different buffer_size 
    if there is a roll over (very likely).
    Ref: https://stackoverflow.com/a/22058673
    """
    hasher = hashlib.md5()
    # hasher = hashlib.sha1()

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def strip_file_format(filename:str) -> str:
    """ Return format extension of file name/path. """
    assert isinstance(filename, str), "The variable '{}' is not a string.".format(filename)
    parts = filename.split('.')
    if len(parts) > 1:
        format = parts[-1].strip()
        return format
    else:
        logging.debug("'{}' file extension not recognised.")
        return None


def read_pdf_file(file_path:str, page_separator:str="\n", metadata=True, password="") -> str:
    """ 
    Convert PDF file's content to text.
    Decrypt file with password if encrypted.
    Access meta data (author,creator,etc).
    """
    # Access pdf file
    reader = PdfReader(file_path)
    # Decrypt with password if encrypted
    if reader.is_encrypted:
        reader.decrypt(password)
    elif password:
        logging.info("The file '{}' was not encrypted.".format(file_path))
    str1 = ""
    # Extract meta data
    if metadata:
        str1 += str(reader.metadata)
    # Extract text in pages of file
    pages_gen = (pg.extract_text() for pg in reader.pages)
    str1 = page_separator.join(pages_gen)
    return str1
    

def read_file(file_path:str) -> str:
    """ Read a file and return it's text content.
    Only specific file formats are supported.
     """
    file_format_ext = strip_file_format(file_path)
    if file_format_ext == 'pdf':
        return read_pdf_file(file_path)