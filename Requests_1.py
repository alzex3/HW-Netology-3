import requests

heroes_list = ['Hulk', 'Captain America', 'Thanos']


def smart_superhero(heroes):
    heroes_int = {}
    for hero in heroes:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        hero = requests.get(url).json()
        for data in hero['results']:
            if data['name'] in heroes:
                heroes_int[int(data['powerstats']['intelligence'])] = data['name']
    print(f'Самый умный супергерой из списка: {heroes_int[max(heroes_int.keys())]}')


smart_superhero(heroes_list)
