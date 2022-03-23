from django.http import Http404

from store.models import (Category, Author, Publishing, Book, Customer, Balance, Order, Item, Comment, Rate)
from store.serializers import (CategorySerializer, AuthorSerializer, PublishingSerializer, BookSerializer, 
                                CustomerSerializer, BalanceSerializer, OrderSerializer, ItemSerializer, 
                                CommentSerializer, RateSerializer
                            )
                            
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
        operation_description="Add a Category",
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
        operation_description="Get a Category",
        responses={200: CategorySerializer()},
        tags=['Category'],
    )
    def get(self, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Category",
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
        operation_description="Delete the Category",
        responses={204: CategorySerializer()},
        tags=['Category'],
    )
    def delete(self, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Authors",
        responses={200: AuthorSerializer(many=True)},
        tags=['Author'],
    )
    def get(self):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= AuthorSerializer,
        operation_description="Add an Author",
        responses={201: AuthorSerializer()},
        tags=['Author'],
    )
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get an Author",
        responses={200: AuthorSerializer()},
        tags=['Author'],
    )
    def get(self, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Author",
        responses={206: AuthorSerializer()},
        tags=['Author'],
    )
    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Author",
        responses={204: AuthorSerializer()},
        tags=['Author'],
    )
    def delete(self, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublishingListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Publishings",
        responses={200: PublishingSerializer(many=True)},
        tags=['Publishing'],
    )
    def get(self):
        publishing = Publishing.objects.all()
        serializer = PublishingSerializer(publishing, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= PublishingSerializer,
        operation_description="Add a Publishing",
        responses={201: PublishingSerializer()},
        tags=['Publishing'],
    )
    def post(self, request):
        serializer = PublishingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublishingDetailView(APIView):

    def get_object(self, pk):
        try:
            return Publishing.objects.get(pk=pk)
        except Publishing.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Publishing",
        responses={200: PublishingSerializer()},
        tags=['Publishing'],
    )
    def get(self, pk):
        publishing = self.get_object(pk)
        serializer = PublishingSerializer(publishing)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Publishing",
        responses={206: PublishingSerializer()},
        tags=['Publishing'],
    )
    def put(self, request, pk):
        publishing = self.get_object(pk)
        serializer = PublishingSerializer(publishing, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Publishing",
        responses={204: PublishingSerializer()},
        tags=['Publishing'],
    )
    def delete(self, pk):
        publishing = self.get_object(pk)
        publishing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class BookListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Books",
        responses={200: BookSerializer(many=True)},
        tags=['Book'],
    )
    def get(self):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= BookSerializer,
        operation_description="Add a Book",
        responses={201: BookSerializer()},
        tags=['Book'],
    )
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Book",
        responses={200: BookSerializer()},
        tags=['Book'],
    )
    def get(self, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the book",
        responses={206: BookSerializer()},
        tags=['Book'],
    )
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Book",
        responses={204: BookSerializer()},
        tags=['Book'],
    )
    def delete(self, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class CustomerListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Customers",
        responses={200: CustomerSerializer(many=True)},
        tags=['Customer'],
    )
    def get(self):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= CustomerSerializer,
        operation_description="Add a Customer",
        responses={201: CustomerSerializer()},
        tags=['Customer'],
    )
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Customer",
        responses={200: CustomerSerializer()},
        tags=['Customer'],
    )
    def get(self, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Customer",
        responses={206: CustomerSerializer()},
        tags=['Customer'],
    )
    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Customer",
        responses={204: CustomerSerializer()},
        tags=['Customer'],
    )
    def delete(self, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BalanceListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Balances",
        responses={200: BalanceSerializer(many=True)},
        tags=['Balance'],
    )
    def get(self):
        balance = Balance.objects.all()
        serializer = BalanceSerializer(balance, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= BalanceSerializer,
        operation_description="Add a Balance",
        responses={201: BalanceSerializer()},
        tags=['Balance'],
    )
    def post(self, request):
        serializer = BalanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BalanceDetailView(APIView):

    def get_object(self, pk):
        try:
            return Balance.objects.get(pk=pk)
        except Balance.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Balance",
        responses={200: BalanceSerializer()},
        tags=['Balance'],
    )
    def get(self, pk):
        balance = self.get_object(pk)
        serializer = BalanceSerializer(balance)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Balance",
        responses={206: BalanceSerializer()},
        tags=['Balance'],
    )
    def put(self, request, pk):
        balance = self.get_object(pk)
        serializer = BalanceSerializer(balance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Balance",
        responses={204: BalanceSerializer()},
        tags=['Balance'],
    )
    def delete(self, pk):
        balance = self.get_object(pk)
        balance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     


class OrderListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Orders",
        responses={200: CustomerSerializer(many=True)},
        tags=['Order'],
    )
    def get(self):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= OrderSerializer,
        operation_description="Add a Order",
        responses={201: OrderSerializer()},
        tags=['Order'],
    )
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Order",
        responses={200: OrderSerializer()},
        tags=['Order'],
    )
    def get(self, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Order",
        responses={206: OrderSerializer()},
        tags=['Order'],
    )
    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Order",
        responses={204: OrderSerializer()},
        tags=['Order'],
    )
    def delete(self, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


class ItemListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Items",
        responses={200: ItemSerializer(many=True)},
        tags=['Item'],
    )
    def get(self):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= ItemSerializer,
        operation_description="Add a Item",
        responses={201: ItemSerializer()},
        tags=['Item'],
    )
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(APIView):

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Item",
        responses={200: ItemSerializer()},
        tags=['Item'],
    )
    def get(self, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Item",
        responses={206: ItemSerializer()},
        tags=['Item'],
    )
    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Item",
        responses={204: ItemSerializer()},
        tags=['Item'],
    )
    def delete(self, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


class CommentListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Comments",
        responses={200: CommentSerializer(many=True)},
        tags=['Comment'],
    )
    def get(self):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= CommentSerializer,
        operation_description="Add a Comment",
        responses={201: CommentSerializer()},
        tags=['Comment'],
    )
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Comment",
        responses={200: CommentSerializer()},
        tags=['Comment'],
    )
    def get(self, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Comment",
        responses={206: CommentSerializer()},
        tags=['Comment'],
    )
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Comment",
        responses={204: CommentSerializer()},
        tags=['Comment'],
    )
    def delete(self, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


class RateListView(APIView):

    @swagger_auto_schema(
        operation_description="List of Rates",
        responses={200: RateSerializer(many=True)},
        tags=['Rate'],
    )
    def get(self):
        rate = Rate.objects.all()
        serializer = RateSerializer(rate, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body= RateSerializer,
        operation_description="Add a Rate",
        responses={201: RateSerializer()},
        tags=['Rate'],
    )
    def post(self, request):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RateDetailView(APIView):

    def get_object(self, pk):
        try:
            return Rate.objects.get(pk=pk)
        except Rate.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get a Rate",
        responses={200: RateSerializer()},
        tags=['Rate'],
    )
    def get(self, pk):
        rate = self.get_object(pk)
        serializer = RateSerializer(rate)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update the Rate",
        responses={206: RateSerializer()},
        tags=['Item'],
    )
    def put(self, request, pk):
        rate = self.get_object(pk)
        serializer = RateSerializer(rate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete the Rate",
        responses={204: RateSerializer()},
        tags=['Rate'],
    )
    def delete(self, pk):
        rate = self.get_object(pk)
        rate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

