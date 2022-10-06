from argparse import ArgumentParser
from utils import choice_action

args = ArgumentParser()

args.add_argument("action", type=str)
args = vars(args.parse_args())
action_in = choice_action(args)
