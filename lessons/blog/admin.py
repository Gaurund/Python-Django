from django.contrib import admin

from .models import *

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Post)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'bio',
        'birth_date',
    ]
    list_filter = [
        'last_name',
        'birth_date',
    ]
    search_fields = [
        'last_name__startswith',
        'email',
    ]
    list_editable = [
        'email',
        'birth_date',
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
        'author',
    ]
    list_filter = [
        'timestamp',
        'author',
        'views',
    ]
    search_fields = [
        'title',
        'author',
    ]
