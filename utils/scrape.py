from threading import Thread
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


class FetchUrls(Thread):
    def __init__(self, page, set_urls):
        Thread.__init__(self)
        self.page = page
        self.set_urls = set_urls

    def run(self, driver):
        driver.get(self.page)
        soup = BeautifulSoup(driver.page_source, "lxml")
        tags_adverts = soup.find_all("a", class_ = "card__title-link")
        for advert in tags_adverts:
            self.set_urls.add(advert.get("href"))

def fetch_urls(number_of_adverts):
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

if __name__ == "__main__":
    set_urls = fetch_urls(1e4)
    print(len(set_urls))
    print(set_urls)
