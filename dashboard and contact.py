from selenium import webdriver
import time
driver = webdriver.Chrome()
def dashboard():
    driver.get('https://www.gamutgurus.com/')
    time.sleep(5)
    contact_us = driver.find_element('name', 'message')
    contact_us.click()
    time.sleep(10)