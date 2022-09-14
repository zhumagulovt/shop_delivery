from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
# from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from delivery.consumers import CourierConsumer  # Importing notification Consumer from consumers.py
from .channelsmiddleware import JWTAuthMiddlewareStack

application = ProtocolTypeRouter({ 
    # Websocket chat handler
    'websocket': AllowedHostsOriginValidator(  # Only allow socket connections from the Allowed hosts in the settings.py file
        JWTAuthMiddlewareStack(  # Session Authentication, required to use if we want to access the user details in the consumer 
            URLRouter(
                [
                    path("ws/couriers/", CourierConsumer.as_asgi()),    # Url path for connecting to the websocket to send notifications.
                ]
            )
        ),
    ),
})