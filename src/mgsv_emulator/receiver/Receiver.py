class Receiver:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """
    def __init__(self):
        # most of the commands are encrypted (use a session key to encrypt data)
        # override those in command definition
        self.encrypt = True
        self.compress = True

    def action(self, data, msgid):
        response = {
            'compress': self.compress,
            'data': {
                    'crypto_type': 'COMMON',
                    'flowid': None,
                    'msgid': msgid,
                    'result': 'NOERR',
                    'rqid': 0,
                    'xuid': 0,
            },
            'original_size': 0,
            'session_crypto': self.encrypt,
            'session_key': None
        }
        for key in data:
            response['data'][key] = data[key]
#        if self.encrypt:
#            response['session_key'] = get_session_key??
        # add default headers to the response body
        # check for authorization?
        return response
