class DictToClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if type(v) == dict:
                self.__dict__.update({k: DictToClass(**v)})
            else:
                self.__dict__.update({k: v})
