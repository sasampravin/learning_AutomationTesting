from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver")
dr = webdriver.Chrome(service=ser_obj)
dr.get('https://www.facebook.com/')
dr.maximize_window()
dr.find_element(By.ID, 'email').send_keys('abc@gmail.com')
time.sleep(2)
dr.find_element(By.NAME, 'pass').send_keys('12345')
time.sleep(2)
act_title = dr.title
exp_title = 'Facebook – log in or sign up'
if act_title == exp_title:
    print('login test passed')
else:
    print('login test failed')
print('\nprogram completed successfully')
time.sleep(2)
dr.close()




