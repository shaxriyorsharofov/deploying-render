from django.contrib import admin
from .models import News
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['author', 'date']

admin.site.register(News, NewsAdmin)