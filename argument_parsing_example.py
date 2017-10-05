# Copied from the accepted answer here:
# https://stackoverflow.com/questions/27529610/call-function-based-on-argparse

# This example shows how you can have mutually exclusive arguments and
# then map them to a function later when requesting the argument.

import argparse
parser = argparse.ArgumentParser(
    description='Generate the names of various things through command line')


def a():
    print('a')


def b():
    print('b')


FUNCTION_MAP = {'a': a,
                'b': b}

parser.add_argument('command', choices=FUNCTION_MAP.keys())

args = parser.parse_args()

func = FUNCTION_MAP[args.command]
func()
