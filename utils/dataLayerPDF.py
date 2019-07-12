from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.conf import settings as djangoSettings
from io import BytesIO
from PyPDF2 import PdfFileReader,PdfFileWriter
import sys
from datetime import datetime
import os

from django.core.files import File
from os.path import basename
import requests
from tempfile import NamedTemporaryFile
from urllib.parse import urlsplit



def copy_filelike_to_filelike(src, dst, bufsize=16384):
	while True:
		buf = src.read(bufsize)
		if not buf:
			break
		dst.write(buf)

def formatFieldTextByChoice(field):
	fieldChoice=field.get("field__field_display")
	if(fieldChoice=='NONE'):
		fieldText=field.get("field_text").upper()
	elif(fieldChoice=='FULLDATE'):
		dateTimeObj = field.get("field_date")
		fieldText=dateTimeObj.strftime("%d %m %Y") #Formats to the date 11 10 1984			
	elif(fieldChoice=='DATE'):
		dateTimeObj = field.get("field_date")
		fieldText=dateTimeObj.strftime("%d")	
	elif(fieldChoice=='MONTH'):
		dateTimeObj = field.get("field_date")
		fieldText=dateTimeObj.strftime("%m")	
	elif(fieldChoice=='YEAR'):
		dateTimeObj = field.get("field_date")
		fieldText=dateTimeObj.strftime("%Y")
	elif(fieldChoice=='FULLDATE_TEXT_MONTH'):
		dateTimeObj = field.get("field_date")
		fieldText=dateTimeObj.strftime("%d %B %Y")		# formats the date as 16 June 1984 
	else:
		fieldText=''

	return fieldText	

def addText(FieldData, FormData):
	
	cellSizeX=(float(FormData.cellSize_X)/2)
	cellSizeY=(float(FormData.cellSize_Y)/2)

	fileName='svg_on_canvas.pdf'
	tempFileSystemPath=fileName
	buffer = BytesIO()
	my_canvas = canvas.Canvas(buffer , pagesize=A4) 
	lastFieldPage=0
	for field in FieldData:
		#print(field)
		
		letterCount=0
		currentPage=field.get("field_page_number")
		if(currentPage==lastFieldPage+1):
			lastFieldPage=currentPage
			my_canvas.showPage()# change to next page
		
		


		fieldText=formatFieldTextByChoice(field)
		for letter in fieldText:
			textobject = my_canvas.beginText()


			fontSize=field.get("font_size")
			textobject.setFont('Courier', fontSize)

			pdfCellXOffset=cellSizeX -(fontSize/4)
			pdfCellYOffset=cellSizeY -(fontSize/4)

			xPos=float(field.get("field_x"))+(letterCount*float(field.get("field_x_increment"))) +pdfCellXOffset
			yPos=float(field.get("field_y")) + pdfCellYOffset
			textobject.setTextOrigin(xPos, yPos)
			#textobject.setCharSpace(10.1)
			textobject.textLine(letter)
			my_canvas.drawText(textobject)
			letterCount=letterCount+1	

	
	my_canvas.save()
	pdf = buffer.getvalue()	
	
	return pdf	
	baseLayerTempFile=downloadFile(FormData.file_path.url)
	
	EmptyForm = PdfFileReader(baseLayerTempFile)
	dataLayer=PdfFileReader(buffer)
	emptyFormPageCount=EmptyForm.getNumPages()
	dataLayerPagecount=dataLayer.getNumPages()
	#print(emptyFormPageCount)
	#print(dataLayerPagecount)
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
	#baseLayerTempFile.close()
	return output			
	# with open("join.pdf", "wb") as outputStream:
	# 	output.write(outputStream)
	# return "join.pdf"

# def downloadFile(webFilePath):
# 	with NamedTemporaryFile(delete=False) as tf:
# 		r = requests.get(webFilePath, stream=True)
# 		for chunk in r.iter_content(chunk_size=4096):
# 			tf.write(chunk)
# 	return tf

def downloadFile(webFilePath):
	# with NamedTemporaryFile(delete=False) as tf:
	new_buffer = BytesIO()
	r = requests.get(webFilePath)	
	new_buffer.write(r.content)
	return new_buffer
	
