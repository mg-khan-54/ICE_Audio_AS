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
        """this method downloads all the available images from the product page"""
        raw_images_urls=response.xpath("//div[@id = 'PInfo_Left']/descendant::a/@href").getall()
        clean_image_urls = []
        for image_url in raw_images_urls:
            url = "https://iceaudio.no/"+image_url[1:]
            clean_image_urls.append(url)

        yield {
            "image_urls": clean_image_urls
        }


