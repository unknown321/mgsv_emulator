from mgsv_emulator.command.Command import Command

class CMD_GET_COMBAT_DEPLOY_RESULT(Command):

    def execute(self, data):
        return self._receiver.action(data)

