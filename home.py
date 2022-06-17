# from selenium import webdriver
# import time
#
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver: WebDriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(50)
# driver.get('http://practice.automationtesting.in/')
# driver.maximize_window()
#
# driver.execute_script("window.scrollBy(0, 600);")
# selen_r_btn = driver.find_element_by_xpath('//h3[text()="Selenium Ruby"]')
# selen_r_btn.click()
# rev_btn = driver.find_element_by_css_selector('[href="#tab-reviews"]')
# rev_btn.click()
#
# five_stars = driver.find_element_by_class_name('star-5')
# five_stars.click()
# y_review = driver.find_element_by_id('comment')
# y_review.send_keys('Nice book!')
# name_field = driver.find_element_by_id('author')
# name_field.send_keys('Ivan')
# mail_field = driver.find_element_by_id('email')
# mail_field.send_keys('ivan@gmail.ru')
# subm_btn = driver.find_element_by_id('submit')
# subm_btn.click()
