from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time
serv_obj = ChromeService("C:\Drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.flipkart.com/')
driver.maximize_window()
time.sleep(2)
sliders = driver.find_elements(By.CLASS_NAME, '_1mIbUg')
print(len(sliders))
tags = driver.find_elements(By.TAG_NAME, 'a')
print(len(tags))
print('\ntest case successfully executed')
driver.close()

