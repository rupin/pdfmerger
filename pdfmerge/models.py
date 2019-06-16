from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

class PDFForm(models.Model):	
	
	pdf_type=models.IntegerField()
	pdf_name=models.CharField(max_length=100)
	file_path=models.FileField()	

class FormField(models.Model):	
	
	fk_pdf_id=models.ForeignKey('PDFForm', on_delete=models.CASCADE)
	field_type=models.IntegerField()
	field_page_number=models.IntegerField()
	field_x=models.DecimalField(max_digits=6,decimal_places=2)
	field_y=models.DecimalField(max_digits=6,decimal_places=2)
	field_x_increment=models.DecimalField(max_digits=6,decimal_places=2)
	
class UserData(models.Model):	
	fk_user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	field_type=models.IntegerField()
	field_text=models.CharField(max_length=200)
	
	