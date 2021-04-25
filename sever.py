from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astronaut = StringField('Id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('Id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль астронавта', validators=[DataRequired()])

    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
