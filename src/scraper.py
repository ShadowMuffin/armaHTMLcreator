from bs4 import BeautifulSoup
import requests

class Scraper:

    def __init__(self, page=""):
        self.page = page
        self.soup = self.create_bs()
        self.links = {}


    def create_bs(self):
        return BeautifulSoup(requests.get(self.page).content, "html.parser")

    def extract_modlist(self):
        tags = self.soup.find("div", id="RequiredItems").find_all('a')
        return tags

    def create_links(self, tags):
        for tag in tags:
            self.links[tag.text.strip()] = tag["href"]

    def extract_mission_name(self):
        return self.soup.find("div", "workshopItemTitle").text.strip()


