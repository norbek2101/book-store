from django.http import Http404

from store.models import (Category, Author, Publishing, Book, Customer, Balance, Order, Item, Comment, Rate)
from store.serializers import (CategorySerializer)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema


class CategoryListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Catgories",
        responses={200: CategorySerializer(many=True)},
        tags=['Category'],
    )
    def get(self):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= CategorySerializer,
        operation_description="Add Single Category",
        responses={201: CategorySerializer()},
        tags=['Category'],
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get single Category",
        responses={200: CategorySerializer()},
        tags=['Category'],
    )
    def get(self, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the category",
        responses={206: CategorySerializer()},
        tags=['Category'],
    )
    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the task",
        responses={204: CategorySerializer()},
        tags=['Category'],
    )
    def delete(self, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)