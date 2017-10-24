from command.Command import Command

class CMD_GET_PLAYER_PLATFORM_LIST(Command):

	def execute(self, data):
		return self._receiver.action(data)

