from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.conf import settings as djangoSettings
from io import BytesIO
from PyPDF2 import PdfFileReader,PdfFileWriter
import sys

import os

fontSize=15
pdfCellXOffset=(16.9/2)-(fontSize/4)
pdfCellYOffset=(19.86/2)-(fontSize/4)

def copy_filelike_to_filelike(src, dst, bufsize=16384):
	while True:
		buf = src.read(bufsize)
		if not buf:
			break
		dst.write(buf)


def addText(FieldData):
	fileName='svg_on_canvas.pdf'
	tempFileSystemPath=fileName
	buffer = BytesIO()
	my_canvas = canvas.Canvas(buffer , pagesize=A4) 
	lastFieldPage=0
	for field in FieldData:
		#print(field)
		fieldText=field.get("field_text").upper()
		letterCount=0
		currentPage=field.get("field_page_number")
		if(currentPage==lastFieldPage+1):
			lastFieldPage=currentPage
			my_canvas.showPage()# change to next page 

		for letter in fieldText:
			textobject = my_canvas.beginText()
			textobject.setFont('Courier', fontSize)
			xPos=float(field.get("field_x"))+(letterCount*float(field.get("field_x_increment"))) +pdfCellXOffset
			yPos=float(field.get("field_y")) + pdfCellYOffset
			textobject.setTextOrigin(xPos, yPos)
			#textobject.setCharSpace(10.1)
			textobject.textLine(letter)
			my_canvas.drawText(textobject)
			letterCount=letterCount+1	

	
	my_canvas.save()
	pdf = buffer.getvalue()
	
	# temporarylocation="datalayer.pdf"
	# with open(temporarylocation, "wb") as outfile:
	# 	copy_filelike_to_filelike(buffer, outfile)
	# buffer.close()
	# return pdf
	#buffer.close()



	baseLayerPath=os.path.join(djangoSettings.STATIC_DIR, 'pdfs/SingaporeVisa.pdf')	
	

	
	EmptyForm = PdfFileReader(open(baseLayerPath, "rb"))
	dataLayer=PdfFileReader(buffer)
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

	return output			
	# with open("join.pdf", "wb") as outputStream:
	# 	output.write(outputStream)
	# return "join.pdf"

