from cats_1 import Cat

pet_house = [
    {
        'name': "Барон",
        'gender':  "мальчик",
        'age': 2
    },
    {
        'name': "Сэм",
        'gender': "мальчик",
        'age': 2 
    }
]    

cat_list = []
for d in pet_house:
    for v in d.values():
        if v == "мальчик":
            cat_male = Cat(name=d['name'], gender=d['gender'], age=d['age']).get_cat()
            cat_list.append(cat_male)
cat_list = set(cat_list)
for i in cat_list:
    print(*i, sep=", ")       