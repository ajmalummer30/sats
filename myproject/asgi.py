import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django

django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from myproject import routing
from channels.security.websocket import AllowedHostsOriginValidator




application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
    ),
})

