import logging
from .. import settings
from ..invoker.Invoker import Invoker
from ..receiver.Receiver import Receiver
logger = logging.getLogger(settings.LOGGER_NAME)


class ProxyHandler(object):
    def __init__(self, command_name, command_data, player=None):
        self._command_name = command_name
        self._command_data = command_data
        self._player = player

    def preprocess(self):
        logger.info('I am preprocess')
        logger.info('Got a proxyfied preprocess command to handle: {}'.format(self._command_name))
        mod = __import__('mgsv_emulator.proxy_handler.command.{}'.format(self._command_name), fromlist=["PROXY_PRE_{}".format(self._command_name)])
        command = getattr(mod, "PROXY_PRE_{}".format(self._command_name))
        command.execute(data=self._command_data)

    def postprocess(self, _data=None):
        logger.info('I am postprocess')

        logger.info('Got a proxyfied preprocess command to handle: {}'.format(self._command_name))
        mod = __import__('mgsv_emulator.proxy_handler.command.{}'.format(self._command_name), fromlist=["PROXY_POST_{}".format(self._command_name)])
        command = getattr(mod, "PROXY_POST_{}".format(self._command_name))
        command.execute(data=_data)
