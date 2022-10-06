# //Аргументы запуска файла:
# //    RATE - получение текущего курса (USD/UAH)
# //    AVAILABLE - получение остатков по счетам
# //    BUY XXX - покупка xxx долларов. При отсутсвии грвен для покупки выводит сообщение типа UNAVAILABLE, REQUIRED BALANCE UAH 2593.00, AVAILABLE 1000.00
# //    SELL XXX - продажа xxx долларов. При отсутсвии долларов для продажи выводит сообщение типа UNAVAILABLE, REQUIRED BALANCE USD 200.00, AVAILABLE 135.00
# //    BUY ALL - покупка долларов на все возможные гривны.
# //    SELL ALL - продажа всех долларов.
# //    NEXT - получить следующий курс
# //    RESTART - начать игру с начала (с начальными условиями)

from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("action", type=str)
# args.add_argument("--age", type=int, nargs='?', default=0)
# args.add_argument("--job", type=str, nargs='?', default='')

args = vars(args.parse_args())
print(args)

# if args['action'] == "NEXT":
#     print(args['action'])