from django.contrib import admin
from . models import thalapathymodel

# Register your models here.
@admin.register(thalapathymodel)
class bmwadmins(admin.ModelAdmin):
    list_display=('id','name','fvt')
