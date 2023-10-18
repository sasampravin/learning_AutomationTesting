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
xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[1]/h2')
print(xpath.text)
time.sleep(2)
print('test case successfully executed')
driver.close()

