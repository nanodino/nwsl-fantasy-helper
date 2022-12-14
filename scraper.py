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
    scores_and_fixtures_url = "https://fbref.com/en/comps/182/schedule/NWSL-Scores-and-Fixtures#sched_11498_1"
    scores_and_fixtures_page = driver.get(scores_and_fixtures_url)
    time.sleep(3)
    scores_and_fixtures_source = driver.page_source
    scores_soup = BeautifulSoup(scores_and_fixtures_source, features="html.parser")
    scores_table = scores_soup.find("table", {"id": "sched_2022_182_1"})
    
    return scores_table

def get_past_match_report_squads_and_urls(scores_table):
    scores_table_head = scores_table.find('thead')
    scores_table_body = scores_table.find('tbody')
    
    cols = scores_table_head.find_all('th')
    col_names = []
    for col in cols:
        col_names.append(col.get_text())

    fixtures = scores_table_body.find_all('tr')
    fixtures_dict = {}
    counter = 1
    for fixture in fixtures:
        try:
            match_report_cell = fixture.find("td", {"data-stat": "match_report"})
            is_past_match = 1 if match_report_cell.get_text() == "Match Report" else 0
        except:
            pass

        if is_past_match == 1:
            try:
                match_url = match_report_cell.contents[0].attrs['href'] 
                home_team = fixture.find("td", {"data-stat": "home_team"}).get_text()
                away_team = fixture.find("td", {"data-stat": "away_team"}).get_text()

                fixtures_dict[counter] = {}
                fixtures_dict[counter]["home"] = home_team
                fixtures_dict[counter]["away"] = away_team
                fixtures_dict[counter]["url"] = match_url
                counter += 1
            except:
                pass

    return fixtures_dict


def access_fbref_boxscore(driver, match_url, home, away):
    match_page = driver.get(match_url)
    time.sleep(9)
    match_source = driver.page_source
    match_soup = BeautifulSoup(match_source, features="html.parser")
    team_tables = match_soup.find_all("div", id=lambda x: x and x.startswith("all_player_stats"))
    keeper_tables = match_soup.find_all("div", id=lambda x: x and x.startswith("all_keeper_stats"))

    home_team_html_table = team_tables[0].find("table")
    away_team_html_table = team_tables[1].find("table")
    home_keeper_html_table = keeper_tables[0].find("table")
    away_keeper_html_table = keeper_tables[1].find("table")

    return home_team_html_table, home_keeper_html_table, away_team_html_table, away_keeper_html_table


def read_match_data(match_source):
    match_soup = BeautifulSoup(match_source)
    print(match_soup)
