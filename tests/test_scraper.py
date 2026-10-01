from application.scraper.scraper import CarScraper


def test_parse():

    scraper = CarScraper("https://example.com")

    html = """
    <html>
        <head>
            <title>Test Car Website</title>
        </head>
    </html>
    """

    result = scraper.parse(html)

    assert result["title"] == "Test Car Website"
