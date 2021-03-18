'''
1.10.4 Думаю, лучше не использовать base, как глобальную переменную в классе,
а например  вне класса проходить по списку, и уже готовый элемент записывать
в класс. Сейчас классы опираются на base, но обычно это более независимые 
сущности, которые импортируются в другие файлы. 
'''
class Balance:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        if name not in base:
            print("Такого имени в базе нет")
        else:
            for i in base[self.name]: # инициализация стартового баланса
                for k, v in i.items():
                    if k == "money":
                        i[k]= money
            
    def add_money(self, money):  # пополнение баланса
        for i in base[self.name]:
            for k, v in i.items():
                if k == "money":
                    i[k]+= money
        dif = "пополнен" if money >= 0 else "уменьшен"
        print(f"Баланс {dif} на {money} руб.")
    
    def balance_out(self):  # вывод баланса клиента
        for i in base[self.name]:
            for k, v in i.items():
                if k == "money":
                    print(f"Клиент '{self.name}'. Баланс: {v} руб.")


class Visitor(Balance):
    def __init__(self, name, town, status):
        self.name = name
        self.town = town
        self.status = status
        base[self.name] = [{"town":self.town}, {"status": self.status}, {"money": 0}]
    
    def get_visitors_list(self): # печать всего списка гостей
        for i in base:
            print(i+", г. "+base[i][0]['town']+", статус "+"'"+base[i][1]["status"]+"'")
        

#base = {"Женя Петров": [{"town":"Урюпинск"}, {"status": "ученик"}, {"money": 0}]}
#v1 = Visitor("Петя Женин", "Ногинск", "маг")
#v2 = Visitor("Вася Пупкин", "Мордор", "джедай")
#v1.balance_out()
#v1.add_money(15)
#v1.balance_out()
#v2.get_visitors_list()