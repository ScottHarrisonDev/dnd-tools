# Path wankery
import sys
import json
import random
sys.path.insert(0, '../')

from generator import Generator


class Name_Generator(Generator):

    json = ""
    delimiter = ""

    #def __init__(self):
        # Does anything need to go here?

    def setup(self, filepath, delimiter):
        # Get json with the filepath
        self.delimiter = delimiter
        with open(filepath) as json_file:
            self.json = json.loads(json_file.read())
        return self.json

    def generate(self):
        # Do stuff with the json
        full_name = ""
        i = 1
        for element in self.json:
            full_name += random.choice(self.json[element])
            if i < len(self.json):
                full_name += self.delimiter
            i += 1
        return full_name