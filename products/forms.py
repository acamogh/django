from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=120)
    email=forms.EmailField()
    comment=forms.CharField(max_length=120,widget=forms.TextInput)