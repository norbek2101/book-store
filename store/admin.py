from django.contrib import admin
from store.models import (Category, Author, Publishing, Book, Customer, Balance, Order, Item, Comment, Rate)

admin.register(Category)
admin.register(Author)
admin.register(Publishing)
admin.register(Book)
admin.register(Customer)
admin.register(Balance)
admin.register(Order)
admin.register(Item)
admin.register(Comment)
admin.register(Rate)

