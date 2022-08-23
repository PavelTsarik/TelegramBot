import telebot, bs4, requests, random
# Юмор
url = 'https://humornet.ru/anekdot/korotkie/page/3/'
r = requests.get(url)
# print(r.status_code)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
an = soup.find_all('div', class_='text')
# print(an)
clear_an = []
for i in an:
    clear_an.append(i.getText())
# print(clear_an)


# Погода
url_2 = 'https://pogoda.mail.ru/prognoz/minsk/'
r_2 = requests.get(url_2)
# print(r_2.status_code)
soup_2 = bs4.BeautifulSoup(r_2.text, 'html.parser')
an_2 = soup_2.find_all('div', class_="information__content__temperature")
# print(an_2)
clear_an_2 = []
for o in an_2:
    clear_an_2.append(o.getText())
# print(clear_an_2)


# Кино
url_3 = 'https://bycard.by/afisha/minsk/kino?view=top'
r_3 = requests.get(url_3)
# print(r_3.status_code)
soup_3 = bs4.BeautifulSoup(r_3.text, 'html.parser')
an_3 = soup_3.find_all('div', class_="by-type__row")
# print(an_3)
clear_an_3 = []
for o in an_3:
    clear_an_3.append(o.getText())
# print(clear_an_3)

# Новости
url_4 = 'https://smartpress.by/'
r_4 = requests.get(url_4)
# print(r_4.status_code)
soup_4 = bs4.BeautifulSoup(r_4.text, 'html.parser')
an_4 = soup_4.find_all('ul', class_="list-event")
# print(an_4)
clear_an_4 = []
for o in an_4:
    clear_an_4.append(o.getText())
# print(clear_an_4)

bot = telebot.TeleBot('5711056505:AAGNkOqfBbg69L4MzD0RJEJt56sWPm21fcE')

@bot.message_handler()
def get_text(message):
    if message.text == 'Анекдот' or message.text == 'анекдот':
        rand_anek = random.choice(clear_an)
        bot.send_message(message.chat.id, rand_anek)
    if message.text == 'Погода' or message.text == 'погода':
        bot.send_message(message.chat.id, clear_an_2)
    if message.text == 'Кино' or message.text == 'кино':
        bot.send_message(message.chat.id, clear_an_3)
    if message.text == 'Новости' or message.text == 'новости':
        bot.send_message(message.chat.id, clear_an_4)
bot.polling(none_stop=True)