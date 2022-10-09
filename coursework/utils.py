import json
import random

def make_restart():
    config_file = read_json('config.json')
    write_json('state_system.json', config_file)

def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def write_json(filename1, filename2):
    with open(filename1, 'w') as json_file:
        json.dump(filename2, json_file, indent=2)

def choice_action(args):
    if args['value_1'] == 'NEXT' and args['value_2'] == '':
        info_system = read_json(filename='state_system.json')
        next_course = round(random.uniform((info_system["course"] - info_system['delta']), (info_system["course"] + info_system['delta'])), 2)
        info_system["course"] = next_course
        write_json(filename1='state_system.json', filename2=info_system)
    elif args['value_1'] == 'RATE' and args['value_2'] == '':
        info_system = read_json(filename='state_system.json')
        info_course = info_system["course"]
        print(info_course)
    elif args['value_1'] == 'AVAILABLE' and args['value_2'] == '':
        info_system = read_json(filename='state_system.json')
        print("USD", info_system["USD"], "UAH", info_system["UAH"])
    elif args['value_1'] == 'BUY' and args['value_2'] == 'ALL':
        info_system = read_json(filename='state_system.json')
        summa_usd = info_system["UAH"] / info_system['course']
        info_system['USD'] = round(info_system['USD'] + summa_usd, 2)
        info_system['UAH'] = info_system['UAH'] - info_system['UAH']
        write_json(filename1='state_system.json', filename2=info_system)
    elif args['value_1'] == 'BUY' and args['value_2'] != 'ALL':
        try:
            value_2_float = float(args['value_2'])
            info_system = read_json(filename='state_system.json')
            need_uah = value_2_float * info_system['course']
            if info_system['UAH'] - need_uah < 0:
                print('UNAVAILABLE, REQUIRED BALANCE UAH ' + str(need_uah) + ', ' + 'AVAILABLE ' + str(info_system['UAH']))
            else:
                info_system['UAH'] = round(info_system['UAH'] - need_uah, 2)
                info_system["USD"] = round(info_system["USD"] + value_2_float, 2)
                write_json(filename1='state_system.json', filename2=info_system)
        except ValueError:
            pass
    elif args['value_1'] == 'SELL' and args['value_2'] == 'ALL':
        info_system = read_json(filename='state_system.json')
        summa_uah = info_system['USD'] * info_system['course']
        info_system['UAH'] = round(info_system['UAH'] + summa_uah, 2)
        info_system['USD'] = info_system['USD'] - info_system['USD']
        write_json(filename1='state_system.json', filename2=info_system)
    elif args['value_1'] == 'SELL' and args['value_2'] != 'ALL':
        try:
            value_2_float = float(args['value_2'])
            info_system = read_json(filename='state_system.json')
            if info_system['USD'] - value_2_float < 0:
                print('UNAVAILABLE, REQUIRED BALANCE USD ' + str(value_2_float) + ', ' + 'AVAILABLE ' + str(info_system['USD']))
            else:
                info_system['USD'] = round(info_system['USD'] - value_2_float, 2)
                info_system["UAH"] = round(info_system["UAH"] + value_2_float * info_system['course'], 2)
            write_json(filename1='state_system.json', filename2=info_system)
        except ValueError:
            pass
    elif args['value_1'] == 'RESTART' and args['value_2'] == '':
        make_restart()
    else:
        pass
