import configparser
import glob, os
from PyPDF2 import PdfFileReader
from Models.Paper import Paper
from pathlib import Path

papers = dict()
home = str(Path.home())

config = configparser.ConfigParser()
config.read(home + '/.config/papergirl/paper.ini')

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        file_name = os.path.basename(path)
        number_of_pages = pdf.getNumPages()

    papers[file_name]=(Paper(info.author, info.creator, info.producer, info.subject, info.title, file_name, path))


os.chdir( home + "/" + config['PAPER']['inbox'])
for file in glob.glob("*.pdf"):
    get_info(file)
