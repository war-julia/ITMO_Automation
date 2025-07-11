# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

        # Поиск элементов
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "login-button")

#
    if username and password and submit_button:
        print("Элементы найдены")



# Вызов функции
check_elements()


