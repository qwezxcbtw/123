import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = '7162923227:AAFrSNAL3p8lDOFp0Yu26UJQTDf06znl_Gc'
bot = telebot.TeleBot(TOKEN)


username1 = '@googLe_As'  
username2 = '@ggoper01'  


@bot.message_handler(commands=['start'])
def start(message):
    
    keyboard = InlineKeyboardMarkup()
    
    keyboard.row(InlineKeyboardButton('🧿GOOGLE CHART🧿', url='https://t.me/+jIflDWcxouk3ZDcy'))
    keyboard.row(InlineKeyboardButton('🧿GOOGLE CHANNEL🧿', url='https://t.me/+JAH0VHZDhi5kMDEy'))
    keyboard.row(InlineKeyboardButton('🧿OPERATOR🧿', url=f'tg://resolve?domain={username1}'),
                  InlineKeyboardButton('🧿OPERATOR', url=f'tg://resolve?domain={username2}'))
    
    
    with open(r'C:\Users\GGG\Desktop\images\example.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, reply_markup=keyboard)


bot.polling(none_stop=True)
