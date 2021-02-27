from django.contrib import admin
from testApp.models import punejobs,hydjobs,banglorejobs,chennaijobs

# Register your models here.

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class banglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(punejobs,punejobsAdmin)
admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(banglorejobs,banglorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
