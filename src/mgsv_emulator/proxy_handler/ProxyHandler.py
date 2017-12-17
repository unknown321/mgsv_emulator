import logging
from .. import settings
from ..invoker.Invoker import Invoker
from ..receiver.Receiver import Receiver
logger = logging.getLogger(settings.LOGGER_NAME)


class ProxyHandler(object):
    """
    A class which executes functions before and after proxying the main function
    """
    def __init__(self, command_name, command_data, player=None):
        self._command_name = command_name
        self._command_data = command_data
        self._player = player

    def _get_function(self, ftype):
        result = None
        logger.debug('Looking for command {}'.format(self._command_name))
        try:
            mod = __import__('mgsv_emulator.proxy_handler.command.{}'.format(self._command_name),
                    fromlist=["PROXY_PRE_{}".format(self._command_name)])
        except Exception as e:
            logger.debug('Cannot import module {}: {}'.format(self._command_name, str(e)))
        else:
            try:
                command = getattr(mod, "{}{}".format(ftype, self._command_name))
            except Exception as e:
                logger.debug('Cannot import function {}{}'.format(ftype,self._command_name))
            else:
                if callable(command):
                    result = command
        return result

    def preprocess(self):
        command = self._get_function("PROXY_PRE_")
        command.execute(data=self._command_data)

    def postprocess(self, _data=None):
        command = self._get_function("PROXY_POST_")
        command.execute(data=_data)
