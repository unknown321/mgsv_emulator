from command.Command import Command

class CMD_SALE_RESOURCE(Command):

	def execute(self, data):
		return self._receiver.action(data)

