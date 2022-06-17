from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: WebDriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://practice.automationtesting.in/')
driver.maximize_window()



shop_btn = driver.find_element_by_xpath('//a[text()="Shop"]')
shop_btn.click()

driver.execute_script("window.scrollBy(0, 300);")

app_btn = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
app_btn.click()

time.sleep(2)

items = driver.find_element_by_class_name('cartcontents')
items.click()

ptc_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
ptc_btn.click()

first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='billing_first_name']")))
first_name.send_keys("Ivan")

last_name = driver.find_element_by_css_selector('[name="billing_last_name"]')
last_name.send_keys("Petrov")

mail_field = driver.find_element_by_css_selector('[name="billing_email"]')
mail_field.send_keys("IvPetrov@gmail.ru")

phone_field = driver.find_element_by_css_selector('[name="billing_phone"]')
phone_field.send_keys("89214910417")

country_field = driver.find_element_by_id("s2id_billing_country")
country_field.click()
country_field1 = driver.find_element_by_id("s2id_autogen1_search")
country_field1.send_keys("Russ")

choose_country = driver.find_element_by_id("select2-results-1")
choose_country.click()

street_address = driver.find_element_by_css_selector('[name="billing_address_1"]')
street_address.send_keys("Nevsky")

city_field = driver.find_element_by_css_selector('[name="billing_city"]')
city_field.send_keys("Saint-Petersburg")

county_field = driver.find_element_by_css_selector('[name="billing_state"]')
county_field.send_keys("Lenobl")

postcode_field = driver.find_element_by_css_selector('[name="billing_postcode"]')
postcode_field.send_keys("195177")

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(5)

payment_choose = driver.find_element_by_id("payment_method_cheque")
payment_choose.click()

time.sleep(3)

place_order = driver.find_element_by_id("place_order")
place_order.click()

thank_you_check = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

check_payments = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3)>td"), "Check Payments"))

driver.quit()




# jsdsaa = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]')
# jsdsaa.click()
#
# items = driver.find_element_by_class_name('cartcontents')
# items.click()
# time.sleep(3)
#
# del_app = driver.find_element_by_css_selector('[data-product_id="182"]')
# del_app.click()
#
# time.sleep(4)
#
# undo_btn = driver.find_element_by_link_text("Undo?")
# undo_btn.click()
# time.sleep(4)
# quan_field = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quan_field.clear()
# quan_field.send_keys("3")
#
# upd_bas_btn = driver.find_element_by_css_selector('[value="Update Basket"]')
# upd_bas_btn.click()
#
# quan_field1 = driver.find_element_by_css_selector('[max="9665"]')
# quan_field1_val = quan_field1.get_attribute("value")
# assert quan_field1_val == "3"
#
# time.sleep(5)
#
# ap_coup_btn = driver.find_element_by_css_selector('.coupon>.button:nth-child(3)')
# ap_coup_btn.click()
#
# message = driver.find_element_by_css_selector('.woocommerce-error>li')
# message_text = message.text
# assert message_text == "Please enter a coupon code."
#
# driver.quit()



# items = driver.find_element_by_class_name('cartcontents')
# items_text = items.text
# assert items_text == "1 Item"
# pr_book = driver.find_element_by_css_selector('.wpmenucart-contents>.amount')
# pr_book_text = pr_book.text
# assert pr_book_text == "₹180.00"
# items.click()
# subtotal = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']>.woocommerce-Price-amount"), "₹180.00"))
#
# total = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Total']>strong>span"), "₹189.00"))
#
# driver.quit()

# my_ac = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
# my_ac.click()
# user_field = driver.find_element_by_id("username")
# user_field.send_keys("ivanov@gmail.ru")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Bdfyjd-Cj,frf12@")
# login_btn = driver.find_element_by_css_selector('[name="login"]')
# login_btn.click()


# and_book = driver.find_element_by_class_name("post-169")
# and_book.click()
# old_price = driver.find_element_by_css_selector('.price>del>span')
# new_price = driver.find_element_by_css_selector('.price>ins>span')
# old_price_text = old_price.text
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
#
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
#
# book_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
#
# driver.quit()
# from selenium.webdriver.support.select import Select
# sel_sort = driver.find_element_by_class_name("orderby")
# sel_check = driver.find_element_by_css_selector('[value="menu_order"]')
# sel_check_sel = sel_check.get_attribute("selected")
# print(sel_check_sel)
# sel_sort_pr = Select(sel_sort)
# sel_sort_pr.select_by_value("price-desc")
# sel_check_pr = driver.find_element_by_xpath('//option[@value="price-desc"]')
#
# sel_sort1 = driver.find_element_by_class_name("orderby")
# sel_pr_check = sel_check_pr.get_attribute("selected")
# print(sel_pr_check)
# book_html5 = driver.find_element_by_xpath('//h3[text()="HTML5 Forms"]')
# book_html5.click()
# head_book = driver.find_element_by_css_selector('[itemprop="name"]')
# head_book_check = head_book.text
# assert head_book_check == "HTML5 Forms"

# html_btn = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]')
# html_btn.click()
# numb_books = driver.find_element_by_xpath('//div[@id="woocommerce_product_categories-2"]/ul/li[2]/span')
# numb_books_check = numb_books.text
# assert numb_books_check == "(3)"