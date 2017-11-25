from mgsv_emulator.database import Database

class Url():
    def __init__(self):
        self._database = Database()
        self._database.connect()

    def get_url(self, url_type):
        full_url = None
        sql = 'SELECT value from settings where name="base_url"'
        base_url = self._database.fetch_query(sql, (), get_dict=True)[0]['value']
        sql = 'SELECT url_link from url where url_type = %s'
        values = (url_type,)
        result = self._database.fetch_query(sql, values, get_dict=True)
        if len(result) == 1:
            full_url = base_url + result[0]['url_link']
        return full_url

    def get_url_version(self, url_type):
        version = 0
        sql = 'SELECT url_version from url where url_type = %s'
        values = (url_type,)
        result = self._database.fetch_query(sql, values, get_dict=True)
        if len(result) == 1:
            version = result[0]['url_version']
        return version


    def get_all_urls(self):
        all_urls = ()
        sql = 'SELECT url_link, url_type, url_version from url'
        values = ()
        result = self._database.fetch_query(sql, values, get_dict=True)
        if len(result) > 0:
            all_urls = result
        return all_urls
