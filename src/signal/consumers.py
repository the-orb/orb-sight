
from channels import Group
from channels.sessions import channel_session
# import logging
# import sys
# import json

# https://github.com/Conchylicultor/DeepQA/blob/master/chatbot_website/chatbot_interface/consumer.py

# logger = logging.getLogger(__name__)

def _getClientName(client):
    """ Return the unique id for the client
    Args:
        client list<>: the client which send the message of the from [ip (str), port (int)]
    Return:
        str: the id associated with the client
    """
    return 'room-' + client[0] + '-' + str(client[1])

@channel_session
def ws_connect(message):
    Group('signal').add(message.reply_channel)


@channel_session
def ws_disconnect(message):
    Group('signal').discard(message.reply_channel)


@channel_session
def ws_receive(message):
    Group('signal').add(message.reply_channel)
        