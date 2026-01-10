class CurrencyService:
    """
    Serviciu pur matematic. Nu ține minte datele, doar calculează.
    """
    @staticmethod
    def calculate_cross_rate(amount, rate_from, rate_to):
        # Formula: (Suma / Rata_Sursa) * Rata_Destinatie
        amount_in_usd = amount / rate_from
        final_amount = amount_in_usd * rate_to
        return final_amount