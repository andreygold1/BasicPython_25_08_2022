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
    return data


def buy_all(data):
    summa_usd = make_rounding(data["UAH"] / data['course'])
    data['USD'] = data['USD'] + summa_usd
    data['UAH'] = round(data['UAH'] - summa_usd * data['course'], 2)
    return data


def sell_all(data):
    summa_uah = data['USD'] * data['course']
    data['UAH'] = data['UAH'] + round(summa_uah, 2)
    data['USD'] = data['USD'] - data['USD']
    return data


def buy_parts(data, value):
    need_uah = round(value * data['course'], 2)
    if data['UAH'] - need_uah < 0:
        print('UNAVAILABLE, REQUIRED BALANCE UAH ' + str(need_uah) + ', ' + 'AVAILABLE ' + str(
            data['UAH']))
    else:
        data['UAH'] = round(data['UAH'] - need_uah, 2)
        data["USD"] = data["USD"] + value
    return data


def sell_parts(data, value):
    if data['USD'] - value < 0:
        print('UNAVAILABLE, REQUIRED BALANCE USD ' + str(value) + ', ' + 'AVAILABLE ' + str(
            data['USD']))
    else:
        data['USD'] = round(data['USD'] - value, 2)
        data["UAH"] = data["UAH"] + round(value * data['course'], 2)
    return data


def make_rounding(value):
    temp_value = math.floor(value * 100)
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
        data_change = change_cource(info_system)
        write_json(filename1='state_system.json', data=data_change)
    elif args['value_1'] == 'RATE' and args['value_2'] == '':
        print(info_system["course"])
    elif args['value_1'] == 'AVAILABLE' and args['value_2'] == '':
        print("USD", info_system["USD"], "UAH", info_system["UAH"])
    elif args['value_1'] == 'BUY' and args['value_2'] != 'ALL':
        data_change = buy_parts(info_system, float(args['value_2']))
        write_json(filename1='state_system.json', data=data_change)
    elif args['value_1'] == 'BUY' and args['value_2'] == 'ALL':
        data_change = buy_all(info_system)
        write_json(filename1='state_system.json', data=data_change)
    elif args['value_1'] == 'SELL' and args['value_2'] == 'ALL':
        data_change = sell_all(info_system)
        write_json(filename1='state_system.json', data=data_change)
    elif args['value_1'] == 'SELL' and args['value_2'] != 'ALL':
        data_change = sell_parts(info_system, float(args['value_2']))
        write_json(filename1='state_system.json', data=data_change)
    elif args['value_1'] == 'RESTART' and args['value_2'] == '':
        make_restart()
    else:
        print("Укажите одно из действий")
        read_txt('action_guide.txt')
