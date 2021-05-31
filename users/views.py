from django.contrib.auth.hashers import make_password
from users.models import User
from users.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, "users/sign_in1.html")

def mypage(request):
    return render(request, "users/status.html")

def registerPage(request):
	form = RegisterForm()
	if request.method == 'POST':
			form = RegisterForm(request.POST)
			user = User(
           		email=form.data.get('email'),
            	name=form.data.get('name'),
            	password=make_password(form.data.get('password')),
            	level='user'
        	)
			user.save()
			username = form.cleaned_data.get('first_name')
			messages.success(request, 'Account was created for ' + user)

			return redirect('verify')
	context = {'form':form}
	return render(request, 'users/sign_up1.html', context)

