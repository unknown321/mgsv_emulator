from command.Command import Command

class CMD_GENERIC_ERROR(Command):

    def execute(self, data):
        return self._receiver.action(data)

