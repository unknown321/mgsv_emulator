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
			"CMD_SEND_IPANDPORT": self.cmd_send_ipandport,
			"CMD_GET_PLAYERLIST": self.cmd_get_playerlist,
			"CMD_SET_CURRENTPLAYER": self.cmd_set_currentplayer,
			"CMD_GET_ABOLITION_COUNT": self.cmd_get_abolition_count,
			"CMD_GET_CHALLENGE_TASK_REWARDS": self.cmd_get_challenge_task_rewards,
			"CMD_GET_LOGIN_PARAM": self.cmd_get_login_param,
			"CMD_GET_COMBAT_DEPLOY_RESULT": self.cmd_get_combat_deploy_result,
			"CMD_GET_SERVER_ITEM_LIST": self.cmd_get_server_item_list,
			"CMD_SYNC_RESOURCE": self.cmd_sync_resource,
			"CMD_SYNC_SOLDIER_BIN": self.cmd_sync_soldier_bin,
			"CMD_SEND_BOOT": self.cmd_send_boot,
			"CMD_GET_INFORMATIONLIST": self.cmd_get_informationlist,
			"CMD_SYNC_MOTHER_BASE": self.cmd_sync_mother_base,
			"CMD_GET_FOB_STATUS": self.cmd_get_fob_status,
			"CMD_GET_ONLINE_PRISON_LIST": self.cmd_get_online_prison_list,
			"CMD_GET_OWN_FOB_LIST": self.cmd_get_own_fob_list,
			"CMD_MINING_RESOURCE": self.cmd_mining_resource,
			"CMD_UPDATE_SESSION": self.cmd_update_session,
			"CMD_GET_CHALLENGE_TASK_TARGET_VALUES": self.cmd_get_challenge_task_target_values,
		}
		self._db = Database()
		self._db.connect()
		# not sure if calls to logger will work without <self>
		self.logger = Logger()

	def _command_get(self, name):
		return server_commands[name]

	def process_message(self, client_request, client_ip, httpMsg=None):
		msgid = client_request['data']['msgid']
		self.logger.log_event(msgid)
		command = None
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
			else:
				command = self._handlers[msgid](client_request)

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

	def _populate_player_default_values(self, player_id):
		pass

	def _append_session_key(self, command):
		# session key is required for command
		# db.get_session_key
		# do I really need that function?
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

			self.logger.log_event('konami resp: ' + str(decoded_kon_resp))

			data = decoded_kon_resp['data']
			player = self._db.player_find_by_steam_id(data['account_id'])
			if player:
				#update
				pass
			else:
				self._db.player_add(data, client_ip)
				player_id = self._db.player_find_by_steam_id(data['account_id'])[0]
				self._populate_player_default_values(player_id)

		else:
			self.logger.log_event('konami returned none?')
		return decoded_kon_resp


#======CMD_REQAUTH_HTTPS
	def cmd_reqauth(self, client_request):
		data = client_request['data']
		self.logger.log_event('looking for steam_id {} {}'.format(data['user_name'], len(data['user_name'])))
		player = self._db.player_find_by_steam_id(data['user_name'])
		if len(player) != 1:
			self.logger.log_event('looking for steam_id {}, {} found!'.format(data['user_name'], len(player)))
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
		return command

#======CMD_GET_PLAYERLIST
	def cmd_get_playerlist(self, client_request):
		sql = 'select espionage_lose, espionage_win, fob_grade, fob_point,\
			fob_rank, is_insurance, league_grade, league_rank, \
			name, playtime, point from player_vars JOIN players on player_vars.player_id = players.id \
			WHERE session_id = %s'
		values = (client_request['session_key'],)
		data = self._db.fetch_query(sql, values)[0]
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		d = command['data']['player_list'][0]
		d['espionage_lose'] = data[0]
		d['espionage_win'] = data[1]
		d['fob_grade'] = data[2]
		d['fob_point'] = data[3]
		d['fob_rank'] = data[4]
		d['index'] = 0
		d['is_insurance'] = data[5]
		d['league_grade'] = data[6]
		d['league_rank'] = data[7]
		d['name'] = data[8]
		d['playtime'] = data[9]
		d['point'] = data[10]
		command['data']['player_num'] =  1
		return command

#======CMD_SET_CURRENTPLAYER
	def cmd_set_currentplayer(self, client_request):
		sql = 'select id from players WHERE session_id = %s'
		values = (client_request['session_key'],)
		data = self._db.fetch_query(sql, values)[0]
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['data']['player_id'] = data[0]
		return command

#======CMD_GET_ABOLITION_COUNT
	def cmd_get_abolition_count(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		d = command['data']
		d['date'] = int(time.time())
		d['count'] = 1
		d['max'] = 999999
		d['num'] = 0
		d['status'] = 0
		return command

#======CMD_GET_CHALLENGE_TASK_REWARDS
	def cmd_get_challenge_task_rewards(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		# TODO: user-defined variables from mysql
		from .vars import task_list
		d = command['data']
		d['task_list'] = task_list.task_list
		d['task_count'] = len(task_list.task_list)
		return command

#======CMD_GET_LOGIN_PARAM
	def cmd_get_login_param(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import login_params
		d = command['data']
		for key in login_params.login_params:
			d[key] = login_params.login_params[key]
		return command

#======CMD_GET_COMBAT_DEPLOY_RESULT
	def cmd_get_combat_deploy_result(self, client_request):
		# TODO: need to get an example of successful combat deployment
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_SERVER_ITEM_LIST_
	def cmd_get_server_item_list(self, client_request):
		# list of returned items depends on client development rate
		# ie client has development rank of 5 - we return items for ranks 1-5
		# this logic is probably depedent on vars in weapon-related luas which is not covered in emulator
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import server_items
		command['data']['item_list'] = copy.deepcopy(server_items.item_list)
		command['data']['item_num'] = len(command['data']['item_list'])
		return command

#======CMD_SYNC_RESOURCE
	def cmd_sync_resource(self, client_request):
		# TODO: figure out parameters sent by client and what should we send back
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_SYNC_SOLDIER_BIN
	def cmd_sync_soldier_bin(self, client_request):
		# TODO: decode soldier params from binary (cheatengine guys did it)
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_SEND_BOOT_
	def cmd_send_boot(self, client_request):
		# ok 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_INFORMATIONLIST
	def cmd_get_informationlist(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import infolist
		command['data']['info_list'] = copy.deepcopy(info_list.info_list)
		command['data']['info_num'] = len(command['data']['info_list'])
		return command

#======CMD_SYNC_MOTHER_BASE
	def cmd_sync_mother_base(self, client_request):
		# TODO: db integration
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_FOB_STATUS
	def cmd_get_fob_status(self, client_request):
		# TODO: db integration
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_ONLINE_PRISON_LIST
	def cmd_get_online_prison_list(self, client_request):
		# TODO: get a successful response from server
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_OWN_FOB_LIST
	def cmd_get_own_fob_list(self, client_request):
		# TODO: db integration 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_MINING_RESOURCE
	def cmd_mining_resource(self, client_request):
		# TODO: db integration 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command


#======CMD_UPDATE_SESSION
	def cmd_update_session(self, client_request):
		# TODO: seems ok, check different status flags 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_CHALLENGE_TASK_TARGET_VALUES
	def cmd_get_challenge_task_target_values(self, client_request):
		# TODO: db integration
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

