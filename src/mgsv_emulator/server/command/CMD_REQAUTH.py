from command.Command import Command

class CMD_REQAUTH(Command):

	def execute(self, data):
		return self._receiver.action(data)

