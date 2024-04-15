from django.contrib import admin
from userauths.models import profile, User



class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','Phone']
    list_editable=['email','Phone']

class ProfielAdmin(admin.ModelAdmin):
    list_display= ['full_name','gender','country','address']
    

admin.site.register(User, UserAdmin)
admin.site.register(profile, ProfielAdmin)

