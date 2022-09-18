from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('categories/<int:pk>/', views.ProductsByCategoryView.as_view()),
    path('order/', views.create_order_view)
]