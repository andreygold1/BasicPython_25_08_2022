import json
import random
import string


# Функция generate_txt_data. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.
# ---------------------------------------------------------------------------------------------------------
# def generate_txt_data(filename):
#     with open(filename, 'w') as file_1:
#         rand_letters = string.ascii_letters + string.digits + ' '
#         rand_string = ''.join(random.choice(rand_letters) for i in range(random.randint(100, 1000)))
#         print(rand_string)
#         file_1.write("".join(rand_string))
#
#
# def read_file(filename):
#     with open(filename, 'r') as file_2:
#         data_txt = file_2.read()
#         return data_txt
#
#
# my_file = 'txt_data.txt'
# file_txt = generate_txt_data(my_file)
# print(read_file(my_file))

##########################################################################################################
# Функция generate_json_data. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
# -----------------------------------------------------------------------------------------------------------

def random_key():
    list_leters = []
    for index in range(5):
        rand_leter = random.choice(string.ascii_lowercase)
        list_leters.append(rand_leter)
    key = ''.join(list_leters)
    return key


def random_value():
    rand_value = random.choice([random.randint(-100, 100), (random.uniform(0, 1)), (random.choice([False, True]))])
    return rand_value


def random_dict():
    dictionary = {}
    for index in range(random.randint(5, 20)):
        dictionary.update({random_key(): random_value()})
    return dictionary


def write_json(filename, dict):
    with open(filename, 'w') as json_file:
        json.dump(dict, json_file, indent=2)


def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


file_in = 'dictionary.json'
file_out = write_json(filename=file_in, dict=random_dict())
print(read_json(file_in))

############################################################################################################
# Функция generate_and_write_file. Написать функцию которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
#
# Разрешается создавать дополнительные (вспомогательные) функции.

