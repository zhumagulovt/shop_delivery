from channels.generic.websocket import WebsocketConsumer

import json

from asgiref.sync import async_to_sync


class CourierConsumer(WebsocketConsumer):

    def connect(self):
        self.group_name = "couriers" 
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        
        self.accept()

    def disconnect(self, close_code):
        self.close()

    # Функция отправки уведомления
    def notify(self, event):
        self.send(text_data=json.dumps(event["text"]))