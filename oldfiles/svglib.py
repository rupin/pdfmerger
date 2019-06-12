import svgwrite
from reportlab.graphics import renderPDF, renderPM

dwg = svgwrite.Drawing('test.svg', profile='tiny', size=("210mm", "297mm"))

dwg.add(dwg.text('Test', x=[20], y=[40]))
dwg.save()    
renderPDF.drawToFile(dwg,"test.pdf")
   # renderPM.drawToFile(drawing, 'svg_demo.png', 'PNG')
