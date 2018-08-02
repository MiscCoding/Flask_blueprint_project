__author__ = 'inchan'


class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotExistsError(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectPasswordError(Exception):
    def __init__(self, message):
        self.message = message

class UserAlreadyRegisteredError(UserError):
    pass

class InvalidEmailError(UserError):
    pass