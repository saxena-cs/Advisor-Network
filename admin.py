from django.contrib import admin
from .models import Advisormodel

@admin.register(Advisormodel)
# Register your models here.
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['id','name','profile_url']