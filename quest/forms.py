from django import forms
from .models import *

class Addmessage(forms.ModelForm):
   class Meta:
        model = Message
        fields = ['mail','text']
        widgets ={
            'text': forms.Textarea(attrs={'cols':40,'rows':10})
        }
