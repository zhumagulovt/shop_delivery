from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer
from .services import create_order, create_order_items, set_total_price_of_order


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


@api_view(['POST'])
def create_order_view(request):
    data = request.data
    
    delivery_time = datetime.strptime(data['delivery_time'], '%H:%M').time()

    order = create_order(
        data['name'], data['phone_number'], data['address'], delivery_time
    )

    order_items = data['order_items']

    create_order_items(order_items, order)
    
    # Указать цену после добавления всех предметов
    set_total_price_of_order(order)

    return Response("ok")
