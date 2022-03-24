from django.urls import path
from store.views import (CategoryListView, CategoryDetailView, AuthorListView, AuthorDetailView, 
                            PublishingListView, PublishingDetailView, BookListView, BookDetailView,
                            CustomerListView, CustomerDetailView, BalanceListView, BalanceDetailView,  
                            OrderListView, OrderDetailView, ItemListView, ItemDetailView,
                            CommentListView, CommentDetailView, RateListView, RateDetailView
)    
                        


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    path('publishing/', PublishingListView.as_view()),
    path('publishing/<int:pk>/', PublishingDetailView.as_view(), name='publishing-detail'),

    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('customer/', CustomerListView.as_view()),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    path('balance/', BalanceListView.as_view()),
    path('balance/<int:pk>/', BalanceDetailView.as_view(), name='balance-detail'),

    path('order/', OrderListView.as_view(), ),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('item/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),

    path('comment/', CommentListView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    path('rate/', RateListView.as_view()),
    path('rate/<int:pk>/', RateDetailView.as_view(), name='rate-detail'),
    
]