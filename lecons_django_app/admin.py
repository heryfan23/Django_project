from django.contrib import admin
from .models import Articles
# Register your models here.
class DonnerArt(admin.ModelAdmin):
    list_display = ('titre','prix','desc','images')
    search_fields = ("titre","prix")
admin.site.register(Articles,DonnerArt)