import string


PDF_FILE_FORMAT = "pdf"
TEXT_FILE_FORMAT = "txt"
RICH_TEXT_FORMAT = "rtf"

MICROSOFT_WORD_FILE_FORMATS = {'doc', 'docs', }
MICROSOFT_EXCEL_FILE_FORMATS = {"xls", "xlsx", }
MICROSOFT_FILE_FORMATS = {
    *MICROSOFT_WORD_FILE_FORMATS, 
    *MICROSOFT_EXCEL_FILE_FORMATS
    }

JPEG_FILE_FORMATS = {"jpeg", "jpg", "jpe",}
TIFF_FILE_FORMATS = {"tiff", "tif",}
BMP_FILE_FORMATS = {"bmp", "dib",}
IMAGE_FILE_FORMATS = {
    *JPEG_FILE_FORMATS,
    *TIFF_FILE_FORMATS,
    *BMP_FILE_FORMATS,
    "png", "pcx",
    # "rle",
    }

TEXT_FILE_FORMATS = {TEXT_FILE_FORMAT, }

# OpenOffice StarOffice
# https://helpx.adobe.com/acrobat/kb/supported-file-formats-acrobat-reader.html

SCANNABLE_FILE_FORMATS = {
    PDF_FILE_FORMAT, 
    *TEXT_FILE_FORMATS, 
    *IMAGE_FILE_FORMATS, 
    *MICROSOFT_FILE_FORMATS, 
    }


DEF_BUFFER_SIZE = 65536     # 64kB chunks


RANDOM_STRING_OPTIONS = string.ascii_letters


TEST_PDF_FILE = "tests/test.pdf"