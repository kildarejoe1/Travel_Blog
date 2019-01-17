__author__="hmorrin"
from database import Database

class Post(object):
    def __init__(self,blog_id,title,content,author,date,id):
        self.title=title
        self.content=content
        self.author=author
        self.id = id


    def save_to_db(self):
        Database.insert(collection="posts", data=self.json())

    @staticmethod
    def retrieve_from_db(id):
        data= Database.find_one(collection="posts",query={"id":id})

    def json(self):
        return {
            "id":self.id,
            "blog_id":self.author,
            "content":self.content,
            "title":self.title,
            "created_date":self.created_date
        }

        
