# flask 모듈에서 Flask 클래스와 url_for 메소드 를 가져옴
from flask import Flask, url_for

# Flask 클래스를 통해, FlaskApp 객체(인스턴스) 생성
FlaskApp = Flask(__name__)

# route decorator 통해서, URI 접근


@FlaskApp.route("/")
def HelloFlask():
    return '<h1>Hello Flask!!</h1>'

# 동적 URI 변수(<변수>) 사용

# URI 추가: /Login/<ID>/ --> 기본형(string 타입) 파라미터인 ID


@FlaskApp.route('/login/<ID>')
def login_id(ID):
    return '<h1> Login ID: %s</h1>' % ID

# URI 추가: /pass/<PASS>/ --> Int 타입 파라미터 PASS


@FlaskApp.route('/pass/<int:PASS>')
def pass_num(PASS):
    return '<h1>Password: %s</h1>' % PASS


# FlaskApp 객체(인스턴스) 실행
if __name__ == '__main__':
    FlaskApp.debug = True   # FlaskApp 디버그 모드로 실행
    # FlaskApp.run()
    with FlaskApp.test_request_context():
        print(url_for('login_id', ID='Klasse'))
        print(url_for('pass_num', PASS=1234))
