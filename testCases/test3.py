from asyncio.windows_events import NULL
from tokenize import Double
from turtle import update
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://csgoempire.com/'
driver = webdriver.Chrome(r"C:\Test\chromedriver.exe")
driver.get(url)


def func_countdown():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-2xl.font-bold.font-numeric")))
    timer_t = driver.find_element(By.CSS_SELECTOR, ".text-2xl.font-bold.font-numeric").text

    return timer_t


def func_check_rolling():
    timer = func_countdown()
    check = driver.find_element(By.CSS_SELECTOR, ".text-center.text-light-grey-1.uppercase.tracking-wide")

    if bool(check.is_displayed) == True:
        print("You can Bet: " + timer)

    if (bool(check.is_displayed) != True):
        print("rolling")


while True:
    func_check_rolling()
