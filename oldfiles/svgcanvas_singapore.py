# svg_on_canvas.py
 
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
fontSize=15
pdfCellXOffset=(16.9/2)-(fontSize/4)
pdfCellYOffset=(19.86/2)-(fontSize/4)
 
def addText(FieldData):
	my_canvas = canvas.Canvas('svg_on_canvas.pdf', pagesize=A4) 
	lastFieldPage=0
	for field in FieldData:
		#print(field)
		fieldText=field["text"].upper()
		letterCount=0
		currentPage=field["page"]
		if(currentPage==lastFieldPage+1):
			lastFieldPage=currentPage
			my_canvas.showPage()# change to next page 

		for letter in fieldText:
			textobject = my_canvas.beginText()
			textobject.setFont('Courier', fontSize)
			xPos=field["x"]+(letterCount*field["h-inc"])
			textobject.setTextOrigin(xPos, field["y"])
			#textobject.setCharSpace(10.1)
			textobject.textLine(letter)
			my_canvas.drawText(textobject)
			letterCount=letterCount+1	

	#
	
		

	my_canvas.save()
 
if __name__ == '__main__':
	newField={}
	fieldData=[] 
	newField["x"]=137+pdfCellXOffset
	newField["y"]=676+pdfCellYOffset
	newField["text"]="Rupin Raghavji Chheda"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=494+pdfCellYOffset
	newField["text"]="India"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=107+pdfCellXOffset
	newField["y"]=566+pdfCellYOffset
	newField["text"]="11 10 1984"
	newField["h-inc"]=16.5
	newField["page"]=0
	newField["type"]="block-text-date"
	fieldData.append(newField)
	

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=466+pdfCellYOffset
	newField["text"]="Maharastra"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=436+pdfCellYOffset
	newField["text"]="indian"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=408+pdfCellYOffset
	newField["text"]="indian"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=205+pdfCellXOffset
	newField["y"]=367+pdfCellYOffset
	newField["text"]="passport"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=205+pdfCellXOffset
	newField["y"]=310+pdfCellYOffset
	newField["text"]="f6612779"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=128+pdfCellXOffset
	newField["y"]=282+pdfCellYOffset
	newField["text"]="05 06 2006"
	newField["h-inc"]=16.5
	newField["page"]=0
	newField["type"]="block-text-date"
	fieldData.append(newField)


	newField={}
	newField["x"]=392+pdfCellXOffset
	newField["y"]=282+pdfCellYOffset
	newField["text"]="11 10 1984"
	newField["h-inc"]=16.5
	newField["page"]=0
	newField["type"]="block-text-date"
	fieldData.append(newField)

	newField={}
	newField["x"]=129+pdfCellXOffset
	newField["y"]=231+pdfCellYOffset
	newField["text"]="india"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=129+pdfCellXOffset
	newField["y"]=206+pdfCellYOffset
	newField["text"]="mumbai"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=188+pdfCellXOffset
	newField["y"]=159+pdfCellYOffset
	newField["text"]="india"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=188+pdfCellXOffset
	newField["y"]=133+pdfCellYOffset
	newField["text"]="maharastra"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=188+pdfCellXOffset
	newField["y"]=104+pdfCellYOffset
	newField["text"]="kandivali"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=188+pdfCellXOffset
	newField["y"]=77+pdfCellYOffset
	newField["text"]="mumbai"
	newField["h-inc"]=17
	newField["page"]=0
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=80+pdfCellXOffset
	newField["y"]=57+pdfCellYOffset
	newField["text"]="202 radhika darshan hemukalani cross road 2"
	newField["h-inc"]=9
	newField["page"]=0
	newField["type"]="free-text"
	fieldData.append(newField)


	newField={}
	newField["x"]=99.9+pdfCellXOffset
	newField["y"]=751+pdfCellYOffset
	newField["text"]="Engineer"
	newField["h-inc"]=17
	newField["page"]=1
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=270+pdfCellXOffset
	newField["y"]=726+pdfCellYOffset
	newField["text"]="Bachelor in engineering"
	newField["h-inc"]=9
	newField["page"]=1
	newField["type"]="free-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=703+pdfCellYOffset
	newField["text"]="Jain"
	newField["h-inc"]=9
	newField["page"]=1
	newField["type"]="free-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=30.765+pdfCellXOffset
	newField["y"]=413.65+pdfCellYOffset
	newField["text"]="16"
	newField["h-inc"]=17
	newField["page"]=1
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=166+pdfCellXOffset
	newField["y"]=413.65+pdfCellYOffset
	newField["text"]="14"
	newField["h-inc"]=17
	newField["page"]=1
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=94+pdfCellXOffset
	newField["y"]=387+pdfCellYOffset
	newField["text"]="16 ah hood road"
	newField["h-inc"]=17
	newField["page"]=1
	newField["type"]="block-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=104+pdfCellXOffset
	newField["y"]=681+pdfCellYOffset
	newField["text"]="Leisure and Travel"
	newField["h-inc"]=9
	newField["page"]=1
	newField["type"]="free-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=323+pdfCellXOffset
	newField["y"]=658+pdfCellYOffset
	newField["text"]="1st November 2018"
	newField["h-inc"]=9
	newField["page"]=1
	newField["type"]="free-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=102+pdfCellXOffset
	newField["y"]=366+pdfCellYOffset
	newField["text"]="Ramada Singapore"
	newField["h-inc"]=9
	newField["page"]=1
	newField["type"]="free-text"
	fieldData.append(newField)

	newField={}
	newField["x"]=279+pdfCellXOffset
	newField["y"]=529+pdfCellYOffset
	newField["text"]="indian"
	newField["h-inc"]=9
	newField["page"]=1
	newField["type"]="free-text"
	fieldData.append(newField)

	
	#print(fieldData) 
	addText(fieldData)

