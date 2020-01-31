import isbnlib
import pdftitle
import socket
import PyPDF2
import re

def is_connected():
    try:
        host = socket.gethostbyname("1.1.1.1")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except OSError:
        pass
    return False

def get_isbn(pdf_path, max_pages=5):
    with open(pdf_path, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        pages = [reader.getPage(i).extractText().replace('\n', '') for i in range(max_pages)]

        isbn_13 = r"(?:I\w*S\w*B\w*N\w*(?:[-\s]13)?:?\ )?(?=[0-9]{13}|(?=(?:[0-9]+[-\ ]){4})[-\ 0-9]{17})(97[89][-\ ]?[0-9]{1,5}[-\ ]?[0-9]+[-\ ]?[0-9]+[-\ ]?[0-9])"

        isbn_10 = r"(?:I\w*S\w*B\w*N\w*(?:[-\s:]10)?:?\s)?(?=[0-9X]{10}|(?=(?:[0-9]+[-\ ]){3})[-\ 0-9X]{13})([0-9]{1,5}[-\ ]?[0-9]+[-\ ]?[0-9]+[-\ ]?[0-9X])"


        matches_13 = re.finditer(isbn_13, '\n'.join(pages[:]), re.MULTILINE)
        matches_10 = re.finditer(isbn_10, '\n'.join(pages[:]), re.MULTILINE)

        m13 = [match.group() for match in matches_13]
        m10 = [match.group() for match in matches_10]

        m13 = list(set(m13) - set(m10))
        m10 = list(set(m10) - set(m13))

        res = [re.sub(r'ISBN \d{2}:?', '', s).strip()
               for s in m13 + m10]

        return res

def get_title(isbn_numbers):

    for isbn in isbn_numbers:
        cleaned_isbn = isbnlib.clean(isbn)
        if (isbnlib.is_isbn13(cleaned_isbn) or isbnlib.is_isbn10(cleaned_isbn)):
            book = isbnlib.meta(cleaned_isbn)
            return book['Title']
            break

    # return "no meta data was found."

if is_connected():
    isbn = get_isbn('/home/fuzie/Documents/Books/Neil A. Campbell et al. - Biology_ A Global Approach (Global Edition)-Pearson (2017).pdf')
    title = get_title(isbn)
    print(title)
