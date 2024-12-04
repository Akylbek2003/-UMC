from flask import Flask, request, session, redirect, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.models import db, User, Post
from app.admin import initialize_admin
from flask_migrate import Migrate
from app.routes import register_routes
from flask_babel import Babel
# Создание приложения
app = Flask(__name__, template_folder="app/templates")
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = 'static/uploads/videos/'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv', 'webm'}
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
# Инициализация расширений
db.init_app(app)
register_routes(app)
migrate = Migrate(app, db)
babel = Babel(app)
# Регистрация маршрутов и админки
initialize_admin(app, db)

# Создание таблиц при запуске
with app.app_context():
    db.create_all()

# Запуск приложения
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
