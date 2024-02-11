from ast import ClassDef
from msilib.schema import Class
from django.contrib import admin
from .models import *

class user_Admin(admin.ModelAdmin):
    list_display=("u_id","u_name","u_mailid","pswd","hobby","address","profession","dob","education","phone_no","pic")

class chat_Admin(admin.ModelAdmin):
    list_display=("msgsender_id","msgreceiver_id","message","time")

class requestAdmin(admin.ModelAdmin):
    list_display=("reqsender_id","reqreceiver_id","req_status","time")



admin.site.register(user,user_Admin)
admin.site.register(chat,chat_Admin)
admin.site.register(Req,requestAdmin)