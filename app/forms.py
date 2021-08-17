from django.forms import ModelForm,TextInput,Select
# from django import forms
from . models import Entrys

class ReportForm(ModelForm):
    class Meta:
        model = Entrys
        fields = '__all__'
        