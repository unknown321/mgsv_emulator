from collections import OrderedDict
from . import settings

urls = {
#	"tppps3":"gate responds, but we don't have auth info (parameter names and values)",
	"tppps4":"same",
	"tpp360":"uses different static enc key",
	"tppone":"uses different static enc key",
	"mgostm":"mgo on steam!",
	"mgo360":"xbox 360 mgo",
	"mgoone":"xbone mgo",
	"mgops3":"you got the idea",
	"mgops4":"yea",
	"/tppps3/gate":[
                "CMD_GET_INFORMATIONLIST",
                "CMD_GET_SVRLIST",
                "CMD_GET_SVRTIME",
                "CMD_GET_URLLIST"
	],

	"/tppps3/main":[
		"CMD_AUTH_NPTICKET",
		"CMD_REQAUTH_HTTPS_PS3",
		"CMD_GET_ABOLITION_COUNT"
	],

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
		"CMD_SEND_MISSION_RESULT",
		"CMD_GET_DAILY_REWARD",
		"CMD_GET_FOB_REWARD_LIST",
		"CMD_GET_PLAYER_PLATFORM_LIST",
		"CMD_SEND_ONLINE_CHALLENGE_TASK_STATUS",
		"CMD_GET_FOB_TARGET_DETAIL",
		"CMD_SNEAK_MOTHER_BASE",
		"CMD_GET_FOB_PARAM",
		"CMD_CHECK_SERVER_ITEM_CORRECT",
		"CMD_ACTIVE_SNEAK_MOTHER_BASE",
		"CMD_OPEN_WORMHOLE",
		"CMD_SEND_SNEAK_RESULT",
		"CMD_GET_RANKING",
		"CMD_EXCHANGE_LEAGUE_POINT2",
		"CMD_ADD_FOLLOW",
		"CMD_DELETE_FOLLOW",
		"CMD_SYNC_EMBLEM",
		"CMD_GET_WORMHOLE_LIST",
	]
}

not_implemented = [
	"CMD_APPROVE_STEAM_SHOP",
	"CMD_CALC_COST_FOB_DEPLOY_REPLACE",
	"CMD_CALC_COST_TIME_REDUCTION",
	"CMD_CANCEL_COMBAT_DEPLOY",
	"CMD_CANCEL_COMBAT_DEPLOY_SINGLE",
	"CMD_CANCEL_SHORT_PFLEAGUE",
	"CMD_CHECK_CONSUME_TRANSACTION",
	"CMD_CHECK_DEFENCE_MOTHERBASE",
	"CMD_COMMIT_CONSUME_TRANSACTION",
	"CMD_CONSUME_RESERVE",
	"CMD_CREATE_NUCLEAR",
	"CMD_CREATE_PLAYER",
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
	"CMD_EXTEND_PLATFORM",
	"CMD_GET_CAMPAIGN_DIALOG_LIST",
	"CMD_GET_COMBAT_DEPLOY_LIST",
	"CMD_GET_CONTRIBUTE_PLAYER_LIST",
	"CMD_GET_DEVELOPMENT_PROGRESS",
	"CMD_GET_ENTITLEMENT_ID_LIST",
	"CMD_GET_FOB_DAMAGE",
	"CMD_GET_FOB_DEPLOY_LIST",
	"CMD_GET_FOB_EVENT_DETAIL",
	"CMD_GET_FOB_EVENT_LIST",
	"CMD_GET_FOB_EVENT_POINT_EXCHANGE_PARAMS",
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
	"CMD_NOTICE_SNEAK_MOTHER_BASE",
	"CMD_OPEN_STEAM_SHOP",
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
	"CMD_SEND_NUCLEAR",
	"CMD_SEND_SUSPICION_PLAY_DATA",
	"CMD_SEND_TROOPS",
	"CMD_SET_SECURITY_CHALLENGE",
	"CMD_SPEND_SERVER_WALLET",
	"CMD_START_CONSUME_TRANSACTION",
	"CMD_SYNC_MOTHER_BASE",
	"CMD_SYNC_RESET",
	"CMD_SYNC_SOLDIER_DIFF",
	"CMD_USE_PF_ITEM",
	"CMD_USE_SHORT_PF_ITEM"
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
                "CMD_AUTH_NPTICKET": {
                        "compress": False,
                        "data": {
                                "country": "ww",
                                "lang": "en",
                                "msgid": "CMD_AUTH_NPTICKET",
                                "region": 4,
                                "rqid": 0,
                                "np_ticket": settings.NPTICKET,
                                "np_ticket_size": settings.NP_TICKET_SIZE
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
                "CMD_REQAUTH_HTTPS_PS3": {
                        'compress': False,
                        'data': {
                                'is_tpp': 1,
                                'msgid': 'CMD_REQAUTH_HTTPS',
                                'platform': 'PS3',
                                'rqid': 0,
                                'ugc': 1,
                                'user_name': settings.PS3_PSN_ID,         # get it from psn ticket
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
				'xnaddr': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'	# a fully qualified game console address (also referred to as an XNADDR) 
												# https://patentimages.storage.googleapis.com/pdfs/US20040009815.pdf
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
					'base': -1,			# current level of corresponding section
					'combat': -1,
					'develop': -1,
					'medical': -1,
					'security': -1,
					'spy': -1,
					'suport': -1
				},
				'section_soldier': {
					'base': -1,			# amount of soldiers in unit
					'combat': -1,
					'develop': -1,
					'medical': -1,
					'security': -1,
					'spy': -1,
					'suport': -1
					},
				'soldier_num': -1, 		# soldiers total
				'soldier_param': -1,	# base64-encoded binary soldier data
				'version': 2712
			},
			'original_size': 0,
			'session_crypto': True,
			'session_key': -1
		}
	},

	{
		"CMD_SEND_MISSION_RESULT": {
		# important note - this was sent twice after completing mission 10036 
		# first request mission_id: 10036 
		# second: and 30010, other values were the same
		# records are also sent after fob missions
			"compress": False,
			"data": {
				"mission_id": -1,
				"msgid": "CMD_SEND_MISSION_RESULT",
				"rqid": 0,
				"send_record": {
					"battle_gear_move": 0,
					"cbox": [
						0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					],
					"crack_climb": 1,
					"crawl_move": -1,		# time in game ticks? distance? mine was about 180,000,000
					"espionage_radio": 0,
					"garbage_box": 0,
					"horse_move": -1,		# see crawl_move
					"optional_Radio": 0,
					"squat_move": -1,		# see crawl_move
					"stand_move": -1,		# see crawl_move
					"suit": [
						0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					],
					"toilet": 0,
					"vehicle_move": -1,			# see crawl_move
					"walker_gear_move": -1		# see crawl_move
				}
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}

	},

	{
		"CMD_GET_DAILY_REWARD": {
			"compress": False,
			"data": {
				"msgid": "CMD_GET_DAILY_REWARD",
				"rqid": 0
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}
	},

	{
		"CMD_GET_FOB_REWARD_LIST": {
			"compress": False,
			"data": {
				"high_rank": -1,	# no idea what is that number is, mine was ~1000
				"msgid": "CMD_GET_FOB_REWARD_LIST",
				"rqid": 0,
				"version": 1099
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}
	},

	{
		"CMD_GET_PLAYER_PLATFORM_LIST": {
			"compress": False,
			"data": {
				"msgid": "CMD_GET_PLAYER_PLATFORM_LIST",
				"rqid": 0
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}
	},

	{
		"CMD_SEND_ONLINE_CHALLENGE_TASK_STATUS": {
		# I think it was when I did one of the challenges during the mission
			"compress": False,
			"data": {
				"array_size": 8,
				"msgid": "CMD_SEND_ONLINE_CHALLENGE_TASK_STATUS",
				"rqid": 0,
				"status_list": [
				# completed challenge is not 0 and probably equal to position in array
					0, 1, 0, 0, 0, 0, 0, 0
				],
				"version": -1		# date when challenges were updated, ie 20170228
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}
	},

	{
		"CMD_GET_FOB_TARGET_DETAIL": {
			"compress": False, 
			"data": {
				"high_rank": -1,		# no idea what is that number is, mine was ~1000
				"is_event": 0,
				"is_plus": 1, 
				"is_sneak": 1, 
				"mode": "ACTUAL", 
				"mother_base_id": -1, 	# id of target fob
				"msgid": "CMD_GET_FOB_TARGET_DETAIL", 
				"rqid": 0
			}, 
			"original_size": 0, 
			"session_crypto": True, 
			"session_key": -1
		}
	},

	{
		"CMD_SNEAK_MOTHER_BASE": {
			"compress": False,
			"data": {
				"fob_index": 0,
				"is_event": 0,
				"is_plus": 1,
				"is_security_challenge": 0,
				"is_sneak": 1,
				"mode": "ACTUAL",
				"mother_base_id": -1,	# id of the fob you are invading
				"msgid": "CMD_SNEAK_MOTHER_BASE",
				"platform": 0,
				"player_id": 0,
				"rqid": 0,
				"wormhole_player_id": 0,
				"xnkey": "AAAAAAAAAAAAAAAAAAAAAA==",
				"xnkid": "AAAAAAAAAAA="
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}

	},

	{
		"CMD_GET_FOB_PARAM": {
			"compress": False,
			"data": {
				"msgid": "CMD_GET_FOB_PARAM",
				"rqid": 0
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}

	},

	{
		"CMD_CHECK_SERVER_ITEM_CORRECT": {
			"compress": False,
			"data": {
				"item_list": [	# list of item ids, take values from TppEquip.*
					-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
				],
				"item_list_num": 11,
				"msgid": "CMD_CHECK_SERVER_ITEM_CORRECT",
				"rqid": 0
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}

	},

	{
		"CMD_ACTIVE_SNEAK_MOTHER_BASE": {
		# I think it was sent when I alerted the fob
			"compress": False, 
			"data": {
				"mother_base_id": -1, 		# id of the fob you are invading
				"msgid": "CMD_ACTIVE_SNEAK_MOTHER_BASE", 
				"rqid": 0
			}, 
			"original_size": 0, 
			"session_crypto": True, 
			"session_key": -1
		}
	},

	{
		"CMD_OPEN_WORMHOLE": {
			"compress": False, 
			"data": {
				"flag": "BLACK", # ?
				"is_open": 1, 
				"msgid": "CMD_OPEN_WORMHOLE", 
				"player_id": -1, 			# owner of invaded fob
				"retaliate_score": -1,  	# I think score is calculated somewhere in o50050_sequence.lua (or whatever it's name is)
				"rqid": 0, 
				"to_player_id": -1			# your id
			}, 
			"original_size": 0, 
			"session_crypto": True, 
			"session_key": -1
		}
	},

	{
		"CMD_SEND_SNEAK_RESULT": {
		# command after finishing fob mission
		    "compress": False,
		    "data": {
		        "capture_nuclear": 0,
		        "capture_placement": {
		            "emplacement_gun_east": 0,
		            "emplacement_gun_west": 0,
		            "gatling_gun": 0,
		            "gatling_gun_east": 0,
		            "gatling_gun_west": 0,
		            "mortar_normal": 0
		        },
		        "capture_player_soldier_num": 0,
		        "capture_resource": {
		            "biotic_resource": 0,
		            "common_metal": 0,
		            "fuel_resource": 0,
		            "minor_metal": 0,
		            "precious_metal": 0
		        },
		        "capture_soldier_count": [
		            0, 0, 0, 0, 0, 0, 0, 0, 0, 0
		            # amount of soldiers for each rank, from E to S++
		        ],
		        "capture_soldier_id": [
		            {
		                "param": [
		                    -1,	# some soldier params, 2 ints per soldier
		                    -1
		                ]
		            },
		            {
		                "param": [
		                    -1,
		                    -1
		                ]
		            } # etc
		        ],
		        "capture_soldier_num": -1,			# amount of captured soldiers
		        "capture_support_soldier_num": 0,
		        "cleared_plant_count": -1,			# amount of cleared plants, you get a notification after clearing one
		        "count_of_neutralize_intruder": 0,
		        "count_of_neutralized_by_intruder": 0,
		        "damage_point": -1,				# it can be damage taken or damage given. I didn't use lethal weapons and yet it was ~170000
		        "destroy_placement": {
		            "emplacement_gun_east": 0,
		            "emplacement_gun_west": 0,
		            "gatling_gun": 0,
		            "gatling_gun_east": 0,
		            "gatling_gun_west": 0,
		            "mortar_normal": 0
		        },
		        "event": {
		            "attacker_info": {
		                "npid": {
		                    "handler": {
		                        "data": "",
		                        "term": 0
		                    }
		                },
		                "player_id": 0,
		                "player_name": "NotImplement",
		                "ugc": 0,
		                "xuid": 0
		            },
		            "attacker_league_grade": 0,
		            "attacker_sneak_grade": 0,
		            "capture_nuclear": 0,
		            "capture_resource": {
		                "biotic_resource": 0,
		                "common_metal": 0,
		                "fuel_resource": 0,
		                "minor_metal": 0,
		                "precious_metal": 0
		            },
		            "cluster": 0,
		            "data": "",		# mysterious base64-encoded data, a lot of data, most likely your movement and action history
		            "gmp": 0,
		            "is_win": 0,
		            "layout_code": -1,	# ?
		            "position_x": 0,
		            "position_z": 0,
		            "regist_date": 0,
		            "rotate_y": 0,
		            "size": -1		# size of what?
		        },
		        "event_point": 0,
		        "event_version": 2,
		        "high_rank": -1,	# no idea what is that number is, mine was ~1000
		        "injure_soldier_num": 0,
		        "injure_support_soldier_num": 0,
		        "is_event": 0,
		        "is_goal": 1,		# did you reach the door
		        "is_perfect_stealth": 0,
		        "is_plus": 1,		# always 1 because steam has no plus
		        "is_sneak": 1,		# alert was raised, but sneak is still 1 (???)
		        "is_supporter": 0,
		        "kill_soldier_num": 0,
		        "kill_support_soldier_num": 0,
		        "mission_task_complete_bits": -1,	# name speaks for itself, no idea how is it calculated. Was <10 for real fob, >100 for fob event
		        "mode": "ACTUAL",
		        "mother_base_id": -1,	# id of attacked fob, huge number for real fob, <10 for fob event 
		        "msgid": "CMD_SEND_SNEAK_RESULT",
		        "open_wormhole": 1,
		        "recover_resource": {
		            "biotic_resource": 0,
		            "common_metal": 0,
		            "fuel_resource": 0,
		            "minor_metal": 0,
		            "precious_metal": 0
		        },
		        "result_type": 0,
		        "retaliate_point": -1,		# I think score is calculated somewhere in o50050_sequence.lua (or whatever it's name is), same value as retaliate_score
		        "retaliate_wormhole": 0,
		        "rqid": 0,
		        "sneak_point": -1,		# esp points
		        "sneak_result": "WIN",
		        "version": 1
		    },
		    "original_size": 0,
		    "session_crypto": True,
		    "session_key": -1
		}
	},

	{
		"CMD_GET_RANKING": {
		# get fob ranking
			"compress": False, 
			"data": {
				"event_id": 0, 		# corresponding event id, 0 for real fobs, number for events
				"get_type": "BEST", # or AROUND for scores around you
				"index": 0, 
				"is_new": 0, 
				"msgid": "CMD_GET_RANKING", 
				"num": 1, 			# 1 is for best, 16 for around
				"rqid": 0, 
				"type": "SNEAK"		# SNEAK_EVENT for event
			}, 
			"original_size": 0, 
			"session_crypto": True, 
			"session_key": -1
		}
	},

	{
		"CMD_EXCHANGE_LEAGUE_POINT2": {
			"compress": False, 
			"data": {
			# unknown values, it was an exchange for 5 S dev-type soldiers
				"common_value": 8, 
				"is_event": 1, 
				"msgid": "CMD_EXCHANGE_LEAGUE_POINT2", 
				"num_to_exchange": 1, 
				"rqid": 0, 
				"type": 1, 
				"unique_id": 2
			}, 
			"original_size": 0, 
			"session_crypto": True, 
			"session_key": -1
		}
	},

	{
		"CMD_ADD_FOLLOW": {
		# provide FOB support to someone 
			"compress": False, 
			"data": {
				"msgid": "CMD_ADD_FOLLOW", 
				"np_id": {
					"handler": {
						"data": "", 
						"term": 0
					}
				}, 
				"player_id": -1, 	# player id to support
				"rqid": 0, 
				"steam_id": 0, 
				"xu_id": 0
			}, 
			"original_size": 0, 
			"session_crypto": True, 
			"session_key": -1
		}
	},

	{
		"CMD_DELETE_FOLLOW": {
		# discontinue FOB support
			"compress": False, 
			"data": {
				"msgid": "CMD_DELETE_FOLLOW", 
				"player_id": -1, 	# player id to unfollow
				"rqid": 0
			}, 
			"original_size": 0, 
			"session_crypto": True, 
			"session_key": -1
		}
	},

	{
		"CMD_SYNC_EMBLEM": {
			"compress": False,
			"data": {
				"emblem": {
					"parts": [
						{
							"base_color": -1,
							"frame_color": -1,
							"position_x": -1,			# from -100 to 100?
							"position_y": -1,
							"rotate": 0,
							"scale": -1,
							"texture_tag": -1
						},
						{
							"base_color": -1,
							"frame_color": -1,
							"position_x": -1,
							"position_y": -1,
							"rotate": 0,
							"scale": -1,
							"texture_tag": -1
						},
						{	
							"base_color": -1,
							"frame_color": -1,
							"position_x": -1,
							"position_y": -1,
							"rotate": 0,
							"scale": -1,
							"texture_tag": -1
						},
						{
							"base_color": -1,
							"frame_color": -1,
							"position_x": -1,
							"position_y": -1,
							"rotate": 0,
							"scale": -1,
							"texture_tag": -1
						}
					]
				},
				"msgid": "CMD_SYNC_EMBLEM",
				"rqid": 0
			},
			"original_size": 0,
			"session_crypto": True,
			"session_key": -1
		}
	},

	{
		"CMD_GET_WORMHOLE_LIST": {
			'compress': False,
			'original_size': 0,
			'data': {
				'flag': 'BLACK',	# possible value - FRIENDLY
				'msgid': 'CMD_GET_WORMHOLE_LIST',
				'rqid': 0
			},
			'session_key': -1,
			'session_crypto': True
		}
	}
]

for i in commlist:
	client_commands.update(i)
