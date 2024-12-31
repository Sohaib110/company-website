from django.contrib import admin
from app.models import GeneralInfo, Service

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
   list_display = ['company_name', 'location', 'email', 'phone', 'open_hours']
   
   read_only_fields = ['email']
   
   
   
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
   list_display = ['title', 'description']
   
   search_fields = ['title','description']
   
    
