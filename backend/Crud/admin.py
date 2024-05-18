from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    
    
admin.site.register(Todo, TodoaAdmin)
