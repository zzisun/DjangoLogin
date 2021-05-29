from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=64, label="First name")
    last_name = forms.CharField(max_length=64, label="Last name")
    email = forms.EmailField(label="Email address", required=True)
    mobile_number = forms.CharField(max_length=64, label="Mobile number")
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'mobile_number', 'email', 'password')


# class UserChangeForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ('email',)