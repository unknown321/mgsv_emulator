from .encoder import Encoder
from .decoder import Decoder
import base64
from .client_commands import client_commands, urls
from .httpclient import HttpClient
from datetime import datetime
from . import settings
from copy import deepcopy
from .logger import Logger

class Client(object):
	"""mgsv client"""
	def __init__(self, platform='stm'):
		super(Client, self).__init__()
		self.__session_key__ = None
		self.__encoder__ = Encoder()
		self.__decoder__ = Decoder()
		self.__platform__ = platform
		self._logger = Logger()

	def __command_get__(self, name):
		return deepcopy(client_commands[name])

	def __append_session_key__(self, command):
		if command['session_key'] == -1:
			# session key is required for command
			if self.__session_key__:
				command['session_key'] = self.__session_key__
			else:
				raise Exception('Session key is required for this command, but no key provided')

	def __response_decode__(self, response):
		text = response.text.replace('\r\n','')
		text = self.__decoder__.decode(text)
		return text

	def __response_get_keys__(self, text):
		if not self.__session_key__:
			if 'session' in text['data']:
				self.__session_key__ = text['data']['session']
		if not self.__encoder__.__session_blowfish__:
			if 'crypto_key' in text['data']:
				self.__encoder__.__init_session_blowfish__( bytearray( base64.decodestring(text['data']['crypto_key'].encode() ) ) )

	def __append_command_options__(self, command, options):
		# TODO: make a proper update function
		# this will overwrite any values in data section, incuding dicts which is really bad
		# https://stackoverflow.com/a/3233356/1938027
		self._logger.log_event('Applying user-supplied options to command {}:\n{}'.format(str(command['data']['msgid']), str(options)))
		for key in options:
			if key in command['data']:
				self._logger.log_event('Overwriting key {} in command {}'.format(str(key), str(command['data']['msgid'])))
				command['data'][key] = options[key]
		self._logger.log_event('Applied options to command {}: {}'.format(str(command['data']['msgid']), str(command)))

	def send_command(self, command, options=None):
		httpclient = HttpClient()
		comm = self.__command_get__(command)
		self.__append_session_key__(comm)
		if options:
			self.__append_command_options__(comm, options)
		encrypted_request = self.__encoder__.encode(comm)
		for url in urls:
			if 'tpp'+self.__platform__ in url:
				if command in urls[url]:
					self._logger.log_event("Sending client command {}: {}". format(command, str(comm)))
					r = httpclient.send(encrypted_request, url)
					return self.__parse_response__(r)

	def __parse_response__(self, r):
		if r.status_code != 200:
			print(r.status_code, r.text)
			return {}
		text = self.__response_decode__(r)
		if text['data']['result'] != 'NOERR':
			self._logger.log_event("{} {}".format(r.url,text))
		self.__response_get_keys__(text)
		return text


	def login(self, steam_id=None, magic_hash=None):
		responses = []
		commands = [
			'CMD_GET_URLLIST',
			'CMD_GET_SVRLIST',
			# 'CMD_AUTH_STEAMTICKET',		# you will need to set up ticket and its size; tickets also expire
			'CMD_GET_SVRTIME',
		]

		if self.__platform__ == 'ps3':
			commands.append('CMD_REQAUTH_HTTPS_PS3')
		elif self.__platform__ == 'stm':
			commands.append('CMD_REQAUTH_HTTPS')

		for i in commands:
			if i == 'CMD_REQAUTH_HTTPS' and steam_id and magic_hash:
				options = {"user_name": steam_id, "hash": magic_hash}
				response = self.send_command(i, options)
			else:
				response = self.send_command(i)
			responses.append(response)
		return responses


	def get_nuclear(self):
		comm = 'CMD_GET_ABOLITION_COUNT'
		return [self.send_command(comm)]

	def get_login_data(self):
		comm = 'CMD_GET_LOGIN_PARAM'
		return [self.send_command(comm)]

	def get_info_list(self):
		comm = 'CMD_GET_INFORMATIONLIST'
		return [self.send_command(comm)]
