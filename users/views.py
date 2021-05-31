from django.contrib.auth.hashers import make_password
from users.models import User
from users.forms import RegisterForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from django.contrib import messages


def home(request):
    return render(request, "users/sign_in1.html")

def mypage(request):
    return render(request, "users/status.html")

def verifyAccount(request):
    return render(request, "users/sign_up2.html")

def registerPage(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			# new_user = models.User.objects.create_user(**form.cleaned_data)
			# login(request, new_user)
			username = form.cleaned_data.get('first_name')
			messages.success(request, 'Account was created for ' + username)
			return redirect('verify')
		else:
			print("error")
	else:
		form = UserCreationForm()
	context = {'form':form}
	return render(request, 'users/sign_up1.html', context)

