from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
values = ['dcaf1f90-29a7-4abd-97eb-085388108410@True',
          '3f11e56f-0af4-433c-85ca-0b6499fbd68c@True',
          '0baa596f-51c1-4395-8847-cd0be47e33a3@True',
          '9ed53a83-8107-41f6-92bd-8d2cf53aa577@True',
          'e3da8448-5924-41cb-83ae-c0cd7d3ab720@True']

path ='~/Desktop/proj/geckodriver'
driver = webdriver.Firefox()

driver.get('http://127.0.0.1:8000/quest')
time.sleep(1)
yesbutton = driver.find_element_by_tag_name('input').click()
try:
    for i in values:
        driver.find_element_by_css_selector(f"[value='{i}']").click()
        time.sleep(1)
        driver.find_element_by_id('save').click()
        time.sleep(1)
        alert = driver.switch_to.alert.accept()
        time.sleep(1)
        driver.find_element_by_css_selector("[value='Следующий вопрос']").click()
except NoSuchElementException:
    driver.find_element_by_css_selector("[value='Завершить']").click()
succesful = driver.find_element_by_xpath('//p[contains(text(), "Ваш результат")]')
if succesful:
    print('успешно пройден ')
