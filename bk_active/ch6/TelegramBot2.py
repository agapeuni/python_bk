# 텔레그램 모듈 가져오기
import telegram

# 메시지 가져오기: Bot --> Application
KlasseBot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
KlasseBot = telegram.Bot(token=KlasseBot_token)
messages = KlasseBot.getUpdates()
for msg in messages:
	print(msg.message)


