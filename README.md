from dbs import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    english = db.Column(db.Integer, default=0)
    python = db.Column(db.Integer, default=0)
    c = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return "<student id:{} name:{} english:{} python:{} c:{}>".format(self.id, self.name, self.english, self.python, self.c)
