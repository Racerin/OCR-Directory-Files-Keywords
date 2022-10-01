import tempfile
import os
import unittest

import lib

class TestLibrary(unittest.TestCase):

    def test_strip_file_format(self):
        # Test valid names
        inputs = (
            "example.txt",
            "pdf.pdf"
        )
        ans = (
            "txt",
            "pdf"
        )
        for ipt, an in zip(inputs, ans):
            assert lib.strip_file_format(ipt) == an, "{} > {}".format(ipt,an)

    def test_hash_file1(self):
        """ Create temp file and test hash function. """
        return None
        try:
            # Generate a non-existent file name
            filename = None
            while filename is None:
                temp_filename = lib.random_string(20)
                if not os.path.exists(temp_filename):
                    filename = temp_filename
            
            # Hash file content
            with open(filename, mode="xb") as f:
                ans = lib.hash_file(f.name)
                # print(ans)
                assert isinstance(ans, str), "This file suppose to return a str variable. {}".format(type(ans))
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_hash_file(self):
        """ 
        Create temp file and test hash function.
        For some reason I'm unable to access temp files so I create my own.
         """
        with lib.my_temp_file(20) as f:
            ans = lib.hash_file(f.name)
            print(ans)
            assert isinstance(ans, str), "This file suppose to return a str variable. {}".format(type(ans))

    def test_read_pdf_file(self):
        """ 
        Read pdf file.
        Test done using test.pdf file.
        """
        # Open perfectly normal file
        ans = lib.read_pdf_file(lib.PARAMS.TEST_PDF_FILE)
        assert isinstance(ans, str)
        # print(ans)
