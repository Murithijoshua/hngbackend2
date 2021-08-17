from django.contrib import admin

# Register your models here.
from .models import Entrys


@admin.register(Entrys)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Message')
    # list_display_links = None