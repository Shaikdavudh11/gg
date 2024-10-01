from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
def test_dashboard():
    driver.get('https://www.gamutgurus.com/')
    time.sleep(10)
# def contact():
#     contact_us = driver.find_element('xpath', '/html/body/section/div/div/div[1]')
#     contact_us.click()
#     time.sleep(10)
#     write_query = driver.find_element('xpath','//*[@id="sticky-enquiry-form"]/div[2]/textarea')
#     write_query.send_keys('Test Query')
#     email = driver.find_element('id','frm-email')
#     email.send_keys('test@gamutgurus.com')
#     mobile = driver.find_element('id','frm-mobile')
#     mobile.send_keys('9866763270')
#     submit_query = driver.find_element('id','sticky-enquirt-btn')
#     submit_query.click()
# def devops_course():
    devops_details = driver.find_element('xpath','/html/body/section/section[5]/section[1]/div/div[1]/div/div/div[3]/a/div[1]/ul/li[2]')
    devops_details.click()
    time.sleep(5)
    download_curriculum = driver.find_element('xpath','/html/body/section[1]/section[2]/div[2]/div/div/div[1]/div[3]/div[1]/button')
    download_curriculum.click()
    email = driver.find_element('id','user-email')
    email.send_keys('test@gamutgurus.com')
    phone = driver.find_element('id','user-phone')
    phone.send_keys('9866763270')
    download = driver.find_element('xpath','//*[@id="lead-form"]/button')
    download.click()
    time.sleep(50)
# def contact():
#     ggpap = driver.find_element('id','navbarSupportedContent')
#     time.sleep(10)
#     assert 'https://www.gamutgurus.com/' in driver.current_url
# # def test_apply_button:
# #     apply_button = driver.find_element(By.CSS_SELECTOR, 'button[data-target="#exampleModal3"]')
# #     apply_button.click()
# #     time.sleep(10)