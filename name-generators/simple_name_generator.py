# Path wankery
import json
import random

from generator import Generator


class Simple_Name_Generator(Generator):

    json = ''

    def setup(self):
        # Get json with the filepath
        dir_path = self.directory(__file__)

        with open(dir_path + '\simple_names.json') as json_file:
            self.json = json.loads(json_file.read())
        return self.json

    def generate(self):
        # Simple name generator just takes a first and second name out of the json file.

        full_name = ''
        for key in self.json:

            full_name += random.choice(self.json[key]) + ' '

        return full_name.title()
