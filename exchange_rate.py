import requests
import json


def get_rate():
    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = json.loads(response.text)
        return float(data['Valute']['USD']['Value'])
    except requests.ConnectionError:
        print('Нет соединения')
        return 99.03
