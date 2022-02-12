# flask 모듈에서 Flask 클래스를 가져옴
from flask import Flask

# Flask 클래스를 통해, FlaskApp 객체(인스턴스) 생성
FlaskApp = Flask(__name__)

# route decorator 통해서, URI 접근
@FlaskApp.route("/")
def HelloFlask():
	return 'Hello Flask!!'

# URI 추가: /Login/<ID>/ --> 기본형(string 타입) 파라미터인 ID
@FlaskApp.route('/login/<ID>')
def login_id(ID):
	return 'Login ID: %s' % ID

# URI 추가: /pass/<PASS>/ --> Int 타입 파라미터 PASS
@FlaskApp.route('/pass/<int:PASS>')
def pass_num(PASS):
	return 'Password: %s' % PASS

# FlaskApp 객체(인스턴스) 실행
if __name__ == '__main__':
	FlaskApp.debug = True   # FlaskApp 디버그 모드로 실행
	FlaskApp.run()













