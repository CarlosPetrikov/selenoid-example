# -*- coding: latin1 -*-
from selenium import webdriver
#from selenium.webdriver.common.by import By
from loguru import logger

from config.settings import (
    SELENOID_IP,
    BROWSER_CAPABILITIES
)

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

#---------------------------------[CONFIG]----------------------------------#

logger.add("./logs/info.log", rotation="50 MB", level="INFO", filter=lambda record: record["level"].name == "INFO")
logger.add("./logs/debug.log", rotation="50 MB", level="DEBUG", filter=lambda record: record["level"].name == "DEBUG")
logger.add("./logs/exceptions.log", rotation="50 MB", level="ERROR")

#----------------------------------[MAIN.]----------------------------------#

try:
    chrome = webdriver.Remote(
        command_executor=f"http://{SELENOID_IP}:4444/wd/hub",
        desired_capabilities=BROWSER_CAPABILITIES
    )
    
    chrome.get("https://docs.python.org/3/")
    logger.info("Website accessed! :D")
    
    input("Press any key to exit...")
    chrome.quit()
    
except:
    logger.exception("Exception when accessing the website! Closing remote chrome...")

    try:
        chrome.quit()
    except:
        pass
