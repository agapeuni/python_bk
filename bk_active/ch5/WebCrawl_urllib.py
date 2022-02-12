# 파이썬 기본 라이브러리 사용: Web 라이브리 urllib
import urllib.request

# 변수 또는 인자 값
target_url = "http://www.python.org"
url_request = urllib.target_url

# 웹 크롤링 --> 웹 페이지 가져오기
web_page = url_request.urlopen(target_url)
print(web_page.read())




