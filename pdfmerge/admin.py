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
	
class PDFFormAdmin(admin.ModelAdmin):
    pass

class PDFFormFieldAdmin(admin.ModelAdmin):
	list_display = ['pdf__pdf_name', 'field__field_description',]
  

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PDFForm)
admin.site.register(Field)
admin.site.register(PDFFormField,PDFFormFieldAdmin)

admin.site.register(UserProfile)
admin.site.register(GeneratedPDF)
