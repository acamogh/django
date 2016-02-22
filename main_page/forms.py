from django import forms
from main_page.models import Signup


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['fullname','email']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_base, provider=email.split('@')
        domain, extension=provider.split('.')

        if not extension == 'edu':
            raise forms.ValidationError('please use a valid .edu email address')

        try:
            Signup.objects.get(email__iexact=email)
        except Signup.DoesNotExist:
            return email
        raise forms.ValidationError('A user with that email already exists.')

class ContactForm(forms.Form):
    name=forms.CharField(max_length=128, )
    email=forms.EmailField()
    phone=forms.IntegerField(required=False,)
    message=forms.CharField(widget=forms.Textarea)

