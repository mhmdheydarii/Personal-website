from django.contrib import admin
from .models import Project, Skill, Service, Contact
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'updated_date']
    search_fields = ['title']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'updated_date', 'status']
    search_fields = ['title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'created_date', 'is_seen']
    search_fields = ['email']

admin.site.register(Skill)

