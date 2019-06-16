from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from django.conf import settings as djangoSettings
from io import BytesIO
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
	return pdf
	
# def mergePDFs(fileName)
# 	#formPages=["form1.pdf", "svg_on_canvas.pdf"] #Singapore Visa
# 	#formPages=["Spain Visa.pdf", "svg_on_canvas.pdf"] # spain Visa
# 	baseLayerPath=djangoSettings.STATIC_URL + "/pdfs/SingaporeVisa.pdf"

# 	EmptyForm = PdfFileReader(open(baseLayerPath, "rb"))
# 	dataLayer=PdfFileReader(open(fileName, "rb"))
# 	emptyFormPageCount=EmptyForm.getNumPages()
# 	dataLayerPagecount=dataLayer.getNumPages()
# 	output = PdfFileWriter()
# 	if(emptyFormPageCount>=dataLayerPagecount):
# 		for pageIndex in range(0,dataLayerPagecount):
# 			dataPage=dataLayer.getPage(pageIndex)
# 			formPage=EmptyForm.getPage(pageIndex)
# 			formPage.mergePage(dataPage)
# 			output.addPage(formPage)

# 		for emptyPagesIndex in range(dataLayerPagecount, emptyFormPageCount):
# 				formPage=EmptyForm.getPage(emptyPagesIndex)
# 				output.addPage(formPage)


# 	with open("join.pdf", "wb") as outputStream:
# 	output.write(outputStream)		