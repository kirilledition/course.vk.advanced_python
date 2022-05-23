class ValidatorDescriptor:
    def validation(self, value):
        return True

    def __init__(self, field_name):
        self.field_name = field_name

    def __set__(self, obj, val):
        if self.validation(val):
            setattr(obj, self.field_name, val)
        else:
            raise AttributeError()

    def __get__(self, obj, obj_type):
        return getattr(obj, self.field_name)


class Integer(ValidatorDescriptor):
    def validation(self, value):
        return isinstance(value, int) and not isinstance(value, bool)


class String(ValidatorDescriptor):
    def validation(self, value):
        return isinstance(value, str)


class PositiveInteger(Integer):
    def validation(self, value):
        return super().validation(value) and value > 0


class Data:
    num = Integer("_num")
    name = String("_name")
    price = PositiveInteger("_price")

    def __init__(self):
        pass
