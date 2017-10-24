from command.Command import Command

class CMD_SEND_BOOT(Command):

    def execute(self, data):
        return self._receiver.action(data)

