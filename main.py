import scraper

def main():
    print("main!")
    driver = scraper.set_up_webdriver()
    scores_and_fixtures = scraper.get_scores_and_fixtures_table(driver)
    match_dict = scraper.get_past_match_report_squads_and_urls(scores_and_fixtures)

    for item in match_dict.items():
        home_team = item[1]['home']
        away_team = item[1]['away']
        url = "https://fbref.com" + item[1]['url']
        match_source = scraper.access_fbref_boxscore(driver, url, home_team, away_team)

if __name__ == '__main__':
    main()