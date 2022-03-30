from django.contrib import admin
from store.models import (Category, Author, Publishing, Book, Customer, Balance, Order, Item, Comment, Rate)

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publishing)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Balance)
admin.site.register(Order)
admin.site.register(Item)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'book')
    list_editable = ('customer', 'book',)

admin.site.register(Rate)

