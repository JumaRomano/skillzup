from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Grade

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role', 'profile_picture', 'date_of_birth']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade', 'remarks']
