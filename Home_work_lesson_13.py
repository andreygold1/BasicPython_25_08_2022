import json
import re


# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# --------------------------------------------------------------------------------------------------

def read_file(filename):
    with open(filename, 'r') as json_file:
        values = json.load(json_file)
        return values


file_in = "data.json"
data = read_file(file_in)

###################################################################################################
# 2. Написать "функцию сортировки" данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# --------------------------------------------------------------------------------------------------

sort_surname = sorted(data, key=lambda item: item["name"].split()[-1])
print(sort_surname)

###################################################################################################
# 3. Написать функцию сортировки по количеству слов в поле "text".
# --------------------------------------------------------------------------------------------------

# Вариант решения №1
sotr_text = sorted(data, key=lambda item: len(item["text"].split(" ")))
print(sotr_text)

# Вариант решения №2
def sort_len_text(item):
    text_in = item["text"]
    return len(text_in.split(" ")), text_in


sorted_values = sorted(data, key=sort_len_text)
print(sorted_values)
###################################################################################################
# 4. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# ---------------------------------------------------------------------------------------------------

def d_retr(years_in: str) -> int:
    year_death = re.match(r".+\s(\d+)\D*$", years_in).group(1)
    year_death = -int(year_death) if ("BC" in years_in) else int(year_death)
    return year_death


sort_year_death = sorted(data, key=lambda item: d_retr(item["years"]))
print(sort_year_death)