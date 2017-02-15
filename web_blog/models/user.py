import uuid

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

    def register(self):
        pass

    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def savedb(self):
        pass

