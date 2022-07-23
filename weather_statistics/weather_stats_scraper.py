# 1. input location & retrieve url
# 2. change date within url
# ex. https://www.wunderground.com/history/daily/KOAK/date/2020-2-9 -> https://www.wunderground.com/history/daily/KOAK/date/DATE


import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

options = webdriver.ChromeOptions()
#options.add_argument("headless")
PATH = 'Data/chromedriver-1'
driver = webdriver.Chrome(PATH,options=options)
driver.get('https://www.wunderground.com/history')



data = pd.read_csv('power_data.csv')
df = pd.DataFrame(data)

df = df.dropna()

for area in df['Geographic Areas']:
    input = driver.find_element_by_name('historySearch')
    input.send_keys(area)
    input.send_keys(Keys.RETURN)
    driver.find_element_by_class_name('submit-btn button radius ng-star-inserted').click()
    driver.find_element_by_class_name('submit-btn button radius ng-star-inserted').click()
    time.sleep(5)
    print(driver.current_url)
    driver.get('https://www.wunderground.com/history')

