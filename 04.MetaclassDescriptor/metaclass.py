class CustomMeta(type):
    prefix = "custom_"

    @staticmethod
    def prefixed_setattr(prefix):
        def setattr(self, name, value):
            if name.startswith(prefix):
                new_name = name
            else:
                new_name = prefix + name
            self.__dict__[new_name] = value
        return setattr

    @staticmethod
    def prefix_dict_keys(dct, prefix):
        prefixed_dct = {}
        for key, value in dct.items():
            if (key[:2] == "__") and (key[-2:] == "__") or key.startswith(prefix):
                prefixed_dct[key] = value
            else:
                prefixed_dct[prefix + key] = value
        return prefixed_dct

    def __new__(cls, name, bases, classdict, **kwargs):
        new_classdict = cls.prefix_dict_keys(classdict, cls.prefix)
        new_classdict["__setattr__"] = cls.prefixed_setattr(cls.prefix)
        new_cls = super().__new__(cls, name, bases, new_classdict, **kwargs)
        return new_cls


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
