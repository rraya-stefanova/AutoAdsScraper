import time
from typing import Optional, Any

import requests
from bs4 import BeautifulSoup

from src.exceptions import AutoAuthenticationError, AutoNotFoundError, AutoException, AutoServerError


class HTTPClient:
    def __init__(self) -> None:
        self.session = requests.Session()

    def validate_response(self, response, url) -> None :
        if response.status_code in range(200, 300):
            return
        if response.status_code == 401:
            raise AutoAuthenticationError(response)
        if response.status_code == 404:
            raise AutoNotFoundError(response)
        if response.status_code == 429:
            retry_after = response.headers.get('Retry-After')
            if retry_after:
                try:
                    wait_seconds = int(retry_after)
                except ValueError:
                    wait_seconds = 60

                time.sleep(wait_seconds)
                next_response = requests.get(url)
                self.validate_response(next_response, url)

        if response.status_code >= 500:
            raise AutoServerError(response)
        raise AutoException(response)

    def fetch(
            self,
            url: str,
            params: Optional[dict] = None,
            headers: Optional[dict] = None,
    ) -> requests.Response:
        if not self.session:
            self.session = requests.Session()

        response = self.session.get(url, params=params, headers=headers)
        self.validate_response(response, url)
        return response

    def get_data(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None) -> Any:
        response = self.fetch(url, params=params)

        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return response.json()
        return response.text

