from command.Command import Command

class CMD_GET_SERVER_ITEM(Command):

    def execute(self, data):
        return self._receiver.action(data)

