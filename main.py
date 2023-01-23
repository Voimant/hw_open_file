file_path = "cook_book.txt"

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
                       'кол-во': quoly,
                       'ед.изм': uom

                           })
        f.readline()
        cook_book[name_recipe] = employ




print(cook_book)

