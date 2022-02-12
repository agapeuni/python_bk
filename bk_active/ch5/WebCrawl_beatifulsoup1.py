# 셀레니움(Selenium) + 뷰티플수프(BeautifulSoup)
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

# 변수 또는 인자 값
target_url = "https://music.naver.com/"

# 웹 크롤링 --> 웹 페이지 가져오기
driver.get(target_url)

# 웹페이지 스트링
web_page = driver.page_source
print(web_page)

# 웹페이지 스트링을 객체로 전환
bs_soup = BeautifulSoup(web_page,'html.parser')
print(bs_soup)
