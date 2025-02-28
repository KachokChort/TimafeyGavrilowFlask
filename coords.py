import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
geocode1 = ('Хабаровск')
geocode2 = ('Уфа')
geocode3 = ('Нижний Новгород')
geocode4 = ('Калининград')

data = [geocode1, geocode2, geocode3, geocode4]
# Готовим запрос.
geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode1}&format=json'

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    for i in data:
        geocoder_request = f'{server_address}apikey={api_key}&geocode={i}&format=json'
        response = requests.get(geocoder_request)
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]['Components'][1]['name']
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Печатаем извлечённые из ответа поля:
        print(toponym_address) #, "имеет координаты:", toponym_coodrinates)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")