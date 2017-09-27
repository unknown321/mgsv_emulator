-- create database mgsv_server;
use mgsv_server;

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

-- player parameters, WIP
create table if not exists player(
	id int NOT NULL AUTO_INCREMENT,
	name_plate_id int, 
	PRIMARY KEY(id),
	FOREIGN KEY(name_plate_id) REFERENCES name_plate(id)
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
	session_id varchar(32),			-- session identifier used for further communications, expires if there was no commands for client for 2 mins
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
	player_num int, -- always 1
	-- data from sync_mother_base:
	mother_base_num int,

	mother_base_data json,
	PRIMARY KEY(id),
	FOREIGN KEY(player_id) REFERENCES players(id) ON DELETE CASCADE
);


-- unused params
-- sync_mother_base
--
---- equip_flag
---- equip_grade
---- invalid_fob
---- local_base_param
---- local_base_time
---- mother_base_num
---- pf_skill_staff
---- pickup_open
---- section_open
---- security_level
---- tape_flag
---- version
