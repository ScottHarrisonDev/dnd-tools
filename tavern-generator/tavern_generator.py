import json
import random

from generator import Generator


class Tavern_Generator(Generator):

    # Taverns are named with an adjective or verb followed by a noun.
    # e.g. The Thirsty Baboon

    # It would be useful to add verbosity levels:
    # 0 = Just the name
    # 1 = Also services
    # 2 = Also notable patrons

    def setup(self):
        # Get json with the filepath
        dir_path = self.directory(__file__)

        self.nouns = self.load_json(dir_path + '/nouns.json')
        self.adjectives = self.load_json(dir_path + '/adjectives.json')
        self.verbs = self.load_json(dir_path + '/verbs.json')
        self.patrons = []

    def load_json(self, filepath):
        return_json = ''
        with open(filepath) as json_file:
            return_json = json.loads(json_file.read())
        return return_json

    def generate(self):
        # This function doens't feel very pythony right now.
        # How to make that better?

        # Get a descriptor, a verb or an adjective
        use_verb = random.choice([0, 1]) == 1
        descriptor_list = []
        deescriptor = ''

        if use_verb:
            descriptor_list = self.verbs
        else:
            descriptor_list = self.adjectives

        for key in descriptor_list:
            descriptor = random.choice(descriptor_list[key])

        # Get a noun
        noun = random.choice(self.nouns['nouns'])

        return '{} {}'.format(descriptor, noun).title()
