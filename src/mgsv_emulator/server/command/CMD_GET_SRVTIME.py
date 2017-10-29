from mgsv_emulator.command.Command import Command

class CMD_GET_SRVTIME(Command):

    def execute(self, data):
        return self._receiver.action(data)

