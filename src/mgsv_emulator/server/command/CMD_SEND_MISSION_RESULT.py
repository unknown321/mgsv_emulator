from command.Command import Command

class CMD_SEND_MISSION_RESULT(Command):

	def execute(self, data):
		return self._receiver.action(data)

