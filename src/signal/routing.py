# from channels.staticfiles import StaticFilesConsumer
from signal import consumers
# from django.conf.urls import url
from channels.routing import ProtocolTypeRouter #, URLRouter
# from channels.auth import AuthMiddlewareStack

channel_routing = {
    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.
    # 'http.request': StaticFilesConsumer(),

    # TODO: From the original examples, there is more (https://github.com/jacobian/channels-example/)
    # Wire up websocket channels to our consumers:
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,
}

application = ProtocolTypeRouter({
    """
    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^chat/admin/$", AdminChatConsumer),
            url(r"^chat/$", PublicChatConsumer),
        ])
    ),

    # Using the third-party project frequensgi, which provides an APRS protocol
    'aprs': APRSNewsConsumer,
    """
})