from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    treasure = browser.find_element_by_id("input_value")
    tre_val = treasure.text
    y = calc(tre_val)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(y)

    #option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    #option1.click()

    #button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    #option2.click()

    button = browser.find_element_by_class_name("btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(1)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

