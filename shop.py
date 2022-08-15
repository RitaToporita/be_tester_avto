import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# # 1 Открыть страницу
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# #driver.implicitly_wait(5)
# driver.find_element_by_id('menu-item-50').click()
# # 2 Залогиниться
# driver.find_element_by_id('username').send_keys('ritatoporita1@gmail.com')
# driver.find_element_by_id('password').send_keys('Parol123321!')
# driver.find_element_by_id("password").click()
# time.sleep(3)
# driver.find_element_by_css_selector('.login .woocommerce-Button.button').click()
# # 3 Нажмите на вкладку "Shop"
# driver.find_element_by_css_selector('#menu-item-40 > a').click()
# # 4 Откройте книгу "HTML 5 Forms"
# driver.find_element_by_css_selector('.products.masonry-done > li:nth-child(3) > a:nth-child(1)').click()
# # 5 проверка заголовка
# element = driver.find_element_by_css_selector(".product_title.entry-title")
# element_get_text = element.text
# if element_get_text == "HTML5 Forms":
#     print('заголовок страницы "HTML5 Forms"')
# else:
#     print('заголовок страницы не "HTML5 Forms"')
# driver.quit()
#  2 #
# 1 Открыть страницу
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# #driver.implicitly_wait(5)
# driver.find_element_by_id('menu-item-50').click()
# # 2 Залогиниться
# driver.find_element_by_id('username').send_keys('ritatoporita1@gmail.com')
# driver.find_element_by_id('password').send_keys('Parol123321!')
# driver.find_element_by_id("password").click()
# time.sleep(3)
# driver.find_element_by_css_selector('.login .woocommerce-Button.button').click()
# # 3 Нажмите на вкладку "Shop"
# driver.find_element_by_css_selector('#menu-item-40 > a').click()
# # 4 Откройте категорию "HTML"
# driver.find_element_by_css_selector('.cat-item.cat-item-19 > a').click()
# # # 5 Добавьте тест, что отображается три товара
# find_elem = len(driver.find_elements_by_css_selector('.products.masonry-done > li'))
# if find_elem == '3':
#     print("На странице 3 товара")
# else:
#     print("На странице ", find_elem, "товара")
# driver.quit()
#  3   #
# # 1 Открыть страницу
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# #driver.implicitly_wait(10)
# time.sleep(3)
# driver.find_element_by_id('menu-item-50').click()
# # 2 Залогиниться
# driver.find_element_by_id('username').send_keys('ritatoporita1@gmail.com')
# driver.find_element_by_id('password').send_keys('Parol123321!')
# driver.find_element_by_id("password").click()
# time.sleep(3)
# driver.find_element_by_css_selector('.login .woocommerce-Button.button').click()
# # 3 Нажмите на вкладку "Shop"
# time.sleep(3)
# driver.find_element_by_css_selector('#menu-item-40 > a').click()
# # 4 Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# element1 = driver.find_element_by_tag_name('[value = "menu_order"]')
# element1_checked = element1.get_attribute("checked")
# if element1_checked is not None:
#     print("выбран вариант сортировки по умолчанию ")
# else:
#     print("выбран другой вариант сортировки")
# # # 5 Отсортируйте товары по цене от большей к меньшей
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# # Снова объявите переменную с локатором основного селектора сортировки
# # Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# element2 = driver.find_element_by_tag_name('[value = "price-desc"]')
# element2_checked = element2.get_attribute("checked")
# if element2_checked is not None:
#     print("выбран вариант сортировки по цене от большей к меньшей")
# else:
#     print("выбран другой вариант сортировки")
# driver.quit()

#   4  #
# # 1 Открыть страницу
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_id('menu-item-50').click()
# # 2 Залогиниться
# driver.find_element_by_id('username').send_keys('ritatoporita1@gmail.com')
# driver.find_element_by_id('password').send_keys('Parol123321!')
# driver.find_element_by_id("password").click()
# time.sleep(3)
# driver.find_element_by_css_selector('.login .woocommerce-Button.button').click()
# # 3 Нажмите на вкладку "Shop"
# time.sleep(3)
# driver.find_element_by_css_selector('#menu-item-40 > a').click()
# # 4 Откройте книгу "Android Quick Start Guide"
# driver.find_element_by_css_selector('.products.masonry-done :nth-child(1) .woocommerce-LoopProduct-link .attachment-shop_catalog.size-shop_catalog.wp-post-image').click()
# # # 5 Добавьте тест, что содержимое старой цены = "₹600.00", используйте assert
# # old_price = driver.find_element_by_css_selector('.price :nth-child(1) .woocommerce-Price-amount.amount')
# # old_price_text = old_price.text
# # new_price = driver.find_element_by_css_selector('.price :nth-child(2) .woocommerce-Price-amount.amount')
# # new_price_text = new_price.text
# # assert old_price_text == "₹600.00"
# # assert new_price_text == "₹450.00"
# # 6 Добавьте явное ожидание и нажмите на обложку книги
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, ".images"))).click()
# # 7 Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
#driver.quit()

#  5 #
# # 1 Открыть страницу
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# # 2 Нажмите на вкладку "Shop"
# driver.find_element_by_css_selector('#menu-item-40 > a').click()
# # 3 Добавьте в корзину книгу "HTML5 WebApp Development"
# driver.find_element_by_tag_name('[data-product_id="182"]').click()
# # 4 Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# time.sleep(3)
# item = driver.find_element_by_css_selector('#wpmenucartli  > a > span[class=cartcontents]').text
# price = driver.find_element_by_css_selector('#wpmenucartli  > a > span[class=amount]').text
# assert item == "1 Item"
# assert price == "₹180.00"
# # 5 Перейдите в корзину
# driver.find_element_by_css_selector('#wpmenucartli > a').click()
# # 6 Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# subtotal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-subtotal > td > span"))).text
# assert subtotal is not None
# # 7 Используя явное ожидание, проверьте что в Total отобразилась стоимость
# total = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".order-total > td > strong >span"))).text
# assert total is not None
# driver.quit()

#  6 #
# # 1 Открыть страницу
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# # 2 Нажмите на вкладку "Shop"
# driver.find_element_by_css_selector('#menu-item-40 > a').click()
# # 3 Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# driver.find_element_by_tag_name('[data-product_id="182"]').click()
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(3)
# driver.find_element_by_tag_name('[data-product_id="180"]').click()
# time.sleep(3)
# # 4 Перейдите в корзину
# driver.find_element_by_css_selector('#wpmenucartli > a').click()
# # 5 Удалите первую книгу
# time.sleep(3)
# driver.find_element_by_css_selector('tbody> :nth-child(1).cart_item .product-remove :nth-child(1)').click()
# # 6 Нажмите на Undo (отмена удаления)
# total = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.woocommerce-message > a'))).click()
# # 7 В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# num = driver.find_element_by_css_selector('tbody> :nth-child(2).cart_item .input-text.qty.text')
# num.clear()
# num.send_keys('3')
# # 8 Нажмите на кнопку "UPDATE BASKET"
# driver.find_element_by_css_selector('.actions > :nth-child(2).button').click()
# # 9 Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# val_book = driver.find_element_by_css_selector('tbody> :nth-child(2).cart_item .input-text.qty.text')
# value_book = val_book.get_attribute('value')
# assert value_book == "3"
# # 10 Нажмите на кнопку "APPLY COUPON"
# time.sleep(3)
# driver.find_element_by_tag_name('[value="Apply Coupon"]').click()
# # 11
# message_err = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-error"))).text
# assert message_err == 'Please enter a coupon code.'
# driver.quit()

#  7 #
# 1 Открыть страницу
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2 Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
driver.find_element_by_css_selector('#menu-item-40 > a').click()
driver.execute_script("window.scrollBy(0, 300);")
# 3 Добавьте в корзину книгу "HTML5 WebApp Development"
driver.find_element_by_tag_name('[data-product_id="182"]').click()
time.sleep(3)
# 4 Перейдите в корзину
driver.find_element_by_css_selector('#wpmenucartli > a').click()
# 5 Нажмите "PROCEED TO CHECKOUT"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward"))).click()
# 6 Заполните все обязательные поля
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'billing_first_name'))).send_keys('Pupkin')
driver.find_element_by_id('billing_last_name').send_keys('Vasya')
driver.find_element_by_id('billing_email').send_keys('Pupkin@nomail.com')
driver.find_element_by_id('billing_phone').send_keys('+79999999999')
# селектор #
driver.find_element_by_id('select2-chosen-1').click()
driver.find_element_by_id('s2id_autogen1_search').send_keys('Iceland')
driver.find_element_by_class_name('select2-result-label').click()
# остальные поля #
driver.find_element_by_id('billing_address_1').send_keys('Basseynaya st.')
driver.find_element_by_id('billing_address_2').send_keys('11, apt. 5')
driver.find_element_by_id('billing_postcode').send_keys('100000')
driver.find_element_by_id('billing_city').send_keys('St. Petersburg')
# 7 Выберите способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_id('payment_method_cheque').click()
# 8 Нажмите PLACE ORDER
driver.find_element_by_id('place_order').click()
# 9
pay_prov1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-thankyou-order-received"))).text
assert pay_prov1 == "Thank you. Your order has been received."
# 10
pay_prov = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//tfoot/tr[3]/td"))).text
assert pay_prov == "Check Payments"

