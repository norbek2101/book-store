from django.urls import path
from store.views import (CategoryListView, CategoryDetailView)


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    
]