from django.contrib import admin
from .models import Plan, Benefit


class BenefitInline(admin.StackedInline):
    model =  Benefit
    extra = 2


class BenefitAdmin(admin.ModelAdmin):
    inlines = [BenefitInline]

admin.site.register(Plan,BenefitAdmin)

