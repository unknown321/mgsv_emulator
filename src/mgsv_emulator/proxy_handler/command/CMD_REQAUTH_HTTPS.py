import logging
from mgsv_emulator.database.Database import Database
from mgsv_emulator.server.entity.User import User
from mgsv_emulator import settings
logger = logging.getLogger(settings.LOGGER_NAME)

class PROXY_PRE_CMD_REQAUTH_HTTPS():
    def __init__():
        pass
    def execute(data):
        pass

class PROXY_POST_CMD_REQAUTH_HTTPS():
    def __init__():
        pass
    def execute(data, request_data):
        d = data['data']
        r = request_data
        db = Database()
        db.connect()
        player = db.player_find_by_steam_id(r['user_name'],True)
        if len(player) !=1:
            log.error('Found {} players with steamid {}'.format(len(player), r['user_name']))
            return
        else:
            player = player[0]
        if player['magic_hash']:
            pass
        else:
            if d['result'] == 'NOERR':
                # auth backend said that hash-steamid pair was ok
                query = 'UPDATE server_user SET magic_hash=%s WHERE steam_id=%s'
                values = (r['hash'], r['user_name'])
                db.execute_query(query, values)
