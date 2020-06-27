from os import getcwd
import re
from bs4 import BeautifulSoup

class HtmlBuilder:

    def __init__(self, htmlfilename, path=""):
        self.htmlfilename = htmlfilename
        self.template = self.extract_template_data()
        self.copy_template_to_new_file(path)
        self.htmlfile = open(f"{path}{self.htmlfilename}.html", "r+")
        self.soup = BeautifulSoup(self.htmlfile, "html.parser")

    def extract_template_data(self):
        with open(r"../templates/base_preset.html", "r") as template_file:
            ret = template_file.read()
        return ret

    def copy_template_to_new_file(self, path):
        self.htmlfile = open(f"{self.htmlfilename}.html", "w")
        self.htmlfile.write(self.template)
        self.htmlfile.close()
   

    def write_line(self, *line):
        table = self.soup.find("table")
        linesoup = BeautifulSoup(f'<tr data-type="ModContainer"><td data-type="DisplayName">{line[0]}</td><td><span class="from-steam">Steam</span></td><td><a href="{line[1]}" data-type="Link">{line[1]}</a></td></tr>', "html.parser")
        table.append(linesoup)

    def change_meta_tag(self):
        tag = self.soup.find("meta", {"name":"arma:PresetName"})
        tag['content'] = self.htmlfilename

    def change_header(self):
        tag = self.soup.find("h1").find("strong")
        tag.string = self.htmlfilename


    def initialize_file(self):
        self.change_meta_tag()
        self.change_header()
        print(self.soup.contents)
    
    def finish(self):
        self.htmlfile.close()