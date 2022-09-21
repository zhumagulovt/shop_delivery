from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from delivery.consumers import CourierConsumer
from .channelsmiddleware import JWTAuthMiddlewareStack

application = ProtocolTypeRouter({ 
    # Websocket уведомления
    'websocket': AllowedHostsOriginValidator(  # Only allow socket connections from the Allowed hosts in the settings.py file
        JWTAuthMiddlewareStack(  # Кастомная JWT авторизация
            URLRouter(
                [
                    path("ws/couriers/", CourierConsumer.as_asgi()),
                ]
            )
        ),
    ),
})