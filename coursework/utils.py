import json
import math
import random


def make_restart():
    config_file = read_json('config.json')
    write_json('state_system.json', config_file)


def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


def write_json(filename1, data):
    with open(filename1, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def change_cource(data):
    next_course = round(random.uniform((data["course"] - data['delta']),
                                       (data["course"] + data['delta'])), 2)
    data["course"] = next_course
    return data["course"]


def buy_all(data):
    summa_usd = make_rounding(data["UAH"] / data['course'])
    if summa_usd > 0:
        data['USD'] = data['USD'] + summa_usd
        data['UAH'] = round(data['UAH'] - data['USD'] * data['course'], 2)
        return data
    else:
        print('Недостаточно средств для покупки валюты')


def sell_all(data):
    summa_uah = data['USD'] * data['course']
    print(summa_uah)
    data['UAH'] = data['UAH'] + round(summa_uah, 2)
    data['USD'] = data['USD'] - data['USD']


def buy_parts(data, value):
    try:
        value_2_float = round(float(value), 2)
        need_uah = round(value_2_float * data['course'],2)
        if data['UAH'] - need_uah < 0:
            print('UNAVAILABLE, REQUIRED BALANCE UAH ' + str(need_uah) + ', ' + 'AVAILABLE ' + str(
                data['UAH']))
        else:
            data['UAH'] = round(data['UAH'] - need_uah, 2)
            data["USD"] = data["USD"] + value_2_float
        return data
    except ValueError:
        print("Ошибка ввода суммы покупки")


def sell_parts(data, value):
    try:
        value_2_float = round(float(value), 2)
        if data['USD'] - value_2_float < 0:
            print('UNAVAILABLE, REQUIRED BALANCE USD ' + str(value_2_float) + ', ' + 'AVAILABLE ' + str(
                data['USD']))
        else:
            data['USD'] = round(data['USD'] - value_2_float, 2)
            data["UAH"] = data["UAH"] + round(value_2_float * data['course'], 2)
    except ValueError:
        print("Ошибка ввода суммы продажи")

def make_rounding(value):
    print(value)
    temp_value = math.floor(value * 100)
    print(temp_value)
    print(temp_value / 100)
    return temp_value / 100

def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())

def choice_action(args):
    info_system = read_json(filename='state_system.json')
    if args['value_1'] == 'NEXT' and args['value_2'] == '':
        change_cource(info_system)
        write_json(filename1='state_system.json', data=info_system)
    elif args['value_1'] == 'RATE' and args['value_2'] == '':
        print(info_system["course"])
    elif args['value_1'] == 'AVAILABLE' and args['value_2'] == '':
        print("USD", info_system["USD"], "UAH", info_system["UAH"])
    elif args['value_1'] == 'BUY' and args['value_2'] != 'ALL':
        buy_parts(info_system, args['value_2'])
        write_json(filename1='state_system.json', data=info_system)
    elif args['value_1'] == 'BUY' and args['value_2'] == 'ALL':
        buy_all(info_system)
        write_json(filename1='state_system.json', data=info_system)
    elif args['value_1'] == 'SELL' and args['value_2'] == 'ALL':
        sell_all(info_system)
        write_json(filename1='state_system.json', data=info_system)
    elif args['value_1'] == 'SELL' and args['value_2'] != 'ALL':
        sell_parts(info_system, args['value_2'])
        write_json(filename1='state_system.json', data=info_system)
    elif args['value_1'] == 'RESTART' and args['value_2'] == '':
        make_restart()
    else:
        print("Недопустимая команда! Укажите одну из команд\n")
        read_txt('action_guide.txt')


