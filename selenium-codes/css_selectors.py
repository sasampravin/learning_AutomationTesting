from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver")
dr = webdriver.Chrome(service=ser_obj)
dr.get('https://admin-demo.nopcommerce.com/login')
dr.maximize_window()
dr.find_element(By.CSS_SELECTOR, 'input#Email').clear()
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, '#Email').send_keys('abc@gmail.com')
time.sleep(2)
dr.find_element(By.CSS_SELECTOR, 'input.password').clear()
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, '.password').send_keys('12345')
time.sleep(2)
dr.find_element(By.CSS_SELECTOR, 'input[type=checkbox]').click()
act_title = dr.title
exp_title = 'Your store. Login'
if act_title == exp_title:
    print('login test passed')
else:
    print('login test failed')
print('\nprogram completed successfully')
time.sleep(2)
dr.close()

