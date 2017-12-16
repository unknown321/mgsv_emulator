import os

#============================================================================

# you need a static key to decode communications between client and server
# where to get: inside mgsvtpp.exe
STATIC_KEY_FILE_PATH = '/var/www/mgsv_server/static_key.bin'

#============================================================================
# logging

LOG_FILE_PATH = '/var/log/app.log'
LOGGER_NAME = 'mgsv'

#============================================================================
# proxy

# PROXY_ALL will proxy ALL commands to konami servers
PROXY_ALL = False

# PROXY_ALWAYS is a list of commands that will be always proxyfied 
# regardless of PROXY_ALL value
PROXY_ALWAYS = ['CMD_REQAUTH_HTTPS', 'CMD_AUTH_STEAMTICKET']

#============================================================================
# client authentication
# in general, there are two cases:
#  - if you want to emulate the client, set your steamid and magic_hash
#  - if you want to run a server, set them empty - this is important.
#     In case you set them non-empty, run the server and database goes down, these
#     credentials will be used for other players - thus sending wrong data about 
#     your account
#
#  you can also set them to yours, enable PROXY_ALL (or add commands into PROXY_ALWAYS)
#  and run server locally to capture commands for debugging
#
# STEAM_ID is client's steamid, duh
STEAM_ID = '76561197960287930'

# MAGIC_HASH is a hash returned from konami in response to CMD_REQAUTH_HTTPS
# essentially a password
MAGIC_HASH = 'QM8ZNBWTIFY7PFFBXVL6NQ=='
