#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from clients.models import Company, Comment

class ContactForm(forms.Form):
	email = forms.EmailField(label='Your email please')
	message = forms.CharField(widget=forms.Textarea)
	
class CompanyForm(ModelForm):
    class Meta:
        model = Company

class CommentForm(ModelForm):
    class Meta:
        model = Comment