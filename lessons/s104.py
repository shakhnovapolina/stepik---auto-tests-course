from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    field1 = browser.find_element_by_xpath("//input[@class='form-control first'][@required='']")
    field1.send_keys("Ivan")
    time.sleep(2)
    field2 = browser.find_element_by_xpath("//input[@class='form-control second'][@required='']")
    field2.send_keys("Ivanov")
    time.sleep(2)
    field3 = browser.find_element_by_xpath("//input[@class='form-control third'][@required='']")
    field3.send_keys("mail@none.ru")
    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(2)

    link1 = "http://suninjuly.github.io/registration2.html"
    browser.get(link1)

    # Ваш код, который заполняет обязательные поля
    field1 = browser.find_element_by_xpath("//input[@class='form-control first'][@required='']")
    field1.send_keys("Ivan")
    time.sleep(2)
    field2 = browser.find_element_by_xpath("//input[@class='form-control second'][@required='']")
    field2.send_keys("Ivanov")
    time.sleep(2)
    field3 = browser.find_element_by_xpath("//input[@class='form-control third'][@required='']")
    field3.send_keys("mail@none.ru")
    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()