from pdfmerge.models import *
from dateutil.parser import *
import datetime
import pandas as pd

def saveUserProfileFields(fieldList, p_user):
	defaultDate=datetime.date(1987, 6,15)
	for field in fieldList:
		#print(field)
		fieldValue=field.get("userValue")
		fieldObject=Field.objects.get(id=field.get("ID"))	
		userProfile=UserProfile.objects.filter(user=p_user,field=fieldObject)
		field_display=fieldObject.field_display

		userProfileExists=userProfile.count()
		if(field_display=="FULLDATE"):
			#fieldDate=datetime.datetime.strptime(fieldValue, '%d %B, %Y').date()
			fieldText=parse(fieldValue).date().strftime("%B %d, %Y")
			#print(fieldText)
		else:
			fieldText=fieldValue
		if(userProfileExists==1): # The User Profile Exists
			
			userUpdateStatus=userProfile.update(field_text=fieldText)
				
		else:
			
			userCreatestatus=UserProfile(user=p_user,field=fieldObject, field_text=fieldText,field_date=defaultDate)
			userCreatestatus.save()


def getUserFormData(request, pdfid):
	loggedUserID=request.user.id
	#pdfid=pdf_id

	#get details about the form
	formData=PDFForm.objects.get(id=pdfid)
	
	#get all fields in PDF related to PDFID
	fieldsinPDF=PDFFormField.objects.filter(pdf=pdfid).values_list(
																	"field",
																	"field_x",
																	"field_page_number",
																	"field_y",
																	"field_x_increment",
																	"field__field_display",
																	"font_size",
																	'field_index',
																	 named=True 
																	 )
	
	#get all fields Related to User in UserProfile and that match the fields in the PDFForm
	userFields=UserProfile.objects.filter(user=loggedUserID).values_list(
																	"field", 
																	"field_text",
																	"field__field_description",
																	"field__field_question",																																
																	named=True
																	)
	#dprint.dprint(queryset)

	#Set the column as index on which the join is to be made in pandas
	#print(userFields)
	userFieldDF=pd.DataFrame(list(userFields)).set_index('field')
	PDFFieldsDF=pd.DataFrame(list(fieldsinPDF)).set_index('field')
	
	#Make the Join
	combinedDF=userFieldDF.join(PDFFieldsDF, on='field',lsuffix='_left', rsuffix='_right')
	combinedDF.sort_values(by=['field_page_number', 'field_index'],inplace=True)
	#
	#remove rows with NA Values. Will happen when the number of rows in the above datasets differ in count. 
	combinedDF.dropna(0,inplace=True)
	#dprint.dprint(combinedDF)
	#sort the Dataframe by Field Page Number, then convert it to a list of dictionaries
	dataSet=combinedDF.to_dict('records')

	return dataSet, formData