from selenium import webdriver
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    res = math.log(abs(12 * math.sin(x)))


    browser.find_element_by_id("answer").send_keys(str(res))
    browser.find_element_by_id("robotCheckbox").click()

    selector = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", selector)
    selector.click()
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