# 셀레니움(Selenium) 패키지 및 웹드라이버 로드
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

# 변수 또는 인자 값
target_url = "https://www.naver.com/"

# 웹 크롤링 --> 웹 페이지 가져오기
driver.get(target_url)

'''
# 검색창 찾기
search_box = driver.find_element_by_name('query')

# 검색창에 검색어(Python) 입력하기
search_box.send_keys('Python')

# 검색창 실행하기
search_box.submit()
'''
# 검색창 찾기 + 검색창에 검색어(Python) 입력하기
driver.find_element_by_name('query').send_keys('Python')
# 검색창 실행하기
driver.find_element_by_name('query').submit()

# 종료
# driver.close()






