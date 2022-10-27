# Написать класс Quotes.
# Параметр инициализации - количество цитат (int), и имя файла для сохранения (формат json, параметр по умолчанию)
#
# В классе реализовать метод get_quotes.
# Метод сохраняет список оветов (список словарей) сервиса http://forismatic.com/ru/api/. Если метод не вызван - список пустой.
# Если автор не указан, цитату не брать. Цитаты не должны повторяться (уникальные, без повтора).
#
# В классе реализовать метод print_quotes.
# Метод печатает из списока полученных ответов от сервера только цитату и автора (а не весь словарь). По одной в каждой строке.
#
# Реализовать метод save_quotes.
# Метод сохраняет список оветов (список словарей) в json файл.
# Перед сохранением в json, записи отсортировать по фамилии автора (повторим функцию сортировки).
# Функцию для сортировки в класс засовывать не нужно. Напишите ее отдельно перед классом ))
#
# Не забудьте написать try except для обработки ошибки при получении цитат.
# Там не всегда срабатывает преобразование в json.

import json
import requests


def sort_by_surname(item: dict):
    surname = item["quoteAuthor"].split()[-1]
    return surname


class Quotes:
    def __init__(self, count: int):
        self.count = count
        self.quotes_1 = self.get_quotes()
        self.filename = "my_file.json"

    def get_quotes(self):
        quote_list = []
        temp_count = 0
        url = "http://api.forismatic.com/api/1.0/"
        while temp_count != self.count:
            params = {
                "method": "getQuote",
                "format": "json",
                "key": temp_count,
                "lang": "en"
            }
            response = requests.get(url, params=params)
            try:
                if response.json()['quoteAuthor']:
                    quote_list.append(response.json())
                    temp_count += 1
                else:
                    return response.json()
            except (requests.exceptions.JSONDecodeError):
                pass
        return self.get_quotes()

    def print_quotes(self):
        for quote in self.quotes_1:
            text = quote["quoteText"].strip()
            author = quote["quoteAuthor"].strip()
            print(f"\"{text}\" - {author}.")

    def save_quotes(self):
        with open(self.filename, "w") as file_json:
            json.dump(sorted(self.quotes_1, key=sort_by_surname), file_json)
