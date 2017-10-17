from command.Command import Command

class CMD_TEST(Command):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    def execute(self, data):
        return self._receiver.action(data)
