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

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'mobile_number', 'email', 'password')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)