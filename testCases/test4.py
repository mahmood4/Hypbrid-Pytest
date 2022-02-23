from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import threading
import pyautogui
import time
import cv2
from pytesseract import *
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

ser = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=ser)
from selenium.webdriver.common.by import By
import mss
import mss.tools

pytesseract.tesseract_cmd = r'...tesseract.exe'

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


if __name__ == "__main__":

    window = tk.Tk()
    window.geometry("431x550")
    window.configure(bg="#ECECEC")
    window.title("BOT")
    window.iconbitmap("icon.ico")


    def webscrape(username, original):
        t = time.time()

        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(f'https://cod.tracker.gg/warzone/profile/atvi/{username}/overview')
        page_title = driver.find_elements(By.CLASS_NAME, 'lead')

        if not page_title or page_title[0] == "WARZONE STATS NOT FOUND":
            print("WARZONE STATS NOT FOUND - Private profile")
            usernameBox.delete(0, tk.END)
            usernameBox.insert(0, "WARZONE STATS NOT FOUND - Private profile")

        else:
            usernameBox.delete(0, tk.END)
            usernameBox.insert(0, original)
            search = driver.find_elements(By.CLASS_NAME, 'value')

            if len(search) > 4:
                print("Wins:", search[0].text)
                winsBox.delete(0, tk.END)
                winsBox.insert(0, search[0].text)

                print("Win %:", search[1].text)
                winPercentageBox.delete(0, tk.END)
                winPercentageBox.insert(0, search[1].text)

                print("Kills:", search[2].text)
                killsBox.delete(0, tk.END)
                killsBox.insert(0, search[2].text)

                print("K/D:", search[3].text)
                KDBox.delete(0, tk.END)
                KDBox.insert(0, search[3].text)

                print("Score/min:", search[4].text)
                scoreMinBox.delete(0, tk.END)
                scoreMinBox.insert(0, search[4].text)

            else:
                print("Incorrect name or private profile")

                usernameBox.delete(0, tk.END)
                usernameBox.insert(0, original)

                winsBox.delete(0, tk.END)
                winsBox.insert(0, "-----")

                winPercentageBox.delete(0, tk.END)
                winPercentageBox.insert(0, "-----")

                killsBox.delete(0, tk.END)
                killsBox.insert(0, "-----")

                KDBox.delete(0, tk.END)
                KDBox.insert(0, "-----")

                scoreMinBox.delete(0, tk.END)
                scoreMinBox.insert(0, "-----")

        elapsed = time.time() - t
        print(elapsed, "Time to webscrape")
        webscrapeBox.delete(0, tk.END)
        webscrapeBox.insert(0, str(round(elapsed, 2)) + " seconds")

        driver.close()