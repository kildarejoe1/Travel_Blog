__author__="hmorrin"
from database import Database

class Post(object):
    def __init__(self,blog_id,title,content,author,id):
        self.title=title
        self.content=content
        self.author=author
        self.id = id


    def save_to_db(self):
        Database.insert(table_name="posts", data=self.json())

    @staticmethod
    def retrieve_from_db(id):
        data= Database.find_one(table_name="posts",query={"id":id})

    def json(self):
        return {
            "id":self.id,
            "blog_id":self.author,
            "content":self.content,
            "title":self.title,
            "created_date":self.created_date
        }
