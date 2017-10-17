from invoker.Invoker import Invoker
from receiver.Receiver import Receiver
from comm_parser.CommandParser import CommandParser


class CommandProcessor:
    def __init__(self):
        pass

    def parse_request(self,request):
        pass

    def process(self, request):
        parser = CommandParser()
        command_name = parser.parse_name(request)
        command_data = parser.parse_data(request)
        mod = __import__('server_commands.{}'.format(command_name), fromlist=[command_name])
        command = getattr(mod, command_name)
        receiver = Receiver()
        my_command = command(receiver)
        invoker = Invoker()
        invoker.store_command(my_command)
        invoker.store_data(command_data)
        return invoker.execute_commands()
