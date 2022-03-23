from django.urls import path
from store.views import (CategoryListView, CategoryDetailView, AuthorListView, AuthorDetailView, 
                            PublishingListView, PublishingDetailView, BookListView, BookDetailView,
                            CustomerListView, CustomerDetailView, BalanceListView, BalanceDetailView,  
                            OrderListView, OrderDetailView, ItemListView, ItemDetailView,
                            CommentListView, CommentDetailView, RateListView, RateDetailView
                        )    
                        


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),

    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view()),

    path('publishing/', PublishingListView.as_view()),
    path('publishing/<int:pk>/', PublishingDetailView.as_view()),

    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view()),

    path('customer/', CustomerListView.as_view()),
    path('customer/<int:pk>/', CustomerDetailView.as_view()),

    path('balance/', BalanceListView.as_view()),
    path('balance/<int:pk>/', BookDetailView.as_view()),

    path('order/', OrderListView.as_view()),
    path('order/<int:pk>/', OrderDetailView.as_view()),

    path('item/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),

    path('comment/', CommentListView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),

    path('rate/', RateListView.as_view()),
    path('rate/<int:pk>/', RateDetailView.as_view()),
    
]