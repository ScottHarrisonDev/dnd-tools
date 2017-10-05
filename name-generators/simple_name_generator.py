# Path wankery
import sys
import json
import random
sys.path.insert(0, '../')

from generator import Generator


class Simple_Name_Generator(Generator):

    json = ""
    delimiter = ""

    # def __init__(self):
    # Does anything need to go here?

    def setup(self, filepath, delimiter):
        # Get json with the filepath
        self.delimiter = delimiter
        with open(filepath) as json_file:
            self.json = json.loads(json_file.read())
        return self.json

    def generate(self):
        # Simple name generator just takes a first and second name out of the json file.

        full_name = ''
        for key, value in self.json.items():

            full_name += random.choice(value) + ' '

        return full_name
