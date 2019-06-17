from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

class PDFForm(models.Model):
	#pass	
	pdf_type=models.IntegerField(default=0)
	pdf_name=models.CharField(max_length=100,default='')
	file_path=models.FileField(default='')	

class FormField(models.Model):
	#pass	
	fk_pdf_id=models.ForeignKey('PDFForm', on_delete=models.CASCADE,default=0)
	field_type=models.IntegerField(default=0)
	field_page_number=models.IntegerField(default=0)
	field_x=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	field_y=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	field_x_increment=models.DecimalField(max_digits=6,decimal_places=2,default=0)
	class Meta:
		ordering= ("field_page_number", "field_type")
	
class UserData(models.Model):
	#pass	
	fk_user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
	field_type=models.IntegerField(default=0)
	field_text=models.CharField(max_length=200,default='')
	field_date=models.DateField()

	

	
	