from command.Command import Command

class CMD_SET_CURRENTPLAYER(Command):

    def execute(self, data):
        return self._receiver.action(data)

