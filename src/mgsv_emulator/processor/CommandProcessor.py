from ..invoker.Invoker import Invoker
from ..receiver.Receiver import Receiver
from ..comm_parser.CommandParser import CommandParser
from ..encoder.Encoder import Encoder
from ..decoder.Decoder import Decoder
from ..proxy.Proxy import Proxy
from .. import settings
import importlib

import logging
logger = logging.getLogger('mgsv')


class CommandProcessor:
    def __init__(self):
        pass

    def parse_request(self,request):
        pass

    def process(self, request):
        decoder = Decoder()
        decoded_request = decoder.decode(request)

        logger.debug('Decoded request: {}'.format(decoded_request))

        parser = CommandParser()
        command_name = parser.parse_name(decoded_request)
        command_data = parser.parse_data(decoded_request)
        logger.info('Got a command: {}'.format(command_name))
        if settings.PROXY_ALL or command_name in settings.PROXY_ALWAYS:
            proxy = Proxy()
            result = proxy.send_data(request)
        else:
            mod = __import__('mgsv_emulator.server.command.{}'.format(command_name), fromlist=[command_name])
            command = getattr(mod, command_name)
            receiver = Receiver()
            my_command = command(receiver)
            invoker = Invoker()
            invoker.store_command(my_command)
            invoker.store_data(command_data)
            execution_result = invoker.execute_commands()

            logger.info('Execution result: {}'.format(str(execution_result)))

            # there is only one command per request 
            encoder = Encoder()
            result = encoder.encode(execution_result[command_name])
        return result
