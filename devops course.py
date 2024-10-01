# from telnetlib import EC
#
# from selenium import webdriver
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# def test_dashboard():
#     driver.get('https://www.gamutgurus.com/')
#     time.sleep(10)
#     devops_details = driver.find_element('xpath',
#                                          '/html/body/section/section[5]/section[1]/div/div[1]/div/div/div[3]/a/div[1]/ul/li[2]')
#     devops_details.click()
#     time.sleep(5)
#     download_curriculum = driver.find_element('xpath',
#                                               '/html/body/section[1]/section[2]/div[2]/div/div/div[1]/div[3]/div[1]/button')
#     download_curriculum.click()
#     email = driver.find_element('id', 'user-email')
#     email.send_keys('test@gamutgurus.com')
#     phone = driver.find_element('id', 'user-phone')
#     phone.send_keys('9866763270')
#     download = driver.find_element('xpath', '//*[@id="lead-form"]/button')
#     download.click()
#     time.sleep(10)
#     # demo_vedeo = driver.find_element('xpath','/html/body/section[1]/section[2]/div[2]/div/div/div[2]/a/img')
#     # demo_vedeo.click()
#     # time.sleep(10)
#
#     demo_video = driver.find_element('xpath', '/html/body/section[1]/section[2]/div[2]/div/div/div[2]/a/img')
#     demo_video.click()
#
#     # Wait for the new tab to open
#     time.sleep(60)
#
#     # Get the current window handle (original tab)
#     original_tab = driver.current_window_handle
#
#     # Switch to the new tab
#     for handle in driver.window_handles:
#         if handle != original_tab:
#             driver.switch_to.window(handle)
#             break
#
#     # Wait for the video to load (you can adjust the condition based on your needs)
#     time.sleep(10)  # This is a simple wait; consider using WebDriverWait for better practice
#
#     # Check if the video is loaded (replace 'video_xpath' with the actual XPath of the video element)
#     try:
#         video_element = driver.find_element('xpath', '/html/body/section[1]/section[2]/div[2]/div/div/div[2]/a/img')  # Replace with actual video element XPath
#         print("Video is loading.")
#     except:
#         print("Video is not loading.")
#
#     # Switch back to the original tab
#     driver.switch_to.window(original_tab)
#
#     keyfeature_section = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="course_navbar"]/ul/li[1]/a')))
#     keyfeature_section.click()
#     driver.execute_script("arguments[0].click();", keyfeature_section)
#     time.sleep(10)
from selenium import webdriver
import time

driver = webdriver.Chrome()


def test_dashboard():
    driver.get('https://www.gamutgurus.com/')
    time.sleep(10)
    devops_details = driver.find_element('xpath', '/html/body/section/section[5]/section[1]/div/div[1]/div/div/div['
                                                  '3]/a/div[1]/ul/li[2]')
    devops_details.click()
    time.sleep(5)
    download_curriculum = driver.find_element('xpath',
                                              '/html/body/section[1]/section[2]/div[2]/div/div/div[1]/div[3]/div['
                                              '1]/button')
    download_curriculum.click()
    email = driver.find_element('id', 'user-email')
    email.send_keys('test@gamutgurus.com')
    phone = driver.find_element('id', 'user-phone')
    phone.send_keys('9866763270')
    download = driver.find_element('xpath', '//*[@id="lead-form"]/button')
    download.click()
    time.sleep(10)
    demo_video = driver.find_element('xpath', '/html/body/section[1]/section[2]/div[2]/div/div/div[2]/a/img')
    demo_video.click()
    time.sleep(60)
    original_tab = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
    time.sleep(10)
    try:
        video_element = driver.find_element('xpath', '/html/body/section[1]/section[2]/div[2]/div/div/div[2]/a/img')
        print("Video is loading.")
    except:
        print("Video is not loading.")
    driver.switch_to.window(original_tab)
    time.sleep(10)
    # keyfeature_section = driver.find_element('xpath', '//*[@id="course_navbar"]/ul/li[1]/a')
    # keyfeature_section.click()
    training_button = driver.find_element('xpath','//*[@id="master-project-work-tab"]/li[1]/img')
    training_button.click()
    time.sleep(5)
    placement_button = driver.find_element('xpath','//*[@id="Beginners-tab"]')
    placement_button.click()
    time.sleep(5)
    afterjob_button = driver.find_element('xpath','//*[@id="Beginners-tab"]')
    afterjob_button.click()
    time.sleep(5)
test_dashboard()
driver.quit()
