from PyPDF2 import PdfFileReader,PdfFileWriter
import sys
pdfs=["drawing1.pdf", "drawing2.pdf", "drawing3.pdf"]
#print (f, k)
base = PdfFileReader(open("base.pdf", "rb"))
basePage=base.getPage(0)
output = PdfFileWriter()
for pdf in pdfs:    
    file = PdfFileReader(open(pdf, "rb"))    
    basePage.mergePage(file.getPage(0))
    
    


output.addPage(basePage)
with open("join.pdf", "wb") as outputStream:
    output.write(outputStream)
