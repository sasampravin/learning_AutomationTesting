from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager
serv_obj = ChromeService("C:\Drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_1aeuamiuit_b&adgrpid=58746164597&hvpone=&hvptwo=&hvadid=617721280249&hvpos=&hvnetw=g&hvrand=17035119575916738990&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061994&hvtargid=kwd-298741529014&hydadcr=5903_2362026')
driver.maximize_window()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input.nav-input[type=text]').click()
time.sleep(2)
print('\ntest case successfully executed')
driver.close()

