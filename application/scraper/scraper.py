import requests
from bs4 import BeautifulSoup


class CarScraper:

    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        response = requests.get(
            self.url,
            timeout=30,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()
        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")

        listings = []

        for card in soup.select(".car-listing"):
            title = card.select_one(".title")
            price = card.select_one(".price")
            mileage = card.select_one(".mileage")
            location = card.select_one(".location")

            listing = {
                "title": title.get_text(strip=True) if title else None,
                "price": price.get_text(strip=True) if price else None,
                "mileage": mileage.get_text(strip=True) if mileage else None,
                "location": location.get_text(strip=True) if location else None,
                "source": self.url
            }

            listings.append(listing)

        return {
            "source": self.url,
            "total_listings": len(listings),
            "listings": listings
        }

    def run(self):
        html = self.fetch_page()
        return self.parse(html)

