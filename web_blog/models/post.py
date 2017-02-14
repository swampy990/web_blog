import uuid
import datetime

from web_blog.common.Database import Database

__author__ = 'Craig'

class Post(object):
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blogID = blog_id
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id
        self.created_date = date

    def savedb(self):
        Database.insert(collection ='posts', data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blogID': self.blogID,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data =  Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blogID': id})]


