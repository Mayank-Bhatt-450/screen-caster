from django import forms
from . import models
class data__f(forms.ModelForm):
    class Meta():
        model = models.data_m
        fields = '__all__'
