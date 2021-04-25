import sys
from io import BytesIO
import requests
from PIL import Image
from find_delta import find_delta_meters

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response_1 = requests.get(geocoder_api_server, params=geocoder_params)

if not response_1:
    pass

json_response_1 = response_1.json()
toponym = json_response_1["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")


search_api_server = "https://search-maps.yandex.ru/v1/"

api_key = "d0ce2ab6-de1b-471e-abc6-91173b1eae61"

address_ll = ','.join([toponym_longitude, toponym_lattitude])

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response_2 = requests.get(search_api_server, params=search_params)
if not response_2:
    pass

json_response_2 = response_2.json()
pt = []

for i in range(10):
    try:
        organization = json_response_2["features"][i]
        org_name = organization["properties"]["CompanyMetaData"]["name"]
        org_com_data = organization["properties"]["CompanyMetaData"]
        org_address = org_com_data["address"]
        point = organization["geometry"]["coordinates"]
        org_point = "{0},{1}".format(point[0], point[1])
        try:
            org_time = org_com_data["Hours"]["text"]
            print(org_point)
            if org_time:
                if 'круглосуточно' in org_time:
                    pt.append(org_point + ',pmgns')
                else:
                    pt.append(org_point + ',pmbls')
            else:
                pt.append(org_point + ',pmgrs')
        except KeyError:
            pt.append(org_point + ',pmgrs')
    except IndexError:
        print('меньше 10 аптек найдено.')

pt.append("{0},pm2dgl".format(address_ll) + ',org')

map_params = {
    "ll": address_ll,
    "l": "map",
    "pt": '~'.join(pt)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

# print('Название: ', org_name)
# print('Адрес: ', org_address)
# print('Время работы: ', org_time)
# print('Расстояние: ', find_delta_meters(address_ll, org_point), 'м')

Image.open(BytesIO(
    response.content)).show()
