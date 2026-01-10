import sys
from backend.data_provider import RateProvider
from backend.forex_engine import ForexMarket
from frontend.console_interface import ConsoleUI


def main():
    # 1. Initializare Backend
    provider = RateProvider()
    rates = provider.fetch_rates()
    market = ForexMarket(rates)

    # 2. Initializare Frontend (Consola)
    app = ConsoleUI(market)

    # 3. Start
    app.run()


if __name__ == "__main__":
    main()