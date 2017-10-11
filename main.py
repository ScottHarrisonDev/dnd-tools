# Path wankery
import sys
sys.path.insert(0, './name-generators')
sys.path.insert(0, './tavern-generator')

import argparse

# Import all the generator files.
from simple_name_generator import Simple_Name_Generator
from component_name_generator import Component_Name_Generator
from tavern_generator import Tavern_Generator


COMMAND_MAP = {
    'simple': Simple_Name_Generator,
    'compose': Component_Name_Generator,
    'tavern': Tavern_Generator
}

# TODO: Split the argparse setup into it's own function?




def main():

    # Parse some input to decide what to generate.
    parser = argparse.ArgumentParser(
        description='Generate the names of various things through command line. You must choose one these positional arguments:')

    # Required arguments to choose a generator.
    parser.add_argument('command', choices=COMMAND_MAP.keys())

    # HACK: These optional arguments include metavar='\b' which was required to make the
    # --help output not show capitalised versions of each argument. I know this is a stupid
    # solution and a better formatting approach should be investigated,
    # but I found the answer here: https://stackoverflow.com/a/16968273/6488602

    # Optional arguments
    parser.add_argument(
        '-t', '--title', metavar='\b', dest='title', help="Optionally generate a title to append to the name.", type=str)

    parser.add_argument(
        "-n", '--number', metavar='\b', dest='number', default=1,
        help='Optionally run the generator multiple times. You must provide a positive, non-zero number.', type=int)

    args = parser.parse_args()

    repeats = args.number
    title = args.title

    # There must be a better way to ensure this? Maybe some argparse configuration?
    if repeats <= 0:
        print('Please supply a positive integer for your -n argument')

    # TODO: Is there a nice way to add additional generators form the optional commands?
    # Like Additional_Generators = A list of classes from a map.
    # Loop that list and execute each generator, appending the results?

    # Choose a generator, execute it, jobs a good'un.
    Chosen_Generator = COMMAND_MAP[args.command]

    for i in range(repeats):
        name_gen = Chosen_Generator()
        name_gen.setup()
        name = name_gen.generate()
        print(name)


if __name__ == '__main__':

    main()
