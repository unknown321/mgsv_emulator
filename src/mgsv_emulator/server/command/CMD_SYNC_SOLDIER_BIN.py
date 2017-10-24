from command.Command import Command

class CMD_SYNC_SOLDIER_BIN(Command):

    def execute(self, data):
        return self._receiver.action(data)

