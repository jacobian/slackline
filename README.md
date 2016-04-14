# Slackline - Channels for Slack Bots

Slackline lets you write [Slack Bot Users](https://api.slack.com/bot-users)
using Django and [Channels](http://channels.readthedocs.org/). Specifically,
Slackline speaks Slack's [Real Time Messaging API](https://api.slack.com/rtm),
and pushes those messages onto a channel for your app to consume.

**This is a work in progress, it probably doesn't work very well yet, and is
likely to change substantially before I release it.** If you want to give it
a try anyway, these steps might work:

1. Create a Slack bot user (see https://api.slack.com/bot-users).
2. `python setup.py develop`
3. `pip install channels`
4. `cd example`, then create a `.env` with your Slack bot token and Redis URL.
5. `foreman start`
6. :fingers-crossed: