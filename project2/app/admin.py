from django.contrib import admin
from .models import farmer, farm1


# Register your models here.
class showadmin(admin.ModelAdmin):
    model = 'farmer'
    list_display = ['name', 'image', 'des']
    list_editable = ('image', 'des',)
    list_filter = ('des',)

class loveadmin(admin.ModelAdmin):
     model = 'farm1'
     list_display = ['image','des','date']
     list_editable = ('des','date',)

admin.site.register(farmer, showadmin)

admin.site.register(farm1, loveadmin)
