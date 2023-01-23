file_path = "cook_book.txt"

with open(file_path,'rt',encoding = "utf-8" ) as f:
    cooks_book = {}
    for line in f:
        name_recipe = f.readline().strip()
print(name_recipe)