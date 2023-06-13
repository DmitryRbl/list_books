from config import db
 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text())
    info = db.Column(db.Text())
    slug = db.Column(db.String(50))

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.Text())
    read = db.Column(db.Boolean())

    def get(self):
        return {"id": self.id, "title": self.title, "author": self.author, "read": self.read}
    def set(self, new_self):
        self.read = new_self['read']
        self.title = new_self['title']
        self.author = new_self['author']