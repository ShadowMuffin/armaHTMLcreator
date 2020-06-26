from bs4 import BeautifulSoup
import requests

class Scraper:

    def __init__(self, page=""):
        self.page = page
        self.__soup = None
        self.links = {}
        self.create_bs()




    def create_bs(self):
        self.soup = BeautifulSoup(requests.get(self.page).content, "html.parser")

    def extract_modlist(self):
        tags = self.soup.find("div", id="RequiredItems").find_all('a')
        return tags

    def create_links(self, tags):
        for tag in tags:
            self.links[tag.text.strip()] = tag["href"]




def main():
    scraper = Scraper(r"https://steamcommunity.com/sharedfiles/filedetails/?id=2139200035&searchtext=")
    scraper.create_links(scraper.extract_modlist())
    print(scraper.links)

main()