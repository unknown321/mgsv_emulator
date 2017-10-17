#!/usr/bin/python3
from mgsv_emulator.emulator.httpclient import HttpClient
from .client_commands import urls as server_urls
from datetime import datetime
from database import Database
from .logger import Logger

from .client import Client

#def log_event(text, event_type=0):
#	logfile = open('/var/www/mgsv_server/logs/app.log','a')
#	logfile.write('[{}] {}: {}\n'.format(datetime.now(), event_type, text))
#	logfile.close()

class ClientProxy(object):
	"""proxy that takes client requests and sends them to konami servers"""
	def __init__(self, crypto_key=None):
		self._client = Client()
		if crypto_key:
			self._client.__encoder__.__init_session_blowfish__( bytearray( base64.decodestring(crypto_key.encode()) ) )
		self._logger = Logger()
		self._db = Database()
		self._db.connect()


	def send_full_command(self, command, command_name):
		# just take whole command and send it to konami
		# this exact command will work only for CMDs before authentication
		httpclient = HttpClient()
		response = None
		command_found = False
		for url in server_urls:
			if command_name in server_urls[url]:
				command_found = True
				response = httpclient.send(command, url)
				self._logger.log_event("Proxying command {}, url {}, status {}".format(str(command_name), str(url), str(response.status_code)))
		else:
			if not command_found:
				self._logger.log_event("Proxifying command {} failed, command not found in client_commands!".format(str(command_name)))
		if response:
			return response.text
		else:
			return response

	def send_full_command_with_auth(self, command, command_name):
		self._logger.log_event("Got a command for proxying: {}".format(str(command)))
		orig_session_key = command['session_key']

		player = self._db.player_find_by_session_id(orig_session_key, True)
		response = None
		if player:
			self._client.login(steam_id = player['steam_id'], magic_hash=player['magic_hash'])
			command['session_key'] = self._client.__session_key__
			response = self._client.send_command(command_name, options = command['data'])
			self._logger.log_event("Proxying command {},  response:\n {}".format(str(command_name), str(response)))
			response['session_key'] = orig_session_key
		else:
			self._logger.log_event("Cannot find player during proxy procedure")
		return response
