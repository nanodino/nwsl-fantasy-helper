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

def get_scores_and_fixtures_table(driver):
    scores_and_fixtures_url = "https://fbref.com/en/comps/182/schedule/NWSL-Scores-and-Fixtures#sched_11498_1"
    scores_and_fixtures_page = driver.get(scores_and_fixtures_url)
    time.sleep(3)
    scores_and_fixtures_source = driver.page_source
    scores_soup = BeautifulSoup(scores_and_fixtures_source, features="html.parser")
    scores_table = scores_soup.find("table", {"id": "sched_11498_1"})

    return scores_table

def get_past_match_report_urls(scores_table):
    scores_table_head = scores_table.find('thead')
    scores_table_body = scores_table.find('tbody')
    
    cols = scores_table_head.find_all('th')
    fixtures = scores_table_body.find_all('tr')
    col_names = []

    for col in cols:
        col_names.append(col.get_text())

    print(col_names)


def read_match_data(match_source):
    match_soup = BeautifulSoup(match_source)
    print(match_soup)


def main():
    print("main!")
    driver = set_up_webdriver()
    scores_and_fixtures = get_scores_and_fixtures_table(driver)
    get_past_match_report_urls(scores_and_fixtures)
    # match_source = access_fbref(driver)

if __name__ == '__main__':
    main()