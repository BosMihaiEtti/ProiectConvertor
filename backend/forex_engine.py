import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from backend.converter_service import CurrencyService


class ForexMarket:
    def __init__(self, rates):
        self.rates = rates
        self.available_currencies = sorted(list(rates.keys()))

    def convert(self, amount, from_curr, to_curr):
        """Executa conversia curenta."""
        if from_curr not in self.rates or to_curr not in self.rates:
            raise ValueError("Moneda selectata nu este disponibila.")

        return CurrencyService.calculate_cross_rate(
            amount,
            self.rates[from_curr],
            self.rates[to_curr]
        )

    def get_ohlc_data(self, from_curr, to_curr, days=30):
        """
        Genereaza date SIMULATE tip OHLC (Open-High-Low-Close) pentru grafice candlestick.
        """
        if from_curr == to_curr:
            return None

        current_rate = self.convert(1.0, from_curr, to_curr)
        dates = pd.date_range(end=datetime.today(), periods=days)

        # Setari de volatilitate pentru simulare
        volatility = current_rate * 0.008  # aprox 0.8% miscare zilnica

        ohlc_data = []
        # Pornim de la pretul curent si mergem inapoi in timp
        last_close = current_rate

        for _ in range(days):
            # Simulam o miscare a zilei (random walk)
            change = np.random.normal(0, volatility)

            # Calculam valorile zilei (simulat)
            close_price = last_close
            open_price = close_price - change  # Ziua anterioara s-a inchis aici

            # High si Low sunt putin peste/sub open si close
            high_price = max(open_price, close_price) + abs(np.random.normal(0, volatility / 2))
            low_price = min(open_price, close_price) - abs(np.random.normal(0, volatility / 2))

            ohlc_data.append([open_price, high_price, low_price, close_price])
            last_close = open_price  # Pretul de deschidere de azi devine inchiderea de ieri

        # Inversam ordinea cronologica (de la vechi la nou)
        ohlc_data.reverse()

        df = pd.DataFrame(data=ohlc_data, index=dates, columns=['Open', 'High', 'Low', 'Close'])
        return df