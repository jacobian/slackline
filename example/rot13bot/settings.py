import os

SECRET_KEY = "it's a secret to everyone"

INSTALLED_APPS = ['channels']

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {"hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')]},
        "ROUTING": "rot13bot.routing.channel_routing",
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        },
        'rot13bot': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}