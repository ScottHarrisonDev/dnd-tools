# Path wankery
import sys
sys.path.insert(0, './name-generator')

from name_generator import Name_Generator

if __name__ == "__main__":

    # Parse some input to decide what to generate.
    name_gen = Name_Generator()
    name_gen.setup(sys.argv[1], sys.argv[2])
    print(name_gen.generate())
