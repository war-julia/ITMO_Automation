# from selenium import webdriver
#
# driver = webdriver.Chrome()  # драйвер
# driver.get('https://demoqa.com/')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://demoqa.com/')

try:
    icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
    print('Элемент найден')
except NoSuchElementException:
    print('Элемент не найден')

driver.quit()




