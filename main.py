from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import pandas as pd
import re
import pathlib
import os

def set_up_webdriver():
    options = Options()
    options.add_argument("-headless")
    serv = Service(log_path=os.devnull, executable_path = GeckoDriverManager().install())
    driver = Firefox(options=options, service=serv)

    return driver

def get_list_of_match_report_urls(driver):
    scores_and_fixtures_url = "https://fbref.com/en/comps/182/schedule/NWSL-Scores-and-Fixtures#sched_11498_1"
    scores_and_fixtures_page = driver.get(scores_and_fixtures_url)
    time.sleep(3)
    scores_and_fixtures_source = driver.page_source

    print(scores_and_fixtures_source)

    return match_source


def read_match_data(match_source):
    match_soup = BeautifulSoup(match_source)
    print(match_soup)


def main():
    print("main!")
    driver = set_up_webdriver()
    match_source = access_fbref(driver)
    read_match_data(match_source)

if __name__ == '__main__':
    main()