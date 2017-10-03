# Path wankery
import sys
sys.path.insert(0, '../')

from generator import Generator


class Name_Generator(Generator):

    filepath = ""
    json = ""

    def __init__(self):
        # Does anything need to go here?

    def setup(self, filepath):
        print(filepath)
        # Get json with the filepath
        json = filepath
        return json

    def generate(self, json):
        # Do stuff with the json
        print(json)
