import json
import logging
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol

log = logging.getLogger(__name__)

class SlackRealTimeMessagingProtocol(WebSocketClientProtocol):
    def onConnect(self, response):
        log.info("rtm connected peer=%s", response.peer)

    def onMessage(self, payload, isBinary):
        message = json.loads(payload.decode('utf-8'))
        log.info("message type=%s", message['type'])
        log.debug("message payload=%s", message)

        # FIXME: should this just be a general "slack.rtm.event" message? 
        # FIXME: do we need reply_channel? We might not.
        self.factory.channel_layer.send("slack.rtm." + message['type'], {
            "slack_token": self.factory.slack_token,
            "event": message
        })

    def onClose(self, wasClean, code, reason):
        log.info("rtm closed reason=%s", reason)

class SlackRealTimeMessagingFactory(WebSocketClientFactory):
    protocol = SlackRealTimeMessagingProtocol

    def __init__(self, *args, **kwargs):
        self.slack_token = kwargs.pop('slack_token')
        self.channel_layer = kwargs.pop('channel_layer')
        super(SlackRealTimeMessagingFactory, self).__init__(*args, **kwargs)