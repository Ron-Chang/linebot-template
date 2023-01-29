class Const:
    _STR_FORMAT_TYPE = {'title', 'upper', 'lower'}

    _INVALID_TYPES = {
        classmethod,
        staticmethod
    }

    @classmethod
    def value_to_key(cls, value):
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPES:
                continue
            if v == value:
                return k
        return None

    @classmethod
    def key_to_value(cls, key):
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPES:
                continue
            if k == key:
                return v
        return None

    @classmethod
    def get_keys(cls):
        return [k for k, v in cls.__dict__.items() if type(v) not in cls._INVALID_TYPES and not k.startswith('_')]

    @classmethod
    def get_values(cls):
        return [v for k, v in cls.__dict__.items() if type(v) not in cls._INVALID_TYPES and not k.startswith('_')]

    @classmethod
    def to_dict(cls, reverse=False, fmt=None, delimiter=None):
        """
        class Status(_Const):
            NOT_STARTED = 1
            STARTED = 2
            COMPLETED = 3

        to_dict()
            -> {'NOT_STARTED': 1, 'STARTED': 2, 'COMPLETED': 3}

        to_dict(reverse=True, fmt='lower' or 'title', delimiter=' ')
            -> {1: 'not started', 2: 'started', 3: 'completed'}
        """
        delimiter = delimiter or ' '
        if not isinstance(delimiter, str):
            raise ValueError(f'Invalid delimiter: {delimiter}')
        fmt = fmt or 'upper'
        if fmt.lower() not in cls._STR_FORMAT_TYPE:
            raise ValueError(f'Invalid format type {fmt}')
        result = dict()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPES:
                continue
            if '_' not in k or delimiter != '_':
                k = k.replace('_', delimiter)
            k = getattr(k, fmt.lower())()
            data = {v: k} if reverse else {k: v}
            result.update(data)
        return result


