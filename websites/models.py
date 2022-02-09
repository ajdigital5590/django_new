from django.db import models
from django.contrib.auth import settings
from django.utils.timezone import datetime

# Create your models here.

class Product(models.Model):

    objects = models.Manager

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product/', max_length=150)

    is_active = models.BooleanField(
        default=True, null=True, blank=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)


    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"

    def __str__(self):
        return self.name  


class Gallery(models.Model):

    objects = models.Manager

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/', max_length=150)

    is_active = models.BooleanField(
        default=True, null=True, blank=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)


    class Meta:
        verbose_name_plural = "Gallery"
        verbose_name = "Gallery"

    def __str__(self):
        return self.name  

class Popular(models.Model):

    objects = models.Manager

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='popular/', max_length=150)

    is_active = models.BooleanField(
        default=True, null=True, blank=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)


    class Meta:
        verbose_name_plural = "Popular"
        verbose_name = "Popular"

    def __str__(self):
        return self.name  



class Storage(models.Model):

    objects = models.Manager

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='storage/', max_length=150)

    is_active = models.BooleanField(
        default=True, null=True, blank=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)


    class Meta:
        verbose_name_plural = "Storage"
        verbose_name = "Storage"

    def __str__(self):
        return self.name 

class Contact(models.Model):

    objects = models.Manager

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=150, default='')
    message = models.TextField()

    created_on = models.DateField(
        default=datetime.now, editable=False, null=True, blank=True)
    is_active = models.BooleanField(
        default=True, editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact Us"
        verbose_name = "Contact Us"

    def __str__(self):
        return self.name
 