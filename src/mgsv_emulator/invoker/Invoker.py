class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []
        self._command_data = []

    def store_command(self, command):
        self._commands.append(command)

    def store_data(self, data):
        self._command_data.append(data)

    def execute_commands(self):
        answer = {}
        for num,command in enumerate(self._commands):
            result = command.execute(self._command_data[num])
            answer[command.__class__.__name__] = result
        return answer