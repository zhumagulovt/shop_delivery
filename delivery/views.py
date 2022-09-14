from rest_framework.views import APIView
from rest_framework.response import Response

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class TestNotification(APIView):

    def post(self, request):

        channel_layer = get_channel_layer()
        data = request.data 
        # channel_layer.group_channels('couriers')
        async_to_sync(channel_layer.group_send)(
            "couriers",  # Group Name
            {
                "type": "notify",   # Custom Function written in the consumers.py
                "text": data,
            },
        )
        return Response(
            {
                "ok": True
            }
        )


