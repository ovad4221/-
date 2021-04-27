import random
from helpful import get_town_photo
from flask import Flask, render_template, redirect
from requests import get
from models import *

app = Flask(__name__)
params = {
    'title': 'Угадай город!',
    'style': '/static/css/style.css'
}
list_of_towns = ['Томбов', 'Архангельск', 'Москва', 'Калининград', 'Минск', 'Санкт-Петербург']
app.config['SECRET_KEY'] = '#Auction%Topic%Secret$%Key!!!'
new_town = ''
town = ''

total_result = 0


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def start():
    global town, new_town, total_result, list_of_towns

    if not list_of_towns:
        list_of_towns = ['Томбов', 'Архангельск', 'Москва', 'Калининград', 'Минск', 'Санкт-Петербург']
    new_town = random.choice(list_of_towns)
    get_town_photo(new_town)
    list_of_towns.remove(new_town)

    form = Form()
    if form.validate_on_submit():
        if form.name.data == town:
            if list_of_towns:
                town = new_town
                return render_template('towns.html', **params, message='О, вы угадали, идем дальше!!!',
                                       button_label='Дальше?', ex_flag_compare=True, form=form)
            else:
                town = new_town
                return render_template('towns.html', **params, message='Вы закончили, мои поздравления!',
                                       button_label='Заново?', ex_flag_compare=True, form=form)
        else:
            if list_of_towns:
                town = new_town
                return render_template('towns.html', **params, message=f'Это же {town}, давайте дальше.',
                                       button_label='Дальше?', ex_flag_compare=True, form=form)
            else:
                town = new_town
                return render_template('towns.html', **params,
                                       message=f'Это же {town}, а вы тем самым закончили.',
                                       button_label='Заново?', ex_flag_compare=True, form=form)
    town = new_town
    return render_template('towns.html', **params, ex_flag_compare=False, form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
