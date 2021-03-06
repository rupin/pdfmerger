from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

#Class has reference to all PDFForms
class PDFForm(models.Model):
	#pass	
	pdf_type=models.IntegerField(default=0)
	pdf_name=models.CharField(max_length=100,default='')
	file_path=models.FileField(default='',upload_to='pdfs')
	cellSize_X=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	cellSize_Y=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	pdf_description=models.CharField(max_length=200,default="")
	image=models.FileField(default='',upload_to='photos')
	def __str__(self):
		return self.pdf_name
	class Meta:
		ordering= ("pdf_name",)

#Class has reference to every form Field created
class Field(models.Model):
	#pass	
	FIELD_STATES = (
						('DYNAMIC', 'DYNAMIC'),
						("STATIC", "STATIC"),
						
					)
	field_description=models.CharField(max_length=200, default='')
	field_question=models.CharField(max_length=300, default='')
	field_state=models.CharField(max_length=20, choices=FIELD_STATES, default="STATIC")


	FIELD_CHOICES = (
						('NONE', 'NONE'),
						("FULLDATE", "FULLDATE"),
						("DATE", "DATE"),
						("MONTH", "MONTH"),
						("YEAR", "YEAR"),
						('FULLDATE_TEXT_MONTH','FULLDATE_TEXT_MONTH'),
						('CHECK_BOX','CHECK_BOX'),
						('MULTICHOICE','MULTICHOICE')
					)

	field_display = models.CharField(max_length=20,choices=FIELD_CHOICES,default="NONE")

	FIELD_CATEGORY_CHOICES = (
						('PERSONAL', 'Personal'),
						('DOCUMENT', 'Document'),
						('ADDRESS', 'Address'),
						
						
					)
	category= models.CharField(max_length=20,choices=FIELD_CATEGORY_CHOICES,default="PERSONAL")
	category_order= models.IntegerField(default=0)
	multichoice_options=models.CharField(max_length=200,default='')
	def __str__(self):
		return self.field_description
	class Meta:
		ordering= ("category", "category_order", "field_description")
	
	
#class relates form field id with PDF ID, a pdf can have multiple fields of same kind. 
class PDFFormField(models.Model):
	#pass	
	pdf=models.ForeignKey('PDFForm', on_delete=models.CASCADE,default=0)
	field=models.ForeignKey(Field, on_delete=models.CASCADE,default=0)	
	field_page_number=models.IntegerField(default=0)
	field_x=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	field_y=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	field_x_increment=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	font_size=models.IntegerField(default=12)   
	field_index=models.IntegerField(default=0) 
	# for Multichoice, these will have comm seperated values of field positions in X and Y directions
	field_x_choices=models.CharField(max_length=200,default='')
	field_y_choices=models.CharField(max_length=200,default='')
	class Meta:
		ordering= ("field_page_number","field_index")
	


    
#class stores extra user data, which is treated as a form field. 	
class UserProfile(models.Model):
	#pass	
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
	field=models.ForeignKey(Field, on_delete=models.CASCADE,default=11)	
	field_text=models.CharField(max_length=200,default='')
	field_date=models.DateField(null=True)


	# for multichoice type questions, this stores the index of the user choice
	data_index=models.IntegerField(default=0)  
	class Meta:
		unique_together = ('user', 'field')
	
#class has reference to all pdfs users have generated/requested
class GeneratedPDF(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
	pdf=models.ForeignKey('PDFForm', on_delete=models.CASCADE,default=0)
	date_created=models.DateTimeField(auto_now=True)
	class Meta:
		ordering= ("date_created",)
	



	

	
	