import re
import codecs
import logging

import slackclient

log = logging.getLogger(__name__)
rot13_pattern = re.compile(r'rot13[: ]+?(.*)')

def message_consumer(message):
    log.debug("message: %s", message['event'])
    slack = slackclient.SlackClient(message['slack_token'])
    m = rot13_pattern.match(message["event"]["text"])
    if m:
        rotated = codecs.encode(m.group(1), 'rot13')
        reply = slack.api_call('chat.postMessage', 
            channel = message["event"]["channel"], 
            text = rotated, 
            as_user = True
        )
        if not reply.get('ok'):
            log.error('slack error posting message: %s', reply)