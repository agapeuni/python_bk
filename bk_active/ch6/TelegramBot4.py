# 텔레그램 확장(extend) 라이브러리로부터, 두개의 메쏘드(Updater, CommandHandler)를 추가합니다.
from telegram.ext import Updater, CommandHandler

# Bot 토큰(Token)
KlasseBot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Who are you?
def who_cmd(bot, update):
    update.message.reply_text('저는 {}입니다.'.format(update.message.from_user.first_name))

# help command
def help_cmd(bot, update):
    update.message.reply_text('무엇을 도와 드릴까요?')

# 봇(Bot)의 변경사항이 있으면, 이를 처리 하는 객체
# 이벤트 루프(event loop)를 통해서 주기적으로 변경 사항 체크
updater = Updater(KlasseBot_token)

# 'who' 명령어에 대한 객체 생성 및 함수 연결
# 'help' 명령어에 대한 객체 생성 및 함수 연결
who_cmd_handler1 = CommandHandler('who', who_cmd)
help_cmd_handler2 = CommandHandler('help', help_cmd)

# 'who' 명령어 객체를 디스패처(dispatcher)핸들러에 추가
# 'help' 명령어 객체를 디스패처(dispatcher)핸들러에 추가
updater.dispatcher.add_handler(who_cmd_handler1)
updater.dispatcher.add_handler(help_cmd_handler2)

# 어플리케이션 기동
updater.start_polling()
updater.idle()



