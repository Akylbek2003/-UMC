from flask import request, session, redirect, jsonify, render_template, current_app
from sqlalchemy import desc
from app.models import Participation
import os
import uuid
from werkzeug.utils import secure_filename
from app.models import db, Participation

def register_routes(app):
    @app.route('/is_logged_in', methods=['GET'])
    def is_logged_in():
        return jsonify(is_logged_in=True)

    @app.route('/setlang')
    def setlang():
        lang = request.args.get('lang', 'en')
        session['lang'] = lang
        return redirect(request.referrer or '/')

    @app.route('/email_signup', methods=['POST'])
    def email_signup():
        email = request.json.get('email')
        print(email)
        return jsonify(success=True)

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

    @app.route('/')
    def index():
        participants = Participation.query.all()
        return render_template('index.html', participants=participants)

    @app.route('/submit_participation', methods=['POST'])
    def submit_participation():
        if 'file' not in request.files:
            return 'Нет файла'

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower()
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)

            full_name = request.form['full_name']
            department = request.form['department']

            new_participant = Participation(full_name=full_name, department=department, file_path=filepath)
            db.session.add(new_participant)
            db.session.commit()

            return 'Форма отправлена успешно!'
        else:
            return 'Неверный формат файла, поддерживаются только видео форматы'
