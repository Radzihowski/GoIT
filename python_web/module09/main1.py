import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        # Scrape quotes
        for quote in response.css(".quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        # Scrape author details
        yield {
            "name": response.css("h3.author-title::text").get().strip(),
            "birthdate": response.css("span.author-born-date::text").get(),
            "birthplace": response.css("span.author-born-location::text").get().strip(),
            "description": response.css("div.author-description::text").get().strip(),
        }

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        author_links = response.css(".quote span a::attr(href)").getall()
        for link in author_links:
            yield response.follow(link, callback=self.parse_author)

    def parse_author(self, response):
        yield {
            "name": response.css("h3.author-title::text").get().strip(),
            "birthdate": response.css("span.author-born-date::text").get(),
            "birthplace": response.css("span.author-born-location::text").get().strip(),
            "description": response.css("div.author-description::text").get().strip(),
        }
