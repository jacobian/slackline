import os
import importlib
import logging
import sys

import click
import slackclient
from autobahn.twisted.websocket import WebSocketClientFactory, connectWS
from twisted.internet import reactor

from .slack_protocol import SlackRealTimeMessagingFactory

@click.command()
@click.option('--log-level', type=click.Choice('critical error warning info debug'.split()), default='info')
@click.option('--token', metavar='SLACK_TOKEN', envvar='SLACK_TOKEN', help='Slack API Token')
@click.argument('channel_layer', required=True)
def cli(log_level, token, channel_layer):
    # Configure logging
    logging.basicConfig(level = getattr(logging, log_level.upper()),
                        format = "%(asctime)-15s %(levelname)-8s %(message)s")

    # load the channel layer - total copypasta from daphne
    sys.path.insert(0, ".")
    module_path, object_path = channel_layer.split(":", 1)
    channel_layer = importlib.import_module(module_path)
    for bit in object_path.split("."):
        channel_layer = getattr(channel_layer, bit)

    # Run the RTM client. This is two steps: we have to call Slack's rtm.start
    # REST API method, which returns a WebSocket URL we can then connect the
    # client to. 
    #
    # FIXME: I don't know what happens if/when this socket gets closed;
    # presumably we'd want to reconnect, but I don't know how/where we'd do
    # that.
    slack_client = slackclient.SlackClient(token)
    reply = slack_client.api_call('rtm.start')
    if not reply.get('ok'):
        click.echo('Error starting RTM connection: {}'.format(reply))
        sys.exit(1)

    factory = SlackRealTimeMessagingFactory(reply['url'], slack_token=token, channel_layer=channel_layer)
    connectWS(factory)
    reactor.run()