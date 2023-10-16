from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from postScraper import PostScraper
from userScraper import UserScraper
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-t", "--type", dest="type", help="type of scrape: post or user", required=True)
    
    # if user scrape
    parser.add_argument("-u", "--user", dest="user_url", help="user profile link")
    
    # if post scrape
    parser.add_argument("-q", "--query", dest="search_term",  help="search query in quotes")
    parser.add_argument("-c", "--count", dest="total_post_count", help="number of posts or users to scrape", default=50)
    
    args = parser.parse_args()
        
    options = ChromeOptions()
    options.add_argument("start-maximized");
    driver = webdriver.Chrome(options=options)
    
    if(args.type == "user"):
        user_scraper = UserScraper(driver, args.search_term)
        user_scraper.run()
        sys.exit()

    post_scraper = PostScraper(driver, args.search_term, int(args.total_post_count))
    post_scraper.run()