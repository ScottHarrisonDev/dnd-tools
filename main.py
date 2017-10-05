# Path wankery
import sys
sys.path.insert(0, './name-generators')

# Import all the generator files.
from simple_name_generator import Simple_Name_Generator

if __name__ == '__main__':

    # Parse some input to decide what to generate.

    # TODO: add a parser for the argument here.
    # arg1 = sys.argv[1]

    name_gen = Simple_Name_Generator()
    name_gen.setup()
    print(name_gen.generate())
