from mgsv_emulator.command.Command import Command

class CMD_SEND_IPANDPORT(Command):

    def execute(self, data):
        return self._receiver.action(data)

