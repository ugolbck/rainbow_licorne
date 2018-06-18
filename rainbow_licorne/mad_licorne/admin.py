from django.contrib import admin
from mad_licorne.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'release_date', 'author', )
	search_field = ('title', )
	list_filter = ('category', )

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'content', 'comment_date', )
	search_field = ('name', )

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)