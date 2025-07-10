# from selenium import webdriver
#
# driver = webdriver.Chrome()  # драйвер
# driver.get('https://demoqa.com/')


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # драйвер
driver.get('https://demoqa.com/')

#поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is not None:
    print('Элемент  не найден')
else:
    print('Элемент найден')



