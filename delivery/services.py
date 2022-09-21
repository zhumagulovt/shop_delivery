from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_notification_to_courier(data):
    channel_layer = get_channel_layer()
    # data = message 
    # channel_layer.group_channels('couriers')
    async_to_sync(channel_layer.group_send)(
        "couriers",  # Group Name
        {
            "type": "notify",   # Custom Function written in the consumers.py
            "text": data,
        },
    )
