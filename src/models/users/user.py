import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

__author__ = "inchan"

class User(object):
    def __init__(self, email, password, _id = None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        ##this method verifies an email password combo
        ## email : user email
        ## password : hashed password
        ## param :
        user_data = Database.find_one("user", {"email": email})
        if user_data is None:

            raise UserErrors.UserNotExistsError('Your user does not exist.')
            pass
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError('Your password was wrong.')
            pass

        return True

