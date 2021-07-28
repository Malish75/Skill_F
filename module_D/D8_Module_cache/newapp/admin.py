from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'new_post', 'time_in_new_post', 'author', )
    list_display_links = ('title', 'id')
    search_fields = ('title', 'new_post')

admin.site.register(Post, PostAdmin)
