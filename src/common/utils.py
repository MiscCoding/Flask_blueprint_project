__author__ = 'inchan'

from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w]+\.)+[\w]+$') #hello
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        ##return pbkdf12_sha512 encrypted password

        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):

        return pbkdf2_sha512.verify(password, hashed_password)
