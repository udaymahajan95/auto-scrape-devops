from scraper.scraper import CarScraper


def main():
    url = "https://example.com"

    scraper = CarScraper(url)

    result = scraper.run()

    print("Scraping completed")
    print(result)


if __name__ == "__main__":
    main()
