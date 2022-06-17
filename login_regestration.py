from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: WebDriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(50)
driver.get('http://practice.automationtesting.in/')
driver.maximize_window()

my_ac = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
my_ac.click()
# reg_m = driver.find_element_by_id("reg_email")
# reg_m.send_keys("ivanov@gmail.ru")
# reg_pas = driver.find_element_by_id("reg_password")
# reg_pas.send_keys("Bdfyjd-Cj,frf12@")
# reg_btn = driver.find_element_by_css_selector('[name="register"]')
# reg_btn.click()
# user_field = driver.find_element_by_id("username")
# user_field.send_keys("ivanov@gmail.ru")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Bdfyjd-Cj,frf12@")
# login_btn = driver.find_element_by_css_selector('[name="login"]')
# login_btn.click()
# out_btn = driver.find_element_by_link_text("Logout")
# out_btn_check = out_btn.text
# assert out_btn_check == "Logout"