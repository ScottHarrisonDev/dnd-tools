class Generator(object):
    def setup(self, filepath):
        raise NotImplementedError

    def generate(self, json):
        raise NotImplementedError
