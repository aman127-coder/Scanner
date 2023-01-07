import datetime
import telegram
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dateutil.tz import gettz

bot_token = "5043956698:AAEAyotBQJB9Z5TpDZl1LMQiltyCm1d_kSc"
group_id = "cllinkscan"

bot = telegram.Bot(token=bot_token)
mwdurl = "https://chartink.com/screener/dikgha"
sendFileUrl = "".join(["https://api.telegram.org/bot",
                      bot_token, "/sendDocument?chat_id=", group_id])

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")


def get_screened_stocks_mwd(mwdurl):

    driver = webdriver.Chrome(
        executable_path=".\chromedriver_win32\chromedriver.exe", options=chrome_options)
    driver.get(mwdurl)
    table = pd.read_html(driver.find_element(
        By.XPATH, '//*[@id=\"DataTables_Table_0\"]').get_attribute('outerHTML'))
    driver.close()
    return table[0]


def mwd():
    print("inside mwd")

    screened_stocks = get_screened_stocks_mwd(mwdurl)
    screened_stocks_list = list(screened_stocks['Symbol'])
    for stock in screened_stocks_list:
        bot.send_message(
            chat_id=group_id, text=f'{stock} :: MWD Setup {datetime.datetime.now(tz=gettz("Asia/Kolkata"))}')
    print("Ending Else")


while True:
    if (datetime.date.today().weekday() != 6) & (datetime.date.today().weekday() != 5):

        hours = [9, 10, 11, 12, 13, 14, 15]
        minutes = [0, 15, 30, 45]

        for hour in hours:
            for minute in minutes:
                schedule_time = datetime.time(hour, minute)
                if (schedule_time >= datetime.time(9, 15)) & (schedule_time <= datetime.time(15, 30)):
                    print("Inside For and Before Test mwd execution ",
                          datetime.datetime.now(tz=gettz("Asia/Kolkata")))
                    mwd()
                    print("Inside For and After mwd execution")
