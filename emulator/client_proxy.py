#!/usr/bin/python3
from mgsv_emulator.emulator.httpclient import HttpClient
from .client_commands import urls
from datetime import datetime

def log_event(text, event_type=0):
	logfile = open('/var/www/mgsv_server/logs/app.log','a')
	logfile.write('[{}] {}: {}\n'.format(datetime.now(), event_type, text))
	logfile.close()

class ClientProxy(object):
	"""proxy that takes client requests and sends them to konami servers"""
	def __init__(self, crypto_key=None):
		pass
		# self._client = Client()
		# you will probably need to add session id to make requests after authentication
		# if crypto_key:
		#	self._client.__encoder__.__init_session_blowfish__( bytearray( base64.decodestring(crypto_key.encode()) ) )

	def send_full_command(self, command, command_name):
		# just take whole command and send it to konami

		# bad import, move upward
		httpclient = HttpClient()
		r = None
		for url in urls:
			if command_name in urls[url]:
				r = httpclient.send(command, url)
				log_event(str(r.status_code) + '\n' + str(command) + '\n' + str(url))
		if r:
			return r.text
		else:
			return r