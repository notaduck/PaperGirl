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
        
        # isb_13 = re.compile(r'''
# (?:I.*S.*B.*N.*(?:-13)?:?\ )?(?=[0-9]{13}|(?=(?:[0-9]+[-\ ]){4})[-\ 0-9]{17})97[89][-\ ]?[0-9]{1,5}[-\ ]?[0-9]+[-\ ]?[0-9]+[-\ ]?[0-9]
        #         ''', re.MULTILINE)
         
        isb_13 ="(?:I.*S.*B.*N.*(?:-13)?:?\ )?(?=[0-9]{13}|(?=(?:[0-9]+[-\ ]){4})[-\ 0-9]{17})(97[89][-\ ]?[0-9]{1,5}[-\ ]?[0-9]+[-\ ]?[0-9]+[-\ ]?[0-9])"
        # isb_10 = re.compile(r'''(
        #         (?:ISBN(?:-10)?:?\ )?     # Optional ISBN/ISBN-10 identifier.
        #         (?=                       # Basic format pre-checks (lookahead):
        #           [0-9X]{10}$             #   Require 10 digits/Xs (no separators).
        #          |                        #  Or:
        #           (?=(?:[0-9]+[-\ ]){3})  #   Require 3 separators
        #           [-\ 0-9X]{13}$          #     out of 13 characters total.
        #         )                         # End format pre-checks.
        #         [0-9]{1,5}[-\ ]?          # 1-5 digit group identifier.
        #         [0-9]+[-\ ]?[0-9]+[-\ ]?  # Publisher and title identifiers.
        #         [0-9X]                    # Check digit.
        #         $
        #         ''', re.VERBOSE)

        # matches = [isb_13.match(page) for page in pages]
        # match = isb_13.findall(pages[3], re.DOTALL)
        match = re.search(isb_13, pages[3], flags=re.MULTILINE)
        # print(match.gr, "\n")
        print(match.group(1),  "\n")
        # [print(page) for page in pages]
        # print(pages[3])





get_isbn('/home/daniel/Projects/PaperGirl/demo.pdf')


     



