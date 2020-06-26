import scraper
import html_builder




def main():
    page = input("Input page > ")
    scrap = scraper.Scraper(page)
    builder = html_builder.HtmlBuilder(scrap.extract_mission_name())

    links = scrap.create_links(scrap.extract_modlist())

    for link in links:
        builder.write_line(link, links[link])

    html_builder.finish()

main()



