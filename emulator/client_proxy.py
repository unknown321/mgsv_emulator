#!/usr/bin/python3
from mgsv_emulator.emulator.httpclient import HttpClient
from .client_commands import urls
from datetime import datetime
from .logger import Logger

from .client import Client

#def log_event(text, event_type=0):
#	logfile = open('/var/www/mgsv_server/logs/app.log','a')
#	logfile.write('[{}] {}: {}\n'.format(datetime.now(), event_type, text))
#	logfile.close()

class ClientProxy(object):
	"""proxy that takes client requests and sends them to konami servers"""
	def __init__(self, crypto_key=None):
		pass
		# self._client = Client()
		# you will probably need to add session id to make requests after authentication
		# if crypto_key:
		#	self._client.__encoder__.__init_session_blowfish__( bytearray( base64.decodestring(crypto_key.encode()) ) )
		self._logger = Logger()

	def send_full_command(self, command, command_name):
		# just take whole command and send it to konami
		# this exact command will work only for commands before authentication
		# TODO: make a proper version that will figure out if we need to log in on konami servers

		# bad import, move upward
		httpclient = HttpClient()
		r = None
		for url in urls:
			if command_name in urls[url]:
				r = httpclient.send(command, url)
				self._logger.log_event("Proxying command {}, status {}".format(str(command_name), str(r.status_code)))
		if r:
			return r.text
		else:
			return r

	def send_full_command_with_auth(self, command, command_name):
		c = Client()
		c.login()
		command['session_key'] = c.__session_key__
		encrypted_request = c.__encoder__.encode(command)

		httpclient = HttpClient()
		r = None
		for url in urls:
			if command_name in urls[url]:
				r = httpclient.send(encrypted_request, url)
				self._logger.log_event("Proxying command {}, status {}".format(str(command_name), str(r.status_code)))
		if r:
			ans =  c.__response_decode__(r)
			return ans
		else:
			return r

