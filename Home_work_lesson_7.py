# 1. Дано целое число (int). Определить сколько нулей в этом числе.
# _________________________________________________________________

# chislo = 1002023501
# my_chislo = 0
# number = str(chislo).count(str(my_chislo))
# print(number)

#########################################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
# ___________________________________________________________________________________________________________

# chislo_1 = 1002000
# count = 0
# my_str = str(chislo_1)[::-1]
# for element in my_str:
#     if element == '0':
#         count += 1
#     else:
#         break
# print(count)

#########################################################################
# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
# __________________________________________________________________________________________________________

# my_list1 = [1, 2.3, 5, 'a', 9]
# my_list2 = [5, 'q', 'w', 'e', 'r', 't', 'y']
# my_result = []
# for _ in my_list1[::2]:
#     my_result.append(_)
# for _ in my_list2[1::2]:
#     my_result.append(_)
# print(my_result)

############################################################################################################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
# __________________________________________________________________________________________________________

# my_list = [1,2,3,4,6,56,0]
# new_list = []
# for element in my_list[1:]:
#     new_list.append(element)
# new_list.append(my_list.pop(0))
# print(new_list)

#############################################################################################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
# ___________________________________________________________________________________________________________

# my_list = [1,2,3,4,6,56,0]
# print(my_list, id(my_list))
# my_list.append(my_list.pop(0))
# print(my_list, id(my_list))

#############################################################################################################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
# ___________________________________________________________________________________________________________

# my_str = "43 больше чем 34 но меньше чем 56"
# new_str = my_str.split()
# chislo = 0
# for index in range(len(new_str)):
#     if new_str[index].isdigit():
#         chislo += int(new_str[index])
# print(chislo)

#############################################################################################################
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк)
# ____________________________________________________________________________________________________________

# my_str = "My long string"
# l_limit = my_str.find('o')
# r_limit = my_str.rfind('g')
# sub_str = my_str[(l_limit+1):r_limit]
# print(sub_str)

###############################################################################################################
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
# _____________________________________________________________________________________________________________
#???????????????????????????????????????
# my_str = 'abcde'
# result = []
# for el in (my_str)[:2:2]:
#     result.append(el)
# print(result)
# result = []
# for element in my_str[::2]:
#     result.append(element)
# print(result)


###############################################################################################################
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
# _____________________________________________________________________________________________________________

# my_list = [2,4,1,5,3,9,0,7]
# count = 0
# for index in range(len(my_list[:-1])):
#     if (my_list[index] > (my_list[index-1] + my_list[index+1])):
#         count += 1
# print(count)

###############################################################################################################
# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
# _____________________________________________________________________________________________________________

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for index in range(len(my_list)):
#     if type(my_list[index]) == str:
#         new_list.append(my_list[index])
# print(new_list)


###############################################################################################################
# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
# _____________________________________________________________________________________________________________

# ?????????????????????????????????????

###############################################################################################################
# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# _____________________________________________________________________________________________________________

# ?????????????????????????????????????

###############################################################################################################
# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу
# ________________________________________________________________________________________________________________

# ?????????????????????????????????????