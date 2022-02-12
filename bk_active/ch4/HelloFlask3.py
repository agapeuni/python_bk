# flask 모듈에서 Flask 클래스와 render_template 메서드를 가져옴
from flask import Flask, render_template

# Flask 클래스를 통해, FlaskApp 객체(인스턴스) 생성
FlaskApp = Flask(__name__)


@FlaskApp.route("/")
def hello():
    return '<h1>Klasse</h1>'

# 한개 입력 파라미터


@FlaskApp.route("/userinfo1/<username>")
def user(username):      # 뷰함수
    return render_template('UserInfo1.html', name=username)
# 세개 입력 파라미터


@FlaskApp.route("/userinfo2/<username>/<location>/<age_num>")
def user2(username, location, age_num):      # 뷰함수
    return render_template('UserInfo2.html', name=username, country=location, age=age_num)


if __name__ == "__main__":  # 실행 확인
    FlaskApp.run()  # 플라스크 어플리리케이션 실행
