file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'
file_4 = '4.txt'



with open(file_1,'r',encoding = "utf-8" ) as f:
    text_1 = ''
    count_line_1 = []
    count = 0
    for line in f:
        count += 1
        count_line_1.append(count)
        text_1 += line
print(count_line_1)
print(text_1)

with open(file_2,'r',encoding = "utf-8" ) as f:
    text_2 = ''
    count_line_2 = 0
    for line in f:
        count_line_2 += 1
print(count_line_2)

with open(file_3,'r',encoding = "utf-8" ) as f:
    text_3 = ''
    count_line_3 = 0
    for line in f:
        count_line_3 += 1
print(count_line_3)

with open(file_4, 'w',encoding = "utf-8" ):
    
