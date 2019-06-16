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


def addText(FieldData):
	fileName='svg_on_canvas.pdf'
	tempFileSystemPath=fileName
	buffer = BytesIO()
	my_canvas = canvas.Canvas(buffer , pagesize=A4) 
	lastFieldPage=0
	for field in FieldData:
		#print(field)
		fieldText=field.get("text").upper()
		letterCount=0
		currentPage=field.get("text")
		if(currentPage==lastFieldPage+1):
			lastFieldPage=currentPage
			my_canvas.showPage()# change to next page 

		for letter in fieldText:
			textobject = my_canvas.beginText()
			textobject.setFont('Courier', fontSize)
			xPos=field.get("x")+(letterCount*field.get("h-inc")) +pdfCellXOffset
			yPos=field.get("y") + pdfCellYOffset
			textobject.setTextOrigin(xPos, yPos)
			#textobject.setCharSpace(10.1)
			textobject.textLine(letter)
			my_canvas.drawText(textobject)
			letterCount=letterCount+1	

	
	my_canvas.save()
	pdf = buffer.getvalue()
	buffer.close()
	return buffer
	
def mergePDFs(fileBuffer):
	#formPages=["form1.pdf", "svg_on_canvas.pdf"] #Singapore Visa
	#formPages=["Spain Visa.pdf", "svg_on_canvas.pdf"] # spain Visa
	#buffer = BytesIO()
	baseLayerPath=os.path.join(djangoSettings.STATIC_DIR, 'pdfs/SingaporeVisa.pdf')

	temporarylocation="datalayer.pdf"
	with open(temporarylocation,'wb') as out: ## Open temporary file as bytes
		out.write(fileBuffer.getvalue())                ## Read bytes into file


	EmptyForm = PdfFileReader(open(baseLayerPath, "rb"))
	dataLayer=PdfFileReader(datalayer.pdf)
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


	return 	output