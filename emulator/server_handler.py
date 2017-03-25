#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.dirname(__file__))
# how is this import possible, database is 2 levels higher
from database import Database
from datetime import datetime
import time
import copy
from .server_commands import server_commands
from .logger import Logger



class ServerHandler(object):
	"""class that processes requests and composes answers
	however, last changes to command are made by encoder:
	original size is calculated after session encoding"""
	def __init__(self):
		self._handlers = {
			"CMD_AUTH_STEAMTICKET": self.cmd_auth_ticket,
			"CMD_REQAUTH_HTTPS": self.cmd_reqauth,
			"CMD_GET_URLLIST": self.cmd_get_urllist,
			"CMD_GET_SVRLIST": self.cmd_get_srvlist,
			"CMD_GET_SVRTIME": self.cmd_get_srvtime,
		}
		self._db = Database()
		self._db.connect()
		# not sure if calls to logger will work without <self>
		logger = Logger()

	def _command_get(self, name):
		return server_commands[name]

	def process_message(self, client_request, client_ip, httpMsg=None):
		msgid = client_request['data']['msgid']
		if msgid == 'CMD_AUTH_STEAMTICKET':
			# authenticating user, need to save ip
			# httpMsg is encoded version of CMD_AUTH_STEAMTICKET
			command = self._handlers[msgid](httpMsg, client_ip)
		else:
			# every other command, process as usual
			if client_request['session_key']:
				player = self._db.player_find_by_session_id(client_request['session_key'])
				if len(player) == 1:
					command = self._handlers[msgid](client_request)
				else:
					command = self.get_error()

		if isinstance(command, dict):
			if 'session_key' in command:
				if command['session_key'] == -1 and client_request['session_key']:
					command['session_key'] = client_request['session_key']
		return command

	def _session_exists(self, session_id):
		if session_id:
			self._db.user_find_by_session_id(session_id)
		else:
			pass


	def _append_session_key(self, command):
		# session key is required for command
		# db.get_session_key
		if self.__session_key__:
			command['session_key'] = 'fgsfds'
		else:
			raise Exception('Session key is required for this command, but no key provided')

	def get_error(self):
		# TODO: find all ERR_ codes and use them
		return 1

	# BAD
	# def _append_date(self, command):
	# 	unix_time = int(time.time())
	# 	if command['data']['msgid'] == 'CMD_GET_SVRTIME':
	# 		command['data']['date'] = unix_time

	# 	if command['data']['msgid'] == 'CMD_GET_ABOLITION_COUNT':
	# 		command['data']['info']['date'] = unix_time

	# 	if command['data']['msgid'] == 'CMD_GET_INFORMATIONLIST':
	# 		for i in command['data']['info_list']:
	# 			i['date'] = unix_time
	# 		command['data']['info_num'] = len(command['data']['info_list'])

	def _generate_crypto_key(self):
		return 'AAAAAAAAAAAAAAAAAAAAAA=='

	def _generare_session_id(self):
		return 'fgsfds'


#======CMD_GET_URLLIST
	def cmd_get_urllist(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_SVRLIST
	def cmd_get_srvlist(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_SVRTIME
	def cmd_get_srvtime(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['data']['date'] = int(time.time())
		return command

#======CMD_AUTH_STEAMTICKET
	def cmd_auth_ticket(self, client_request, client_ip):
		# initial auth, just send ticket to konami to get steam_id back
		from .client_proxy import ClientProxy
		proxy = ClientProxy()
		proxied_response = proxy.send_full_command(client_request, 'CMD_AUTH_STEAMTICKET')
		if proxied_response:
			# auth_steamticket is not encoded with session key
			# decode data from konami and use in our db
			from .decoder import Decoder
			decoder = Decoder()
			decoded_kon_resp = decoder.decode(proxied_response)

			logger.log_event('konami resp: ' + str(decoded_kon_resp))

			data = decoded_kon_resp['data']
			player = self._db.player_find_by_steam_id(data['account_id'])
			if player:
				#update
				pass
			else:
				self._db.player_add(data, client_ip)
				# populate table player_values with default data

		else:
			logger.log_event('konami returned none?')
		return decoded_kon_resp


#======CMD_REQAUTH_HTTPS
	def cmd_reqauth(self, client_request):
		data = client_request['data']
		logger.log_event('looking for steam_id {} {}'.format(data['user_name'], len(data['user_name'])))
		player = self._db.player_find_by_steam_id(data['user_name'])
		if len(player) != 1:
			logger.log_event('looking for steam_id {}, {} found!'.format(data['user_name'], len(player)))
		else:
			# generate session id and crypto_key
			session_id = self._generare_session_id()
			crypto_key = self._generate_crypto_key()

			sql = 'update players set magic_hash=%s, \
						  session_id=%s, \
						  crypto_key=%s where id = %s'
			values = (data['hash'], session_id, crypto_key, player[0][0])
			self._db.execute_query(sql, values)

			command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
			command['data']['session'] = session_id
			command['data']['crypto_key'] = crypto_key
			command['data']['user_id'] = player[0][0]
			command['data']['smart_device_id'] = player[0][4]
		return command

#======CMD_SEND_IPANDPORT
	def cmd_send_ipandport(self, client_request):
		data = client_request['data']
		sql = 'update players set ex_ip=%s,\
					  ex_port=%s,\
					  in_ip=%s,\
					  in_port=%s,\
					  nat=%s,\
					  xnaddr=%s where session_id = %s'
		values = (data['ex_ip'], data['ex_port'], data['in_ip'], data['in_port'],
				data['nat'], data['xnaddr'], client_request['session_key'])
		self._db.execute_query(sql, values)

		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['session_key'] = client_request['session_key']
		return command

#======CMD_GET_PLAYERLIST
	def cmd_get_playerlist(self, client_request):
		pass
		#player_list': [{'espionage_lose': , 
		#'espionage_win': , 
		#'fob_grade': , 
		#'fob_point': , 
		#'fob_rank': , 
		#'index': 0, 
		#'is_insurance': 0, 
		#'league_grade': , 
		#'league_rank': , 
		#'name': '', 
		#'playtime': 0, 
		#'point': 0}], 
		#'player_num': 1,
