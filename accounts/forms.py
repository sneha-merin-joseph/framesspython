from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField( max_length=200, required=False)
    last_name = forms.CharField( max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already in use.")
            return email
        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            # Check if passwords match
            if password1 and password2 and password1 != password2:
                raise ValidationError("Passwords do not match")

            # Check password complexity (you can customize this based on your requirements)
            if len(password1) < 8:
                raise ValidationError("Password must be at least 8 characters long")
            if not any(char.isdigit() for char in password1):
                raise ValidationError("Password must contain at least one digit")
            if not any(char.isalpha() for char in password1):
                raise ValidationError("Password must contain at least one letter")

            return password2

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']