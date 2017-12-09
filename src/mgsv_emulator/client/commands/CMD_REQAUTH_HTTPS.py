def CMD_REQAUTH_HTTPS(self, login, password):
    data = {
        'compress': False,
        'data': {
            'hash': password,        # some magic hash, 16 bytes
            'is_tpp': 1,
            'msgid': 'CMD_REQAUTH_HTTPS',
            'platform': 'Steam',
            'rqid': 0,
            'ugc': 1,
            'user_name': login,        # 768121315156131
            'ver': 'NotImplement'
        }, 
        'original_size': 0,
        'session_crypto': False,
        'session_key': ''
    }
    return data