from django.contrib import admin
from .models import Category, Company, Deal

# Register your models here.
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Deal)

