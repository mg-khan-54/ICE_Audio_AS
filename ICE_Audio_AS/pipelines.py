# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class IceAudioAsPipeline:
#     def process_item(self, item, spider):
#         return item

"""this pipeline is for images downloaded with custom naming"""
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline


class custom_name_pipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
       return request.url.split('/')[-1]


class files_pdf_naming(FilesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        refined_name = request.url.split('/')[-1]
        return refined_name
