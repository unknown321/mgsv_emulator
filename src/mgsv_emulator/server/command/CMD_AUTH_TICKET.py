from mgsv_emulator.command.Command import Command

class CMD_AUTH_TICKET(Command):

    def execute(self, data):
        return self._receiver.action(data)

