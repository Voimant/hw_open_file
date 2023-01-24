from pprint import pprint

file_path = "cook_book.txt"


def get_shop_list_by_dishes(dishes,person_count):
    order_sheet = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingr["кол-во"] *= person_count
                pop_key = ingr.pop("Ингридиент")
                order_sheet[pop_key] = ingr

    return order_sheet




with open(file_path,'r',encoding = "utf-8" ) as f:
    cook_book = {}
    for line in f:
        name_recipe = line.strip()
        emp_count = int(f.readline())
        employ = []
        for i in range(emp_count):
            emp = f.readline().strip()
            ingridient,quoly,uom, = emp.split(' | ')

            employ.append({
                       'Ингридиент': ingridient,
                       'кол-во': int(quoly),
                       'ед.изм': uom

                           })
        f.readline()
        cook_book[name_recipe] = employ

print("HW_1--------------------\n")
pprint(cook_book)
print("HW_2------------------------\n")
pprint(get_shop_list_by_dishes(['Омлет','Запеченный картофель'],2))


