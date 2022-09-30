from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import os
import time

def set_up_webdriver():
    options = Options()
    options.add_argument("-headless")
    serv = Service(log_path=os.devnull, executable_path = GeckoDriverManager().install())
    driver = Firefox(options=options, service=serv)

    return driver

def get_scores_and_fixtures_table(driver):
    i = 0
    in_error = 0
    while(in_error == 0):
        scores_and_fixtures_url = "https://www.fotmob.com/leagues/9134/matches/nwsl/by-date?page={}".format(i)
        i += 1

    return driver  #temp return

def is_fotmob_in_error():
    pass