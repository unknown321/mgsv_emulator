#!/usr/bin/python3
import MySQLdb

class Database(object):
    """docstring for Database"""
    def __init__(self):
        pass

    def connect(self):
        self._db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="123",
                     db="mgsv_server")

    def disconnect(self):
        self._db.close()

    def execute_query(self, query, values):
        cur = self._db.cursor()
        cur.execute(query, values)
        self._db.commit()

    def fetch_query(self, query, values, get_dict=False):
        if get_dict:
            cur = self._db.cursor(MySQLdb.cursors.DictCursor)
        else:
            cur = self._db.cursor()
        cur.execute(query, values)
        return cur.fetchall()

    def player_add(self, data, client_ip):
        sql = "insert into players (steam_id, currency, password, smart_device_id, client_ip)\
                values (%s, %s, %s, %s, %s)"
        values =(
                data['account_id'],
                data['currency'],
                data['loginid_password'],
                data['smart_device_id'],
                client_ip
            )
        return self.execute_query(sql, values)

    def player_find_by_steam_id(self, steam_id, get_dict=False):
        sql = 'select * from server_user where steam_id = %s'
        values = (steam_id,)
        result = self.fetch_query(sql, values, get_dict)
        return result

    def player_find_by_session_id(self, session_id, get_dict=False):
        sql = 'select * from server_user where session_id = %s'
        values = (session_id,)
        result = self.fetch_query(sql, values, get_dict)
        if len(result) == 1:
            return result[0]
        else:
            return result
