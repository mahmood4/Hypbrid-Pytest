import os
import pickle
import time

from selenium import webdriver
driver = webdriver.Chrome(r"C:\syed\test11\chromedriver.exe")# driver path should start with r
URL = "https://www.google.com"
driver.get(URL)
time.sleep(10)
if os.path.exists('cookies.pkl'):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(5)
# check if still need login
# if yes:
# write login code
# when login success save cookies using
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))