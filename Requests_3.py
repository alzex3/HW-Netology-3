import requests


def get_questions(from_date, to_date, tag):
    questions = requests.get(f'https://api.stackexchange.com//2.3/questions?fromdate={from_date}'
                             f'&todate={to_date}&order=desc&sort=activity&tagged={tag}&site=stackoverflow')

    print(f'Список вопросов c {from_date} до {to_date} по тегу {tag}:\n')

    for data in questions.json()['items']:
        print(f'Пользователь {data["owner"]["display_name"]}:\n{data["title"]}\n')


get_questions('2021-08-13', '2021-08-14', 'python')
