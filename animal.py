"""An animal base class."""
"""Modified on 2022/10/15"""
"""Modified on 2022/10/16"""
# modified 2022/11/19 11:17

class Animal(object):

    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
