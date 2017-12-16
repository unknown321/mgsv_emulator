import logging
from mgsv_emulator.server.entity.User import User
from mgsv_emulator import settings
logger = logging.getLogger(settings.LOGGER_NAME)

class PROXY_PRE_CMD_REQAUTH_HTTPS():
    def __init__():
        pass
    def execute(data):
        pass

class PROXY_POST_CMD_REQAUTH_HTTPS():
    def __init__():
        pass
    def execute(data):
        # check if user exists
        # if not - create using info from data
        user = User()
        pass
