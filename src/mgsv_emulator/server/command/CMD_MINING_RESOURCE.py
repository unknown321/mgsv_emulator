from command.Command import Command

class CMD_MINING_RESOURCE(Command):

	def execute(self, data):
		return self._receiver.action(data)

