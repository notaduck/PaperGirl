import configparser
import glob, os
from PyPDF2 import PdfFileReader
from Models.Paper import Paper
from pathlib import Path

config = configparser.ConfigParser()
config.read(str(Path.home()) + '/.config/papergirl/config.ini')

papers = dict()
files = []
PATH = str(Path.home()) + "/"  + config['PAPERGIRL']['inbox']

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        file_name = os.path.basename(path)
        number_of_pages = pdf.getNumPages()

    return Paper(info.author, info.creator, info.producer, info.subject, info.title, file_name, path)

def get_files( ):
    os.chdir(PATH)
    files = glob.glob("*.pdf")
    return files

