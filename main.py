import os

from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

from Date import get_count, get_birthday
from Weather import WeatherParam
from util import get_words, get_random_color

if __name__ == '__main__':
    # start_date = os.environ['START_DATE']
    # city = os.environ['CITY']
    # birthday = os.environ['BIRTHDAY']
    # app_id = os.environ["APP_ID"]
    # app_secret = os.environ["APP_SECRET"]
    # user_id = os.environ["USER_ID"]
    # template_id = os.environ["TEMPLATE_ID"]
    # weather_key = os.environ["WEATHER_KEY"]
    start_date = "2022-12-02"
    city = "510100"
    birthday = "03-13"
    app_id = "wx1621120a18807ad4"
    app_secret = "0246bb9e0d663f1cb226d7d5ac290730"
    user_id = "o-mpX6gKQHHu1ZdniUz1Iv9d_knY"
    template_id = "zZPqsOlpZ5PArU33aw4FPGTMVc_1u2NtHDojs-xTJeQ"
    weather_key = "bc98c6921f7c19a0f0a7a2655a5038f5"
    client = WeChatClient(app_id, app_secret)
    wm = WeChatMessage(client)
    weather_res = WeatherParam(weather_key, city).get_weather()
    data = {
        "weather": {"value": weather_res.weather},
        "temperature": {"value": weather_res.temperature},
        "love_days": {"value": get_count(start_date)},
        "birthday_left": {"value": get_birthday(birthday)},
        "words": {"value": get_words(),
                  "color": get_random_color()
                  }
    }
    res = wm.send_template(user_id, template_id, data)
