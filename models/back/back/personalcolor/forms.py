from django import forms

class MyForm(forms.Form):
    image = forms.ImageField()