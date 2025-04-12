import scrapy
import json
from pathlib import Path

class JsonSpider(scrapy.Spider):
    name = "json"

    def start_requests(self):
        file_path = Path(__file__).parent.parent.parent.parent / "jobs_project" / "data" / "s01.json"
        if file_path.exists():
            yield scrapy.Request(f"file://{file_path}", callback=self.parse)
        else:
            self.logger.error(f"File not found: {file_path}")

    def parse(self, response):
        json_data = json.loads(response.text)
        for data in json_data:
            yield data