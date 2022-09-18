from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product, Order, OrderItem
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


@api_view(['POST'])
def create_order_view(request):
    data = request.data

    order = Order.objects.create(
        name=data['name'],
        phone_number=data['phone_number'],
        address=data['address']
    )

    order_items = data['order_items']

    for order_item in order_items:
        OrderItem.objects.create(
            order=order,
            product_id=order_item['product_id'],
            quantity=order_item['quantity']
        )
    
    print(data)
    return Response("ok")
