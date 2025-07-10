# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_elements():
    # Инициализация драйвера (предполагается, что драйвер уже установлен и в PATH)
    driver = webdriver.Chrome()

    try:
        # Переход на страницу
        driver.get("https://www.saucedemo.com/")

        # Поиск элементов
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "login-button")

        # Если все элементы найдены
        if username and password and submit_button:
            print("Элементы найдены")

    except NoSuchElementException:
        print("Один или несколько элементов не найдены")

    finally:
        driver.quit()

# Вызов функции
check_elements()



