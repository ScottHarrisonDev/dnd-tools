class Generator(object):

    def directory(self, file):
        import os
        return os.path.dirname(os.path.realpath(file))

    def setup(self):
        raise NotImplementedError

    def generate(self):
        raise NotImplementedError
