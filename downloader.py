import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv

df = pd.read_csv('csv/Account_name_reels.csv')

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

for index, row in df.iterrows():
    print(index)
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://ummy.net/en38rR/')
    driver.find_element(By.XPATH, '/html/body/section/div/div/input').send_keys(f"{row['Reel Link']}")
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/section/div/div/button').click()
    time.sleep(20)
    driver.find_element(By.XPATH, '/html/body/div[3]/section[2]/div[2]/div[2]/div/a').click()
    time.sleep(20)
    driver.execute_script("window.open('');")
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
