from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'id')
    prepopulated_fields = {'slug':['title']}

admin.site.register(Category, CategoryAdmin)


class ImageInline(admin.TabularInline):
    model = Image


class VideoInlide(admin.TabularInline):
    model = Video


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_of_create', 'owner', 'id')
    prepopulated_fields = {'slug':['title']}
    inlines = [ImageInline, VideoInlide]

admin.site.register(Product, ProductAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    prepopulated_fields = {'slug':['title']}

admin.site.register(Genre, GenreAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'product', 'created')

admin.site.register(Comment, CommentAdmin)