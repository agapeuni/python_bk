# 텔레그램 모듈 가져오기
import telegram

# 메시지 가져오기: Bot --> Channel
KlasseBot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
KlasseBot = telegram.Bot(token=KlasseBot_token)

KlasseBot.sendMessage(chat_id='@KlasseBotChannelClientId', text="메시지 보내기: Bot --> Channel")


