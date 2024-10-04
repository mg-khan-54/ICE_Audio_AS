# """This program scraps the data from website named Ice Audio AS"""
# import csv
# import scrapy
#
# class IceAudioAs(scrapy.Spider):
#     """spider class to scrape website name Ice Audio AS"""
#
#     name = "Audio"
#     start_urls = [
#         "https://iceaudio.no/"
#     ]
#
#     def parse(self, response):
#         """parse methot which provides response from the given link"""
#
#         link = response.css("ul#treemenu1:first-child ul a::attr('href')").getall()
#         # link = response.css("ul#treemenu1:first-child ul a")
#         yield from response.follow_all(link, self.parse_scrap)
#
#     def parse_scrap(self, response):
#         """this function yields the category panel from
#         the main page and calls the next function to scrap next linked page"""
#         link = response.css("div.boxVareliste td:nth-child(2) a::attr('href')")
#         yield from response.follow_all(link, self.parse_scrap_page)
#
#     def parse_scrap_page(self, response):
#         """this method scraps all the data of each product and creates a csv file"""
#         title = response.xpath("//div[@id = 'PInfo_Top']/descendant"
#                                "::strong/text()").get(default='').strip()
#
#         varient = response.xpath("//div[@id = 'PInfo_Top']/text()").get(default='').strip()
#         title_item_number = response.xpath("//div[@id = 'PInfo_Right']/descendant::"
#                                            "tr[1]/descendant::strong/text()").get(default='').strip()
#         value_item_number = response.xpath('//div[@id = "PInfo_Right"]/descendant::'
#                                            'tr[1]/descendant::td[2]/text()').get(default='').strip()
#         title_unit = response.xpath("//div[@id = 'PInfo_Right']/descendant::tr[2]/"
#                                     "descendant::strong/text()").get(default='').strip()
#         value_unit = response.xpath('//div[@id = "PInfo_Right"]/descendant::tr[2]/'
#                                     'descendant::td[2]/text()').get(default='').strip()
#         title_list_price = response.xpath("//div[@id = 'PInfo_Right']/descendant::"
#                                           "tr[3]/descendant::strong/text()").get(default='').strip()
#         value_list_price = response.xpath('//div[@id = "PInfo_Right"]/descendant::'
#                                           'tr[3]/descendant::td[2]/text()').get(default='').strip()
#         title_number_of_packages = response.xpath("//div[@id='PInfo_Right']/descendant"
#                                                   "::tr[4]/descendant::strong/text()").get(default='').strip()
#         value_number_of_packages = response.xpath('//div[@id="PInfo_Right"]/descendant'
#                                                   '::tr[4]/descendant::td[2]/text()').get(default='').strip()
#         title_weight = response.xpath("//div[@id = 'PInfo_Right']/descendant::tr[5]/"
#                                       "descendant::strong/text()").get(default='').strip()
#         value_weight = response.xpath('//div[@id = "PInfo_Right"]/descendant::tr[5]/'
#                                       'descendant::td[2]/text()').get(default='').strip()
#         all_details = response.xpath("//div[@id = 'PInfo_Right']/ul").getall()
#
#         with open("file.csv", "a", newline="", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             writer.writerow([title, varient, title_item_number, value_item_number,
#                              title_unit, value_unit, title_list_price, title_number_of_packages,
#                              value_list_price, value_number_of_packages, title_weight,
#                              value_weight, all_details])
#         yield {
#             "title": title,
#             "varient": varient,
#             "title_item_number": title_item_number,
#             "value_item_number": value_item_number,
#             "title_unit": title_unit,
#             "value_unit": value_unit,
#             "title_list_price": title_list_price,
#             "value_list_price": value_list_price,
#             "title_number_of_packages": title_number_of_packages,
#             "value_number_of_packages": value_number_of_packages,
#             "title_weight": title_weight,
#             "value_weight": value_weight,
#             "details": all_details
#         }
