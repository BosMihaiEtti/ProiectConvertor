
import requests

BASE_CURRENCY = "EUR"
API_URL = f"https://open.er-api.com/v6/latest/{BASE_CURRENCY}"


def get_rates():

    fallback_rates = {
        "EUR": 1.0,
        "RON": 4.9,
        "USD": 1.1,
        "GBP": 0.85,
    }

    try:

        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            print("ATENTIE: API-ul a raspuns, dar result != 'success'.")
            print("Se folosesc cursurile de rezerva (locale).")
            return fallback_rates

        rates = data.get("rates")

        if not isinstance(rates, dict):
            print("ATENTIE: Raspuns neasteptat de la API (nu exista 'rates' valid).")
            print("Se folosesc cursurile de rezerva (locale).")
            return fallback_rates

        rates[BASE_CURRENCY] = 1.0

        return rates

    except requests.exceptions.RequestException as e:

        print("ATENTIE: Eroare de retea sau API:", e)
        print("Se folosesc cursurile de rezerva (locale).")
        return fallback_rates
