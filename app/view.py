from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    column_display_pk = True
    column_labels = {
        'id' : 'ID',
        'username': 'Имя пользователья',
        'last_seen': 'Последний вход',
        'image_user': 'Аватар',
        'posts': 'Посты',
        'email': 'Емайл',
        'password': 'Пароль',
        'role': 'Роль',
        'file': 'Выберите изображение'
    }

    column_list = ['id', 'role', 'username', 'email', 'password', 'last_seen', 'image_user']
    