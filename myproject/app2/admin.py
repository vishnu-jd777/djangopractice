from django.contrib import admin
from . models import bmwlist

# Register your models here.
@admin.register(bmwlist)
class bmwadmin(admin.ModelAdmin):
    list_display=('id','title','para','price')