from django.contrib import admin
from myform.models import Subscribe

# Register your models here.
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_displays = ['__all__']