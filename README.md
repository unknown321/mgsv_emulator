# mgsv_emulator
mgsv client/server emulator

Types of encryption implemented: COMMON, COMPOUND.

# Encryption details
Every message between server and client is encrypted using blowfish algorythm.
Unfortunately it slightly differs from realisation provided here (https://www.schneier.com/academic/blowfish/download.html), so I had to rewrite it from scratch.

Decryption process:

 * decode base64-encoded message into bytestream
 * decode bytestream using static blowfish key (hardcoded into exe) into json message
 * message['data'] is usually base64-decoded message
 * if 'session_crypto' is true, then contents of message['data'] are encrypted with blowfish using session cryptokey provided by server during auth phase
 * if 'compress' is true, then decoded message['data'] is also compressed using zlib

Message with compression and encryption:

    base64(
        blowfish_static(
            base64(
                blowfish_session(
                    zlib('test')
                )
            )
        )

Encryption process is the same, but backwards.

# How to use
Provide your credentials in settings.py (steamid and magic_hash parsed from previously captured session). Steam_ticket is not required.
Dump static_key from exe (or ask me very nicely).

Client:

    from emulator import Client
    c = Client()
    c.login()

login() will automatically parse requests and save session cryptokey (so you won't have to manually use it every time).
Afterwards, feel free to call any command available, see https://github.com/unknown321/mgsv_nuke_watcher as an example.

# Server status:

Done:
 * CMD_GET_URLLIST
 * CMD_GET_SVRLIST
 * CMD_GET_INFORMATIONLIST - Online messages that pop up after logging in
 * CMD_GET_FOB_STATUS - Your win-lose records for attack and defense
 * CMD_GET_SVRTIME - speaks for itself
 * CMD_GET_CHALLENGE_TASK_TARGET_VALUES - FOB and PF records

Todo list:

 * Login procedure, which includes generation of crypto keys, session id, etc (CMD_AUTH_STEAMTICKET, CMD_REQAUTH_HTTPS). This will involve setting up mysql server to save user data.
 * Player list stuff (CMD_GET_PLAYERLIST, CMD_SET_PLAYERLIST)
 * Challenge task rewards (414 tasks from konami)
 * Login params (CMD_GET_LOGIN_PARAM), which includes cluster_build_costs, fob_event_task_list, online_challenge_task, server_product_params, server_texts and staff_rank_bonus_rates.
 * Figure out parameters sent by client in CMD_SEND_BOOT
 * Figure out parameters sent by client in CMD_SYNC_MOTHER_BASE
 * CMD_SYNC_RESOURCE - order of parameters is unknown
 * CMD_SYNC_SOLDIER_BIN - figure out how to decode list of soldiers, there was some info on cheatengine forums
 * CMD_GET_OWN_FOB_LIST - parameters construct_param and mother_base_id look weird 
 * CMD_MINING_RESOURCE - break_time parameter?

Low-priority:

 * CMD_GET_COMBAT_DEPLOY_RESULT - need to send troops and parse the response first
 * CMD_GET_ONLINE_PRISON_LIST - same as above

Login procedure (from start to title menu):

    CMD_GET_URLLIST
    CMD_GET_SVRLIST
    CMD_GET_SVRTIME
    CMD_AUTH_STEAMTICKET
    CMD_REQAUTH_HTTPS
    CMD_SEND_IPANDPORT
    CMD_GET_PLAYERLIST
    CMD_SET_CURRENTPLAYER
    CMD_GET_ABOLITION_COUNT
    CMD_GET_CHALLENGE_TASK_REWARDS
    CMD_GET_LOGIN_PARAM
    CMD_GET_INFORMATIONLIST
    CMD_SEND_BOOT
    CMD_GET_COMBAT_DEPLOY_RESULT
    CMD_GET_SERVER_ITEM_LIST
    CMD_SYNC_MOTHER_BASE
    CMD_SYNC_RESOURCE
    CMD_SYNC_SOLDIER_BIN
    CMD_GET_FOB_STATUS
    CMD_GET_ONLINE_PRISON_LIST
    CMD_GET_OWN_FOB_LIST
    CMD_MINING_RESOURCE
    CMD_GET_SVRTIME
    CMD_GET_CHALLENGE_TASK_TARGET_VALUES