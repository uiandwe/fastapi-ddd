from dataclasses import dataclass
from os import path, environ
from typing import List


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR: str = path.dirname(path.dirname(
        path.dirname(path.abspath(__file__))))
    DB_POOL_RECYCLE: int = 900
    DB_POOL_SIZE: int = 20
    DB_ECHO: bool = True
    DEBUG: bool = False
    TEST_MODE: bool = False

    def __getitem__(self, key):
        return getattr(self, key)


@dataclass
class StgConfig(Config):
    DB_URL: str = environ.get("DB_URL", "")
    DB_URL_PRD: str = environ.get("DB_URL_PRD", "")
    AWS_DB_URL: str = environ.get("AWS_DB_URL", "")
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    API_KEY = "1234qwer"
    API_KEY_NAME = "access_token"



@dataclass
class LocalConfig(Config):
    SECRET_KEY = "C9584AC7C07EA01132F7E1423FB6C6F20B5651E9"
    DB_URL: str = environ.get("DB_URL", "")
    DB_URL_PRD: str = environ.get("DB_URL_PRD", "")
    AWS_DB_URL: str = environ.get("AWS_DB_URL", "")
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    API_KEY = "1234qwer"
    API_KEY_NAME = "access_token"


@dataclass
class ProdConfig(Config):
    SECRET_KEY = "C9584AC7C07EA01132F7E1423FB6C6F20B5651E9"
    DB_URL: str = environ.get("DB_URL", "")
    DB_URL_PRD: str = environ.get("DB_URL_PRD", "")
    AWS_DB_URL: str = environ.get("AWS_DB_URL", "")
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    API_KEY = "1234qwer"
    API_KEY_NAME = "access_token"


@dataclass
class DevConfig(Config):
    SECRET_KEY = "C9584AC7C07EA01132F7E1423FB6C6F20B5651E9"
    DB_URL: str = environ.get("DB_URL", "")
    DB_URL_PRD: str = environ.get("DB_URL_PRD", "")
    AWS_DB_URL: str = environ.get("AWS_DB_URL", "")
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    API_KEY = "1234qwer"
    API_KEY_NAME = "access_token"


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig, local=LocalConfig,
                  dev=DevConfig, stg=StgConfig)
    return config[environ.get("API_ENV", "local")]()
