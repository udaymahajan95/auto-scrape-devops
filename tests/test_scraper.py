from pathlib import Path

from application.scraper.scraper import CarScraper


def test_parse_car_listings():

    scraper = CarScraper("https://example-car-site.com")

    fixture_path = Path(__file__).parent / "fixtures" / "sample_cars.html"

    html = fixture_path.read_text()

    result = scraper.parse(html)

    assert result["total_listings"] == 3

    assert result["listings"][0]["title"] == "2022 Toyota Camry SE"
    assert result["listings"][0]["price"] == "$25,500"
    assert result["listings"][0]["mileage"] == "32,450 miles"
    assert result["listings"][0]["location"] == "New York, NY"

    assert result["listings"][1]["title"] == "2021 Honda Accord Sport"
    assert result["listings"][2]["title"] == "2023 Ford Mustang GT"

