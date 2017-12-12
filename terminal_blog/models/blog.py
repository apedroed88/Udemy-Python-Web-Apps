import uuid
import datetime
from database import Database
from models.post import Post


class Blog(object):

    def __init__(self, title, description, author, id=None):
        self.title = title
        self.description = description
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input('Input blog title here: ')
        content = input('Write post content: ')
        date = input('Date post was created, leave it blank to be chosen today: (format DDMMYY)')
        post = Post(id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=datetime.datetime.strptime(date, "%d%m%Y"))
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.blog_id)

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'blog_id': self.blog_id
        }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'blog_id': id})

        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])