from constants.const import Const


class ErrorCode(Const):
    """
    1. 系統錯誤
    """
    BASE_ERROR = 1001  # 基本錯誤
    UNKNOWN_ERROR = 1002  # 未知錯誤

    """
    2. 資料錯誤
    """
    # SERVER(20-)
    DATA_ERROR = 2001  # 資料錯誤
    DATA_MISSING = 2002  # 資料遺漏
    DATA_REQUIRED = 2004  # 必須提供的資料
    DATA_IMMUTABLE = 2005  # 不可變動

    # CLIENT(21-)
    PAYLOAD_ERROR = 2101  # 酬載錯誤
    PAYLOAD_MISSING_KEY = 2102  # 缺少必要鍵
    PAYLOAD_UNEXPECTED_TYPE = 2103  # 型別錯誤
    JSON_DECODE_ERROR = 2104  # JSON 格式錯誤

    """
    3. 操作錯誤
        - 授權錯誤
        - 操作錯誤
        - 驗證錯誤
        - 檢查錯誤
    """

    # 簡述(30-)
    INVALID_OPERATION = 3001  # 無效的操作
    INVALID_PERMISSION = 3002  # 權限不足
    INVALID_ACCESS_TOKEN = 3003  # 無效通行証書
    INVALID_REFRESH_TOKEN = 3004  # 無效重置証書
    INVALID_PHONE_NUMBER = 3005  # 無效手機號碼
    INVALID_EMAIL = 3006  # 無效信箱
    INVALID_USERNAME = 3007  # 無效使用者名稱
    INVALID_PASSWORD = 3008  # 無效密碼
    INVALID_VERIFY_CODE = 3009  # 無效驗證代碼
    INVALID_KEYWORD_LENGTH = 3010  # 無效關鍵字長度
    INVALID_FILE_SIZE = 3011  # 無效檔案大小
    INVALID_IMAGE_FORMAT = 3012  # 無效圖片格式
    INVALID_BIRTHDAY_FORMAT = 3013  # 無效生日格式
    INVALID_IP_ADDRESS = 3014  # 無效遠端IP地址

    # 細述(31-)
    ACCESS_TOKEN_MISSING = 3101  # 未包含通行証
    ACCESS_TOKEN_IS_EXPIRED = 3102  # 通行証過期

    """
    9.  客製化錯誤
    """

    EXTERNAL_API_CONNECTION_ERROR = 9001  # 外部服務連線錯誤
