from django.contrib import admin

from .models import Column, Article

class ColumnAdmin(admin.ModelAdmin):
	list_display = ('name','addr','intro','nav_display', 'home_display')

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','addr','author',)

admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)
# Register your models here.
