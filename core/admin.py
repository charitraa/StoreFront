from django.contrib import admin
from store.admin import ProductAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as ud
from store.models import Product
from tags.models import TaggedItem
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(ud):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","email","first_name","last_name"),
            },
        ),
    )
    
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model =TaggedItem

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)