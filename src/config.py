import os

from pydantic import BaseSettings


class Settings(BaseSettings):

    TESTING: bool = False
    DEBUG: bool = False

    # --- Config --- #
    # 系統名稱
    SYSTEM_NAME: str
    # 產品名稱
    APP_NAME: str
    # 產品版本
    APP_VERSION: str
    # 產品環境(控制App行為)
    STAGE: str
    # 服務器密鑰
    SECRET_KEY: str

    # --- Service --- #

    # 資料庫設定
    # - Redis
    RS_HOST: str = 'linebot-template-redis'
    RS_PORT: str = '6379'

    # LineBotAPI
    LINEBOT_SECRET: str
    LINEBOT_ACCESS_TOKEN: str


class Testing(Settings):

    TESTING = True
    DEBUG = True


def get_settings():
    stage = os.getenv('STAGE')
    if stage == 'dev':
        return Testing()
    return Settings()


Config = get_settings()
