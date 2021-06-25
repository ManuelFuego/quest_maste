from django import forms
from .models import *

class AddTest(forms.Form):
 #    question = forms.CharField(max_length=250, label = 'вопрос' )

    question = forms.CharField(max_length=250)
    answer = forms.CharField(max_length=250)
    is_right = forms.BooleanField()