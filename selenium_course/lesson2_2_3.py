from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

#def calc(x):
 # return str(num1+num2)


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_1 = browser.find_element_by_id("num1")
    num1 = int(find_1.text)

    find_2 = browser.find_element_by_id("num2")
    num2 = int(find_2.text)

    y = str(num1+num2 )

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y) 

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
