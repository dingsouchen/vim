"""An animal base class."""
"""MOdified on 2022/20/15"""


class Animal(object):

    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
