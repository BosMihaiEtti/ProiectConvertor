class ConsoleUI:
    def __init__(self, market):
        self.market = market

    def run(self):
        print("--- FOREX TRADING CONSOLE ---")
        while True:
            print("\n1. Convert\n2. Exit")
            choice = input("Alege: ")

            if choice == "2":
                break

            if choice == "1":
                try:
                    amt = float(input("Suma: "))
                    frm = input("Din (ex: USD): ").upper()
                    to = input("In (ex: EUR): ").upper()

                    res = self.market.convert(amt, frm, to)
                    print(f"Rezultat: {res:.2f} {to}")
                except Exception as e:
                    print(f"Eroare: {e}")