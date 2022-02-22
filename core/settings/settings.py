"""
https://pydantic-docs.helpmanual.io/usage/settings/
在多个方式为同一字段指定值的情况下Settings，选择值确定如下（按优先级降序排列）：
 - 传递给Settings类初始化程序的参数。
 - 环境变量，例如my_prefix_special_function如上所述。
 - 从 dotenv ( .env) 文件加载的变量。
 - 从秘密目录加载的变量。
 - 模型的默认字段值Settings。

改变优先级
自定义加载源
"""
from typing import Optional

from pydantic import BaseSettings


# class LoggerSettings(BaseSettings):
#     """日志配置"""
#


class APPSettings(BaseSettings):
    # Field(..., env=...)  # 设置别名，环境变量中的名字
    ENV: Optional[str] = None
    TITLE: Optional[str] = None
    DESCRIPTION: Optional[str] = None
    VERSION: Optional[str] = None

    USERNAME: Optional[str] = None

    # nacos
    NACOS_SERVER_IP: str
    NACOS_SERVER_PORT: str
    NACOS_SERVER_ADDRESSES: str
    NACOS_NAMESPACE: str
    NACOS_USERNAME: Optional[str] = None
    NACOS_PASSWORD: Optional[str] = None
    NACOS_GROUP: str
    NACOS_DATA_ID: str

    CELERY_SERVER: Optional[bool] = False
    CELERY_NAME: Optional[str] = None
    RABBITMQ_USER: Optional[str] = None
    RABBITMQ_PASSWORD: Optional[str] = None
    RABBITMQ_SERVER: Optional[str] = None
    RABBITMQ_PORT: Optional[str] = None

    MYSQL_USER: Optional[str] = None
    MYSQL_PASSWORD: Optional[str] = None
    MYSQL_SERVER: Optional[str] = None
    MYSQL_PORT: Optional[str] = None
    MYSQL_DB: Optional[str] = None

    class Config:
        env_prefix = 'FASTAPI_APP_'
        # case_sensitive = True  # 区分大小写

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            """文件加载 > 环境变量 > Nacos加载（传递给Settings类初始化程序的参数） > 默认字段值"""
            return env_settings, init_settings
