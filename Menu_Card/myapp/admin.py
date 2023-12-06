from django.contrib import admin
from .models import MenuUpload

@admin.register(MenuUpload)

class MenuAdmin(admin.ModelAdmin):
    list_display =['id','name','photo','date'] 

# Register your models here.
