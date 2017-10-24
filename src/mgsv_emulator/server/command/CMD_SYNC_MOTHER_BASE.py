from command.Command import Command

class CMD_SYNC_MOTHER_BASE(Command):

	def execute(self, data):
		return self._receiver.action(data)

