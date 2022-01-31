from bs4 import BeautifulSoup
import requests

property_url = "https://www.immoweb.be/fr/annonce/appartement/a-vendre/liege/4020/9719865?searchId=61f3fad5896e6"

request = requests.get(property_url)
soup = BeautifulSoup(request.content, "lxml")

for element in soup.find_all("span", attrs = {"aria-hidden" : "true"}):
    print(element.text)