from channels.routing import route
from .consumers import message_consumer

channel_routing = [
    route("slack.rtm.message", message_consumer)
]