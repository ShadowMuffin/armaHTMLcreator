import scraper
import html_builder




def main():
    page = input("Input page > ")
    scrap = scraper.Scraper(page)
    builder = html_builder.HtmlBuilder(scrap.extract_mission_name())
    builder.initialize_file()

    scrap.create_links(scrap.extract_modlist())
    links = scrap.links
    for mod_name in links:
        builder.write_line(mod_name, links[mod_name])

    builder.finish()

main()



