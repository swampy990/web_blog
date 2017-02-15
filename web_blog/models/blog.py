import uuid
import datetime

from web_blog.common.Database import Database
from web_blog.models.post import Post

__author__ = 'craig'


class Blog(object):
    def __init__(self, author, author_id, title, description, _id=None):
        self.author = author
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id
        self.author_id = author_id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,
                    author=self.author,
                    title=title,
                    content=content,
                    created_date=date)
        post.savedb()

    def get_post(self):
        return Post.from_blog(self._id)

    def savedb(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'author_id': self.author_id,
            'title': self.title,
            'description': self.description,
            'id': self._id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id} )
        return cls(**blog_data)

    @classmethod
    def find_by_autor_id(cls, author_id):
        blogs = Database.find(collection='blogs',
                              query={'author_id': author_id})
        return [cls(**blog) for blog in blogs]
