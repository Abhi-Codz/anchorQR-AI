from urllib.parse import urlparse


class URLValidationAgent:

    @staticmethod
    def validate(url):

        try:
            parsed = urlparse(url)

            valid = bool(
                parsed.scheme and
                parsed.netloc
            )

            return {
                "valid": valid,
                "domain": parsed.netloc
            }

        except Exception:

            return {
                "valid": False,
                "domain": None
            }