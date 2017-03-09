from django.contrib import admin

# Register your models here.
from .models import profile

class profileAdmin(admin.ModelAdmin):
	list_display =["__unicode__"]
	class Meta:
		model = profile


admin.site.register(profile, profileAdmin)