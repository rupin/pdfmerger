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
	#print(field)
	if(fieldChoice=='NONE'):
		fieldText=field.get("field_text").upper()
	elif(fieldChoice=='FULLDATE'):
		fieldText = field.get("field_text")
		dateObject=datetime.strptime(fieldText,"%B %d, %Y") # accept date as string in a certain format
		fieldText=dateObject.strftime("%d %m %Y")	# convert it to what is required 11 10 1984													#Formats to the date 11 10 1984			
	elif(fieldChoice=='DATE'):
		fieldText = field.get("field_text")
		dateObject=datetime.strptime(fieldText,"%B %d, %Y")	
		fieldText=dateObject.strftime("%Y")
	elif(fieldChoice=='MONTH'):
		fieldText = field.get("field_text")
		dateObject=datetime.strptime(fieldText,"%B %d, %Y")	
		fieldText=dateObject.strftime("%Y")
	elif(fieldChoice=='YEAR'):
		fieldText = field.get("field_text")
		dateObject=datetime.strptime(fieldText,"%B %d, %Y")
		fieldText=dateObject.strftime("%Y")
	elif(fieldChoice=='FULLDATE_TEXT_MONTH'):
		fieldText = field.get("field_text") # date is formatted as June 16, 2019
	elif(fieldChoice=='MULTICHOICE'):
		fieldText = "✔"
		
	else:
		fieldText=''

	#print("fieldText:"+fieldText)	

	return fieldText	

def addText(FieldData, FormData):
	
	cellSizeX=(float(FormData.cellSize_X)/2)
	cellSizeY=(float(FormData.cellSize_Y)/2)

	fileName='svg_on_canvas.pdf'
	tempFileSystemPath=fileName
	my_buffer = BytesIO()
	my_canvas = canvas.Canvas(my_buffer , pagesize=A4) 
	lastFieldPage=0
	#print(FieldData)
	for field in FieldData:
		#print(field)		
		letterCount=0
		currentPage=field.get("field_page_number")
		if(currentPage==lastFieldPage+1):
			lastFieldPage=currentPage
			my_canvas.showPage()# change to next page
		
		

		#print(field)
		fieldText=formatFieldTextByChoice(field)
		fieldChoice=field.get("field__field_display")		
		field_x_increment=float(field.get("field_x_increment"))
		fontSize=field.get("font_size")
		pdfCellXOffset=cellSizeX -(fontSize/4)
		pdfCellYOffset=cellSizeY -(fontSize/4)
		field_x=0
		field_y=0
		if(fieldChoice == "MULTICHOICE"):
			field_x,field_y=getMultiChoicePosition(field)
		else:
			field_x=float(field.get("field_x"))
			field_y=float(field.get("field_y"))
		
		for letter in fieldText:			
			textobject = my_canvas.beginText()			
			textobject.setFont('Courier', fontSize)			
			xPos=field_x +(letterCount*field_x_increment) + pdfCellXOffset
			yPos=field_y + pdfCellYOffset

			textobject.setTextOrigin(xPos, yPos)
			#textobject.setCharSpace(10.1)
			#my_canvas.drawString(xPos, yPos,letter)
			textobject.textLine(letter)
			my_canvas.drawText(textobject)
			letterCount=letterCount+1	

	
	my_canvas.save() # Save The Canvas element

	#pdf = my_buffer.getvalue()	
	
	#return pdf	
	baseLayerTempFile=downloadFile(FormData.file_path.url)
	
	EmptyForm = PdfFileReader(baseLayerTempFile)
	dataLayer=PdfFileReader(my_buffer)
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
	
	#output.addMetadata("Title", "Hello")
	return output			
	

def downloadFile(webFilePath):
	# with NamedTemporaryFile(delete=False) as tf:
	new_buffer = BytesIO()
	r = requests.get(webFilePath)	
	new_buffer.write(r.content)
	return new_buffer
	
def getMultiChoicePosition(field):
	xValues=field.get("field_x_choices")
	yValues=field.get("field_y_choices")
	data_index=field.get("data_index")

	xList=xValues.split(",")
	yList=yValues.split(",")
	field_x_pos=0
	field_y_pos=0
	if(len(xList)-1 >= data_index and len(yList)-1 >= data_index):
		field_x_pos=float(xList[data_index])
		field_y_pos=float(yList[data_index])
		#return int(), int(yList[data_index])

	return field_x_pos,field_y_pos


	#return 20,30