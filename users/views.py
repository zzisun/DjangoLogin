from users.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, "users/sign_in1.html")

def mypage(request):
    return render(request, "users/status.html")

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('status')
	else:
		form = RegisterForm()
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

		context = {'form':form}
		return render(request, 'users/sign_up1.html', context)

# def registerPage(request):
#     """
#     계정생성
#     """
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')

#             raw_password = form.cleaned_data.get('password1')
#             # user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             return redirect('index')
#     else:
#         form = RegisterForm()
#     return render(request, 'users/sign_up1.html', {'form': form})