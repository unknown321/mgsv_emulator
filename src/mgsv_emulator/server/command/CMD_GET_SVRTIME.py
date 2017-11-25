from mgsv_emulator.command.Command import Command
import time

class CMD_GET_SVRTIME(Command):

    def __init__(self, receiver):
        super(CMD_GET_SVRTIME, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False

    def get_time(self):
        data = {
            "date": int(time.time())
        }
        return data

    def execute(self, data):
        data = self.get_time()
        return self._receiver.action(data, self.__class__.__name__)
