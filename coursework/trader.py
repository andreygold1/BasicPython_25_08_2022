from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("action", type=str)
# args.add_argument("--age", type=int, nargs='?', default=0)
# args.add_argument("--job", type=str, nargs='?', default='')

args = vars(args.parse_args())

print(args)
action_in = choice_action(args)
