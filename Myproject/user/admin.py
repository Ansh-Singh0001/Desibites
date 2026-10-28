from django.contrib import admin
from .models import *
# Register your models here.


class ContactusAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","message")

admin.site.register(Contactus,ContactusAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display=("picture","title")

admin.site.register(igallery,igalleryAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=("category","picture")
admin.site.register(category,categoryAdmin)

class menuAdmin(admin.ModelAdmin):
    list_display=("itemname","rate","detail","salerate","itemtype","category","picture")
admin.site.register(menu,menuAdmin)


class bookingAdmin(admin.ModelAdmin):
    list_display=("name","mobno","email","totalperson","date","time","foodtype","mealtype","paymode")
admin.site.register(booking,bookingAdmin)