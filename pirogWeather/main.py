import requests
import telebot

url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = '06657bd5d251a1fd916e3a8d533475d2'
api_telegram = '1459334091:AAExGusB_725lHXlobtuPbD2YJkKfnqHUJk'

bot = telebot.TeleBot(api_telegram)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, ' + str(message.from_user.username) + ',' + '\n' +
                     'чтобы узнать погоду напиши команду /weather <название города>')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, '/start запуск бота\n/help команды бота\n/weather <название города>')


@bot.message_handler(commands=['weather'])
def test(message):
    city_name = message.text[9:]

    try:
        params = {'APPID': api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)
        weather = result.json()

        if weather["main"]['temp'] < 5:
            status = "Сейчас пива на улице не попьешь!"
        elif weather["main"]['temp'] < 10:
            status = "Сейчас прохладно!"
        elif weather["main"]['temp'] > 25:
            status = "На улице адилово!"
        else:
            status = "Сейчас отличная температура!"

        bot.send_message(message.chat.id, "В городе " + str(weather["name"]) + " температура " + str(
            float(weather["main"]['temp'])) + "\n" +
                         "Максимальная температура: " + str(float(weather['main']['temp_max'])) + "\n" +
                         "Минимальная температура: " + str(float(weather['main']['temp_min'])) + "\n" +
                         "Скорость ветра: " + str(float(weather['wind']['speed'])) + "\n" +
                         "Давление: " + str(float(weather['main']['pressure'])) + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "Видимость: " + str(weather['visibility']) + "\n" +
                         "Описание: " + str(weather['weather'][0]["description"]) + "\n\n" + status)

    except:
        bot.send_message(message.chat.id, "Город " + city_name + " не найден")


if __name__ == '__main__':
    bot.polling(none_stop=True)
