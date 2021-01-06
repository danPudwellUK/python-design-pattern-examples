from important_stuff import ImportantStuff
from more_important_stuff import MoreImportantStuff

class Facade(object):
    def __init__(self, important_stuff=None, more_important_stuff=None):
        print("intializing facade")
        self.stuff1 = important_stuff or ImportantStuff()
        self.stuff2 = more_important_stuff or MoreImportantStuff()

    def doStuff(self):
        print("doing facade")
        self.stuff1.doStuff()
        self.stuff2.doStuff()

