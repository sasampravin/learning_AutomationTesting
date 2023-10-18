from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager
serv_obj = ChromeService("C:\Drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.find_element(By.ID, 'email').send_keys('abcd@gmail.com')
time.sleep(1)
driver.find_element(By.NAME, 'pass').send_keys('abc123')
time.sleep(3)
print('First test case successfully executed on locators NAME,ID')
driver.close()

