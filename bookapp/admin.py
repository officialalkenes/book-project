from django.contrib import admin

# Register your models here.
from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat', 'slug']


class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'user', 'isbn']
    list_display_links = ['author', 'title', 'user']


admin.site.register(Book, BookAdmin)



