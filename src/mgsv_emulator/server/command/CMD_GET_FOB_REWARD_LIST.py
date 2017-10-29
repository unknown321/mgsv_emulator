from mgsv_emulator.command.Command import Command

class CMD_GET_FOB_REWARD_LIST(Command):

    def execute(self, data):
        return self._receiver.action(data)

