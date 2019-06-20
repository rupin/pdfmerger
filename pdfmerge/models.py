from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

#Class has reference to all PDFForms
class PDFForm(models.Model):
	#pass	
	pdf_type=models.IntegerField(default=0)
	pdf_name=models.CharField(max_length=100,default='')
	file_path=models.FileField(default='')
	def __str__(self):
		return self.pdf_name

#Class has reference to every form Field created
class Field(models.Model):
	#pass	
	field_description=models.CharField(max_length=200,default='')
	def __str__(self):
		return self.field_description
	
	
#class relates form field id with PDF ID, a pdf can have multiple fields of same kind. 
class PDFFormField(models.Model):
	#pass	
	pdf=models.ForeignKey('PDFForm', on_delete=models.CASCADE,default=0)
	field=models.ForeignKey(Field, on_delete=models.CASCADE,default=0)	
	field_page_number=models.IntegerField(default=0)
	field_x=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	field_y=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	field_x_increment=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	class Meta:
		ordering= ("field_page_number",)



    
#class stores extra user data, which is treated as a form field. 	
class UserProfile(models.Model):
	#pass	
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
	field=models.ForeignKey(Field, on_delete=models.CASCADE,default=0)
	field_text=models.CharField(max_length=200,default='')
	field_date=models.DateField(null=True)
	class Meta:
		unique_together = ('user', 'field',)
	
#class has reference to all pdfs users have generated/requested
class GeneratedPDF(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
	pdf=models.ForeignKey('PDFForm', on_delete=models.CASCADE,default=0)
	date_created=models.DateTimeField(auto_now=True)
	class Meta:
		ordering= ("date_created",)
	



	

	
	