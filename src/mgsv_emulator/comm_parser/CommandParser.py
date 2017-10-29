class CommandParser:
    def parse_name(self, request):
        return request['data']['msgid']
    def parse_data(self, request):
        return request['data']
