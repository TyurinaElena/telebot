import telebot
bot = telebot.TeleBot('5144148734:AAEL1qxIJIXxsHP7lkCwtL9Pb4cLHE3a4RM')

@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса "
                          "программирования на языке Пайтон".format(message.from_user))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)


bot.polling(none_stop=True, interval=0)