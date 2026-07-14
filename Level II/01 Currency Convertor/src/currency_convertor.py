from time import timezone

import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=2*60*60)


@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/a6f1f255fcdfa86d6a21f986/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return data['conversion_rates'][target_currency]


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


if __name__ == "__main__":
    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = float(input("Enter amount: "))
    exchange_rate = get_exchange_rate(
        base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    print(f"{amount}{base_currency} is {converted_amount}{target_currency}")
