from pprint import pprint

file_list = ["1.txt","2.txt","3.txt"]
file_name = "4.txt"


def read_file(file_name):
    file_list = {}
    for o_file in file_name:
        with open(o_file, 'r', encoding="utf-8") as f:
            text_1 = ''
            count = 0
            for o_file in f:
                count += 1
                text_1 += o_file
            file_list[count] = text_1
            # file_list.append({count: text_1})
    return file_list

def write_file(file_name):
    with open(file_name, 'w', encoding="utf-8") as f:
        for k,v in read_file():
            f.write(k)
            f.write(v)



pprint(read_file(sorted(file_list)))
write_file(file_name)
