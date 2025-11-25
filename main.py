
from conversion import convert_currency
from rates_api import get_rates


def main():
    print("=== Convertor valutar (cursuri reale din API) ===")
    print("Se incearca preluarea cursurilor valutare de la API...")


    rates = get_rates()

    print("Cursurile au fost preluate cu succes!")
    print("Cateva monede disponibile:", ", ".join(list(rates.keys())[:10]))
    print()

    while True:
        try:
            amount_str = input("Introdu suma (sau 'exit' pentru iesire): ")
            if amount_str.lower() == "exit":
                print("La revedere!")
                break

            amount = float(amount_str)

            from_currency = input("Moneda sursa (ex: EUR, RON): ")
            to_currency = input("Moneda tinta (ex: EUR, RON): ")

            result = convert_currency(amount, from_currency, to_currency, rates)

            print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
            print("-" * 40)

        except ValueError as e:
            print("Eroare:", e)
            print("Te rog incearca din nou.")
            print("-" * 40)



if __name__ == "__main__":
    main()