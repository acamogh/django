from django.shortcuts import render,HttpResponse
from main_page.forms import SignupForm, ContactForm
from django.core.mail import send_mail
from ecomm import settings

from .models import Signup
from products.models import ProductFeatured


# Create your views here.
def index(request):
    title = 'welcome'
    featured_image=ProductFeatured.objects.first()
    form = SignupForm(request.POST or None)
    context={'title':title,'form':form,'featured_image':featured_image}
    if form.is_valid():
        instance=form.save(commit=False)
        email= form.cleaned_data['email']
        email_save,created=Signup.objects.get_or_create(email=email)
        title = 'thank you'
        context={'title':title}


    return render(request,'index.html',context)

def contact(request):
    title='Contact Us'
    contact_info=ContactForm(request.POST or None)
    if contact_info.is_valid():
        # contact_info.save(commit=False)
        name = contact_info.cleaned_data['name']
        email= contact_info.cleaned_data['email']
        phone= contact_info.cleaned_data['phone']
        message=contact_info.cleaned_data['message']
        from_msg = settings.EMAIL_HOST_USER
        subject=('from: '+name+' email: '+email + 'phone: '+str(phone))

        send_mail(subject , message, from_msg,[from_msg], fail_silently=False)

    return render(request,'contact.html',{'contact_info':contact_info, 'title':title})