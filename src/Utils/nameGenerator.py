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
        pages = [reader.getPage(i).extractText().replace('\n', '') for i in range(10)]
        
        isb_13 ="(?:I.*S.*B.*N.*(?:-13)?:?\ )?(?=[0-9]{13}|(?=(?:[0-9]+[-\ ]){4})[-\ 0-9]{17})(97[89][-\ ]?[0-9]{1,5}[-\ ]?[0-9]+[-\ ]?[0-9]+[-\ ]?[0-9])"
        match = re.search(isb_13, pages[3], flags=re.MULTILINE)
        
        book = isbnlib.meta(match.group(1))
        return book['Title']


if(is_connected):
    get_isbn('/home/daniel/Projects/PaperGirl/demo.pdf')


     



