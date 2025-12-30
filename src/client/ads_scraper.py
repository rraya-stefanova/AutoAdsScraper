from typing import Optional, Any

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from src.client import HTTPClient

load_dotenv()

class AutoAdsScraper(HTTPClient):

    BASE_URL = "https://www.auto.bg"
    SEARCH_URL = f"{BASE_URL}/obiavi/avtomobili-dzhipove"
    HEADERS = {
        "authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        # in order to prevent 403:
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",

    }

    def fetch_search_page(self) -> Any:
        return self.get_data(self.SEARCH_URL, headers=self.HEADERS)

    def extract_data(self) -> None:

        data = self.fetch_search_page()

        if isinstance(data, dict):
            self.process_json(data)
        else:
            for page in range(1, 6):
                if page == 1:
                    url = self.SEARCH_URL
                else:
                    url = f"{self.SEARCH_URL}/page/{page}"

            response = requests.get(url, headers=self.HEADERS)
            cars = self.process_html(response.text)
            # print(f"Found {len(cars)} cars")
            # print(cars[:3])

    def process_json(self, data: dict) -> None:
        pass

    def process_html(self, html: str) -> list[dict]:
        soup = BeautifulSoup(html, "html.parser")
        ads = soup.select('a[href^="/obiavi/avtomobili-dzhipove')

        for ad in ads:
            print(ad.prettify()[:1000])
            title_tag = ad.select_one("a[href*='obiava']")
            price_tag = ad.select_one(".price")

        # links = soup.find_all("a", {"class": "category-name"})
        # jobs_cnt = soup.find_all("span", {"class": "job-qty"})

if __name__ == "__main__":
    scraper = AutoAdsScraper()
    scraper.extract_data()