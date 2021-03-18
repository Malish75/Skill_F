import requests
import json
from config import currencys

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base and quote in currencys and base in currencys:
            raise APIException("Нельзя перевести валюту саму в себя.")
        if quote not in currencys and base not in currencys:
            raise APIException("Не указаны валюты для конвертации.")
        elif quote not in currencys:
            raise APIException(f"{quote} не в списке доступных валют.")
        elif base not in currencys:
            raise APIException(f"{base} не в списке доступных валют.")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Неверно введено количество валюты.")

        r = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={currencys[quote]}&base={currencys[base]}')
        return json.loads(r.content)["rates"][currencys[quote]] * float(amount)