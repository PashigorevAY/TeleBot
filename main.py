import telebot
import requests
import json

API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2a34a0d26cbe1480d486f47f335436dc&lang=ru&units=metric'
TOKEN = '1671788287:AAGkZrkkpc4gAhrTXJBQE4tD6YrDWyUg1oY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
       bot.send_message(message.from_user.id, 'Привет!')
       bot.send_message(message.from_user.id, 'Введи любой город')
    else:
        try:
            receive = requests.get(API_URL.format(city=message.text))
            if receive.status_code == 200:
                bot.send_message(message.from_user.id, receive.content)
                bot.send_message(message.from_user.id, parse_receive(receive.content))
            else:
                bot.send_message(message.from_user.id, 'Город не найден')
                #bot.send_message(message.from_user.id, receive.status_code)
        except:
            bot.send_message(message.from_user.id, 'Ошибка при запросе')


def parse_receive(data):
    PATTERN = 'Страна: {country}\nГород:   {city}\nПогода: {temp}С {description}'
    json_data = json.loads(data)
    #print(json_data)
    country = str(json_data["sys"]['country'])
    description = str(json_data["weather"][0]['description'])
    sity_name = str(json_data["name"])
    temp = str(json_data["main"]["temp"])
    return PATTERN.format(country=country,city=sity_name,temp=temp,description=description)

#RUN
bot.polling()


























#APIWheatherKEY = '2a34a0d26cbe1480d486f47f335436dc'
#SberTestUser




#URL = 'https://api.telegram.org/bot{token}/{method}'





# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
