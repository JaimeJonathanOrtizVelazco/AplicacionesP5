#!usrbinenv python3
import json

import requests


def sw(x):
    clima = {
        'Thunderstorm': 'Tormenta',
        'Clouds': 'Nublado',
        'Clear': 'Despejado',
        'Haze': 'Niebla',
    }
    return clima[x]


url = 'https://api.openweathermap.org/data/2.5/weather'
values = dict()
values["q"] = "Mexico City"
values["appid"] = "734cad68d73a4fa2516e58cd6b97ec21"
values["lang"] = "en"
djson = json.loads(requests.get(url, params=values).content)
print(djson['coord']['lon'])
print(sw(djson['weather'][0]['main']))
