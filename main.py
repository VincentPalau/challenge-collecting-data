"""
Main program follow to work flow.

"""

from utils.file_operation import createCSV
from utils.scrape import ScrapeImmoweb, fetch_urls


def launchScrape():
    set_urls = fetch_urls(10000)
    createCSV("./utils/properties.csv")
    for url in set_urls:
        properties = {}
        ad = ScrapeImmoweb(url,properties)
        ad.scraping_ads()


launchScrape()
        
    
    



