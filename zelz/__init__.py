import os
from flask import Flask
import threading
app = Flask(__name__)

import signal
import sys
import time
import heroku3

from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .helpers.functions.converter import Convert
from .helpers.functions.musictool import *
from .helpers.utils.utils import runasync
from .sql_helper.globals import addgvar, delgvar, gvarstatus
    
    

def original():
   
    __version__ = "3.3.3"
    __license__ = "حقـوق سـورس زدثــون"
    __author__ = "زدثــون <https://T.me/ZThon>"
    __copyright__ = "ZThon Source (C) 2020 - 2024  " + __author__
    
    zedub.version = __version__
    LOGS = logging.getLogger("زدثــون")
    bot = zedub
    
    StartTime = time.time()
    zedversion = "3.3.3"
    
    if Config.UPSTREAM_REPO == "zel":
        UPSTREAM_REPO_URL = "https://github.com/ZThon-Ar/ZTZ"
    else:
        UPSTREAM_REPO_URL = Config.UPSTREAM_REPO
    
    if Config.PRIVATE_GROUP_BOT_API_ID == 0:
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
            Config.BOTLOG = False
            Config.BOTLOG_CHATID = "me"
        else:
            Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
            Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
            Config.BOTLOG = True
    else:
        if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
            Config.BOTLOG_CHATID = int(f"-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
        else:
            Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
        Config.BOTLOG = True
    
    if Config.PM_LOGGER_GROUP_ID == 0:
        if gvarstatus("PM_LOGGER_GROUP_ID") is None:
            Config.PM_LOGGER_GROUP_ID = -100
        else:
            Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
    elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
        Config.PM_LOGGER_GROUP_ID = int(f"-" + str(Config.PM_LOGGER_GROUP_ID))
    
   HEROKU_API_KEY = None
   HEROKU_APP_ID = None
   HEROKU_APP = None
    
    
    # Global Configiables
    COUNT_MSG = 0
    USERS = {}
    COUNT_PM = {}
    LASTMSG = {}
    CMD_HELP = {}
    ISAFK = False
    AFKREASON = None
    CMD_LIST = {}
    SUDO_LIST = {}
    # for later purposes
    INT_PLUG = ""
    LOAD_PLUG = {}
    
    # Variables
    BOTLOG = Config.BOTLOG
    BOTLOG_CHATID = Config.BOTLOG_CHATID
    PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID

threading.Thread(target=original).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
