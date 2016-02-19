from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ContactForm
from .models import Product
from ecomm import settings

# Create your views here.
class ProductViewList(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact_person_name=form.cleaned_data['name']
        contact_person_email=form.cleaned_data['email']
        sub='site: message from '+str(contact_person_name)
        msg=form.cleaned_data['comment']+'Contact Email= '+str(contact_person_email)
        email=settings.EMAIL_HOST_USER
        recipients = ['acamogh@gmail.com']
        send_mail(sub,msg,email,recipients, fail_silently=False)
    return render(request,'contact.html',{'form':form})
