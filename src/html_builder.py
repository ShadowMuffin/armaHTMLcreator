from os import getcwd

class HtmlBuilder:

    def __init__(self, htmlfilename, path=""):
        self.htmlfilename = htmlfilename
        self.htmlfile = open(f"{path}{htmlfilename}", "w")
        self.template = self.extract_template_data()
        self.write_initial_part()

    def extract_template_data(self):
        with open(r"../templates/base_preset.html", "r") as template_file:
            ret = template_file.read()
        return ret

    
    def write_initial_part(self):
        self.htmlfile.write(self.extract_template_data())

    def write_line(self, *line):
        self.htmlfile.seek(1546)
        self.htmlfile.write(f'<tr data-type="ModContainer"><td data-type="DisplayName">{line[0]}</td><td><span class="from-steam">Steam</span></td><td><a href="{line[1]}" data-type="Link">{line[1]}</a></td></tr>')

    def finish(self):
        self.htmlfile.close()

    