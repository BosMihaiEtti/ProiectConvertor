import random
from backend.converter_service import CurrencyService


class ForexMarket:
    def __init__(self, rates):
        self.rates = rates
        self.base_currency = "USD"

    def convert(self, amount, from_curr, to_curr):
        if from_curr not in self.rates or to_curr not in self.rates:
            raise ValueError("Moneda invalida.")

        # Folosim serviciul de conversie pentru calcul
        return CurrencyService.calculate_cross_rate(
            amount,
            self.rates[from_curr],
            self.rates[to_curr]
        )

    def simulate_volatility(self):
        """Modifică prețurile aleatoriu (+/- 0.5%)"""
        for currency in self.rates:
            if currency == "USD": continue
            change = random.uniform(-0.005, 0.005)
            self.rates[currency] *= (1 + change)