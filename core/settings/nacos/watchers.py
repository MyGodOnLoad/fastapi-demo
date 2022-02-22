import json


def parser_config(config):
    """解析nacos数据"""
    content = config.get('content')
    config = json.loads(content)
    return config


def refresh_settings(config):
    """刷新配置"""
    config = parser_config(config)
    print('config: ', config)
    from core import settings
    settings.app_settings = settings.APPSettings(**config)
