from .encoder import Encoder
from .decoder import Decoder
from .server_commands import urls
from .httpclient import HttpClient
from datetime import datetime
from . import settings
from .server_handler import ServerHandler
import base64
from database import Database
from .logger import Logger

class Server(object):
	"""mgsv server"""
	def __init__(self):
		super(Server, self).__init__()
		self._session_key__ = None
		self._encoder = Encoder()
		self._decoder = Decoder()
		self._logger = Logger()

	def process_request(self, httpMsg, client_ip):
		try:
			request = self._decoder.decode(str(httpMsg))
		except Exception as e:
			# log_event(str(e))
			raise e
		else:
			# if session_key is present, then this is an post-auth encrypted session
			# it already uses enc keys, so we need to pull them from db and re-initialize encoder and decoder
			session_key = request['session_key']
			player = None
			if request['session_crypto']:
				db = Database()
				db.connect()
				player = db.player_find_by_session_id(session_key, get_dict=True)
				if not isinstance(player, dict):
					# not a dict, list or None
					self._logger.log_event('Found {} players with session_key {}'.format(len(player), session_key))
					raise ValueError

				self._encoder.__init_session_blowfish__(player['crypto_key'])
				self._decoder.__init_session_blowfish__(player['crypto_key'])
				request = self._decoder.decode(str(httpMsg))

			msgid = request['data']['msgid']
			#self._logger.log_event('New message arrived: {}'.format(msgid))

			handler = ServerHandler(player=player)
			if msgid != 'CMD_AUTH_STEAMTICKET':
				command = handler.process_message(request, client_ip)
			else:
				command = handler.process_message(request, client_ip, httpMsg)
			self._logger.log_event('Returning {}'.format(msgid))
		response = self._encoder.encode(command)
		# debug, remove
#		if msgid == 'CMD_SNEAK_MOTHER_BASE':
#			self._logger.log_event(response)
		return response


	# def __log__(self, data):
	# 	f = open(settings.LOG_PATH,'a')
	# 	f.write(settings.LOG_FORMAT.format(curdate=str(datetime.now()), data=str(data)))
	# 	f.close()




	# def __response_decode__(self, response):
	# 	text = response.text.replace('\r\n','')
	# 	text = self.__decoder__.decode(text)
	# 	return text

	# def __response_get_keys__(self, text):
	# 	if not self.__session_key__:
	# 		if 'session' in text['data']:
	# 			self.__session_key__ = text['data']['session']
	# 	if not self.__encoder__.__session_blowfish__:
	# 		if 'crypto_key' in text['data']:
	# 			self.__encoder__.__init_session_blowfish__( bytearray( base64.decodestring(text['data']['crypto_key'].encode() ) ) )

	# def send_command(self, command):
	# 	httpclient = HttpClient()
	# 	comm = self.__command_get__(command)
	# 	self.__append_session_key__(comm)
	# 	encrypted_request = self.__encoder__.encode(comm)
	# 	for url in urls:
	# 		if command in urls[url]:
	# 			#print(command, url)
	# 			r = httpclient.send(encrypted_request, url)
	# 			return self.__parse_response__(r)



	# def __parse_response__(self, r):
	# 	if r.status_code != 200:
	# 		print(r.status_code, r.text)
	# 		return {}
	# 	text = self.__response_decode__(r)
	# 	if text['data']['result'] != 'NOERR':
	# 		self.__log__([r.url, text])
	# 	self.__response_get_keys__(text)
	# 	return text


