import scrapy

from scrapy_sreality.items import Listing


class ListingSpider(scrapy.Spider):
    TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
    name = "listings"

    def start_requests(self):
        for i in range(1, 26):
            url = "https://www.sreality.cz/hledani/prodej/byty?strana=" + str(i)
            yield scrapy.Request(
                url,
                meta={"playwright": True}
            )

    def parse(self, response):

        for listing in response.css(".dir-property-list > .property"):
            listing = Listing(
                title=listing.css(".name::text").get(),
                imageURL="https://www.sreality.cz" + listing.css('.title::attr("href")').get(),
            )
            yield listing

