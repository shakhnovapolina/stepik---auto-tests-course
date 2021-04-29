from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    num1 = int(x_element.text)
    у_element = browser.find_element_by_id("num2")
    num2 = int(у_element.text)
    res = num1 + num2

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='" + str(res) + "']").click()

    button = browser.find_element_by_tag_name("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()