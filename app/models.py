from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100), nullable=True)  # разрешаем NULL
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    image_user = db.Column(db.String(225), nullable=True, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete-orphan")

    
    def __repr__(self):
        return f"<User {self.name}>"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    image_post = db.Column(db.String(255), nullable=True, default='default.jpg')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    tags = db.relationship('Tag', backref='tag_post', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return self.title 

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
   
    def __repr__(self):
        return self.name 

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return self.name 

class Stroage(db.Model):
    __tablename__ = 'stroage'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    path = db.Column(db.String(128))
    type = db.Column(db.String(4))
    create_date = db.Column(db.DateTime)

class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False, default='')  # default значение

