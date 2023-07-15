class PersonValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.message, self.value)


class PersonTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong type for {}: {}".format(self.message, type(self.value))


class DateValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.message, self.value)


class DateTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong type for {}: {}".format(self.message, type(self.value))



