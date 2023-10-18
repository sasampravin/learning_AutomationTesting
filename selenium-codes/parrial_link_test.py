from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager
serv_obj = ChromeService("D:\Drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Forgotten').click()
time.sleep(2)
print('\ntest case successfully executed')
driver.close()

