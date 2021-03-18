'''
1.10.4 �����, ����� �� ������������ base, ��� ���������� ���������� � ������,
� ��������  ��� ������ ��������� �� ������, � ��� ������� ������� ����������
� �����. ������ ������ ��������� �� base, �� ������ ��� ����� ����������� 
��������, ������� ������������� � ������ �����. 
'''
class Balance:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        if name not in base:
            print("������ ����� � ���� ���")
        else:
            for i in base[self.name]: # ������������� ���������� �������
                for k, v in i.items():
                    if k == "money":
                        i[k]= money
            
    def add_money(self, money):  # ���������� �������
        for i in base[self.name]:
            for k, v in i.items():
                if k == "money":
                    i[k]+= money
        dif = "��������" if money >= 0 else "��������"
        print(f"������ {dif} �� {money} ���.")
    
    def balance_out(self):  # ����� ������� �������
        for i in base[self.name]:
            for k, v in i.items():
                if k == "money":
                    print(f"������ '{self.name}'. ������: {v} ���.")


class Visitor(Balance):
    def __init__(self, name, town, status):
        self.name = name
        self.town = town
        self.status = status
        base[self.name] = [{"town":self.town}, {"status": self.status}, {"money": 0}]
    
    def get_visitors_list(self): # ������ ����� ������ ������
        for i in base:
            print(i+", �. "+base[i][0]['town']+", ������ "+"'"+base[i][1]["status"]+"'")
        

#base = {"���� ������": [{"town":"��������"}, {"status": "������"}, {"money": 0}]}
#v1 = Visitor("���� �����", "�������", "���")
#v2 = Visitor("���� ������", "������", "������")
#v1.balance_out()
#v1.add_money(15)
#v1.balance_out()
#v2.get_visitors_list()