from command.Command import Command

class CMD_GET_DAILY_REWARD(Command):

	def execute(self, data):
		return self._receiver.action(data)

