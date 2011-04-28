from django.contrib import admin
from books.models import Book
from sortable.admin import SortableAdmin

  
def show_image(book):
    '''Show the book's cover'.'''
    if book.image(): return book.image()
show_image.allow_tags = True

class BookAdmin(SortableAdmin):
    list_display_links = ('title', )
    list_display = SortableAdmin.list_display + ('title', 'author', show_image)

admin.site.register(Book, BookAdmin)
