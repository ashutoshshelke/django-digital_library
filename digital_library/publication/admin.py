from django.contrib import admin
from publication.models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','pen_name','gender','age','genre')
    search_fields=('name',)

class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','publisher','publication_date')
    list_filter=('author',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)