import uuid
from flask import session

from web_blog.common.Database import Database
from web_blog.models.blog import Blog

__author__='Craig'

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self.id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

        pass

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            # check the password
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:
            # User does not exist so user can be created
            new_user = cls(email, password)
            new_user.savedb()
            session['email'] = email
            return True
        else:
            # user already exists
            return False

    @staticmethod
    def login(user_email):
        # Login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        return Blog.find_by_autor_id(self._id)

    def json(self):
        return {
            "email": self.email,
            "_id": self.id,
            "password": self.password
        }

    def savedb(self):
        Database.insert("users", self.json())

