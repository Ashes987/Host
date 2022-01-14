russian = open(r'russian2.txt', encoding='utf-8')
poisk = []
spisok_slov = russian.read()
poisk = spisok_slov.split('\n')
import telebot
bot = telebot.TeleBot('1925363878:AAGQfndPMvXk1Fe91rkuzp4l3ha9SwaWy74')
import os

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if " " in message.text:
        bot.send_message(message.from_user.id, "Без пробелов, плиииз😇")
    if len(message.text) == 7:
        spisok_bukv = message.text.lower()
        bot.send_message(message.from_user.id, "Слова из 7ми букв:")
        for i in range(len(poisk)):
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 7:
                bot.send_message(message.from_user.id, poisk[i])           
    if len(message.text) == 7:
        spisok_bukv = message.text.lower()
        bot.send_message(message.from_user.id, "Слова из 6ти букв:")
        for i in range(len(poisk)):
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and len(poisk[i]) == 6:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 6:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 6:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 6:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 6:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 6:
                bot.send_message(message.from_user.id, poisk[i]) 
            if spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 6:
                bot.send_message(message.from_user.id, poisk[i])
    if len(message.text) == 7:
        spisok_bukv = message.text.lower()
        bot.send_message(message.from_user.id, "Слова из 5ти букв:")
        for i in range(len(poisk)):
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i]) 
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[5] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[0] in poisk[i] and spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[2] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
            if spisok_bukv[1] in poisk[i] and spisok_bukv[3] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i]) 
            if spisok_bukv[1] in poisk[i] and spisok_bukv[2] in poisk[i] and spisok_bukv[4] in poisk[i] and spisok_bukv[5] in poisk[i] and spisok_bukv[6] in poisk[i] and len(poisk[i]) == 5:
                bot.send_message(message.from_user.id, poisk[i])
    if " " not in message.text and len(message.text) != 7:
        bot.send_message(message.from_user.id, "Здравствуйте🧙‍♂ Введите, пожалуйста, 7 букв и я найду для вас нужные слова!")

    

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))






