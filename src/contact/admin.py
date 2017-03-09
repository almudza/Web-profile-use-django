from django.contrib import admin

# Register your models here.
from .models import contact

class contactAdmin(admin.ModelAdmin):
	list_display =["name","email","telp","deskripsi"]
	class Meta:
		model = contact


admin.site.register(contact, contactAdmin)