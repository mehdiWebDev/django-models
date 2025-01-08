from django.contrib import admin
from .models import Book, Author, Address, Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("author", "rating", "is_bestselling")
  list_display = ("title", "author", "rating", "is_bestselling")

class AuthorAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name")
  search_fields = ("first_name", "last_name")

class AddressAdmin(admin.ModelAdmin):
  list_display = ("street", "city", "zip")
  search_fields = ("street", "city", "zip")

class CountryAdmin(admin.ModelAdmin):
  list_display = ("name", "code")
  search_fields = ("name", "code")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)

