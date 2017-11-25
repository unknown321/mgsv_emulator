from mgsv_emulator.command.Command import Command

class CMD_GET_SVRLIST(Command):
    def __init__(self, receiver):
        super(CMD_GET_SVRLIST, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False

    def get_svrlist(self):
        # no idea what that server list could be, leave as it is 
        data = {
            'server_num': 0,
            'svrlist': []
        }
        return data

    def execute(self, data):
        data = self.get_svrlist()
        return self._receiver.action(data, self.__class__.__name__)

