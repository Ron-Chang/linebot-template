import json
from app import app
from handlers.redis_key import RedisKey


class DataCache:
    _WILDCARD = '*'

    @classmethod
    def set_balance(cls, uuid, data, user=None):
        user = user or cls._DEFAULT_USER

        name = RedisKey.get_data_key(user, uuid)
        value = json.dumps(data)
        app.rs.set(name=name, value=value)

    @classmethod
    def get_keys(cls, user):
        name = RedisKey.get_data_key(user=user, uuid=cls._WILDCARD)
        return [_.split(':').pop() for _ in app.rs.scan_iter(name)]

    @staticmethod
    def _iterate_by_key(name):
        for key in app.rs.scan_iter(name):
            yield app.rs.get(key)

    @classmethod
    def get_data(cls, user=None, uuid=None):
        name = RedisKey.get_data_key(
            user=user or cls._WILDCARD,
            uuid=uuid or cls._WILDCARD,
        )
        return [json.loads(_) for _ in cls._iterate_by_key(name)]
