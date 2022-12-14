from statistics import mean

# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
# _____________________________________________________________________________________________________________

my_list = ['123', '567', '789']
result = []
for index, value in enumerate(my_list):
    if index % 2 != 0:
        value = value[::-1]
        result.append(value)
    else:
        result.append(value)
print(my_list)
print(result)

###############################################################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# _____________________________________________________________________________________________________________

my_list = ['abc', 'atab', 'qwertya']
result = []
for element in my_list:
    if 'a' in element[0]:
        result.append(element)
print(result)

###############################################################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# _____________________________________________________________________________________________________________

my_list = ['bc', 'tgba', 'a_qwerty', '123', 'aaaaadffd']
result = []
for element in my_list:
    if 'a' in element:
        result.append(element)
print(result)

###############################################################################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]

persons = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Colin", "age": 15},{"name": "Denis", "age": 15}]

# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
young_man = []
min_age = 200
for person in persons:
    if person['age'] < min_age:
        min_age = person['age']
for person in persons:
    if person['age'] == min_age:
        young_man.append(person['name'])
print(young_man)

# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
long_name = []
long_max = 0
for person in persons:
    if len(person['name']) > long_max:
        long_max = len(person['name'])
for person in persons:
    if len(person['name']) == long_max:
        long_name.append(person['name'])
print(long_name)

# в) Посчитать среднее количество лет всех людей из начального списка.
age = []
for person in persons:
    age.append(person['age'])
print(mean(age))

###############################################################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.

my_dict_1 = {"name": "Ray", "age": 45, "country": "The USA", "job": "actor"}
my_dict_2 = {"name": "Nick", "age": 55, "gender": "man"}

# а) Создать список из ключей, которые есть в обоих словарях.

result_1 = []
for key in my_dict_1:
    if key in my_dict_2:
        result_1.append(key)
print(result_1)
# _____________________________________________________________________
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

result_2 = []
for key in my_dict_1:
    if key not in my_dict_2:
        result_2.append(key)
print(result_2)
# _________________________________________________________________________
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

result = dict()
for key in my_dict_1:
    if key not in my_dict_2:
        result[key] = my_dict_1[key]
print(result)
#__________________________________________________________________________________________________
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

result = dict()
for key in my_dict_1 | my_dict_2:
    if key not in my_dict_2:
        result[key] = my_dict_1[key]
    elif key not in my_dict_1:
        result[key] = my_dict_2[key]
    else:
        result[key] = [my_dict_1[key], my_dict_2[key]]
print(result)
