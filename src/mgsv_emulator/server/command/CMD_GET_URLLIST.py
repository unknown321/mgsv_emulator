from mgsv_emulator.command.Command import Command
from mgsv_emulator.server.entity.Url import Url

class CMD_GET_URLLIST(Command):

    def __init__(self, receiver):
        super(CMD_GET_URLLIST, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = True

    def get_url_list(self):
        url = Url()
        all_urls = url.get_all_urls()
        data = {
            'url_list':all_urls,
            'url_num': len(all_urls)
        }
        return data

    def execute(self, data):
        data = self.get_url_list()
        return self._receiver.action(data, self.__class__.__name__)
