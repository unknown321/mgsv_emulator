from ..encoder.Encoder import Encoder
from ..decoder.Decoder import Decoder
from ..httpclient.HttpClient import HttpClient
from .CommandStore import CommandStore
import base64
import logging
import types

def regular_client(command):
    """
    this is a regular decorator for all functions in CommandStore
    it calls the command, gets the results, encodes them,
    sends encoded data to server, gets results and decodes them
    """
    def wrapper(self, *args):
        print('beforecall')
        r = command(self, *args)
        print('aftercall')
        return r
    return wrapper

def decorate_all_in_module(module, decorator):
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, types.FunctionType):
            setattr(module, name, decorator(obj))

class Client(CommandStore):
    """
    mgsv client
    all commands are stored in CommandStore
    """
    def __init__(self, platform='stm', is_proxy=0):
        decorate_all_in_module(CommandStore, regular_client)
        self._session_key = None
        # self._encoder = Encoder()
        # self._decoder = Decoder()
        self._platform = platform
        # Getting logger will work only when class is imported by the server.
        # When you import client without anything, it will create a new logger
        # instance without any log settings. TODO: fix
        self._logger = logging.getLogger('mgsv')

    def proxy_command(self, data):
        pass

    def login(self, login, password):
        return getattr(self, 'CMD_REQAUTH_HTTPS')(login, password)