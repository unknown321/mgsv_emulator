from mgsv_emulator.command.Command import Command

class CMD_SYNC_RESOURCE(Command):

    def execute(self, data):
        return self._receiver.action(data)

