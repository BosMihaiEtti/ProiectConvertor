
def convert_currency(amount, from_currency, to_currency, rates):

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates:
        raise ValueError(f"Moneda sursa necunoscuta: {from_currency}")
    if to_currency not in rates:
        raise ValueError(f"Moneda tinta necunoscuta: {to_currency}")

    rate_from = rates[from_currency]
    rate_to = rates[to_currency]

    amount_in_base = amount / rate_from
    result = amount_in_base * rate_to

    return result