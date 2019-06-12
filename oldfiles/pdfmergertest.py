from PyPDF2 import PdfFileReader,PdfFileWriter
import sys
pdfs=["svg_on_canvas.pdf"]
#print (f, k)
base = PdfFileReader(open("form1.pdf", "rb"))
basePage=base.getPage(0)
output = PdfFileWriter()
for pdf in pdfs:    
    file = PdfFileReader(open(pdf, "rb"))    
    basePage.mergePage(file.getPage(0))
output.addPage(basePage)
with open("join.pdf", "wb") as outputStream:
    output.write(outputStream)
