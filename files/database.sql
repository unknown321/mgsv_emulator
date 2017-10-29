create database if not exists mgsv_server;
use mgsv_server;

create table if not exists url(
        id int NOT NULL AUTO_INCREMENT,
        url_type varchar(10),
        url_version int,
        url_link varchar(100),
        PRIMARY KEY(id)
);


-- player parameters, WIP
create table if not exists player(
	id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(id)
);

create table if not exists player_session(
	id int NOT NULL AUTO_INCREMENT,
	session_hash varchar(50), -- TODO find proper size
	player_id int NOT NULL,
	last_access datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(id),
	FOREIGN KEY(player_id) REFERENCES player(id) ON DELETE CASCADE
);

-- defines parameters of a single FOB, mother_base_param in mother_base_sync command
create table if not exists fob_cluster(
	id int NOT NULL AUTO_INCREMENT,
	area_id int DEFAULT 0, -- always 0 for my fobs
	construct_param int, -- color, location etc
	fob_index int, -- always 0 for my fobs
	mother_base_id int, -- always 0 for my fobs
	platform_count int, -- total amount of built platforms, 28 max
	price int, -- always 0 for my completely finished fobs
	security_rank int, -- security rank level
	PRIMARY KEY(id)
);

-- parameters of cluster security, 4x for one fob
-- common[1-3]_security and unique_security
create table if not exists cluster_params(
	id int NOT NULL AUTO_INCREMENT,
	cluster_id int NOT NULL,
	build int, -- unknown param, 16385 for me - some kind of hash or is it the id?
	cluster_security int, -- defines security zones I guess or something like that, hash value like construct_params
	soldier_rank int, -- 1-9?
	PRIMARY KEY(id),
	FOREIGN KEY(cluster_id) REFERENCES fob_cluster(id) ON DELETE CASCADE
);

-- describes the _amount_ of security on cluster part
create table if not exists common_security(
	id int NOT NULL,
	cluster_params_id int NOT NULL,
	-- params below contain only counts of security stuff
    antitheft int,
    camera int,
    caution_area int,
    decoy int,
    ir_sensor int,
    mine int,
    soldier int,
    uav int,
    voluntary_coord_camera_count int,
    voluntary_coord_mine_count int,
	PRIMARY KEY(id),
	FOREIGN KEY(cluster_params_id) REFERENCES cluster_params(id) ON DELETE CASCADE
);

-- one user can has many player entites
-- at least this is how it looks from server-client communications with player_id parameters

create table if not exists name_plate(
	id int NOT NULL,
	description varchar(100),
	PRIMARY KEY(id)
);


-- server user, one per steam account
create table if not exists server_user(
	id int NOT NULL AUTO_INCREMENT,
						-- there is no point in saving steam_ticket since it renews every time
	steam_id varchar(17), 			-- from server CMD_AUTH_STEAMTICKET, 17-chars steamid
	currency varchar(4),			-- from server CMD_AUTH_STEAMTICKET, 2-3 letter currency, not sure if it can be 4 letters
	password varchar(32),			-- from server CMD_AUTH_STEAMTICKET, loginid_password, base64
	smart_device_id varchar(128),		-- from server CMD_AUTH_STEAMTICKET, smart_device_id, base64
	magic_hash varchar(32), 		-- from client CMD_REQAUTH_HTTPS   , base64 hash from client
	crypto_key varchar(32), 		-- from server CMD_REQAUTH_HTTPS   , blowfish crypto key used for encrypting session messages
	last_login datetime,			-- date of last login
	last_command datetime,			-- date of last received command from client
--	session_id varchar(32),			-- session identifier used for further communications, expires if there was no commands for client for 2 mins
	client_ip varchar(16), 			-- client ip, can be used for static authentication
	ex_ip varchar(16), 				-- from client CMD_SEND_IPANDPORT
	ex_port varchar(7),
	in_ip varchar(16),
	in_port varchar(7),
	nat varchar(48),
	xnaddr varchar(48), 
	PRIMARY KEY(id)
);

create table if not exists player_vars(
	id int NOT NULL AUTO_INCREMENT,
	player_id int NOT NULL,
	espionage_lose int, -- CMD_GET_PLAYERLIST
	espionage_win int,
	fob_grade int, 
	fob_point int, 
	fob_rank int, 
	is_insurance int,
	league_grade int,
	league_rank int,
	name varchar(50),
	playtime int, 
	point int,
	event_point int, 	-- get_login_param
	player_num int, -- always 1
	-- data from sync_mother_base:
	mother_base_num int,

	mother_base_data json,
	PRIMARY KEY(id),
	FOREIGN KEY(player_id) REFERENCES player(id) ON DELETE CASCADE
);

create table if not exists server_state(
	id int NOT NULL AUTO_INCREMENT,
	nuke_num int, -- get_abolition_count 
	nuke_max int,
	status int,
	abolition_count int,
	notes varchar(500),
	hero_threshold_point int, -- get_login_param
	not_hero_threshold_point int,
	is_able_to_buy_fob4 bool,
	is_stuck_rescue bool,
	online_challenge_task_end_date int, -- get_login_param
	PRIMARY KEY(id)
);

create table if not exists server_text(
	identifier varchar(100) NOT NULL,
	language varchar(4) NOT NULL,
	text varchar(50000),
	PRIMARY KEY(identifier,language)
);

create table if not exists staff_rank_bonus_rate(
	id int NOT NULL AUTO_INCREMENT,
	p1 int,
	p2 int,
	PRIMARY KEY(id)
);

create table if not exists fob_event_task_type(
	-- TODO
	id int NOT NULL,
	PRIMARY KEY(id)
);

create table if not exists challenge_task_reward(
	id int NOT NULL,
	bottom_type int,
	rate int,
	section int,
	reward_type int,
	reward_value int,
	PRIMARY KEY(id)
);

create table if not exists tpp_resource(
	-- TODO
	id int NOT NULL,
	PRIMARY KEY(id)
);

create table if not exists cluster_build_costs(
	-- used in get_login params
	-- see cluster_build_costs->etc
	-- most likely first cluster is local cluster and second one is fob
	-- there will be 1-8 entries, 1-4 for local and 5-8 for fob
	id int NOT NULL,
	gmp int,
	resource_a_count int,
	resource_a_id int,
	resource_b_count int,
	resource_b_id int,
	time_minute int,
	PRIMARY KEY(id),
	FOREIGN KEY(resource_a_id) REFERENCES tpp_resource(id) ON DELETE CASCADE,
	FOREIGN KEY(resource_b_id) REFERENCES tpp_resource(id) ON DELETE CASCADE
);

create table if not exists fob_event_task(
	-- used in get_login params
	-- see fob_event_task_list
	id int NOT NULL AUTO_INCREMENT,
	reward int,
	task_type_id int,
	threshold int,
	PRIMARY KEY(id),
	FOREIGN KEY(task_type_id) REFERENCES fob_event_task_type(id) ON DELETE CASCADE
);

create table if not exists mission(
	id int NOT NULL,
	name varchar(100),
	PRIMARY KEY(id)
);


create table if not exists online_challenge_task(
	id int NOT NULL AUTO_INCREMENT,
	mission_id int,
	reward_id int,
	PRIMARY KEY(id),
	FOREIGN KEY(mission_id) REFERENCES mission(id) ON DELETE CASCADE,
	FOREIGN KEY(reward_id) REFERENCES challenge_task_reward(id) ON DELETE CASCADE
);

create table if not exists server_product_param(
	id int NOT NULL,
	dev_coin int,
	dev_gmp int,
	dev_item_1 int, 
	-- reference?
	dev_item_2 int, 
	-- reference?
	dev_platlv01 int,
	dev_platlv02 int,
	dev_platlv03 int,
	dev_platlv04 int,
	dev_platlv05 int,
	dev_platlv06 int,
	dev_platlv07 int,
	dev_rescount01_value int,
	dev_rescount02_value int,
	dev_resource01_id int,
	dev_resource02_id int,
	dev_skil int,
	dev_special int,
	dev_time int,
	open bool,
	product_type int, 
	-- reference?
	use_gmp int,
	use_rescount01_value int,
	use_rescount02_value int,
	use_resource01_id int,
	use_resource02_id int,
	PRIMARY KEY(id),
	FOREIGN KEY(dev_resource01_id) REFERENCES tpp_resource(id) ON DELETE CASCADE,
	FOREIGN KEY(dev_resource02_id) REFERENCES tpp_resource(id) ON DELETE CASCADE,
	FOREIGN KEY(use_resource01_id) REFERENCES tpp_resource(id) ON DELETE CASCADE,
	FOREIGN KEY(use_resource02_id) REFERENCES tpp_resource(id) ON DELETE CASCADE
);


INSERT INTO url(url_type, url_link, url_version) VALUES('GATE','http://192.168.99.100/tppstm/gate',10),('WEB','http://192.168.99.100/tppstm/main',10),('EULA','http://192.168.99.100/tppstmweb/eula/eula.var',4),('HEATMAP','http://192.168.99.100/tppstmweb/heatmap',0),('DEVICE','http://192.168.99.100/tppstm/main',0)

-- unused params
-- sync_mother_base - sent from client
--
-- -- equip_flag
-- -- equip_grade
-- -- invalid_fob
-- -- local_base_param
-- -- local_base_time
-- -- mother_base_num
-- -- pf_skill_staff
-- -- pickup_open
-- -- section_open
-- -- security_level
-- -- tape_flag
-- -- version
--
-- get_login_param - sent from server
-- -- fob_event_task_result_param
-- ---- event_id
-- ---- normal_defense_same_time_bonus
-- ---- event_sneak_clear_point_max
-- ---- event_sneak_clear_point_min
-- ---- ranking_espi_event_ids
-- ---- ranking_pf_event_ids
