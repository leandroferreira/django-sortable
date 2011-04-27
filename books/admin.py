from django.contrib import admin
from books.models import Book

def show_image(book):
    '''Show the book's cover'.'''
    if book.image(): return book.image()
show_image.allow_tags = True

class BookAdmin(admin.ModelAdmin):
    list_display_links = ('title', )
    list_display = ('title', 'author', show_image, )

admin.site.register(Book, BookAdmin)
