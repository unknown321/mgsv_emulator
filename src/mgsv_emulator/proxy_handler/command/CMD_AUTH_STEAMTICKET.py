import logging
from mgsv_emulator import settings
from mgsv_emulator.server.entity.User import User
from mgsv_emulator.database.Database import Database
logger = logging.getLogger(settings.LOGGER_NAME)

class PROXY_PRE_CMD_AUTH_STEAMTICKET():
    def __init__():
        pass
    def execute(data):
        pass

class PROXY_POST_CMD_AUTH_STEAMTICKET():
    def __init__():
        pass
    def execute(data, request_data):
        d  = data['data']
        r = request_data
        db = Database()
        db.connect()
        player = db.player_find_by_steam_id(d['account_id'],True)
        if not player:
            query = """INSERT INTO server_user(steam_id, currency, password,
                smart_device_id, country, lang, region)
                VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            values = (d['account_id'],
                      d['currency'],
                      d['loginid_password'],
                      d['smart_device_id'],
                      r['country'],
                      r['lang'],
                      r['region'])
            db.execute_query(query, values)
