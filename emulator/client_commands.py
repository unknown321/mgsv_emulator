from collections import OrderedDict
import .settings

urls = {
	"/tppstm/gate":[
		"CMD_GET_INFORMATIONLIST",
		"CMD_GET_SVRLIST",
		"CMD_GET_SVRTIME",
		"CMD_GET_URLLIST"
		],

	"/tppstm/main":[
		"CMD_ABORT_MOTHER_BASE",
		"CMD_AUTH_STEAMTICKET",
		"CMD_CHECK_SHORT_PFLEAGUE_ENTERABLE",
		"CMD_ENTER_SHORT_PFLEAGUE",
		"CMD_GET_ABOLITION_COUNT",
		"CMD_GET_CHALLENGE_TASK_REWARDS",
		"CMD_GET_CHALLENGE_TASK_TARGET_VALUES",
		"CMD_GET_COMBAT_DEPLOY_RESULT",
		"CMD_GET_FOB_NOTICE",
		"CMD_GET_FOB_STATUS",
		"CMD_GET_FOB_TARGET_LIST",
		"CMD_GET_LEAGUE_RESULT",
		"CMD_GET_LOGIN_PARAM",
		"CMD_GET_ONLINE_PRISON_LIST",
		"CMD_GET_OWN_FOB_LIST",
		"CMD_GET_PF_POINT_EXCHANGE_PARAMS",
		"CMD_GET_PLAYERLIST",
		"CMD_GET_PREVIOUS_SHORT_PFLEAGUE_RESULT",
		"CMD_GET_SERVER_ITEM_LIST",
		"CMD_GET_SHORT_PFLEAGUE_RESULT",
		"CMD_MINING_RESOURCE",
		"CMD_REQAUTH_HTTPS",
		"CMD_SEND_BOOT",
		"CMD_SEND_IPANDPORT",
		"CMD_SET_CURRENTPLAYER",
		"CMD_SYNC_LOADOUT",
		"CMD_SYNC_RESOURCE",
		"CMD_SYNC_SOLDIER_BIN",
		"CMD_UPDATE_SESSION",
		# "CMD_SYNC_MOTHER_BASE"  # not implemented, too big
	]
}


not_implemented = [

	"CMD_ACTIVE_SNEAK_MOTHER_BASE",
	"CMD_ADD_FOLLOW",
	"CMD_APPROVE_STEAM_SHOP",
	"CMD_CALC_COST_FOB_DEPLOY_REPLACE",
	"CMD_CALC_COST_TIME_REDUCTION",
	"CMD_CANCEL_COMBAT_DEPLOY",
	"CMD_CANCEL_COMBAT_DEPLOY_SINGLE",
	"CMD_CANCEL_SHORT_PFLEAGUE",
	"CMD_CHECK_CONSUME_TRANSACTION",
	"CMD_CHECK_DEFENCE_MOTHERBASE",
	"CMD_CHECK_SERVER_ITEM_CORRECT",
	"CMD_COMMIT_CONSUME_TRANSACTION",
	"CMD_CONSUME_RESERVE",
	"CMD_CREATE_NUCLEAR",
	"CMD_CREATE_PLAYER",
	"CMD_DELETE_FOLLOW",
	"CMD_DELETE_TROOPS_LIST",
	"CMD_DEPLOY_FOB_ASSIST",
	"CMD_DEPLOY_MISSION",
	"CMD_DESTRUCT_NUCLEAR",
	"CMD_DESTRUCT_ONLINE_NUCLEAR",
	"CMD_DEVELOP_SERVER_ITEM",
	"CMD_DEVELOP_WEPON",
	"CMD_ELAPSE_COMBAT_DEPLOY",
	"CMD_EXCHANGE_FOB_EVENT_POINT",
	"CMD_EXCHANGE_LEAGUE_POINT",
	"CMD_EXCHANGE_LEAGUE_POINT2",
	"CMD_EXTEND_PLATFORM",
	"CMD_GET_CAMPAIGN_DIALOG_LIST",
	"CMD_GET_COMBAT_DEPLOY_LIST",
	"CMD_GET_CONTRIBUTE_PLAYER_LIST",
	"CMD_GET_DAILY_REWARD",
	"CMD_GET_DEVELOPMENT_PROGRESS",
	"CMD_GET_ENTITLEMENT_ID_LIST",
	"CMD_GET_FOB_DAMAGE",
	"CMD_GET_FOB_DEPLOY_LIST",
	"CMD_GET_FOB_EVENT_DETAIL",
	"CMD_GET_FOB_EVENT_LIST",
	"CMD_GET_FOB_EVENT_POINT_EXCHANGE_PARAMS",
	"CMD_GET_FOB_PARAM",
	"CMD_GET_FOB_REWARD_LIST",
	"CMD_GET_FOB_TARGET_DETAIL",
	"CMD_GET_MBCOIN_REMAINDER",
	"CMD_GET_NEXT_MAINTENANCE",
	"CMD_GET_ONLINE_DEVELOPMENT_PROGRESS",
	"CMD_GET_PAY_ITEM_LIST",
	"CMD_GET_PF_DETAIL_PARAMS",
	"CMD_GET_PLATFORM_CONSTRUCTION_PROGRESS",
	"CMD_GET_PLAYER_PLATFORM_LIST",
	"CMD_GET_PURCHASABLE_AREA_LIST",
	"CMD_GET_PURCHASE_HISTORY",
	"CMD_GET_PURCHASE_HISTORY_NUM",
	"CMD_GET_RANKING",
	"CMD_GET_RENTAL_LOADOUT_LIST",
	"CMD_GET_RESOURCE_PARAM",
	"CMD_GET_SECURITY_INFO",
	"CMD_GET_SECURITY_PRODUCT_LIST",
	"CMD_GET_SECURITY_SETTING_PARAM",
	"CMD_GET_SERVER_ITEM",
	"CMD_GET_SHOP_ITEM_NAME_LIST",
	"CMD_GET_SNEAK_TARGET_LIST",
	"CMD_GET_STEAM_SHOP_ITEM_LIST",
	"CMD_GET_TROOPS_LIST",
	"CMD_GET_WORMHOLE_LIST",
	"CMD_NOTICE_SNEAK_MOTHER_BASE",
	"CMD_OPEN_STEAM_SHOP",
	"CMD_OPEN_WORMHOLE",
	"CMD_PURCHASE_FIRST_FOB",
	"CMD_PURCHASE_FOB",
	"CMD_PURCHASE_NUCLEAR_COMPLETION",
	"CMD_PURCHASE_ONLINE_DEPLOYMENT_COMPLETION",
	"CMD_PURCHASE_ONLINE_DEVELOPMENT_COMPLETION",
	"CMD_PURCHASE_PLATFORM_CONSTRUCTION",
	"CMD_PURCHASE_RESOURCES_PROCESSING",
	"CMD_PURCHASE_SECURITY_SERVICE",
	"CMD_PURCHASE_SEND_TROOPS_COMPLETION",
	"CMD_PURCHASE_WEPON_DEVELOPMENT_COMPLETION",
	"CMD_RELOCATE_FOB",
	"CMD_RENTAL_LOADOUT",
	"CMD_REQAUTH_SESSIONSVR",
	"CMD_REQUEST_RELIEF",
	"CMD_RESET_MOTHER_BASE",
	"CMD_SALE_RESOURCE",
	"CMD_SEND_DEPLOY_INJURE",
	"CMD_SEND_HEARTBEAT",
	"CMD_SEND_MISSION_RESULT",
	"CMD_SEND_NUCLEAR",
	"CMD_SEND_ONLINE_CHALLENGE_TASK_STATUS",
	"CMD_SEND_SNEAK_RESULT",
	"CMD_SEND_SUSPICION_PLAY_DATA",
	"CMD_SEND_TROOPS",
	"CMD_SET_SECURITY_CHALLENGE",
	"CMD_SNEAK_MOTHER_BASE",
	"CMD_SPEND_SERVER_WALLET",
	"CMD_START_CONSUME_TRANSACTION",
	"CMD_SYNC_EMBLEM",
	"CMD_SYNC_MOTHER_BASE",
	"CMD_SYNC_RESET",
	"CMD_SYNC_SOLDIER_DIFF",
	"CMD_USE_PF_ITEM",
	"CMD_USE_SHORT_PF_ITEM",

]


client_commands = OrderedDict()
commlist = [
	{
		"CMD_GET_URLLIST" : {
			"data": {
				"lang": "ANY",
				"msgid": "CMD_GET_URLLIST",
				"region": "REGION_ALL",
				"rqid": 0
			},
			"session_crypto": False,
			"session_key": "",
			"compress": False,
			"original_size": 0
		}
	},

	{
		"CMD_GET_SVRLIST" : {
			'compress': False,
			'data': {
				'lang': 'ANY', 
				'msgid': 'CMD_GET_SVRLIST',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': False,
			'session_key': ''
		}
	},

	{
		"CMD_AUTH_STEAMTICKET": {
			"compress": False, 
			"data": {
				"country": "ww", 
				"lang": "en", 
				"msgid": "CMD_AUTH_STEAMTICKET", 
				"region": 4, 
				"rqid": 0, 
				"steam_ticket": settings.STEAM_TICKET, 
				"steam_ticket_size": settings.STEAM_TICKET_SIZE
			}, 
			"original_size": 0, 
			"session_crypto": False, 
			"session_key": ""
		}
	},

	{
		"CMD_GET_INFORMATIONLIST": {
			'compress': False, 
			'data': {
				'is_mgo': 0, 
				'lang': 'EN',
				'msgid': 'CMD_GET_INFORMATIONLIST',
				'region': 'REGION_NA',
				'rqid': 0
			}, 
			'original_size': 0,
			'session_crypto': False,
			'session_key': -1
		}
	},

	{
		"CMD_GET_SVRTIME": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_SVRTIME',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': False,
			'session_key': ''
		}
	},

	{
		"CMD_REQAUTH_HTTPS": {
			'compress': False,
			'data': {
				'hash': settings.MAGIC_HASH,		# some magic hash, 16 bytes
				'is_tpp': 1,
				'msgid': 'CMD_REQAUTH_HTTPS',
				'platform': 'Steam',
				'rqid': 0,
				'ugc': 1,
				'user_name': settings.STEAM_ID,		# 768121315156131
				'ver': 'NotImplement'
			}, 
			'original_size': 0,
			'session_crypto': False,
			'session_key': ''
		}
	},

	{
		"CMD_SEND_IPANDPORT": {
			'compress': False,
			'data': {
				'ex_ip': settings.EX_IP, 	# your local ip
				'ex_port': 5733,
				'in_ip': settings.IN_IP,		# your local ip as well
				'in_port': 5733,
				'msgid': 'CMD_SEND_IPANDPORT',
				'nat': 'OPEN_INTERNET',
				'rqid': 0,
				'secure_device_address': 'NotImplement',
				'xnaddr': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
			}, 
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_PLAYERLIST": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_PLAYERLIST',
				'rqid': 0
			}, 
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_SET_CURRENTPLAYER": {
			'compress': False,
			'data': {
				'index': 0,
				'is_reset': 0,
				'msgid': 'CMD_SET_CURRENTPLAYER',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_ABOLITION_COUNT": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_ABOLITION_COUNT',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_CHALLENGE_TASK_REWARDS": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_CHALLENGE_TASK_REWARDS',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_LOGIN_PARAM": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_LOGIN_PARAM',
				'rqid': 0,
				'server_item_platform_info': {
					'platform_base_rank': 0
				}
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_UPDATE_SESSION": {
			'compress': False,
			'data': {
				'msgid': 'CMD_UPDATE_SESSION',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_COMBAT_DEPLOY_RESULT": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_COMBAT_DEPLOY_RESULT',
				'rqid': 0,
				'version': 70
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_SERVER_ITEM_LIST": {
			'compress': False,
			'data': {
				'list_max_count': 320,
				'msgid': 'CMD_GET_SERVER_ITEM_LIST',
				'rqid': 0,
				'server_item_platform_info': {
					'platform_base_rank': 6,
					'special_soldier_type_list': [10, 10, 10, 10, 10, 10, 10, 10]
				}
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
			}
	},

	{
		"CMD_GET_FOB_STATUS": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_FOB_STATUS',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_ONLINE_PRISON_LIST": {
			'compress': False,
			'data': {
				'is_persuade': 1,
				'msgid': 'CMD_GET_ONLINE_PRISON_LIST',
				'num': 100,
				'offset': 0,
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_OWN_FOB_LIST": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_OWN_FOB_LIST',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_MINING_RESOURCE": {
			'compress': False,
			'data': {
				'is_force_mining': 0,
				'is_force_process': 0,
				'msgid': 'CMD_MINING_RESOURCE',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_CHALLENGE_TASK_TARGET_VALUES": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_CHALLENGE_TASK_TARGET_VALUES',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_FOB_NOTICE": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_FOB_NOTICE',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_FOB_TARGET_LIST": {
			'compress': False,
			'data': {
				'index': 0,
				'msgid': 'CMD_GET_FOB_TARGET_LIST',
				'num': 30,
				'rqid': 0,
				'type': 'INJURY'			
						# DEPLOYED     - list is not complete, entries might be wrong
						# CHALLENGE
						# INJURY
						# FR_ENEMY
						# PICKUP_HIGH
						# NUCLEAR
						# TRIAL
						# PICKUP
						# FOLLOWER
						# FOLLOW
						# EMERGENCY
						# SEPARATION
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_ABORT_MOTHER_BASE": {
			'compress': False,
			'data': {
				'msgid': 'CMD_ABORT_MOTHER_BASE',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_LEAGUE_RESULT": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_LEAGUE_RESULT',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_PF_POINT_EXCHANGE_PARAMS": {
			'compress': False,
			'data': {
				'is_event': 0,
				'msgid': 'CMD_GET_PF_POINT_EXCHANGE_PARAMS',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_CHECK_SHORT_PFLEAGUE_ENTERABLE": {
			'compress': False,
			'data': {
				'msgid': 'CMD_CHECK_SHORT_PFLEAGUE_ENTERABLE',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_SHORT_PFLEAGUE_RESULT": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_SHORT_PFLEAGUE_RESULT',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_GET_PREVIOUS_SHORT_PFLEAGUE_RESULT": {
			'compress': False,
			'data': {
				'msgid': 'CMD_GET_PREVIOUS_SHORT_PFLEAGUE_RESULT',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_ENTER_SHORT_PFLEAGUE": {
			'compress': False,
			'data': {
				'msgid': 'CMD_ENTER_SHORT_PFLEAGUE',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_SEND_BOOT": {
			'compress': False,
			'data': {
				'is_goty': 0,
				'is_mbcoin_dlc': 0,
				'msgid': 'CMD_SEND_BOOT',
				'play_time': 0, 		#total playtime in seconds, NOT the time steam shows
				'rqid': 0,
				'send_record': {
					'config': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 	# no idea
					'develop_count': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					'score': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],	# mission scores 
					'score_limit': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # mission scores with score-limiting items
				}
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_SYNC_LOADOUT": {
			'compress': False,
			'data': {
				'loadout': {
					'hand': {
						'id': 0,
						'level_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					},

					'item_level_list': [0, 0, 0, 0, 0, 0, 0, 0],
					'item_list': [0, 0, 0, 0, 0, 0, 0, 0],
					'primary1': {
						'chimera_desc': {
							'color': 0,
							'paint': 1,
							'parts_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
						},
						'chimera_slot': 0,
						'id': 0,
						'is_chimera': 0
					},

					'primary2': {
						'chimera_desc': {
							'color': 0,
							'paint': 1,
							'parts_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
						},
						'chimera_slot': 0,
						'id': 0,
						'is_chimera': 0
					},

					'secondary': {
						'chimera_desc': {
							'color': 0,
							'paint': 1,
							'parts_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
						},
						'chimera_slot': 0,
						'id': 0,
						'is_chimera': 0
					},

					'suit': {
						'camo': 0,
						'face': 0,
						'level': 1,
						'parts': 0
					},

					'support_list': [0, 0, 0, 0, 0, 0, 0, 0]
				},
				'msgid': 'CMD_SYNC_LOADOUT',
				'rqid': 0
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_SYNC_RESOURCE": {
			'compress': False,
			'data': {
				'compensate_resource': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'cumulative_grade': 0,
				'diff_resource1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'diff_resource2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'gmp': 0,
				'hero': 0,
				'is_force_balance': 0,
				'is_hero': 1,
				'is_wallet': 1,
				'msgid': 'CMD_SYNC_RESOURCE',
				'rqid': 0,
				'version': 6903
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_SYNC_SOLDIER_BIN": {
		'compress': False,
		'data': {
			'flag': 'SYNC',
			'force_sync': 0,
			'msgid': 'CMD_SYNC_SOLDIER_BIN',
			'rqid': 0,
			'section': {
				'base': 0,			# current level of corresponding section
				'combat': 0,
				'develop': 0,
				'medical': 0,
				'security': 0,
				'spy': 0,
				'suport': 0
			},
			'section_soldier': {
				'base': 0,			# amount of soldiers in unit
				'combat': 0,
				'develop': 0,
				'medical': 0,
				'security': 0,
				'spy': 0,
				'suport': 0
				},
			'soldier_num': 0, 		# soldiers total
			'soldier_param': -1,	# base64-encoded binary soldier data
			'version': 2712
		},
		'original_size': 0,
		'session_crypto': True,
		'session_key': -1
		}
	}

]

for i in commlist:
	client_commands.update(i)