# Path wankery
import sys
sys.path.insert(0, '../')

from generator import Generator


class Name_Generator(Generator):

    def setup(self, filepath):
        print(filepath)

    def generate(self, json):
        print(json)
