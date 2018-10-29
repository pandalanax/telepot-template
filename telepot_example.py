
"""
Simple telepot Bot with following functions :

1. Send general info if it runs with command : 	'areyourunning'

Note that telepot runs as thread so function handle(msg) can scope everything whats happening.


THINGS TO DO BEFORE RUNNING SUCCESSFULLY :

1. Insert your special token
2. pip3 install telepot

"""


import time
import telepot
from telepot.loop import MessageLoop
import datetime

def handle(msg):
    content_type, chat_type, chat_id =telepot.glance(msg)
    if content_type == 'text':
        if msg['text'] == 'areyourunning':
            bot.sendMessage(chat_id, 'still running')

bot = telepot.Bot(token ='YOUR_TOKEN')

MessageLoop(bot, handle).run_as_thread()

while True:
    print('running')
    time.sleep(1000)

