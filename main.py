from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd

def access_fotmob():
    options = Options()
    options.add_argument("-headless")
    driver = Firefox(options = options)

    match_url = "https://www.fotmob.com/match/3846084/matchfacts/portland-thorns-vs-houston-dash"
    match_page = driver.get(match_url)
    time.sleep(3)
    match_source = driver.page_source

    return match_source

def main():
    print("main!")

if __name__ == '__main__':
    main()