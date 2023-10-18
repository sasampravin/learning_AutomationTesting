from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# somthing went wrong in the code please check once before execution
serv_obj = ChromeService("C:\Drivers\chromedriver_win32\chromedriver")
dr = webdriver.Chrome(service=serv_obj)
dr.get('https://www.amazon.com/')
dr.maximize_window()
dr.find_element(By.CSS_SELECTOR, '//*[@id="twotabsearchtextbox"]').send_keys('apjphotoframes')
dr.implicitly_wait(5)
print('\ntest case successfully executed')
dr.close()

