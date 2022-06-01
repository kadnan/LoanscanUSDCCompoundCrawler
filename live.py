import scrapy
import json


class USDCCompoundSpider(scrapy.Spider):
    name = 'USDC Compound'
    LOANSCAN_HISTORICAL = "https://api.loanscan.io/v1/interest-rates/historical?provider=CompoundV2&interestRateDomain=Supply&intervaltype=Day&startDateTimestamp=1651449600&tokenSymbol=USDC"
    allowed_domains = ["https://loanscan.io"]
    start_urls = [LOANSCAN_HISTORICAL]

    def parse(self, response):
        records = json.loads(response.text)
        for record in records:
            yield {
                "Value": record['value'],
                "Date": record['date'],
            }
