from argparse import ArgumentParser
from utils import choice_action

args = ArgumentParser()

args.add_argument("value_1", type=str, nargs='?', default='')
args.add_argument("value_2", type=str, nargs='?', default='')
args = vars(args.parse_args())
action_in = choice_action(args)
