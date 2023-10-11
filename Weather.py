import json
import math

import requests
import urllib.parse

Params = {
    "key": "bc98c6921f7c19a0f0a7a2655a5038f5",
    "city": "510100",
    "extensions": "base",
    "output": "JSON"
}


def url_join_args(api, query=None, **kwargs):
    result = api
    if not result.endswith('?') and (query or kwargs):
        result = api + '?'
    if query:
        result = result + urllib.parse.urlencode(query)
    if kwargs:
        if query:
            result = result + '&' + urllib.parse.urlencode(kwargs)
        else:
            result = result + urllib.parse.urlencode(kwargs)
    return result


def json_to_obj(jsonStr, objClass):
    parseData = json.loads(jsonStr.strip('\t\r\n'))
    result = objClass()
    result.__dict__ = parseData
    return result


class WeatherResult(object):
    province: str
    city: str
    weather: str
    temperature: str
    humidity: str
    wind_direction: str
    wind_power: str

    def __init__(self, province, city, weather, temperature, humidity, wind_direction, wind_power):
        self.province = province
        self.city = city
        self.weather = weather
        self.temperature = temperature
        self.humidity = humidity
        self.wind_direction = wind_direction
        self.wind_power = wind_power


class WeatherParam:
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    extensions = "base"
    output = "JSON"
    key: str
    city: str

    def __init__(self, key, city):
        if key is None:
            exit(422)
        else:
            self.key = key
        if city is None:
            exit(422)
        else:
            self.city = city

    def get_weather(self):
        params = {
            "key": self.key,
            "city": self.city,
            "extensions": self.extensions,
            "output": self.output
        }
        url = url_join_args(self.url, params)
        print(url)
        res = requests.get(url).json()['lives'][0]
        return WeatherResult(res['province'],
                             res['city'],
                             res['weather'],
                             res['temperature'],
                             res['humidity'],
                             res['winddirection'],
                             res['windpower'])


if __name__ == '__main__':
    print(WeatherParam("bc98c6921f7c19a0f0a7a2655a5038f5", "510100").get_weather())
