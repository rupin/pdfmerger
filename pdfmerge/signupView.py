from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import *

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            user_first_name=form.cleaned_data.get('first_name')
            user_last_name=form.cleaned_data.get('last_name')
            user_full_name=user_first_name+ " " + user_last_name
            field=Field.objects.get(id=1)
            newUser=UserProfile(user=user, field=field, field_text=user_full_name)
            newUser.save()
            return redirect('systemForms')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})