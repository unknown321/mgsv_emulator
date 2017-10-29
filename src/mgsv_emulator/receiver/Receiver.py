class Receiver:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """

    def action(self, data, msgid, is_encrypted=False):
        response = {
            'compress': True,
            'data': {
                    'crypto_type': 'COMMON',
                    'flowid': None,
                    'msgid': msgid,
                    'result': 'NOERR',
                    'rqid': 0,
            },
            'original_size': 0,
            'session_crypto': is_encrypted,
            'session_key': None
        }
        for key in data:
            response['data'][key] = data[key]
#        if is_encrypted:
#            response['session_key'] = get_session_key??
        # add default headers to the response body
        # check for authorization?
        return response
