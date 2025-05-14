import os
import sys

import loguru

from util.CppRequest import CppRequest
from util.KVDatabase import KVDatabase
from util.TimeService import TimeService





BASE_DIR = os.path.dirname(os.path.realpath(sys.executable))
TEMP_PATH = os.path.join(BASE_DIR,'tmp')
os.makedirs(TEMP_PATH, exist_ok=True)
loguru.logger.info(f"设置路径 TEMP_PATH={TEMP_PATH} BASE_DIR={BASE_DIR}")
configDB = KVDatabase(os.path.join(BASE_DIR, "config.json"))
if not configDB.contains("cookie_path"):
    configDB.insert("cookie_path", os.path.join(BASE_DIR, "cookies.json"))
main_request = CppRequest(cookies_config_path=configDB.get("cookie_path"))
global_cookieManager = main_request.cookieManager

## 时间
time_service = TimeService()
time_service.set_timeoffset(time_service.compute_timeoffset())
