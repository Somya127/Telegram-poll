from pyrogram.handlers import PollHandler
from telegram import Poll
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pandas as pd
import time
updater = Updater("2021785278:AAEYJobkBR49Nm5H6hwluU8y-Gl8XtopCHM")
dp = updater.dispatcher

df = pd.read_csv("/Users/harshlariya/Downloads/bot_info.csv")
QUESTIONS = df["Questions"].tolist()
OPTIONS=df['Options'].tolist()
ANSWER=df['Answers'].tolist()
updater.start_polling()
for i in range(0,120):
    try:
       updater.bot.send_poll(-1001323978617,question=QUESTIONS[i],options=OPTIONS[i], type=Poll.QUIZ,correct_option_id=ANSWER[i], is_anonymous=True)
       time.sleep(21600)
       # time.sleep(5)
    except:
           pass


updater.idle()