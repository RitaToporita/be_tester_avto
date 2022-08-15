import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# 1 Открыть вкладку
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
# 2 Скролл страницы
driver.execute_script("window.scrollBy(0, 600);")
# 3 Нажмите на название книги "Selenium Ruby"
driver.find_element_by_css_selector('.post-160.product.type-product.status-publish.has-post-thumbnail.product_cat-selenium.product_tag-ruby.product_tag-selenium.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple .woocommerce-LoopProduct-link').click()
# 4 Нажмите на вкладку "REVIEWS"
driver.find_element_by_xpath('//ul[@class="tabs wc-tabs"]/li[2]/a[1]').click()
# 5 Поставьте рейтинг 5 звезд
driver.find_element_by_css_selector('.comment-form-rating .stars .star-5').click()
#6 Заполните поле текстом
driver.find_element_by_id("comment").send_keys('Nice book!')
#7 Заполните поле текстом
driver.find_element_by_id("author").send_keys('Olya')
#8 Заполните поле текстом
driver.find_element_by_id("email").send_keys('ritatoporita69@gmail.com')
#9 Нажмите submit
driver.find_element_by_id('submit').click()
driver.quit()
