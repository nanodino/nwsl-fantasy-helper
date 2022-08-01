from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import re

def access_fbref():
    options = Options()
    options.add_argument("-headless")
    driver = Firefox(options = options)

    match_url = "https://fbref.com/en/matches/7f334b6a/Houston-Dash-Portland-Thorns-FC-June-12-2022-NWSL"
    match_page = driver.get(match_url)
    time.sleep(3)
    match_source = driver.page_source

    return match_source


def read_match_data(match_source):
    match_soup = BeautifulSoup(match_source)
    print(match_soup)


def main():
    print("main!")
    match_source = access_fbref()
    read_match_data(match_source)

if __name__ == '__main__':
    main()