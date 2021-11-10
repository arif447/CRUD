from django import forms
from crud_app.models import Student_profile
from django.forms import ModelForm

class student_form(forms.ModelForm):
    class Meta:
        model = Student_profile
        fields = '__all__'