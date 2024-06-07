from django.contrib import admin
from .models import PostModel, CommentsModel

# Register your models here.
@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['title']


admin.site.register(CommentsModel)