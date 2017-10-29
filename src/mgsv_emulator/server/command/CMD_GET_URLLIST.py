from mgsv_emulator.command.Command import Command

class CMD_GET_URLLIST(Command):

    def get_url_list(self):
        data = {
            'url_list': [
                {
                    'type': 'GATE',
                    'url': 'https://mgstpp-game.konamionline.com/tppstm/gate',
                    'version': 9
                },
                {
                    'type': 'WEB',
                    'url': 'https://mgstpp-game.konamionline.com/tppstm/main',
                    'version': 9
                },
                {
                    'type': 'EULA',
                    'url': 'http://mgstpp-game.konamionline.com/tppstmweb/eula/eula.var',
                    'version': 3
                },
                {
                    'type': 'HEATMAP',
                    'url': 'http://mgstpp-app.konamionline.com/tppstmweb/heatmap',
                    'version': 0
                },
                {
                    'type': 'DEVICE',
                    'url': 'https://mgstpp-app.konamionline.com/tppstm/main',
                    'version': 0
                }
            ],
            'url_num': 5,
            'xuid': None
       }
        return data

    def execute(self, data):
        data = self.get_url_list()
        return self._receiver.action(data, self.__class__.__name__)

