from rest_framework import serializers
from store.models import (Category, Author, Publishing, Book, Customer, Balance, Order, Item, Comment, Rate)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublishingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publishing
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balance
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'


