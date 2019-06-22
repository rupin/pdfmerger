from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
	
class PDFFormAdmin(ImportExportModelAdmin):
    pass

class PDFFormFieldAdmin(ImportExportModelAdmin):
	model=PDFFormField
	list_display=['pdf', "field"]

class UserProfileAdmin(ImportExportModelAdmin):
	model=UserProfile
	list_display=['user', "field", "field_text", "field_date"]

class FieldAdmin(ImportExportModelAdmin):
    model=Field
    list_display=['id', "field_description",]


    	
    
  

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PDFForm)
admin.site.register(Field)
admin.site.register(PDFFormField,PDFFormFieldAdmin)

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(GeneratedPDF)
