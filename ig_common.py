import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import urllib.request
import ssl
import os

def get_tag_name(search_tag, driver):
    driver.get('https://www.instagram.com')
    time.sleep(20)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(os.getenv('IG_username'))
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(os.getenv('IG_password'))
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
    time.sleep(15)
    # driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys(search_tag)
    time.sleep(15)
    lst = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div').text.split('\n')
    list_of_tag = [v.strip("#") for i, v in enumerate(lst) if i % 2 == 0]
    return list_of_tag

def get_user_name(list_of_tag, driver):
    list_of_account = []
    for tag in list_of_tag:
        driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
        time.sleep(5)
        post_table = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div')
        for post in post_table.find_elements(By.CSS_SELECTOR, '._aabd'):
            post.click()
            account_name = post.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div').textdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div').click()
            list_of_account.append(account_name)
    return list_of_account

def list_user_csv(driver,search_tag,type_of_media):
    list_of_tag = get_tag_name(driver)
    list_of_account = list(set(get_user_name(list_of_tag, driver)))
    columns = [f'{search_tag} Account Name {type_of_media}']
    with open('csv/Account_name.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        # Write each item in a new row
        for item in list_of_account:
            writer.writerow([item])

def get_reel_link(driver):
    master = []
    df = pd.read_csv('csv/Account_name.csv', index_col=0)
    for index, row in df.iterrows():
        driver.get(f'https://www.instagram.com/{index}/reels')
        print(index)
        time.sleep(30)
        if len(driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div/div')) == 0: continue
        table = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div/div')
        for element in table.find_elements(By.CSS_SELECTOR, '.x1i10hfl'):
            dict = {
                'Account Name': index,
                'Reel Link': element.get_attribute('href')
            }
            master.append(dict)
    df = pd.DataFrame(master)
    df.to_csv("csv/Account_name_reels.csv", index=True)