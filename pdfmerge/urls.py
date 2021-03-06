"""pdfmerge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views, signupView, ajaxViews


from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.homePage, name='home'),
	
    path('viewPDF/<int:pdfid>', views.fillForm, name='fillform'),
    path('systemForms/', views.viewSystemForms, name='systemForms'),
    path('addForm/<int:form_id>', views.addFormToProfile, name='systemForms'),
    path('saveDynamicData/<int:pdfid>', views.saveDynamicFieldData, name='saveDynamicData'),
    path('profile/', views.profile, name='profile'),
    path('editPDF/<int:pdfid>', views.editPDFLive, name='profile'),
    path('signup/', signupView.signup, name='signup'),
    path('saveEditedField/', ajaxViews.saveEditedField, name='saveEditedField'),
    path('arrangeFormQuestions/<int:pdfid>', views.arrangeFormQuestions, name='arrangeFormQuestions'),
    path('saveFormFieldSequence/', ajaxViews.saveFormFieldSequence, name='saveFormFieldSequence')

]

urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]

