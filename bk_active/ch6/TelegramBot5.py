# 텔레그램 확장(extend) 라이브러리로부터, 두개의 메쏘드(MessageHandler, Filters)를 추가합니다.
from telegram.ext import Updater, MessageHandler, Filters

# Bot 토큰(Token)
KlasseBot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 사용자가 보낸 메시지를 그래도 돌려 주기
def echo(bot, update):
	update.message.reply_text(update.message.text)

# 봇(Bot)의 변경사항이 있으면, 이를 처리 하는 객체
# 이벤트 루프(event loop)를 통해서 주기적으로 변경 사항 체크
updater = Updater(KlasseBot_token)

# echo 메시지에 대한 객체 생성 및 함수 연결
echo_msg_handler = MessageHandler(Filters.text, echo)

# echo 메시지 객체를 디스패처(dispatcher)핸들러에 추가
updater.dispatcher.add_handler(echo_msg_handler)

# 어플리케이션 기동
updater.start_polling()
updater.idle()









