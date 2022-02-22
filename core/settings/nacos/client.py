import json

import nacos

from core import settings
from core.settings.nacos.watchers import refresh_settings


SERVER_IP = settings.app_settings.NACOS_SERVER_IP
SERVER_PORT = settings.app_settings.NACOS_SERVER_PORT
NAMESPACE = settings.app_settings.NACOS_NAMESPACE
GROUP = settings.app_settings.NACOS_GROUP
DATA_ID = settings.app_settings.NACOS_DATA_ID

SERVER_ADDRESSES = f"http://{SERVER_IP}:{SERVER_PORT}"

client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
# #client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")

# 获取配置，初始化项目配置
config_data = client.get_config(DATA_ID, GROUP)
settings.app_settings = settings.APPSettings(**json.loads(config_data))

if not settings.app_settings.CELERY_SERVER:
    print('CELERY_SERVER:', settings.app_settings.CELERY_SERVER)
    # 增加配置变更监听
    client.add_config_watchers(DATA_ID, GROUP, [refresh_settings])
