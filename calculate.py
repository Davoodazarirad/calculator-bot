import telebot

cal = telebot.TeleBot("6685150273:AAFVI-VfNCDwMSsbnWrK89YU8qkW3D7mq7s")

dokme = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
dokme.add("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "", "/", "=", "C")

am = ""
nm1 = 0
nm2 = 0
Result = 0

@cal.message_handler(commands=['start'])
def send_welcome(message):
    cal.send_message(message.chat.id, "سلام \n ماشین حساب فعال شد", reply_markup=dokme)

@cal.message_handler(func=lambda m: True)
def number1(message):
    global nm1
    if message.text is not None:
        nm1 = int(message.text)
        cal.register_next_step_handler(message, amalgar)

def amalgar(message):
    global am
    for am in ["+", "-", "", "/"]:
        cal.send_message(message.chat.id, am)
        cal.register_next_step_handler(message, number2)

def number2(message):
    global nm2
    global Result
    nm2 = int(message.text)
    if am == "+":
        Result = nm1 + nm2
    elif am == "-":
        Result = nm1 - nm2
    elif am == "*":
        Result = nm1 * nm2
    elif am == "/":
        Result = nm1 / nm2
        
    cal.send_message(message.chat.id, "Result: " + str(Result))

cal.infinity_polling()