from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os 
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements_by_class_name("form-control")
    for element in elements:
       element.send_keys("Мой ответ")

    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_path = os.path.join(current_dir, 'file.txt')

    sendb = browser.find_element_by_css_selector("[type='file']")
    sendb.send_keys(file_path)   

    button = browser.find_element_by_class_name("btn")
    button.click()
    time.sleep(1)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

