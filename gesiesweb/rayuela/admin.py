from django.contrib import admin

from .models import Rayuela

# Register your models here.

class RayuelaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Rayuela, RayuelaAdmin)