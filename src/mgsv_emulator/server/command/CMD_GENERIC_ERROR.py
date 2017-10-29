from mgsv_emulator.command.Command import Command

class CMD_GENERIC_ERROR(Command):

    def execute(self, data):
        return self._receiver.action(data, self.__class__.__name__)

