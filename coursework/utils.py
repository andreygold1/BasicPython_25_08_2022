import json
# RATE - получение текущего курса (USD/UAH)
#     AVAILABLE - получение остатков по счетам
#     BUY XXX - покупка xxx долларов. При отсутсвии грвен для покупки выводит сообщение типа UNAVAILABLE, REQUIRED BALANCE UAH 2593.00, AVAILABLE 1000.00
#     SELL XXX - продажа xxx долларов. При отсутсвии долларов для продажи выводит сообщение типа UNAVAILABLE, REQUIRED BALANCE USD 200.00, AVAILABLE 135.00
#     BUY ALL - покупка долларов на все возможные гривны.
#     SELL ALL - продажа всех долларов.
#     NEXT - получить следующий курс
#     RESTART - начать игру с начала (с начальными условиями)

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
    if args['action'] == 'NEXT':
        print(args['action'])
    elif args['action'] == 'RATE':
        print(args['action'])
    elif args['action'] == 'AVAILABLE':
        print(args['action'])
    elif args['action'] == 'BUY':
        print(args['action'])
    elif args['action'] == 'SELL':
        print(args['action'])
    elif args['action'] == 'BUY ALL':
        print(args['action'])
    elif args['action'] == 'SELL ALL':
        print(args['action'])
    elif args['action'] == 'RATE':
        print(args['action'])
    elif args['action'] == 'RESTART':   #Сделано
        make_restart()
    else:
        print('куда полез')



