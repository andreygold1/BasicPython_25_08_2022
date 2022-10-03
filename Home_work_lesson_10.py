# Все пункты сделать как отдельные функции и их вызовы.

import re



# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
# __________________________________________________________________________________________________________

# def read_file_1(filename):
#     with open(filename, 'r') as file:
#         list_domains = file.read()
#         domains = list_domains.replace(".", "")
#     return domains
#
#
# my_file_1 = "domains.txt"
# new_domains = read_file_1(my_file_1)
# print(new_domains)


###########################################################################################################
# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
# __________________________________________________________________________________________________________

# def read_file_2(filename):
#     with open(filename, 'r') as file1:
#         surnames = '\t'.join([line.split()[1] for line in file1.readlines()])
#     return surnames
#
#
# my_file_2 = "names.txt"
# list_surnames = read_file_2(my_file_2)
# print(list_surnames)


###########################################################################################################
# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]
# __________________________________________________________________________________________________________

# def read_file_3(filename):
#     result = []
#     dict_date = {}
#     with open(filename, 'r') as file:
#         for line in file.readlines():
#             if len(line.split()) > 1:
#                 dict_date['date'] = line.split('-')[0]
#                 result.append(dict_date)
#      return result
#
#
# my_file_3 = 'authors.txt'
# dates = read_file_3(my_file_3)
# print(dates)

###########################################################################################################
# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# # в которых date_original - это дата из строки (если есть),
# а date_modified - это та же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
# ___________________________________________________________________________________________________________

def read_file_4(filename):
    with open(filename, 'r') as file:
        result = []
        for line in file.readlines():
            dict_date = {}
            if len(line.split()) > 1:
                temp_date = line.split('-')[0]
                if len(temp_date.split()) == 3:
                    dd, mm, year = temp_date.split()
                    new_date = re.findall("\d+", dd)
                    new_mm = monthToNum(mm)
                    new_date.append(new_mm)
                    new_date.append(year)
                    date_modified = '/'.join(new_date)
                    dict_date['date_original'] = temp_date
                    dict_date['date_modified'] = date_modified
                    result.append(dict_date)
        return result

def monthToNum(Month):
    return {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }[Month]


my_file_4 = 'authors.txt'
list_date = read_file_4(my_file_4)
print(list_date)
