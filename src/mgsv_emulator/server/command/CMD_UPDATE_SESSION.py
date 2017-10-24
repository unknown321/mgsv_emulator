from command.Command import Command

class CMD_UPDATE_SESSION(Command):

	def execute(self, data):
		return self._receiver.action(data)

