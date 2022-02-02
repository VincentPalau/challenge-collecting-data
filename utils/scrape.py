from threading import Thread, RLock
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils.file_operation import saveToCSV

class FetchUrls(Thread):
    '''
    Collect URLs of ads to scrape

    Attributes :
    ------------
    page : URL of the page
    set_urls : the set where the links from page are stored (we use set to avoid duplicates)
    '''
    def __init__(self, page: str, set_urls: set[str]) -> None:
        Thread.__init__(self)
        self.page = page
        self.set_urls = set_urls

    def run(self, driver: webdriver) -> None:
        '''
        Scrape page to fetch url of each ad
        '''
        driver.get(self.page)
        soup = BeautifulSoup(driver.page_source, "lxml")
        tags_adverts = soup.find_all("a", class_ = "card__title-link")
        for advert in tags_adverts:
            self.set_urls.add(advert.get("href"))

def fetch_urls(number_of_adverts: int) -> set[str]:
    '''
    Returns a set of URLs for a required number of ad
    '''
    set_urls = set()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    i = 1
    while len(set_urls) < number_of_adverts:
        page = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={i}&orderBy=relevance"
        fetch = FetchUrls(page, set_urls)
        fetch.run(driver)
        i += 1
    driver.close()
    return set_urls

class ScrapeImmoweb(Thread):
    '''
    Scrape a single ad.

    Attributes :
    ------------
    keywords_list : a list of the information to scrape from the ad
    url : the URL of the ad
    dictionary : the dictionary to store all the information
    '''
    keywords_list = ["Price", "Bedrooms", "Living area", "Kitchen type", "Furnished", "Terrace surface", "Garden surface", "Surface of the plot", "Number of frontages", "Swimming pool", "Building condition"]
    def __init__(self, url: str, dictionary: dict) -> None:
        Thread.__init__(self)
        self.url = url
        self.dictionary = dictionary

    def scraping_ads(self) -> None:
        '''
        Scrape information from the ad according to the list of keywords and actually adding the type of property from the URL
        '''
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content,"lxml")
        raw_tables = soup.find_all("table", class_= "classified-table")
        for table in raw_tables:
            for row in table.tbody.find_all("tr"):
                head = row.th
                if not(head is None or head.string is None):
                    clean_head = " ".join(row.th.string.split())
                    if clean_head in self.keywords_list:
                        data = row.td
                        if data is None:
                            self.dictionary[" ".join(row.th.string.split())] = None
                        else:
                            data_string = data.string
                            if data_string is None:
                                if clean_head in ["Living area", "Terrace surface", "Surface of the plot", "Garden surface"]:
                                    for span in data("span"):
                                        span.extract()
                                    clean_data = " ".join(data.contents).split()[0]
                                    self.dictionary[clean_head] = clean_data
                                elif clean_head == 'Price':
                                    self.dictionary[clean_head] = data.span.contents[0].split()[-1]
                                elif len(data.span.contents) > 0 :
                                    list_data = data.span.contents[0].split()
                                    if len(list_data) > 0:
                                        self.dictionary[clean_head] = list_data[0]
                                    else:
                                        self.dictionary[clean_head] = None
                                else:
                                     self.dictionary[clean_head] = None
                            else:
                                self.dictionary[" ".join(row.th.string.split())] = " ".join(data.string.split())
        self.dictionary["Type of property"] = self.url.split('/')[5]
        self.dictionary["Locality"] = self.url.split('/')[7]

if __name__ == "__main__": # only use for testing
    set_urls = fetch_urls(3)
    for url in set_urls:
        properties ={}
        ad = ScrapeImmoweb(url, properties)
        ad.scraping_ads()
        print(properties)
