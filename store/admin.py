from django.contrib import admin
from .models import Category, Writer, Book,Profile,Review


class AddCategory(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, AddCategory)

class AddWriter(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Writer, AddWriter)

class AddBook(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock', 'status', 'created', 'updated']
	list_filter = ['status', 'created', 'updated']
	list_editable = ['price', 'stock', 'status']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book, AddBook)

admin.site.register(Profile)
admin.site.register(Review)

