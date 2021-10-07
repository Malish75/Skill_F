from .models import *
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'new_post', 'time_in_new_post', 'author', )
    #list_display = [field.name for field in Post._meta.get_fields()] # must not be a ManyToManyField.
    list_display_links = ('title', 'id',)
    search_fields = ('title', 'new_post', )
    list_filter = ('author', 'category', 'time_in_new_post')  # добавляем примитивные фильтры в нашу админку


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'id', 'author_rating')
    list_display_links = ('author', 'id', 'author_rating')
    # search_fields = ('author', ) - НЕ РАБОТАЕТ!!!!
    list_filter = ('author', 'id', 'author_rating')


class CategoryAdmin(admin.ModelAdmin,):
    list_display = ('category_name', )
    list_display_links = ('category_name', )
    #search_fields = ('category_name', 'subscriber') - НЕ РАБОТАЕТ!!!!
    list_filter = ('category_name',)


# class CategoryAdmin(TranslationAdmin):
#     model = Category  # для перевода


class PostAdmins(TranslationAdmin):
    model = Post  # для перевода


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
