from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from django.conf import settings as djangoSettings
fontSize=15
pdfCellXOffset=(16.9/2)-(fontSize/4)
pdfCellYOffset=(19.86/2)-(fontSize/4)


def addText(FieldData):
	tempFileName=djangoSettings.STATIC_ROOT+'/pdfs/svg_on_canvas.pdf'
	my_canvas = canvas.Canvas('svg_on_canvas.pdf', pagesize=A4) 
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

	return tempFileName
	
		