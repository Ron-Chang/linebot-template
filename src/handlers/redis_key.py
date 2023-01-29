class RedisKey:

    @staticmethod
    def get_data_key(user, uuid):
        return f'data:{user}:{uuid}'
