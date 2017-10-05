# Path wankery
import sys
sys.path.insert(0, './name-generators')

import argparse

# Import all the generator files.
from simple_name_generator import Simple_Name_Generator
from component_name_generator import Component_Name_Generator

COMMAND_MAP = {
    'simple': Simple_Name_Generator,
    'compose': Component_Name_Generator
}


def main():

    # Parse some input to decide what to generate.
    parser = argparse.ArgumentParser(
        description='Generate the names of various things through command line')

    # Required arguments to choose a generator.
    parser.add_argument('command', choices=COMMAND_MAP.keys())

    # Optional arguments
    parser.add_argument(
        '-t', '--title', metavar='\b', help="Optionally generate a title to append to the name.", type=str)

    # TODO: How to add a flag for passing a number and repeating the generation that many times??
    parser.add_argument(
        "-n", metavar='\b', default=1,
        help='How many names would you like? You must provide a positive, non-zero number', type=int)

    args = parser.parse_args()
    Chosen_Generator = COMMAND_MAP[args.command]

    name_gen = Chosen_Generator()
    name_gen.setup()
    print(name_gen.generate())


if __name__ == '__main__':

    main()
