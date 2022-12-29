from django.contrib import admin
from app1.models import Donor,Acceptor
# Register your models here.
class DonorAdmin(admin.ModelAdmin):
    list_display=['name','age','mobile','regno','bloodgroup','address','photo']
class AcceptorAdmin(admin.ModelAdmin):
    list_display=['name','age','mobile','regno','bloodgroup','address','photo']
admin.site.register(Donor,DonorAdmin)
admin.site.register(Acceptor,AcceptorAdmin)
