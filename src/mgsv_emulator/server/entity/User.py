from mgsv_emulator.database.Database import Database

class User():
    def __init__(self):

        self._db = Database().connect()
        pass

    def create_server_user():
        query = """INSERT INTO server_user(steam_id, currency, password, smart_device_id,
            magic_hash, crypto_key, last_login, last_command, client_ip, ex_ip, ex_port,
            in_ipm ip_port, nat, xnaddr)
            values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""
        self._db.execute_query(query, values)
        pass

    def find_by_steamid(self, steamid):
        pass

    def find_by_sessionid(self, sessionid):
        pass

    def create(self):
        pass
