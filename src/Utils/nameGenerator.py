import isbnlib
import pdftitle
import socket
import PyPDF2
import re
# def get_information(isbn):
    

def is_connected():
    try:
        host = socket.gethostbyname("1.1.1.1")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except OSError:
        pass
    return False

def get_isbn(pdf_path):
    with open(pdf_path, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        page = reader.getPage(4)

        print(page.extractText())


get_isbn('/home/daniel/Projects/PaperGirl/demo.pdf')


     



