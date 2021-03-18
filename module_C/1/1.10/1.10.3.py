#Клиент «Иван Петров». Баланс: 50 руб.
class Base:
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
    
    def get_balance(self):
        return self.name, self.money


base = [
    {
        "Иван Петров": 35
    },
    {
        "Петр Иванов": 53
    }
]

for d in base:
    for k, v in d.items():
        out = Base(k, v).get_balance()
    print(f'Клиент «{out[0]}». Баланс: {out[1]} руб.')
