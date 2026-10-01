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

        title = soup.title.string if soup.title else "No title"

        return {
            "source": self.url,
            "title": title.strip()
        }

    def run(self):
        html = self.fetch_page()
        return self.parse(html)
