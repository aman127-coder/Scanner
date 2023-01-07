import telegram
from dateutil.tz import gettz
import datetime

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
from time import sleep
from dateutil.tz import gettz

#Bot Token from Bot Father
bot_token ="5832588970:AAHiZAPirfyM6cn12hUJ_rhsYCcEqn9g1As"
bot = telegram.Bot(token='5832588970:AAHiZAPirfyM6cn12hUJ_rhsYCcEqn9g1As')
#Group Link or Username
group_id = "@amanscreener"

weeklyMWDUrl = "https://chartink.com/screener/dikgha"

def get_screened_stocks(url):
    driver = webdriver.Chrome(
        executable_path=".\chromedriver_win32\chromedriver")
    driver.get(url)
    table = pd.read_html(driver.find_element(By.XPATH, '//*[@id=\"DataTables_Table_0\"]').get_attribute('outerHTML'))
    driver.close()
    return table[0]


def weeklyMWD():
    print("weeklyMWD")

    screened_stocks = get_screened_stocks(weeklyMWDUrl)
    for index, row in screened_stocks.iterrows():
     s = ' '.join(str(i) for i in row.values)
     bot.send_message(chat_id=group_id, text=f'{s} :: Weekly Setup {datetime.datetime.now(tz=gettz("Asia/Kolkata"))}')
    # screened_stocks_list = dict(screened_stocks['Symbol','Price'])
    # #bot.send_message(chat_id=group_id,text= screened_stocks)
    # print(screened_stocks_list)
    # for stock in screened_stocks_list:
    #     bot.send_message(chat_id=group_id, text=f'{stock} :: Weekly Setup {datetime.datetime.now(tz=gettz("Asia/Kolkata"))}')
    # print("Ending Else")

weeklyMWD()
