from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone


from .forms import ContactForm,VariationInventoryFormSet
from .models import Product, Variation
from .mixins import StaffRequiredMixin,LoginRequiredMixin
from ecomm import settings



# Create your views here.
class VariationListView(StaffRequiredMixin,ListView):
    model = Variation
    queryset = Variation.objects.all

    def get_context_data(self, *args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())
        return context

    def get_queryset(self, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            queryset = Variation.objects.filter(product=product)
        return queryset

    def post(self, request, *args, **kwargs):
        formset = VariationInventoryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                # if new_item.title:
                product_pk = self.kwargs.get("pk")
                product = get_object_or_404(Product, pk=product_pk)
                new_item.product = product
                new_item.save()
            messages.success(request, " Your inventory and pricing has been updated.")
            return redirect("ProductViewList")
        raise Http404


class ProductViewList(ListView):
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductViewList, self).get_context_data(*args, **kwargs)
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")  # None
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductViewList, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        print query

        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs


class ProductDetailView(DetailView):
    model = Product


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact_person_name = form.cleaned_data['name']
        contact_person_email = form.cleaned_data['email']
        sub = 'site: message from ' + str(contact_person_name)
        msg = form.cleaned_data['comment'] + 'Contact Email= ' + str(contact_person_email)
        email = settings.EMAIL_HOST_USER
        recipients = ['acamogh@gmail.com']
        send_mail(sub, msg, email, recipients, fail_silently=False)
    return render(request, 'contact.html', {'form': form})
