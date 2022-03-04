# 텔레그램 모듈 가져오기
import telegram

# 메시지 보내기: Application --> Bot
KlasseBot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
KlasseBot = telegram.Bot(token=KlasseBot_token)
KlasseBot_client_id = 'xxxxxxxxxxx'
KlasseBot.sendMessage(chat_id=KlasseBot_client_id, text='메시지내기: Application --> Bot')


