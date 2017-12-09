from mgsv_emulator.command.Command import Command

class CMD_AUTH_STEAMTICKET(Command):

    def __init__(self, receiver):
        super(CMD_AUTH_STEAMTICKET, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False

    def get_account(self, data):
        data = {
            "account_id": 123,  # steamid
            "currency": "USD", 
            "loginid_password": "00000000000000000000000000000000",
            "smart_device_id": "fgsfds" #base64encoded string
        }
        # we need to proxy client request to konami server
        # or implement our own auth service based on client ip
        pass

    def execute(self, data):
        p = Proxy()

        data = self.get_account()
        return self._receiver.action(data, self.__class__.__name__)

