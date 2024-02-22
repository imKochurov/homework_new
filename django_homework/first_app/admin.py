from django.contrib import admin
from .models import CallOrder, SiteAdmins

# Register your models here.

admin.site.register(SiteAdmins)
admin.site.register(CallOrder)
