"""An animal base class."""
"""MOdified on 2022/20/15"""
"""Modified again"""


class Animal(object):

    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
