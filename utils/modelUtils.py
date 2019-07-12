from pdfmerge.models import *
from dateutil.parser import *
import datetime

def saveUserProfileFields(fieldList, p_user):
	defaultDate=datetime.date(1987, 6,15)
	for field in fieldList:
		print(field)
		fieldValue=field.get("userValue")
		fieldObject=Field.objects.get(id=field.get("ID"))	
		userProfile=UserProfile.objects.filter(user=p_user,field=fieldObject)
		field_display=fieldObject.field_display

		userProfileExists=userProfile.count()
		if(userProfileExists==1): # The User Profile Exists
			#if(fieldObject.)
			if(field_display=="FULLDATE"):
				#fieldDate=datetime.datetime.strptime(fieldValue, '%d %B, %Y').date()
				fieldDate=parse(fieldValue).date().strftime("%B %d, %Y")
				print(fieldDate)
				#fieldDate=timestring.Date(fieldValue).date
				#print(fieldDate)
				userUpdateStatus=userProfile.update(field_text=fieldDate)
			else:
				userUpdateStatus=userProfile.update(field_text=fieldValue, field_date=defaultDate)
				
		else:
			if(field_display=="FULLDATE"):
				#fieldDate=datetime.datetime.strptime(fieldValue, '%d %B, %Y').date()
				#fieldDate=timestring.Date(fieldValue).date
				fieldDate=parse(fieldValue).date()
				userCreatestatus=UserProfile(user=p_user,field=fieldObject, field_text=fieldDate)
				userCreatestatus.save()
			else:	
				userCreatestatus=UserProfile(user=p_user,field=fieldObject, field_text=fieldValue,field_date=defaultDate)
				userCreatestatus.save()
