from datetime import datetime

from flask import request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage

from constants.linebot_const import LinebotConst
from handlers.console import Console


class LinebotService:

    _VALID_MESSAGE_TYPES = {
        LinebotConst.MessageType.TEXT,
    }

    def __init__(self, access_token, secret):
        self.linebot = LineBotApi(access_token)
        self.handler = WebhookHandler(secret)

    def _reply(self, token, text):
        message = TextSendMessage(text)
        self.linebot.reply_message(token, message)

    def _extract_data(self, body):
        events = body.get('events')
        if not events:
            Console.log('events is not exist or empty', level=Console.Level.ERROR)
            return None

        event = events.pop()
        token = event.get('replyToken')
        if not token:
            Console.log('reply token not found', level=Console.Level.ERROR)
            return None

        delivery = event.get('deliveryContext')
        is_redelivery = delivery.get('isRedelivery') if delivery else None
        result = {
            'token': token,
            'message': event.get('message'),
            'timestamp': event.get('timestamp'),
            'is_redelivery': is_redelivery,
        }
        return result

    def _exec(self, text, create_at):
        """ Do your business here """
        if text.lower() == 'hello':
            return 'World!'
        return f'[=ERROR=] Unknown message: "{text}"'

    def prompt(self):
        body = request.get_json(force=True)
        data = self._extract_data(body)
        if not data:
            return None

        token = data['token']
        message = data['message']

        type_ = message['type']
        if type_ not in self._VALID_MESSAGE_TYPES:
            """ 略過未支援的訊息類型 """
            text = f'[=ERROR=] Invalid Message Type: {type_}'
        elif type_ == LinebotConst.MessageType.TEXT:
            """ 處理文字訊息 """
            create_at = datetime.fromtimestamp(data['timestamp'] / 1000)
            text = self._exec(message['text'], create_at)
        self._reply(token, text)
