from datetime import datetime

class Comment:
    def __init__(self, name, text):
        self.name = name
        self.text = text

class Post:
    def __init__(self, title, body, comments = [], likes = 0, shares = 0):
        self.title = title
        self.body = body
        self.likes = likes
        self.shares = shares
        self.comments = comments
        self.create_time = datetime.now()



