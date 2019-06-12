# svg_on_canvas.py
 
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
fontSize=12
pdfCellXOffset=(16.9/2)-(fontSize/4)
pdfCellYOffset=(19.86/2)-(fontSize/4)
 
def addText(FieldData):
    my_canvas = canvas.Canvas('svg_on_canvas.pdf', pagesize=A4) 
    for field in FieldData:
    	#print(field)
    	fieldText=field["text"].upper()
    	letterCount=0
    	for letter in fieldText:
    		textobject = my_canvas.beginText()
    		textobject.setFont('Courier', fontSize)
    		xPos=field["x"]+(letterCount*field["h-inc"])
    		textobject.setTextOrigin(xPos, field["y"])
    		#textobject.setCharSpace(10.1)
    		textobject.textLine(letter)
    		my_canvas.drawText(textobject)
    		letterCount=letterCount+1
    

    my_canvas.save()
 
if __name__ == '__main__':
	newField={}
	fieldData=[] 
	newField["x"]=137+pdfCellXOffset
	newField["y"]=676+pdfCellYOffset
	newField["text"]="Rupin Raghavji Chheda"
	newField["h-inc"]=17
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=494+pdfCellYOffset
	newField["text"]="India"
	newField["h-inc"]=17
	fieldData.append(newField)

	newField={}
	newField["x"]=107+pdfCellXOffset
	newField["y"]=566+pdfCellYOffset
	newField["text"]="11"
	newField["h-inc"]=17
	fieldData.append(newField)

	newField={}
	newField["x"]=157+pdfCellXOffset
	newField["y"]=566+pdfCellYOffset
	newField["text"]="10"
	newField["h-inc"]=17
	fieldData.append(newField)

	newField={}
	newField["x"]=207+pdfCellXOffset
	newField["y"]=566+pdfCellYOffset
	newField["text"]="1984"
	newField["h-inc"]=17
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=466+pdfCellYOffset
	newField["text"]="Maharastra"
	newField["h-inc"]=17
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=436+pdfCellYOffset
	newField["text"]="indian"
	newField["h-inc"]=17
	fieldData.append(newField)

	newField={}
	newField["x"]=135+pdfCellXOffset
	newField["y"]=408+pdfCellYOffset
	newField["text"]="indian"
	newField["h-inc"]=17
	fieldData.append(newField)

	
	#print(fieldData) 
	addText(fieldData)

