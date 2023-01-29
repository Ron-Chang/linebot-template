import os
from datetime import datetime
from pprint import pformat


class Console:

    DEBUG_MODE = os.environ.get('LINEBOT_DEBUG_MODE', False)

    try:
        _TERM_WIDTH, _ = os.get_terminal_size(0)
    except BaseException:
        _TERM_WIDTH = 79

    class Level:
        DEBUG = 10
        INFO = 20
        WARNING = 30
        ERROR = 40
        CRITICAL = 50

    class Style:
        """ Style.WHITE + Style.RED_B = Style.WHITE_ON_RED """
        _PX = '\033['
        # style
        ENDC = f'{_PX}0m'
        BOLD = f'{_PX}1m'
        UNDERLINE = f'{_PX}4m'
        # normal
        BLACK = f'{_PX}30m'
        RED = f'{_PX}31m'
        GREEN = f'{_PX}32m'
        YELLOW = f'{_PX}33m'
        BLUE = f'{_PX}34m'
        MAGENTA = f'{_PX}35m'
        CYAN = f'{_PX}36m'
        WHITE = f'{_PX}37m'
        # BG
        BLACK_B = f'{_PX}40m'
        RED_B = f'{_PX}41m'
        GREEN_B = f'{_PX}42m'
        YELLOW_B = f'{_PX}43m'
        BLUE_B = f'{_PX}44m'
        MAGENTA_B = f'{_PX}45m'
        CYAN_B = f'{_PX}46m'
        WHITE_B = f'{_PX}47m'
        # vivid
        BLACK_VIVID = f'{_PX}90m'
        RED_VIVID = f'{_PX}91m'
        GREEN_VIVID = f'{_PX}92m'
        YELLOW_VIVID = f'{_PX}93m'
        BLUE_VIVID = f'{_PX}94m'
        MAGENTA_VIVID = f'{_PX}95m'
        CYAN_VIVID = f'{_PX}96m'
        WHITE_VIVID = f'{_PX}97m'

    ENABLE_PRINT = True
    DEFAULT_LEVEL = Level.INFO

    _BADGE_PATTERN = f'{{style}}[{{level}}]{Style.ENDC} '
    _BADGE_MAP = {
        Level.DEBUG: _BADGE_PATTERN.format(style=Style.GREEN_VIVID, level='D'),
        Level.INFO: _BADGE_PATTERN.format(style=Style.BLUE_VIVID, level='I'),
        Level.WARNING: _BADGE_PATTERN.format(style=Style.YELLOW_VIVID, level='W'),
        Level.ERROR: _BADGE_PATTERN.format(style=Style.RED_VIVID, level='E'),
        Level.CRITICAL: _BADGE_PATTERN.format(style=Style.RED_VIVID + Style.BOLD, level='C'),
    }

    @classmethod
    def format(
        cls,
        msg: str = None,
        level: int = None,
        tag: str = None,
        head: str = None,
        tail: str = None,
        dye: str = None,
        is_fmt: bool = True,
        has_time: bool = True,
    ) -> str:
        now = str()
        if has_time:
            now = f'{str(datetime.now())[:-3]} '

        badge = cls._BADGE_MAP.get(level or cls.DEFAULT_LEVEL)
        if not badge and isinstance(level, str):
            badge = f'{cls.Style.MAGENTA}[{level:8}]{cls.Style.ENDC} '

        dye = dye or str()

        target = str()
        if tag and isinstance(tag, (str, int)):
            target = f'[{tag}] '

        body = msg or str()
        if is_fmt and isinstance(msg, (dict, set, list, tuple)):
            body = f'\n{pformat(msg)}'

        head_div = str()
        if head and isinstance(head, str):
            head = head * cls._TERM_WIDTH
            head_div = f'{head[:cls._TERM_WIDTH]}\n'

        tail_div = str()
        if tail and isinstance(tail, str):
            tail = tail * cls._TERM_WIDTH
            tail_div = f'\n{tail[:cls._TERM_WIDTH]}'

        return (
            f'{head_div}'
            f'{now}{badge}{dye}{target}{body}{cls.Style.ENDC}'
            f'{tail_div}'
        )

    @classmethod
    def log(
        cls,
        msg: str = None,
        level: int = None,
        tag: str = None,
        head: str = None,
        tail: str = None,
        dye: str = None,
        is_fmt: bool = True,
        has_time: bool = True,
    ) -> None:
        if not cls.ENABLE_PRINT:
            return None
        level = level or cls.DEFAULT_LEVEL
        if not cls.DEBUG_MODE and level < cls.Level.INFO:
            return None
        output = cls.format(
            msg=msg,
            level=level,
            tag=tag,
            head=head,
            tail=tail,
            dye=dye,
            is_fmt=is_fmt,
            has_time=has_time,
        )
        print(output)
