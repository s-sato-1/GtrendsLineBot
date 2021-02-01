from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate


class APIClient(LineBotApi):
    def default_sender(self, msg):
        """
        """
        self.broadcast(TextSendMessage(text=msg))
