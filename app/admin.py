from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Post, Tag, Comment, Participation
from app.view import UserView

def initialize_admin(app, db):
    admin = Admin(app, name='Админ', template_mode='bootstrap4')
    admin.add_view(UserView(User, db.session, name='Пользователи'))
    admin.add_view(ModelView(Post, db.session, name='Посты'))
    admin.add_view(ModelView(Participation, db.session, name='Участие'))
    admin.add_view(ModelView(Tag, db.session, name='Тэги'))
    admin.add_view(ModelView(Comment, db.session, name='Комментарии'))
    
    return app