from Models.Paper import Paper
from PyPDF2 import PdfFileReader
from pathlib import Path
import configparser
import glob
import os
import pdftitle

config = configparser.ConfigParser()
config.read(str(Path.home()) + '/.config/papergirl/config.ini')

papers = {}
files = []
PATH = str(Path.home()) + "/"  + config['PAPERGIRL']['inbox']

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        file_name = os.path.basename(path)
        # number_of_pages = pdf.getNumPages()
    title = pdftitle.get_title_from_file(path)

    return Paper(title, info.author, info.creator, info.producer, info.subject,
                 file_name, path)

def get_files():
    os.chdir(PATH)
    return glob.glob("*.pdf")
