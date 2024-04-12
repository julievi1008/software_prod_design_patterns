from abc import ABC, abstractmethod

# Assignment 1) Create class Document(ABC)
#   It should have two methods which are both @abstractmethod: read and write
#       Read only takes self as parameter and the second parameter for write should be the content to be written
#       These are abstract methods so they should only return pass
# WRITE YOUR ANSWER BELOW
class Document(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, content):
        pass

# Assignment 2) Create class PDFDocument(Document)
#   It should override both read and write methods. No need to implement the actual functionality, they should
#   just print something like "Reading a PDF document" and "Writing to PDF document.". They do not need to return anything.
# WRITE YOUR ANSWER BELOW
    
class PDFDocument(Document):
    def read(self):
        print("Reading a PDF document")
    
    def write(self, content):
        print(f'Writing to PDF document content: {content}')


# Assignment 3) Create class WordDocument(Document)
#   It should override both read and write methods. No need to implement the actual functionality, they should
#   just print something like "Reading a Word document" and "Writing to Word document." They do not need to return anything.
# WRITE YOUR ANSWER BELOW
    
class WordDocument(Document):
    def read(self):
        print("Reading a Word document")
    
    def write(self, content):
        print(f'Writing to Word document content: {content}')


# Assignment 4) Create enum DocumentType
# It should have two key & value pairs:
# PDF = "pdf"
# WORD = "word"
from enum import Enum

class DocumentType(Enum):
    PDF = 'pdf'
    WORD = 'word'

# Assignment 5) Create class DocumentFactory
#   This class is the factory that can produce documents.
#   It should have one static method (@staticmethod) called get_document that takes in the type of the document as DocumentType enum.
#     get_document should return back new PDFDocument() or WordDocument() based on the type passed (DocumentType.PDF or DocumentType.WORD)
#     or raise Exception if type is not either one of the accepted types.
# WRITE YOUR ANSWER BELOW

class DocumentFactory:
    @staticmethod
    def get_document(document_type: DocumentType):
        if document_type == document_type.PDF:
            return PDFDocument()
        elif document_type == document_type.WORD:
            return WordDocument()
        else:
            raise ValueError(f"Document type {document_type} is not supported")



# Assignment 6)
# Create a PDF and Word document using the DocumentFactory and call their read() and write() methods,
# which should both just print something out.
# WRITE YOUR ANSWER BELOW

pdf = DocumentFactory.get_document(DocumentType.PDF)
word = DocumentFactory.get_document(DocumentType.WORD)


pdf.read()
pdf.write('Hello world!')
word.read()
word.write('Hello world!')
