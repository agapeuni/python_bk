from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

# 변수 또는 인자 값
target_url = "https://nid.naver.com/nidlogin.login"

# 웹 크롤링 --> 웹 페이지 가져오기
driver.get(target_url)

# 로그인창 찾기 + ID 입력하기
driver.find_element_by_name('id').send_keys('아이디')
# 패스워드창 찾기 + 패스워드  입력하기
driver.find_element_by_name('pw').send_keys('패스워드')
# 로그인 버튼 클릭
driver.find_element_by_class_name('btn_global').click()







