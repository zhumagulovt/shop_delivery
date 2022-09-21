from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    # pagination_class = CustomPagination
    serializer_class = CategorySerializer


class ProductsByCategoryView(ListAPIView):
    # pagination_class = CustomPagination
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        queryset = Product.objects.filter(category_id=category_id).select_related('category')
        return queryset
