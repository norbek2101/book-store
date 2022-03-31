from rest_framework import serializers
from store.models import (Category, Author, Publishing, Book, Customer, Balance, Order, Item, Comment, Rate)

from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
        }

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'about')

    def create(self, validated_data):

        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.save()
        return instance


class PublishingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publishing
        fields = '__all__'

    def create(self, validated_data):
        return Publishing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

  

class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balance
        fields = ('customer', 'amount', 'card_number', 'card_valid_date')

    def create(self, validated_data):
        return Balance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    card_number = serializers.CharField(required=True, write_only=True)
    card_valid_date = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone', 'address', 'created_at', 'updated_at',  'username', 'password', 'password2', 'card_number', 'card_valid_date')


    def to_representation(self, instance):
         data = {}
         data['username'] = instance.user.username
         data['name'] = instance.name
         data['email'] = instance.email
         data['phone'] = instance.phone
         data['address'] = instance.address
         data['created_at'] = instance.created_at
         data['updated_at'] = instance.updated_at
         return data 


    def validate(self, validated_data):
            password = validated_data['password']
            password2 = validated_data['password2']
            if password != password2:
                raise serializers.ValidationError({'password': 'Passwords must match.'})
            return validated_data


    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        card_number = validated_data.pop('card_number')
        card_valid_date = validated_data.pop('card_valid_date')
        user = User.objects.create(username=username, password=password)
        customer = Customer.objects.create(user=user, **validated_data)
        balance = Balance.objects.create(customer = customer, card_number=card_number, card_valid_date=card_valid_date)
        balance.save()
        customer.save()
        return customer


    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields =  '__all__'
        read_only_fields = ['customer']


# class OrderBookSerializer(serializers.Serializer):
#     class Meta:
#         model = Book
#         fields = ('id',)


class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        fields =  ('id','book')
    # depth = 1

    # def to_representation(self, instance):
    #     data = {}
    #     data['id'] = instance.id
    #     data['items'] = instance.items
    #     data['created_at'] = instance.created_at
    #     data['updated_at'] = instance.updated_at
    #     return data


    def create(self, validated_data):
        book = validated_data.pop('book')
        item = Item.objects.create(**validated_data)
        item.book.add(*book)
        item.save()
        return item


 

    


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['customer']
        



class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
