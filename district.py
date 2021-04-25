import sys
import requests


def exit_if_not_found():
    print('не найдено')
    sys.exit()


toponym_to_find = " ".join(sys.argv[1:])
api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": api_key,
    "geocode": toponym_to_find,
    "format": "json"}

response_1 = requests.get(geocoder_api_server, params=geocoder_params)

if not response_1:
    exit_if_not_found()

json_response_1 = response_1.json()
toponym = json_response_1["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

address_ll = ','.join([toponym_longitude, toponym_lattitude])
search_params = {
    "apikey": api_key,
    "geocode": address_ll,
    "kind": 'district',
    'format': 'json'
}

response_2 = requests.get(geocoder_api_server, params=search_params)
if not response_2:
    exit_if_not_found()

json_response_2 = response_2.json()
district_1 = json_response_2["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
district_2 = district_1['metaDataProperty']['GeocoderMetaData']['text']
print(district_2)
