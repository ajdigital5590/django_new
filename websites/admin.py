from django.contrib import admin
from .models import Product, Gallery, Popular, Storage, Contact

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'is_active', 'created_by', 'created_on']

class GalleryAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'is_active', 'created_by', 'created_on']


class PopularAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'is_active', 'created_by', 'created_on']

class StorageAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'is_active', 'created_by', 'created_on']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created_on', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'email']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Popular, PopularAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Product, ProductAdmin)
