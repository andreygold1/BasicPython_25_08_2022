import random
import string


# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# ---------------------------------------------------------------------------
def make_a_mirror_line(list_1):
    result = []
    for index, value in enumerate(list_1):
        if index % 2 != 0:
            value = value[::-1]
            result.append(value)
        else:
            result.append(value)
    return result


my_list = ['123', 'qwe', '789']
my_result = make_a_mirror_line(my_list)
print(my_result)


###############################################################################
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
# -----------------------------------------------------------------------------

def find_strings_starting_with_letter_a(list_1):
    result = []
    for element in list_1:
        if 'a' in element[0]:
            result.append(element)
    return result


my_list = ['abc', 'atab', 'qwertya']
my_result = find_strings_starting_with_letter_a(my_list)
print(my_result)


###############################################################################
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# ------------------------------------------------------------------------------
def find_the_letter_in_string(list_1):
    result = []
    for element in list_1:
        if 'a' in element:
            result.append(element)
    return result


my_list = ['bc', 'tgba', 'a_qwerty', '123', 'aaaaadffd']
my_result = find_the_letter_in_string(my_list)
print(my_result)


################################################################################
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
# --------------------------------------------------------------------------------

def find_strings_in_list(list_1):
    new_list = []
    for element in list_1:
        if type(element) == str:
            new_list.append(element)
    return new_list


my_list = [1, 2, 3, "11", "22", "33"]
my_result = find_strings_in_list(my_list)
print(my_result)


#################################################################################
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
# --------------------------------------------------------------------------------

def find_characters_that_occur_once(string_1):
    new_list = []
    for element in set(string_1):
        if string_1.count(element) == 1:
            new_list.append(element)
    return new_list


my_str = 'qwertyqwer'
my_result = find_characters_that_occur_once(my_str)
print(my_result)

#################################################################################
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# --------------------------------------------------------------------------------

def find_common_characters_in_strings(string_1, string_2):
    new_list = []
    for element in set(string_1).intersection(set(string_2)):
        new_list.append(element)
    return new_list


str_1 = '433qwerty+'
str_2 = '12qwerty'
my_result = find_common_characters_in_strings(string_1=str_1, string_2=str_2)
print(my_result)


#################################################################################
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
# ---------------------------------------------------------------------------------

def find_characters_occurring_in_strings_once(string_1, string_2):
    result = []
    for element in set(string_1).intersection(set(string_2)):
        if str_1.count(element) == 1 and str_2.count(element) == 1:
            result.append(element)
    return result


str_1 = "aaaasdf1"
str_2 = "asdfff2"
my_result = find_characters_occurring_in_strings_once(string_1=str_1, string_2=str_2)
print(my_result)


##################################################################################
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

def create_email(list_1, list_2):
    random_names = random.choice(list_1)
    random_numder = str(random.randint(100, 999))
    random_domains = random.choice(list_2)
    letters = string.ascii_lowercase
    random_string = ''.join(random.sample(letters, random.randint(5, 7)))
    result = random_names + '.' + random_numder + "@" + random_string + '.' + random_domains
    return result


names = ["king", "miller", "kean", "coin"]
domains = ["net", "com", "ua", "io"]
e_mail = create_email(list_2=domains, list_1=names)
print(e_mail)
