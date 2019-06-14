from PyPDF2 import PdfFileReader,PdfFileWriter
import sys


EmptyForm = PdfFileReader(open("form1.pdf", "rb"))
dataLayer=PdfFileReader(open("svg_on_canvas.pdf", "rb"))
emptyFormPageCount=EmptyForm.getNumPages()
dataLayerPagecount=dataLayer.getNumPages()
output = PdfFileWriter()
if(emptyFormPageCount>dataLayerPagecount):
	for pageIndex in range(0,dataLayerPagecount):
		dataPage=dataLayer.getPage(pageIndex)
		formPage=EmptyForm.getPage(pageIndex)
		formPage.mergePage(dataPage)
		output.addPage(formPage)

for emptyPagesIndex in range(dataLayerPagecount, emptyFormPageCount):

 	formPage=EmptyForm.getPage(emptyPagesIndex)
 	output.addPage(formPage)
    

with open("join.pdf", "wb") as outputStream:
    output.write(outputStream)
