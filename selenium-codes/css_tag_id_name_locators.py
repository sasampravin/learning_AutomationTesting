from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time
serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver")
dr = webdriver.Chrome(service=serv_obj)
dr.get('https://admin-demo.nopcommerce.com/login')
dr.maximize_window()
dr.find_element(By.CSS_SELECTOR, 'input#Email').clear()
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, '#Email').send_keys('admin@yourstore.com')
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, 'input.password').send_keys('admin')
time.sleep(1)
print('css tag-id-class test successfully')
dr.close()
