from django.shortcuts import render
from django.db import IntegrityError
from .models import Product, Gallery, Popular, Storage, Contact
# Create your views here.

def index(request):
    try:

        __context = {}
        
        objPopular = Popular.objects.filter(is_active=True).order_by('-pk')

        __context['MainPopular'] = objPopular

        return render(request, 'websites/index.html', __context)
    except Exception as ex:
        return render(request, '404.html', {'error':ex})


def product(request):
    try:
        __context = {}
        
        objProduct = Product.objects.filter(is_active=True).order_by('-pk')

        __context['MainProduct'] = objProduct

        return render(request, 'websites/product.html', __context)
    except Exception as ex:
        return render(request, '404.html', {'error':ex})


def gallery(request):
    try:

        __context = {}
        
        objGallery = Gallery.objects.filter(is_active=True).order_by('-pk')

        __context['MainGallery'] = objGallery

        return render(request, 'websites/gallery.html', __context)
    except Exception as ex:
        return render(request, '404.html', {'error':ex})


def about(request):
    try:
        __context = {}
        
        objStorage = Storage.objects.filter(is_active=True).order_by('-pk')

        __context['MainStorage'] = objStorage

        return render(request, 'websites/about.html', __context)
    except Exception as ex:
        return render(request, '404.html', {'error':ex})
        

def contact(request):
    try:
        __context = {}

        if request.POST:

            try:
                contact = Contact(name=request.POST['name'], email=request.POST['email'], 
                subject=request.POST['subject'],message=request.POST['message'])

                contact.save()

            except IntegrityError as ex:
                __context['form_data'] = {
                    'name': request.POST['name'],  'email': request.POST['email'],
                    'subject': request.POST['subject'],'message': request.POST['message']}

                __context['error'] = ex

        return render(request, 'websites/contact.html', __context)
    except Exception as ex:
        return render(request, '404.html', {'error':ex})


def events(request):
    try:
        return render(request, 'websites/events.html')
    except Exception as ex:
        return render(request, '404.html', {'error':ex})


def faq(request):
    try:
        return render(request, 'websites/faq.html')
    except Exception as ex:
        return render(request, '404.html', {'error':ex})







