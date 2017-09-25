enemy = {
	'attacker_emblem': {
		'parts': []
	},
	'attacker_espionage': {
		'lose': 0,
		'score': 0,
		'section': 0,
		'win': 0
	},
	'attacker_info': {
		'npid': {
			'handler': {
				'data': '',
				'dummy': [0, 0, 0],
				'term': 0
			},
			'opt': [0, 0, 0, 0, 0, 0, 0, 0],
			'reserved': [0, 0, 0, 0, 0, 0, 0, 0]
		},
		'player_id': 0,
		'player_name': 'NotImplement',
		'ugc': 0,
		'xuid': 0
	},
	'attacker_sneak_rank_grade': 0,
	'cluster': 1,		# ? 
	'is_sneak_restriction': 0,
	'is_win': 0,
	'mother_base_param': [
		{
			'area_id': 0,
			'cluster_param': [],
			'construct_param': 59088936,
			#130394987,   # includes fob position on the globe, format unknown
			'fob_index': 0,			# doesn't seem to affect anything
			'mother_base_id': 1,
			'platform_count': 28,
			'price': 0,			# doesn't appear on ui anywhere
			'security_rank': 57
		}
#		{
#			'area_id': 0,
#			'cluster_param': [],
#			'construct_param': 130394987, #184920939,
#			'fob_index': 1,
#			'mother_base_id': 2,
#			'platform_count': 28,
#			'price': 0,
#			'security_rank': 57
#		}, 
#		{
#			'area_id': 0,
#			'cluster_param': [],
#			'construct_param': 130394987,# 147172177,
#			'fob_index': 2,
#			'mother_base_id': 3,
#			'platform_count': 28,
#			'price': 0,
#			'security_rank': 57
#		}, 
#		{
#			'area_id': 0,
#			'cluster_param': [],
#			'construct_param': 130394987,#105024337,
#			'fob_index': 3,
#			'mother_base_id': 4,
#			'platform_count': 28,
#			'price': 0,
#			'security_rank': 57
#		}
	],
	'owner_detail_record': {
		'emblem': {
			'parts': [
				{
					'base_color': 13666141,  # pick up a colour from Assets/tpp/ui/Script/emblem_list.lua, ie  { 167, 31, 31 } (rgb)
					# convert to bgr -  { 31, 31, 167 }
					# convert to hex - 1F1FA7
					# hex -> dec = 2039719
					'frame_color': 2039719,
					'position_x': 5,
					'position_y': 5,
					'rotate': 0,
					'scale': 13,
					'texture_tag': 3573759981 # str32 hash of 'tag' field from Assets/tpp/ui/Script/emblem_list.lua 
				},
				{
					'base_color': 13666141,
					'frame_color': 2039719,
					'position_x': 0,
					'position_y': 0,
					'rotate': 0,
					'scale': 14,
					'texture_tag': 3573759981
				},
				{
					'base_color': 2039719,
					'frame_color': 2039719,
					'position_x': 15,
					'position_y': -13,
					'rotate': 0,
					'scale': 11,
					'texture_tag': 3573759981
				},
				{
					'base_color': 2039719,
					'frame_color': 2039719,
					'position_x': -15,
					'position_y': 13,
					'rotate': 0,
					'scale': 17,
					'texture_tag': 3573759981
				}
			]
		},
		'enemy': 1,			# set to 1 to be able to retaliate
		'espionage': {
			'lose': 200,		# enemy's amount of loses
			'score': 100,		# enemy's esp score
			'section': 0,	# ?? always 0
			'win': 10		# enemy's amount of wins
		},
		'follow': 0,
		'follower': 0,
		'help': 0,
		'hero': 0,
		'insurance': 0,
		'is_security_challenge': 0,
		'league_rank': {
			'grade': 0,			# pf grade?
			'rank': 0,			# pf rank?
			'score': 0			# pf score?
		},
		'name_plate_id': 9,			# nameplate of the enemy, has to match one in owner_fob_record
		'nuclear': 0,
		'online': 0,			# doesn't affect anything as I can see
		'sneak_rank': {
			'grade': 0,		#?
			'rank': 0,		#?
			'score': 0		#?
		},
		'staff_count': 3145	# sum of staff in owner_fob_record
	},
	'owner_fob_record': {
		'attack_count': 1,	# enemy num of attacks
		'attack_gmp': 2,	# damage inflicted(gmp)
		'capture_nuclear': 0,
		'capture_resource': {   # materials stolen
			'biotic_resource': 0,
			'common_metal': 0,
			'fuel_resource': 0,
			'minor_metal': 0,
			'precious_metal': 0
		},
		'capture_resource_count': 0,
		'capture_staff': 0,
		'capture_staff_count': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		'date_time': 0,
		'injury_staff_count': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		'left_hour': 0,
		'name_plate_id': 9,	# nameplate of the enemy, has to match one in owner_fob_record
		'nuclear': 0,
		'processing_resource': {
			'biotic_resource': 0,
			'common_metal': 0,
			'fuel_resource': 0,
			'minor_metal': 0,
			'precious_metal': 0
		},
		'staff_count': [0, 0, 0, 4, 2, 6, 20, 1734, 881, 498],
		'support_count': 0,
		'supported_count': 0,
		'usable_resource': {
			'biotic_resource': 0,
			'common_metal': 0,
			'fuel_resource': 0,
			'minor_metal': 0,
			'precious_metal': 0
		}
	},
	'owner_info': {
		'npid': {
			'handler': {
				'data': '',
				'dummy': [0, 0, 0],
				'term': 0
			},
			'opt': [0, 0, 0, 0, 0, 0, 0, 0],
			'reserved': [0, 0, 0, 0, 0, 0, 0, 0]
		},
		'player_id': 1,
		'player_name': '76561197960287930_player01',
		'ugc': 1,
		'xuid': 76561197960287930
	},
	'sneak_mode': 0
}
