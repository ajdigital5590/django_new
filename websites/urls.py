from django.urls import path
from .views import index, product, gallery, about, contact, events, faq

app_name = 'websites'

urlpatterns = [
    path('',index, name='index'),
    path('product/',product, name='product'),
    path('gallery/',gallery, name='gallery'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('faq/',faq, name='faq'),
    path('events/',events, name='events'),
    
]
