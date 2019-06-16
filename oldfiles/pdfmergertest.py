from PyPDF2 import PdfFileReader,PdfFileWriter
import sys

formPages=["form1.pdf", "svg_on_canvas.pdf"] #Singapore Visa
#formPages=["Spain Visa.pdf", "svg_on_canvas.pdf"] # spain Visa

EmptyForm = PdfFileReader(open(formPages[0], "rb"))
dataLayer=PdfFileReader(open(formPages[1], "rb"))
emptyFormPageCount=EmptyForm.getNumPages()
dataLayerPagecount=dataLayer.getNumPages()
output = PdfFileWriter()
if(emptyFormPageCount>=dataLayerPagecount):
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
