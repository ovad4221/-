from flask import Flask, request
from flask import render_template
from flask import url_for
from flask import redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os
from werkzeug.utils import secure_filename
from random import choice
import json


UPLOAD_FOLDER = './static/imgs_for_galery'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astronaut = StringField('Id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('Id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль астронавта', validators=[DataRequired()])

    submit = SubmitField('Доступ')


@app.route('/')
def ind():
    return render_template('index.html', title='Mars one')


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def tran(prof):
    return render_template('tran.html', title='Заготовка', prof=prof)


@app.route('/list_prof/<list>')
def prof_list(list):
    prof_lis = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
                'врач', 'инженер по терраформированию',
                'специалист по радиционной защите', 'климатолог',
                'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
                'метеоролог', 'оператор марсохода',
                'киберинженер', 'штурман', 'пилот дронов']
    return render_template('prof_list.html', title='Заготовка', list=list, prof_lis=prof_lis)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    person_info = {'title': 'Анкета',
                   'surname': 'Watny',
                   'name': 'Mark', 'education': 'выше среднего',
                   'profession': 'штурман марсохода',
                   'sex': 'male', 'motivation': 'Всегда мечтал застрять на марсе',
                   'ready': 'True'}
    return render_template('auto_answer.html', title=person_info['title'], person_info=person_info)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'success'


@app.route('/distribution')
def distribution():
    crew = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур',
            'Тедди Сандерс', 'Шон Бин', 'Иванов Пётр', 'Петров Иван']
    return render_template('distribution.html', title='Распределение', crew=crew)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('room.html', title='Офрмление каюты', sex=sex, age=age)


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    return render_template('carousel.html', title='Пейзажи марса')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/galery', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/galery')
    photos = os.listdir(UPLOAD_FOLDER)
    for i in range(len(photos)):
        photos[i] = url_for('static', filename=f'imgs_for_galery/{photos[i]}')
    return render_template('galery.html', title='Галерея', photos=photos)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    active_filename = ''
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            active_filename = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/load_photo')

    return render_template('load_photo.html', title='Загрузка фото',
                           photo=url_for('static', filename=f'img/{active_filename}', active_filename=active_filename))


@app.route('/member')
def member():
    with open('./templates/crewmates.json', 'r') as file:
        data = json.load(file)
    crewmate = choice(data['crew'])

    return render_template('member.html', title='Член экипажа',
                           name=crewmate['name'], surname=crewmate['surname'],
                           photo=url_for('static', filename=f'img/{crewmate["photo"]}'), prof_list=crewmate['profession'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
