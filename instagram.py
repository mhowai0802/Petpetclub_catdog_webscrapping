import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
from instascrape import Reel
search_tag = 'dogvideo'
chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
session_id = '58733906784%3AMuCLBiBfhhbiPh%3A7%3AAYdloud_q7xHsoEZmtRIUbDhpilL5BWjOTeOE7rhaQ'

def get_tag_name(driver):
    driver.get('https://www.instagram.com')
    time.sleep(5)
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(
        'mhw0802')
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(
        'joniwhfe5A')
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
    time.sleep(5)
    # driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div').click()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys(
        '#dogvideo')
    time.sleep(5)
    lst = driver.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div').text.split(
        '\n')
    list_of_tag = [v.strip("#") for i, v in enumerate(lst) if i % 2 == 0]
    return list_of_tag


def get_user_name(list_of_tag, driver):
    list_of_account = []
    for tag in list_of_tag:
        driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
        time.sleep(5)
        post_table = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div')
        for post in post_table.find_elements(By.CSS_SELECTOR, '._aabd'):
            post.click()
            account_name = post.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div').text
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div').click()
            list_of_account.append(account_name)
    return list_of_account


def list_user_csv(driver):
    list_of_tag = get_tag_name(driver)
    list_of_account = list(set(get_user_name(list_of_tag, driver)))
    columns = ['Account Name']

    with open('csv/Account_name.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        # Write each item in a new row
        for item in list_of_account:
            writer.writerow([item])


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43",
    "cookie": f'sessionid={session_id};'
}

driver.get('https://www.instagram.com/louby_love/reels')
table = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/div[3]/div/div/div')
for element in table.find_elements(By.CSS_SELECTOR,'.x1i10hfl'):
    print(element.get_attribute('href'))
    insta_reel = Reel(element.get_attribute('href'))
    insta_reel.scrape(headers=headers)
    insta_reel.download('.\hihi.mp4')
    break
