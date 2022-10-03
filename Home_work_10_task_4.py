import re

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
        dict_date = {}
        for line in file.readlines():
            if len(line.split()) > 1:               # ищу строку с количеством элементов более 1
                temp_date = line.split('-')[0]      # разделяю строку за элементы и беру 0 элемент
                dict_date['date_original'] = temp_date   #добавляю в новій словарь оригинальную дату
                dd, mm, year = temp_date.split()    # Разделяю на элементы оригинальную дату
                new_date = re.findall("\d+", dd)    # преобразование строки даты в число, создание списка
                new_mm = monthToNum(mm)             # преобразование строки месяца в порядковый номер
                new_date.append(new_mm)
                new_date.append(year)
                date_modified = '/'.join(new_date)  # объединение элементов списка в в сроку с разделителем "/"
                dict_date['date_modified'] = date_modified  # добавление модифицированной даты в словарь
                result.append(dict_date)  # добавление словаря в результрующий список
            # print(result)
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
list_date_original = read_file_4(my_file_4)
print(list_date_original)