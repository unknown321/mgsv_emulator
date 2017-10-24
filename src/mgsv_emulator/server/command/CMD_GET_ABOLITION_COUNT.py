from command.Command import Command

class CMD_GET_ABOLITION_COUNT(Command):

	def execute(self, data):
		return self._receiver.action(data)

