import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# # 1 Открыть вкладку
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# #driver.implicitly_wait(5)
# # 2 Нажмите на вкладку "My Account Menu"
# driver.find_element_by_id('menu-item-50').click()
# # 3 емейл для регистрации
# driver.find_element_by_id('reg_email').send_keys('ritatoporita1@gmail.com')
# # 4 пароль
# driver.find_element_by_id('reg_password').send_keys('Parol123321!')
# driver.find_element_by_id("reg_password").click()
# # 5 Нажмите кнопку register
# time.sleep(3)
# driver.find_element_by_css_selector('.register .woocommerce-Button.button').click()
# driver.quit()

#  2  #
# 1 Открыть вкладку
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
#driver.implicitly_wait(5)
# 2 Нажмите на вкладку "My Account Menu"
driver.find_element_by_id('menu-item-50').click()
# 3 email для логина
driver.find_element_by_id('username').send_keys('ritatoporita1@gmail.com')
# 4 пароль
driver.find_element_by_id('password').send_keys('Parol123321!')
driver.find_element_by_id("password").click()
# 5 Нажмите кнопку "Login"
time.sleep(3)
driver.find_element_by_css_selector('.login .woocommerce-Button.button').click()
# 6 проверка Logout
element = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")
element_get_text = element.text
if element_get_text == "Logout":
    print('на странице есть элемент "Logout"')
else:
    print('на странице нет элемента "Logout"')
driver.quit()