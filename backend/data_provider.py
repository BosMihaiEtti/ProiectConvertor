import requests

class RateProvider:
    def __init__(self):
        self.api_url = "https://open.er-api.com/v6/latest/USD"
        self.fallback_rates = {
            "USD": 1.0, "EUR": 0.86, "RON": 4.37, "GBP": 0.75,
            "CHF": 0.80, "JPY": 157.88
        }

    def fetch_rates(self):
        try:
            response = requests.get(self.api_url, timeout=3)
            response.raise_for_status()
            data = response.json()
            return data.get("rates", self.fallback_rates)
        except Exception:
            return self.fallback_rates