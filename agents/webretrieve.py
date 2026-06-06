import requests
from bs4 import BeautifulSoup


class WebpageRetrievalAgent:

    @staticmethod
    def retrieve(url):

        try:

            response = requests.get(
                url,
                timeout=10
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            return soup.get_text(
                separator=" ",
                strip=True
            )

        except Exception as e:

            return f"ERROR: {str(e)}"