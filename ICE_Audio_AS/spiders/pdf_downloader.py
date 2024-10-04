"""This program scraps the data from website named Ice Audio AS"""
import scrapy

class IceAudioAs(scrapy.Spider):
    """spider class to scrape website name Ice Audio AS"""

    name = "images_downloader"
    start_urls = [
        "https://iceaudio.no/"
    ]

    def parse(self, response):
        """parse method which provides response from the given link"""

        link = response.css("ul#treemenu1:first-child ul a::attr('href')").getall()
        # link = response.css("ul#treemenu1:first-child ul a")
        yield from response.follow_all(link, self.parse_scrap)

    def parse_scrap(self, response):
        """this function yields the category panel from
        the main page and calls the next function to scrap next linked page"""
        link = response.css("div.boxVareliste td:nth-child(2) a::attr('href')")
        yield from response.follow_all(link, self.parse_scrap_page)

    def parse_scrap_page(self, response):
        """This method scraps and downloads all available PDF files from the product page"""

        url_pdf = response.xpath("//a[contains(@href,'pdf')]/@href").getall()
        url_list = []
        for url in url_pdf:
            url_list.append(response.urljoin(url))
        name_list = []
        for link in url_pdf:
            raw_file_name = link.split("/")[-1]
            name_list.append(raw_file_name)

        yield {
            "Title": name_list,
            "file_urls": url_list,
        }


