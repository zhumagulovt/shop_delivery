from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response

from delivery.services import send_notification_to_courier
from .services import create_order, create_order_items, set_total_price_of_order
from .serializers import OrderSerializer


@api_view(['POST'])
def create_order_view(request):
    
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):

        data = serializer.data

        delivery_time = datetime.strptime(data['delivery_time'], '%H:%M').time()

        order = create_order(
            data['name'], data['phone_number'], data['address'], delivery_time
        )

        order_items = data['items']

        create_order_items(order_items, order)
        
        # Указать цену после добавления всех предметов
        set_total_price_of_order(order)

        message = {
            "name": data['name'],
            "phone_number": data['phone_number'],
            "address": data['address'],
            "delivery_time": data['delivery_time']
        }
        # Отправить уведомление о новом заказе курьеру
        send_notification_to_courier(message)

        return Response("ok")
