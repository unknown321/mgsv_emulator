from invoker.Invoker import Invoker
from receiver.Receiver import Receiver
from comm_parser.CommandParser import CommandParser
from encoder.Encoder import Encoder
from decoder.Decoder import Decoder

class CommandProcessor:
    def __init__(self):
        pass

    def parse_request(self,request):
        pass

    def process(self, request):
        result = request
        decoder = Decoder()
        decoded_request = decoder.decode(result)
        print(decoded_request)

        parser = CommandParser()
        command_name = parser.parse_name(decoded_request)
        command_data = parser.parse_data(decoded_request)
        mod = __import__('server.command.{}'.format(command_name), fromlist=[command_name])
        command = getattr(mod, command_name)
        receiver = Receiver()
        my_command = command(receiver)
        invoker = Invoker()
        invoker.store_command(my_command)
        invoker.store_data(command_data)
        execution_result = invoker.execute_commands()
        # there is only one command per request 
        encoder = Encoder()
        return encoder.encode(execution_result[command_name])
