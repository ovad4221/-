import json


data = {'crew': [{'name': 'Ридли', 'surname': 'Скотт', 'photo': 'man1.jpg', 'profession': ['киберинженер', 'пилот', 'врач']},
                 {'name': 'Энди', 'surname': 'Уир', 'photo': 'man2.jpg', 'profession': ['штурман', 'гляциолог', 'строитель']},
                 {'name': 'Марк', 'surname': 'Уотни', 'photo': 'man3.jpg', 'profession': ['киберинженер', 'пилот дронов', 'инженер-исследователь']},
                 {'name': 'Венката', 'surname': 'Капур', 'photo': 'man4.jpg', 'profession': ['инженер по терраформированию', 'метеоролог', 'врач']},
                 {'name': 'Тедди', 'surname': 'Сандерс', 'photo': 'man5.jpg', 'profession': ['астрогеолог', 'строитель', 'климатолог']},
                 {'name': 'Шон', 'surname': 'Бин', 'photo': 'man6.jpg', 'profession': ['штурман', 'метеоролог', 'врач']},
                 {'name': 'Иванов', 'surname': 'Пётр', 'photo': 'man7.jpg', 'profession': ['инженер жизнеобеспечения', 'пилот', 'штурман']},
                 {'name': 'Петров', 'surname': 'Иван', 'photo': 'man8.jpg', 'profession': ['оператор марсохода', 'пилот', 'экзобиолог']}]}

with open('./templates/crewmates.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)