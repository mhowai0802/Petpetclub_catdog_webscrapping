import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv

df = pd.read_csv('csv/Account_name_reels.csv')

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

for index, row in df.iterrows():
    driver.get('https://ummy.net/en38rR/')
    driver.find_element(By.XPATH, '/html/body/section/div/div/input').send_keys(f"{row['Reel Link']}")
    driver.find_element(By.XPATH, '/html/body/section/div/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/section[2]/div[3]/div/div[1]/a').click()
    time.sleep(5)
