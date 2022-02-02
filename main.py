"""
Main program follow to work flow.

"""

from utils.file_operation import createCSV
from utils.scrape import ScrapeImmoweb, fetch_urls


def launchScrape():
    print("Scraping is begin")
    set_urls = fetch_urls(10000)
    print("All urls are fetched")
    createCSV("./utils/properties.csv")
    print("File was created")
    for url in set_urls:
        properties = {}
        ad = ScrapeImmoweb(url,properties)
        ad.scraping_ads()
    print("Scraping is done.")

launchScrape()